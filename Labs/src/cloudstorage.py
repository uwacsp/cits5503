import os
import boto3
import base64

# ------------------------------
# CITS5503
#
# cloudstorage.py
#
# skeleton application to copy local files to S3
#
# Given a root local directory, will return files in each level and
# copy to same path on S3
#
# ------------------------------ 


ROOT_DIR = '.'
ROOT_S3_DIR = 'STUDENTNUMBER-cloudstorage'


s3 = boto3.resource("s3")

bucket_config = {'LocationConstraint': 'ap-southeast-2'}

def upload_file(folder_name, file, file_name):

    print("Uploading %s" % file)


# Main program
# Insert code to create bucket if not there

try:

    print(response)
except Exception as error:
    pass


# parse directory and upload files

for dir_name, subdir_list, file_list in os.walk(ROOT_DIR, topdown=True):
    if dir_name != ROOT_DIR:
        for fname in file_list:
            upload_file("%s/" % dir_name[2:], "%s/%s" % (dir_name, fname), fname)


print("done")
