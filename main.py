import boto3
import json


def main():
    ec2machines = boto3.client('ec2')
    response = ec2machines.describe_instances()

    # grab ec2 instances and their running state
    for i in response["Reservations"]:
        for h in i["Instances"]:
            instanceID = h["InstanceId"]
            stateEc2 = h["State"]["Name"]
            tagNames = h["Tags"]
            print (f"Instance ID : {instanceID}")
            print (f"state of ec2 : {stateEc2}")
            print (f"tag info : {tagNames}")
            print ("----------")


if __name__ == "__main__":
    
    main()