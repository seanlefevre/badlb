# Bad Load Balancer Balancer

## Purpose
This Application is to be run to offset load balancer issues. Ensuring that nodes do not exceed the limit of requests so that the requests are not dropped

## Prerequisites
Docker (for the load balancer)
Python3 (for the application)

## Setup
run `pip3 install argparse requests` to ensure all required packages are installed

## How to Run
Run `python3 checklb.py`
see Usage for advanced options

## Usage
usage: checklb.py [-h] [-t TARGET] [-p PORT] [-m MIN] [-x MAX]. 

optional arguments:  
| Short arugment | Full arugment | Default | Description |
| :---------------- | :------: | :------: | ----: |
| -h     |   --help  | N/A | show this help message and exit  |
| -t TARGET | --target TARGET | localhost | url of the host to check |
| -p PORT | --port PORT | 8188 | port of the host to check  |
| -m MIN |  --min MIN | 100 | minimum number of requests  |
| -x MAX |  --max MAX | 350 | maximum number of requests |


  -h, --help   show this help message and exit  
  -t TARGET, --target TARGET url of the host to check  
  -p PORT, --port PORT  port of the host to check  
  -m MIN, --min MIN     minimum number of requests  
  -x MAX, --max MAX     maximum number of requests  
