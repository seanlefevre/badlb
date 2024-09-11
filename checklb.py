import requests
from argparse import ArgumentParser
import json
from time import sleep

# Function to get node list
def getnodes(url):
    call = f'{url}/loadbalancer/node_list'
    response = requests.get(call)
    nodedata = response.json()
    return nodedata['nodes']

# Function determines if node needs to be disabled or enabled
def loadlogic(url,nodelist,minReqs,maxReqs):
    for node in nodelist:
        call = f'{url}/loadbalancer/node/{node}'
        response = requests.get(call)
        nodedata = response.json()
        numReqs = int(nodedata['queued_requests'])
        enabled = str(nodedata['enabled'])
        # print(f'{node} is {enabled} has {numReqs} requests')
        #if it is off and healthy turn it back on
        if enabled == 'False':
            if numReqs < int(minReqs):
                turnon(url,node)
        #if it is on and not healthy turn it off
        if enabled == 'True':
            if numReqs > int(maxReqs):
                turnoff(url, node)

# Function enables a node
def turnon(url, node):
    call = f'{url}/loadbalancer/node/{node}/enable'
    requests.post(call)
    print(f'{node} enabled')

# Function disables a node
def turnoff(url, node):
    call = f'{url}/loadbalancer/node/{node}/disable'
    requests.post(call)
    print(f'{node} disabled')

def getlbstats(url):
    call = f'{url}/loadbalancer/stats'
    response = requests.get(call)
    lbstats = response.json()
    numnodes = lbstats['load_balancer_stats']['num_nodes']
    droppct = lbstats['load_balancer_stats']['drop_pct']
    p99 = int(lbstats['load_balancer_stats']['p99_wait_ns'])/100000000
    avgWait = int(lbstats['load_balancer_stats']['average_wait_ns'])/100000000
    queue = lbstats['load_balancer_stats']['requests_queued']
    statstr = f'Total requests queued: {queue}, Average Wait: {avgWait}s, 99% Wait: {p99}s, Requests Dropped: {droppct}%'
    print(statstr)

# Main Function
def main(host,port,minReqs,maxReqs):
    url=f'http://{host}:{port}'
    while True:
        getlbstats(url)
        nodelist = getnodes(url)
        loadlogic(url,nodelist,minReqs,maxReqs)
        sleep(3)

if __name__ == '__main__':
    # Setup Argument Parser
    parser = ArgumentParser()

    # Add Arguments
    parser.add_argument('-t', '--target', dest='target', help='url of the host to check', default='localhost')
    parser.add_argument('-p', '--port', dest='port', help='port of the host to check', default='8188')
    parser.add_argument('-m', '--min', dest='min', help='minimum number of requests', default='100')
    parser.add_argument('-x', '--max', dest='max', help='maximum number of requests', default='350')

    # Parse and Place
    args = parser.parse_args()
    host = args.target
    port = args.port
    minReqs = args.min
    maxReqs = args.max
    main(host,port,minReqs,maxReqs)