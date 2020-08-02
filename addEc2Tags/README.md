# Add EC2 tags to specific OS instances

This script is meant for creating a tag for all instance of specific OS (Linux or Windows). This script will run against all instances that are in either 'running' or 'stopped' state.

When you run the script you will be greeted with options (example below)
```
***** Welcome *****

Which OS would you like to add Tags?         
1) Windows         
2) Linux
> 1
```

In the example, I choose 1 for Windows. Next you will need to input the tag key and value (example below)
```
what is the Tag Key: 
test
What is the Tag value : 
test answer
```

The script will look through your instances and search only those for the OS you specified. It will print them out on your terminal with other current information such as: instanceID, platform, private IPs, and Tags (example below)
```
*****
    Instance ID : i-010000000000
    platform : windows
    Private IPs : 11.1.3.5
    Tags : [{'Key': 'Name', 'Value': 'ANT-test-2016'}]
*****
*****
    Instance ID : i-011111111111
    platform : windows
    Private IPs : 1.2.3.4
    Tags : [{'Key': 'Name', 'Value': 'ANT-test2-2016'}]
*****
```

Finally, you will be prompted if you would like to proceed with creating the tags to the following instances. If you answer with 'y', it will execute the create tag, else it will exit the script (example below)
```
The instances above ^ will receive the new Tag : 
[{'Key': 'test', 'Value': 'test answer'}]
Do you want to proceed? (y/n)
y
```