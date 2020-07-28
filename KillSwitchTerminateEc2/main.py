import boto3
import json

def main():
    # establish connection
    ec2machines = boto3.client('ec2')
    response = ec2machines.describe_instances()
    # array used to store all instance that have the KILL switch keyword
    ids = []
    # grab information of ec2 instances
    for i in response["Reservations"]:
        for h in i["Instances"]:
            instanceID = h["InstanceId"]
            stateEc2 = h["State"]["Name"]
            tagNames = h["Tags"]
            # grab tag values 
            for j in tagNames:
                keyName = j["Key"]
                keyValue = j["Value"]
                killExist = keyValue[0:4]
                # grab instance that are in running state 
                if (keyName == "Name" and h["State"]["Name"] == "running"):
                    
                    # if keyValue = KILL then terminate instance
                    if killExist.lower() == "kill":
                        print (f"Instance ID : {instanceID}")
                        print (f"state of ec2 : {stateEc2}")
                        print (f"key value : {keyValue}")
                        print ("----------")
                        # add all instance ids that have the kill switch
                        ids.append(h["InstanceId"])

    # terminate the instances
    terminateStatus = ec2machines.terminate_instances(InstanceIds = ids)
    print(terminateStatus)


if __name__ == "__main__":
    main()