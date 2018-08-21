# Practical Worksheet 4

Version: 1.1 Date: 20/08/2018 Author: David Glance

## Learning Objectives

1.	KMS Key Management System – creating keys and using the key for symmetric encryption
2.	Using AES Encryption

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

[1] Create a key in KMS and use it to encrypt files on the client before uploading to S3 and decrypt them after downloading from S3
[2] Implement AES using python and test the difference in performance between the KMS solution and the local one. 

## [Step 1] AES Encryption using KMS

Using the IAM console, go into Encryption Keys and create a key
Choose an appropriate alias for the key
Add yourself as the key administrator and choose the user you created above as the key user

In your CloudStorage application add the ability to encrypt and decrypt the files you find using the KMS Client apis of boto3. 

Encrypt only operates on 4 KB of data and so if you were to use this as a means of encrypting larger files, you would have to encrypt the file in chunks and reverse the process for decryption.

## [Step 2] AES Encryption using local python library pycryptodome

Create another version of your CloudStorage program that uses the python library pycryptodome to encrypt and decrypt your files

You can use the example code for doing this from <HERE>


Submission

Submit the python code files you wrote


