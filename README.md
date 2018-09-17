# S3-Backup

Python Script that allows you to automatically upload files to S3 from a desred file folder.  

## Prerequisites

The steps below have are written with the assumption that you have an AWS account and a bucket already setup in S3.
If not, visit [Amazon AWS S3 Docs](https://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html) to learn how to create a bucket. 

## Setup 

  1. Download S3_Backup.py and open in text editor.
  2. Edit AWS Key ID, Secret Key, and Bucket Name to match your own.  
  ```
  ACCESS_KEY_ID = 'xxxxxxxxxxxxxxxxxxxx'
  ACESSS_SECRETY_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx' 
  BUCKET_NAME = 'bucketxxx' 
  ```
  3. Edit line 22 with the desired local file folder. 
  ```
  source = ''	
  ```
  4. Edit line 26 with the desired file type.
  ```
	if filepath.endswith(".pdf"):
  ```
  
## Automation  

[Mac OSX](https://blog.macsales.com/42196-macos-101-how-to-automate-tasks-on-your-mac)

[Windows](https://www.dummies.com/computers/pcs/how-to-create-a-task-to-run-a-program-in-windows-task-scheduler/)
 
  
# You're All Set!
