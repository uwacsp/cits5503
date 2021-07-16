## Assignments CITS5503 2021

## Week 1

[1.0] [5 points] The evolution of Cloud Computing has been compared to the evolution of electricity supply as a utility. Describe specific problems that Cloud Computing solves as compared to businesses running their own data centres.

[2.0] [5 points] Describe the different categories of services (XaaS) cloud computing can provide with specific examples of each service.

[3.0] [10 points] An established financial company is about to launch their new banking application. Give 5 reasons why the company should use their own data centre rather than cloud computing.

[4.0] [20 points] Describe the concepts of vertical and horizontal scale. Describe 2 different ways in which you could scale a web application horizontally. Describe a potential architecture to scale the database to handle the scaling out of the web servers.

## Week 2

[5.0] [20 points] Describe the steps which you would take on AWS and the decisions that would need to be made to create, configure and run a Virtual Machine Instance.

[6.0] [10 points] Describe EBS and what features it offers

## Week 3

[7.0] [10 points] Describe what virtualisation is and describe the characteristic attributes of the different types of virtualisation (Language, Operating System and Hardware).

[8.0] [10 points] Describe what containers are with reference to Docker and discuss their similarities and differences from operating system virtualisation perspective as provided by VirtualBox.

## Week 4

[9.0] [5 points] You are asked to store data about music albums in a DynamoDB table. For each album, you need to record the title of the album and the artist name. Describe the commands you would use to create a table to store such information and write an entry to that table in DynamoDB.

[10.0] [5 points] Describe how S3 handles consistency of objects and how this approach affects the state of objects when they are read using a GET.

[11.0] [5 points] What are the core components of DynamoDB

[12.0] [5 points] When a Bucket is created, AWS allows the specification of a number of features that can be managed. What are the key properties and features?

## Week 5

[13] [20 points] An organisation has 5 departments and has separated out each of the IAM users into separate groups using paths following the pattern companybucket/department1/*, companybucket /department2/*, companybucket /department3/* etc.

Their IAM account names follow the pattern user@department1.company.com, user@department2.company.com etc.

You are tasked with securing a bucket that contains a folder for each of 5 departments in an organisation. Only people within a department can write to their own folder. Everyone can read from all folders.  

Discuss the principles that you would use to create a policy that would achieve this objective.

Write the policy as a JSON file that you would use.

Note: you can have individual statements for each department.

[14] [5 points]  What aspects of security does the OSI Security Architecture X.800 standard cover? Which particular components of this standard does AWS Identity and Access Management deal with?

[15] [5 points] Name 3 of the keys that you would find in a Policy. Explain their role. An example of a key is “Version” that specifies the version of the policy syntax and is normally “Version”: “2012-10-17”

## Week 6

[16] [10 points] Discuss the reasons why you would use Application Load Balancing and how this would be set up to load balance a Python Django application. Specifically, describe the configuration of the Listener and Target Group running the Python Django application.

[17] [10 Points] Describe 2 ways in which security is implemented in AWS networks at the network level. What are the similarities and differences between these 2 security implementations?

## Week 8

[18] [10 points] When an EC2 instance is created in AWS, it is assigned to a region and a Virtual Private Cloud (VPC). Describe how network addresses are allocated to a VPC and sub-networked when an EC2 instance is created. How is the EC2 connected to other machines and to the Internet?

[19] [10 points] What is DevOps and describe how you would implement the automation of creation of machines, configuration of software and deployment of application programs using AWS.

## Week 9

[20] [10 points] Describe the 3 different types of Machine Learning Models that AWS Machine Learning allows you to use and describe examples of the types of questions you could answer with each one.

[21] [10 points] Describe the different ways in which a Microservice Architecture can be implemented on AWS and what the benefits of this approach might be. How could authentication and authorisation be handled in this approach?

## Week 10

[22] [20 points] [a] [15 points] You have been asked to create a project plan for the new machine learning model your company has asked you to build. List the main tasks and sub-tasks you would need to complete to create the model on AWS. [b] [5 points] How would you measure the accuracy of the model you created?
