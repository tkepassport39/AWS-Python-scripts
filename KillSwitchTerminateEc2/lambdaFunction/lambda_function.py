import json
import boto3
# setup region
region = 'us-east-2'
ec2 = boto3.client('ec2', region_name=region)
# setup list for holding instance IDs
ids =[]

def lambda_handler(event, context):
    print("event : {}".format(event))
    # grab event detail    
    detail = event['detail']

    print('detail : ' + str(detail))
    # no action if this event is not about ec2 instances
    if not (detail["service"] == "ec2" and detail["resource-type"] == "instance"):
        return
    
    # grab resource value
    resources = event["resources"]
    # grab tag of instance
    tags = detail["tags"]
    print("tags : " + str(tags))

    # search for the word kill to exists in the name
    if ("KILL" in tags["Name"]):
        # debug
        print("Tag does contain kill : {}".format(tags["Name"]))
        # grab the instance ID 
        resourceSplit = resources[0].split("/")
        # append instance id to list "ids"
        ids.append(resourceSplit[len(resourceSplit) - 1])
        print("ids : {}".format(ids))
        # Terminate instance
        terminateStatus = ec2.terminate_instances(InstanceIds = ids)
        
    else:
        # no tag with KILL switch in name return nothing
        return 