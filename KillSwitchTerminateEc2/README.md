# Terminate ec2 instances with a KILL switch

All you need to do is make sure you rename your instance tag name to start with KILL-xxxx and run the script. The script will then look at all instances with a running state. Search for any with the tag name KILL-xxx and terminate them. Bye bye ec2 instance. 