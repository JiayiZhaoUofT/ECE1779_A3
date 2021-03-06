import boto3
import botocore
import os
#bucketName = "1779photobucket"
#s3_location = "https://s3-us-west-1.amazonaws.com/1779photobucket/"
bucketName = "a3-resume"
s3_location = "https://s3.amazonaws.com/a3-resume/"

aws_config_arg = {
    'aws_access_key_id': os.environ['aws_access_key_id'],
    'aws_secret_access_key': os.environ['aws_secret_access_key']
}
def s3_upload(filepath, bucketname, filename, acl = "public-read"):
    try:
        # s3 = boto3.client('s3')
        s3 = boto3.client('s3', **aws_config_arg)
        s3.upload_file(filepath,
                       bucketname,
                       filename,
                       ExtraArgs = {
                           "ACL": acl
                       }
        )
    except Exception as e:
        print("Something Happened: ", e)
        return e
    return "{}{}".format(s3_location, filename)

def s3_download(bucketname,keyname,outPutName):
    try:
        s3 = boto3.client('s3')
        s3.Bucket(bucketname).download_file(keyname, outPutName)
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            raise