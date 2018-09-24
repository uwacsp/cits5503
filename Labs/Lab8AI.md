# Practical Worksheet 8

Version: 1.1 Date: 17/9/2018 Author: David Glance

## Learning Objectives

1.	Build out a binary classification model using Amazon Machine Learning
2.	Explore parameters that affect the model’s training and evaluation process

## Technologies Covered

Ubuntu
AWS
Amazon Machine Learning
boto3
Python

## Background

The aim of this lab is to write a program that will:

[1] The principles of the binary classifier using the AWS Machine Learning tutorial 
[2] Understand how the classifier uses banking data to decide who is likely to open a deposit account
[3] Understand how to interpret the predictive performance of the model and set score thresholds

Note that this is essentially the programmatic version of the
demonstration shown online that made use of the AWS UI. It requires
you to understand what was happening at each step. 

## Get Data

### [Step 1] Download data files

Historical data for products like bank term deposit

https://s3.amazonaws.com/aml-sample-data/banking.csv

Data to test whether people will get a term deposit

https://s3.amazonaws.com/aml-sample-data/banking-batch.csv

Put these files in your S3 bucket

The explanation of the attributes in this data and how they are
predictive is here:

https://www2.1010data.com/documentationcenter/prod/Tutorials/MachineLearningExamples/BankMarketingDataSet.html


## Write a python script to create a model 

### [Step 2] Create a Data Source

Use boto3's machine learning call 'create\_data\_source\_from_s3

You will need to create two data sources - one that is used for
training and the other that is used for testing. 

Use defaults where you can. ComputeStatistics needs to be set to true.

Use your student number to identify the data source

Use the schema listed below

### [Step 3] Create the model

Use create\_ml\_model to create a machine learning model from the data
source that you created for training

Use BINARY as the category of supervised model.

Use your student number to identify the ml model

### [Step 4] Evaluate the model

use create\_evaluation to evaluate the model using the data source you
created for evaluation.


### [Step 5] Get the details of the Performance Metrics from the evaluation

use get\_evaluation to get data about the evaluation including the
Performance Metrics from your evaluation.

### [Step 6] Optional: Set the cutoff of the model to 3% and test the banking-batch.csv file



NOTE do this on your VirtualBox VM


## Submission

Submit the python file you wrote.

** REMEMBER** we check that you have actually created data sources and
   models - you will not be awarded any marks if you have not actually
   developed and run your code.


** schema file **

```
{
  "excludedAttributeNames": [], 
  "version": "1.0", 
  "dataFormat": "CSV", 
  "rowId": null, 
  "dataFileContainsHeader": true, 
  "attributes": [
    {
      "attributeName": "age", 
      "attributeType": "NUMERIC"
    }, 
    {
      "attributeName": "job", 
      "attributeType": "CATEGORICAL"
    }, 
    {
      "attributeName": "marital", 
      "attributeType": "CATEGORICAL"
    }, 
    {
      "attributeName": "education", 
      "attributeType": "CATEGORICAL"
    }, 
    {
      "attributeName": "default", 
      "attributeType": "CATEGORICAL"
    }, 
    {
      "attributeName": "housing", 
      "attributeType": "CATEGORICAL"
    }, 
    {
      "attributeName": "loan", 
      "attributeType": "CATEGORICAL"
    }, 
    {
      "attributeName": "contact", 
      "attributeType": "CATEGORICAL"
    }, 
    {
      "attributeName": "month", 
      "attributeType": "CATEGORICAL"
    }, 
    {
      "attributeName": "day_of_week", 
      "attributeType": "CATEGORICAL"
    }, 
    {
      "attributeName": "duration", 
      "attributeType": "NUMERIC"
    }, 
    {
      "attributeName": "campaign", 
      "attributeType": "NUMERIC"
    }, 
    {
      "attributeName": "pdays", 
      "attributeType": "NUMERIC"
    }, 
    {
      "attributeName": "previous", 
      "attributeType": "BINARY"
    }, 
    {
      "attributeName": "poutcome", 
      "attributeType": "CATEGORICAL"
    }, 
    {
      "attributeName": "emp_var_rate", 
      "attributeType": "NUMERIC"
    }, 
    {
      "attributeName": "cons_price_idx", 
      "attributeType": "NUMERIC"
    }, 
    {
      "attributeName": "cons_conf_idx", 
      "attributeType": "NUMERIC"
    }, 
    {
      "attributeName": "euribor3m", 
      "attributeType": "NUMERIC"
    }, 
    {
      "attributeName": "nr_employed", 
      "attributeType": "NUMERIC"
    }, 
    {
      "attributeName": "y", 
      "attributeType": "BINARY"
    }
  ], 
  "targetAttributeName": "y"
}

```
