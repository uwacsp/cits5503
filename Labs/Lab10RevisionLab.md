# Practical Worksheet 10

Version: 1.0 Date: 10/10/2018 Author: David Glance

## Learning Objectives

1. IAM policies applied to S3

## Technologies Covered

Ubuntu
AWS
IAM
S3
Python/Boto scripts
VirtualBox

Note: Do this from your VirtualBox VM – if you do it from any other platform (Windows, Mac – you will need to resolve any potential issues yourself)

## Background

The aim of this lab is to write a program that will:

1. Apply a policy to a set of buckets that will allow users with
   specific IAM user names to access it


## [Step 1] Create bucket folders

Write an application to create 3 folders under your a bucket that is
names <Student Number>-bucket

The folders should be:

<Student Number>-bucket/folder1
<Student Number>-bucket/folder2
<Student Number>-bucket/folder3

## [Step 2] Apply policies to the folders to restrict access to specific users

Create a policy that denies users access to folder 1, folder 2 and
folder 3.

folder 1 deny access to anyone apart from you. To do this you can DENY where the
username is not your aws:username.

folder 2 deny access to anyone who doesn't have a username that
includes the domain @folder2.uwa.edu.au

folder 3 deny access to anyone who doesn't have a username that
includes the domain @folder3.uwa.edu.au 

You can write 3 statements to cover permissions for each folder. 

Apply the policy to the bucket.

You shouldn't be able to access folder2 or folder3. 

This will make more sense when you do the exam.




