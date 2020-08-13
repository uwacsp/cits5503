# Practical Worksheet 5

Version: 1.1 Date: 28/08/2018 Author: David Glance

## Learning Objectives

1.	Networking and NAT
2.	Setting up an Application Load Balancer

Technologies Covered

Ubuntu
AWS
AWS ELB
Networking
NAT
Python/Boto scripts
VirtualBox

Note: Do this from your VirtualBox VM – if you do it from any other platform (Windows, Mac – you will need to resolve any potential issues yourself)

## Background

The aim of this lab is to write a program that will:

[1] Understand how to configure different network arrangements to gain and control access to computers and other networked resources
[2] Understand IP addressing and CIDR and the meaning of TCP and UDP ports

## Networking 

### [Step 1] Configure inbound IP on VirtualBox VM

This can be done in a number of ways, but we are going to use NAT port mapping. When a VM is created in VirtualBox, it defaults to creating a single NAT interface

[1] The VM does not have to be stopped for this but it isn’t a bad idea to make changes when it is stopped.
[2] In the VirtualBox Manager, select the VM you want to configure, then click Settings (Golden Gear Cog) and Network. Adapter 1 should be configured as NAT. Click on Advanced and then Port Forwarding. Set up 2 rules:
   [a] Use the localhost host IP 127.0.0.1 and host port 2222 and map that to Guest Port 22
   [b] Add a similar rule mapping Host Port 8080 to Guest Port 80

[3] Testing! You can test the NAT’d ports by running your docker app and seeing if you can access it from your computer – the url will be http://127.0.0.1:8080 
Enable ssh to the VM by installing **sshd** as follows:

```
sudo apt install tasksel
sudo tasksel install openssh-server
```

start the ssh service by:

```
sudo service ssh start
```

you can stop it using:

```
 sudo service ssh stop
 ```
 
To ssh to the VM, open a terminal on your PC (or use Putty) and ssh as

```
ssh -p 2222 <usermame>@127.0.0.1
```

You should be prompted for your password

### [Step 2] Setting up an Application Load Balancer

The aim of this part of the lab is to create an application load
balancer and load balance requests to 2 EC2 instances. As there is a
restriction of only 20 load balancers per region, we are going to
relax the requirement to create instances and the ELB in the
ap-southeast-2 region.

Before running the application to create a load balancer and
instances, check how many are running in a particular region. Select a
region that has capacity.

**Remember** Delete the load balancer immediately after completing the
lab.

### USE YOUR STUDENT NUMBER TO IDENTIFY ALL RESOURCES

Objective: Write an application to create 2 EC2 instances in two availability zones, create an application load balancer and load balance HTTP requests to the 2 instances. 

You will need to do some manual intervention to get Apache 2 installed and the index.html file edited. Do this after you have created the instances and ALB. In a future lab you will learn how this could be done through a program as well.

[1] Write a Boto3 application to create 2 EC2 instances in two
different availability zones of a specific region. Name the instances
<student number>_zone

Note: You will need to use v2 of the ELB interface:

```
client = boto3.client('elbv2')
```

[2] Create the Application Load Balancer.

The steps involved in this are:

[a] Create the load balancer and specify the two region subnets and a
security group

[b] Create a target group using the same VPC that you used to create
the instances - note the ARN that is output

[c] Register targets in the target group

[d] Create a listener with a default rule Protocol: HTTP and Port 80
forwarding on to the target group

Try and access the EC2 instance using the public IP address of the load balancer in a browser. The load balancer will not be working at this point because Apache 2 is not installed. Check this and then:

On each instance, install apache2

```
sudo apt install apache2
```

Edit the /var/www/html/index.html file to report the instance name

Now Verify that the load balancer is working. You should be able to
access both of the EC2 instances by refreshing the page.


*IMPORTANT* When finished. Delete the Load balancer, target group,
listener and EC2 instances.

 
