# Terminate EC2 instance with Lambda Function

**GOAL:** Create a CloudWatch event that will only get triggered when the "Name" tag value is update with a key word "KILL". Once the CloudWatch event is fired, it will invoke the Lambda function running the python script to terminate the instance.

## How to setup

### Setup a Lambda function
* In the AWS Lambda console
* Click on Create Function
* Select Author from scratch
* Add a name to your function, example "TestEc2Termination"
* Select Python 3.6+ for runtime
* Under Role Name, create a new role name (i.e "role-auto-stop-ec2")

Lambda will create an environment folder with this "TestEc2Termination" name and below it you will find your lambda_function.py.

You may copy and paste the lambda_function.py code I have in this repo to the editor and Save.

### Setup IAM permissions
* In the IAM console
* Select Roles
* Search for the name of the role you created during the Lambda Function setup
* For this demo purpose, I attached the policy "AmazonEC2FullAccess" to give the Lambda function enough permissions to execute the termination command on the instances. Part of my plan to improve this, is to create a granular policy to give explicit permissions to only perform that 1 function.

### Create a CloudWatch event rule
To create a Cloudwatch event rule that will match the tag change on a instance resource event and point to our lambda function. Do the following: 
* In the CloudWatch Events Console
* Choose Create Rule
* Next to "Event Pattern Preview", click Edit 
* Paste the following JSON code
    ```
    {
    "source": [
        "aws.tag"
    ],
    "detail-type": [
        "Tag Change on Resource"
    ],
    "detail": {
        "service": [
        "ec2"
        ],
        "resource-type": [
        "instance"
        ]
    }
    }
    ```
* Under Targets, select the name of your Lambda function
* Give this new rule a name "ec2-lambda-rule" and create rule

### Grant CloudWatch Events permissions to invoke Lambda 
You can use the aws CLI to grant CloudWatch event permissions to invoke your Lambda.

Type the following command (update the region and ARN's in: function-name and source-arn with your custom information):
```
aws lambda add-permission --statement-id "TrustCWEToInvokeAutoEC2Termination" \
--action "lambda:InvokeFunction" \
--principal "events.amazonaws.com" \
--function-name "arn:aws:lambda:us-east-1:123456789012:function:AutoEC2Termination" \
--source-arn "arn:aws:events:us-east-1:123456789012:rule/ec2-instance-rule" \
--region us-east-1
```

### You are all set! 
You can try and test it out by adding to one of your instances Name tag value the "KILL" switch word. After a few seconds you should see your instance status change to stopping and eventually terminated.