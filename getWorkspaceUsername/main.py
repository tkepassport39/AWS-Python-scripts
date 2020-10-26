import boto3
import os
from botocore.config import Config
import sys


def findUser(ipAddr):
    # make sure to use a default config region of us-east-1
    my_config = Config(
        region_name = 'us-east-1',
        signature_version = 'v4',
        retries = {
            'max_attempts': 10,
            'mode': 'standard'
        }
    )
    # create connection to aws workspace
    client = boto3.client('workspaces', config=my_config)
    response = client.describe_workspaces()

    # find the workspace with the Ip address
    # grab the following values: ip addr, username, state
    for i in response['Workspaces']:
        if (i["IpAddress"] == ipAddr):
            user = i["UserName"]
            ip = i["IpAddress"]
            st = i["State"]
            print("IP address: {}".format(ip))
            print("Username: {}".format(user))
            print("State: {}".format(st))


if __name__ == "__main__":
    # grab the ip address input in the terminal and run function
    findUser(sys.argv[1])