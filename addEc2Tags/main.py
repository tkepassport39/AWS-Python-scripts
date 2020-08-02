import boto3
import json

def addTags(user_input, tag_key, tag_value):
    # establish aws connection
    ec2machines = boto3.client('ec2')
    response = ec2machines.describe_instances()

    ids = []
    # add the tags as a dict to this list
    ec2_tags = [
        {
        'Key': tag_key,
        'Value': tag_value
        }
    ]

    for i in response['Reservations']:
        for h in i['Instances']:
            #print(h)
            instanceID = h['InstanceId']
            tagInfo = h['Tags']
            privateIps = h['PrivateIpAddress']

            # only windows machines return a platform field
            try: 
                plat = h['Platform']
            except:
                plat = "linux"

            if user_input == plat:
                print("*****")
                print(f"    Instance ID : {instanceID}")
                print(f"    platform : {plat}")
                print(f"    Private IPs : {privateIps}")
                print(f"    Tags : {tagInfo}")
                print("*****")
                ids.append(instanceID)
    
    if not ids:
        print(f"\nThere are no instances with this OS : {user_input}")
    # create the tags for the specified OS instances
    else:
        #print(f"list of instances : \n{ids}")
        print(f"\nThe instances above ^ will receive the new Tag : \n{ec2_tags}")
        answer = input("Do you want to proceed? (y/n)\n")
        if answer.lower() == "y":
            ec2machines.create_tags(Resources = ids, Tags = ec2_tags)
            print("Tags have been created...")
        else:
            print("You did not select Y therefore quitting...")
            exit

if __name__ == "__main__":
    
    print("***** Welcome *****\n")
    print("Which OS would you like to add Tags?\
         \n1) Windows\
         \n2) Linux")
    # get users input
    user_input = input("> ")
    tag_key = input("what is the Tag Key: \n")
    tag_value = input("What is the Tag value : \n")
    
    if user_input == "1":
        user_input = "windows"
    else:
        user_input = "linux"
    # call the function and send the values
    addTags(user_input, tag_key, tag_value)