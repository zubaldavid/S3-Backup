# David Zubal
# Python Manipulation of S3 bucket
import datetime
import boto3
import os
from os import walk
from botocore.client import Config

now  = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

ACCESS_KEY_ID = 'xxxxxxxxxxxxxxxxxxxx'				 # Key ID
ACESSS_SECRETY_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'  # Security Key
BUCKET_NAME = 'bucketxxx'                                        # Bucket requested in s3 to store data

s3 = boto3.resource(                                             # Connecting to S3 Bucket
	's3',
	aws_access_key_id=ACCESS_KEY_ID,
	aws_secret_access_key=ACESSS_SECRETY_KEY,
	config = Config(signature_version='s3v4')
)
print("\nUploading files to S3...\n")
source = ''							 # Source root folder
for root, directory, files in os.walk(source):                   # Walk through root folder
	for file in files:
		filepath = root + "\\" + file                    # Concatenate root address with file name
		if filepath.endswith(".pdf"):                    # Find suffix of file requested
			print(file)
			data = open(filepath,'rb')
			directory = now + "/" + file
			s3.Bucket(BUCKET_NAME).put_object(Key= directory, Body=data)  # Key is name that will be stored in bucket

print ("\nDone")
