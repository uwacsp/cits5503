# Practical Worksheet 4

Version: 1.2 Date: 23/08/2018 Author: David Glance

## Learning Objectives

1. IAM policies applied to S3
2.	KMS Key Management System – creating keys and using the key for symmetric encryption
3.	Using AES Encryption for client and server side encryption

## Technologies Covered

Ubuntu
AWS
AWS KMS
AES Encryption
Python/Boto scripts
VirtualBox

Note: Do this from your VirtualBox VM – if you do it from any other platform (Windows, Mac – you will need to resolve any potential issues yourself)

## Background

The aim of this lab is to write a program that will:

[1] Apply a policy to your bucket to allow only you as a user to access it
[1] Create a key in KMS and use it to encrypt files on the client before uploading to S3 and decrypt them after downloading from S3
[2] Implement AES using python and test the difference in performance between the KMS solution and the local one. 

## [Step 1] Apply policy to restrict permissions on bucket

Write an application to apply the following policy to the bucket you created in the last lab
to allow only your username to access the bucket. Make the appropriate
changes (folders, username, etc) to the policy as necessary.

```

{ 
   "Version": "2012-10-17", 
   "Statement": {
	   ”Sid": ”AllowAllS3ActionsInUserFolderForUserOnly", 
        "Effect": ”DENY", 
        "Action": “s3:*", 
        "Resource": " arn:aws:s3:::<studentnumber>/folder1/folder2/*",
        ”Condition”: {
            “StringNotLike”: {
                “aws:username”: “nnnn@student.uwa.edu.au”
             }
        } 
    } 
}


```

You can test it by applying the policy to a single folder and using a
username that is not your own. Confirm that you no longer have access
to that folder's contents. 


## [Step 2] AES Encryption using KMS

Write an application to create a KSM key (remember to use your student
number to identify the key)
Choose an appropriate alias for the key and make your username the
administrator and user.

In your CloudStorage application add the ability to encrypt and decrypt the files you find using the KMS Client apis of boto3. 

**Optional**

Encrypt only operates on 4 KB of data and so if you were to use this as a means of encrypting larger files, you would have to encrypt the file in chunks and reverse the process for decryption.

## [Step 3] AES Encryption using local python library pycryptodome

Create another version of your CloudStorage program that uses the python library pycryptodome to encrypt and decrypt your files

You can use the example code for doing this from <HERE>

What is the performance difference between using KMS and using the custom solution?


##Submission

Submit the python code files you wrote


