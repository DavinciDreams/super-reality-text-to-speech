import boto3
s3=boto3.client("s3")
a=s3.upload_file("texts.txt","voice-bucket-1128","text.txt")
print(a)
