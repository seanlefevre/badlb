# Bad Load Balancer Balancer

## Purpose
This application is to be run to offset load balancer issues. It is to ensure that nodes do not exceed the limit of requests and that the requests are not dropped

## Prerequisites
- Docker (for the load balancer)
- Python3 (for the application)

## Setup
- Run `pip3 install argparse requests` to ensure all required packages are installed
- Run `docker run --pull always -it --rm -p 8188:8188 korvus/bad_load_balancer:0.1.1` to start the simulation

## How to Run
- Run `python3 checklb.py`
   
** See Usage for advanced options **

## Usage
Usage: checklb.py [-h] [-t TARGET] [-p PORT] [-m MIN] [-x MAX]. 

Optional arguments:  
| Short arugment | Full arugment | Default | Description |
| :---------------- | :------: | :------: | ----: |
| -h     |   --help  | N/A | show this help message and exit  |
| -t TARGET | --target TARGET | localhost | url of the host to check |
| -p PORT | --port PORT | 8188 | port of the host to check  |
| -m MIN |  --min MIN | 100 | minimum number of requests  |
| -x MAX |  --max MAX | 350 | maximum number of requests |
