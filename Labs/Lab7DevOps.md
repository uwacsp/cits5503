# Practical Worksheet 7

Version: 1.2 Date: 15/9/2018 Author: David Glance

## Learning Objectives

1.	Install and configure Fabric
2.	Deploy a server with nginx installed and configured by Fabric
3. 	Deploy Django code using Fabric

## Technologies Covered

Ubuntu
AWS
Python
Git
Fabric

## Background

The aim of this lab is to write a program that will:
 
[1] Background and basics to Fabric
[2] How to automatically deploy a server using Fabric

### [Step 1] Create an EC2 instance

Use your existing code to create an EC2 instance that you will test
your Fabric-based installation on.

### [Step 2] Install and configure Fabric on your VM

NOTE do this on your VirtualBox VM

The easiest way to install fabric is to:

```
pip install fabric
```

You will need to create a config file in ~/.ssh with the contents:

```
Home <ec2instance>
	Hostname <EC2 instance public DNS>
	User ubuntu
	UserKnownHostsFile /dev/null
	StrictHostKeyChecking no
	PasswordAuthentication no
	IdentityFile <path to your private key>
```
	
You can test fabric from the command line:

Remember to rplace <ec2instance> with your EC2 name you used in the
configuration - use your student number to identify resources.

```
python
>>> from fabric import Connection
>>> c = Connection(‘<ec2instance>’)
>>> result = c.run(‘uname -s’)
Linux
>>>
```

### [Step 3] Write a python script to automate the installation of nginx

Write a python script using fabric to set up and configure nginx as
you did for the Django app last week

This will consiste of doing the same commands you would do manually to
configure nginx but using the commands:

sudo("commands go here separated by ;")

and/or

run("Commands go here separated by ;")

## [Step 4] Update the python script to install your Django app

You will copy the files from your local directory to the new EC2 instance. You may find this easier if you create a tar/zip file first of the code and then untar/unzip on the EC2 machine.

Add the necessary commands to configure the virtual environment and
clone your Django app from your local directory - this is basically taking the
instructions you used in that lab and converting them to Fabric commands.

The final command should be the command to run the server - if you add
an '&' at the end it will run the process in the background. Note -
you would normally use Gunicorn to do this not manage.py runserver but
we are keeping it simple.

The documentation for Fabric is here: http://docs.fabfile.org/en/2.0/

## Submission

Submit the python file you wrote with the Fabric commands

### Marking Criteria

Fabric code sets up nginx correctly configured to run a Django App 2 
marks  
Fabric code installs Django app from Github correctly and runs it
correctly 3 marks  



