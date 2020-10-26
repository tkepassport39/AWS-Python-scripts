# Search Workspace IP

**NOTE**: You can run this using Linux or MacOS

## Problem
When you use the AWS Workspace console you can't search by IP address

## Solution
I created this python code to search the workspaces for a single IP address. The code search will output the workspace: Ip address, username, and state.

## How to Execute
In our AWS tenant via SSO, we are able to copy a quick programmatic access code. Copy the AWS environment variables and paste into your terminal.

Download the Repo. In the terminal, execute the following command (along with the IP address of the workspace you are looking for): 
```
python3 main.py 1.2.3.4
```