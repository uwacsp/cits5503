# Practical Worksheet 9

Version: 1.0 Date: 4/10/2021 Author: Camilo Pestana

## Learning Objectives

1. Learn more about AI and Machine Learning services available on AWS.
2. Use boto3 to get hands-on experience on using useful AI services in AWS for Natural Language Processing (NLP)/ Natural Language Understanding (NLU) and Computer Vision.

## Technologies Covered
- Ubuntu
- AWS Comprehend
- AWS Rekognition
- boto3
- Python

## Background

The aim of this lab is to write a serie of scripts that will test the main features of AWS Comprehend and AWS Rekognition.

## AWS Comprehend

AWS Comprehend offerts different services to analyse text using machine learning. With Comprehend API, you will be able to perform common NLP tasks such as sentiment analysis, or simply detecting the language from the text.

"Amazon Comprehend can discover the meaning and relationships in text from customer support incidents, product reviews, social media feeds, news articles, documents, and other sources. For example, you can identify the feature that’s most often mentioned when customers are happy or unhappy about your product."
[Source](https://ap-southeast-2.console.aws.amazon.com/comprehend/v2/home?region=ap-southeast-2#welcome)

For example, to detect the language used in a given text using boto3 you can use the following code:
```python
import boto3
client = boto3.client('comprehend')

# Detect Entities
response = client.detect_dominant_language(
    Text="The French Revolution was a period of social and political upheaval in France and its colonies beginning in 1789 and ending in 1799.",
)

print(response['Languages'])
```

By executing that code we will get something like this:
```
Output:
[{'LanguageCode': 'en', 'Score': 0.9961233139038086}]
```
This means that the detected language is 'en' (English) and has a confidence in the prediction greater than 0.99. 

*Note*: Remember that often in machine learning the confidence score is expressed as a value in the range [0,1] being zero the lack of certainty and 1 being totally certain of the prediction.

### [Step 1] Detecting Languages from text

#### [Step 1.1] Modify code
Based on the previous code, create a script that can recognized different languages. However, instead of language code (e.g., 'en' for English or 'it' for italian) it should be return the message "<predicted_language> detected with xx% confidence" where <predicted_language> correspond to the name of the language in English and the confidence (x.xx) is given as a percentage. For the previous example the result should look like this:
```
Output:
English detected with 99% confidence
```
#### [Step 1.2] Test your code with other languages

Test your code using the following texts in different languages:

**Spanish:**
"El Quijote es la obra más conocida de Miguel de Cervantes Saavedra. Publicada su primera parte con el título de El ingenioso hidalgo don Quijote de la Mancha a comienzos de 1605, es una de las obras más destacadas de la literatura española y la literatura universal, y una de las más traducidas. En 1615 aparecería la segunda parte del Quijote de Cervantes con el título de El ingenioso caballero don Quijote de la Mancha."

**French:**
"Moi je n'étais rien Et voilà qu'aujourd'hui Je suis le gardien Du sommeil de ses nuits Je l'aime à mourir Vous pouvez détruire Tout ce qu'il vous plaira Elle n'a qu'à ouvrir L'espace de ses bras Pour tout reconstruire Pour tout reconstruire Je l'aime à mourir"
[From the Song: "Je l'Aime a Mourir" - Francis Cabrel ]

**Italian:**
"L'amor che move il sole e l'altre stelle."
[Quote from "Divine Comedy" - Dante Alighieri]

#### [Step 2] Sentiment Analysis

Sentiment analysis (or opinion mining) uses NLP to determine whether data is positive, negative or neutral. Sentiment analysis is often performed on textual data to help businesses monitor brand and product sentiment in customer feedback, and understand customer needs.

**Task:** Use boto3 and AWS comprehend to create a python script for sentiment analysis. Use the previous 3 texts to test the script.

#### [Step 3] Repeat steps from [Step 2] for detecting entities.
Question 1: In your words describe what entities are.

#### [Step 4] Repeat steps from [Step 2] for detecting keyphrases.
Question 1: In your words describe what keyphrases are.

#### [Step 5] Repeat steps from [Step 2] for detecting syntax.
Question 1: In your words describe what keyphrases are.

## AWS Rekognition

AWS Rekognition is the service of AWS that allows you to perform machine learning tasks on images.

Currently, given an image, AWS Rekognition allows you to:
1. **Label Recognition**: Automatically label objects, concepts, scenes, and actions in your images, and provide a confidence score.
2. **Image Moderation**: Automatically detect explicit or suggestive adult content, or violent content in your images, and provide confidence scores.
3. **Facial Analysis**: Get a complete analysis of facial attributes, including confidence scores
4. **Detect Text from an image**: Automatically detect and extract text in your images.

#### [Step 6] In an S3 bucket add some images to test your algorithms.
1. Add an image in an urban setting (To test later your label recognition script)
2. Add an image of a person on the beach (To test Image moderation)
2. Add an image with people showing their faces (For facial analysis)
3. Add an image with text (Extract text from an image)

#### [Step 7] Create scripts using boto3 and rekognition to test label recognition, image moderation, facial ananalysis and extracting text from images.

You can try the demos [here](https://ap-southeast-2.console.aws.amazon.com/rekognition/home?region=ap-southeast-2#)


Lab Assessment:
This semester all labs will be assessed as "Lab notes". You should follow all steps in each lab and include your own comments. In addition, include screenshots showing the output for every commandline instruction that you execute in the terminal and any other relevant screenshots that demonstrate you followed the steps from the corresponding lab. Please also include any linux or python script that you create and the corresponding output you get when executed.
Please submit a single PDF file. The formatting is up to you but a well organised structure of your notes is appreciated.
