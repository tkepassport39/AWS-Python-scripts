# Terminate EC2 instances with a KILL switch

I used python3 to build the script.

## Before running the script
All you need to do is make sure you rename your instance tag name to start with KILL-xxxx and run the script. The script will then look at all instances in a running state with the tag name KILL-xxx and terminate them. Bye bye EC2 instance. 

## how to run script
```
python3 main.py
```