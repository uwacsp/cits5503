# Practical Worksheet 1 Version: 1.1 Date: 6/08/2018 Author: David Glance

## Learning Objectives

1. Register for an AWS account and explore the user interface
1. Obtain API keys and secret
1. Install VirtualBox and an Ubuntu 18.04 VM
1. On the Ubuntu 18.04 instance
1. Install AWS CLI on VM
1. Install a virtual environment with Python 3.6
1. Configure the AWSCLI environment with API details and default region
1. Verify awscli is working and write a python boto script to emulate a awscli command

## Technologies Covered

Ubuntu

AWS

VirtualBox Python/Boto/awscli/bash scripts

NOTE: Whilst some of the work that has been outlined in the labs can be done on lab machines, it is strongly recommended that you use your own laptop for this work. Likewise, you can create virtualenvs on your laptop but it is recommended that you do this on the VM using VirtualBox. Instructions are only provided for this configuration.

## AWS Accounts and Log In
### [1] You will have an account created for you on AWS.

Your username is <student number>@student.uwa.edu.au Password details will be provided separately.

The login is here: https://cits5503.signin.aws.amazon.com/console

You will need to change your password on login – you are encouraged to do that as quickly as possible.

Remember that resources cost money and you should only leave things running as long as you need to complete the practical work. Machines or other resources found running for any significant period of time will be terminated. Persistent offenders will be locked out of the system.

You are able to create your own account using a credit card and utilise free resource tiers on AWS.

### [2] Make sure you can log into your account
### [3] Search and open Identity Access Management

Click on your user account. Click Security Credentials tab: Create access key and make a note of the Access key ID and the secret access key – you will need these for programmatic access to resources.

NOTE: Treat the Access key ID and secret very carefully. If stolen, these details allow someone to create large numbers of resources and do other things with the account

## Virtual Box and Ubuntu VM

### [1] Download and install the appropriate version of VirtualBox

https://www.virtualbox.org/wiki/Downloads

### [2] Download Ubuntu 18.04.1 LTS iso 

https://www.ubuntu.com/download/desktop (approximately 1.62GB)

### [3] Setup VM

Follow the instructions here to set up the VM using the Ubuntu image – remember that when you create the virtual disk, you can put it on an external USB drive 

https://medium.com/@tushar0618/install-ubuntu-16-04-lts-on-virtual-box-desktop-version- 30dc6f1958d0

## AWSCLI, Boto and Python 3.6

### [1] Install Python 3.6

```
sudo add-apt-repository ppa:jonathonf/python-3.6 
sudo apt-get update
sudo apt-get install python3.6
```

### [2] Install a virtual environment with python3.6

```
sudo add-apt-repository ppa:jonathonf/python-3.6 sudo apt-get update
sudo apt-get install python3.6
# Note: the following command is not necessary for those using Ubuntu 16.04 

sudo apt-get install python3-distutils
cd ~
python3.6 -m venv virtualenv --without-pip cd virtualenv/
source bin/activate
sudo apt install curl
curl https://bootstrap.pypa.io/get-pip.py | python3
```

When you type python -V you will get 3.6

Remember that whenever you want to use this environment, you need to do a source bin/activate
You can put this into your .bashrc file (search for how)

### [3] Install awscli 

Instructions are here:

https://docs.aws.amazon.com/cli/latest/userguide/installing.html

```
pip install awscli --upgrade
```

if you have any issues, sometimes you also have to install it using pip3 [4] Configure aws using aws configure NOTE use your own credentials!

https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html

```
aws configure
AWS Access Key ID [None]: AKIAIOSFODNN7EXAMPLE
AWS Secret Access Key [None]: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY 
Default region name [None]: ap-southeast-2
Default output format [None]: json
```

NOTE if you have any issues with clipboard copy paste from your machine to the VM, you have to enable clipboard copying from the Devices menu of VirtualBox. You will need to run and install the VirtualBox Guest Additions first from the same menu (On 18.04 you need to install build tools first sudo apt install linux-headers-$(uname -r) build-essential dkms
)

### [5] Install boto3

```
pip3 install boto3
```

You are now set!!

NOTE Choice of editor on Ubuntu. My favourite editor is Emacs – Vi is already installed – you have to install Vim or Emacs if you need it. You can also install other editors – just be careful of memory

## Exploring and testing the environment
### [1] Test the aws environment by running:

```
aws ec2 describe-regions –output table
```

### [2] Test the python environment

```
python3
>>> import boto3
>>> ec2 = boto3.client(‘ec2’)
>>> response = ec2.describe_regions() >>> print(response)
```

This will create an un-tabulated response.

### [3] Put this code into a python file and tabulate the print to have 2 columns with Endpoint and RegionName

### [4] Spend some time looking at VirtualBox and especially the configuration for its CPU, RAM, Disk, Network























