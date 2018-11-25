import boto3
import botocore

bucketName = "a3-resume"
s3_location = "https://s3.amazonaws.com/a3-resume/"

def s3_upload(filepath, bucketname, filename, acl = "public-read"):
    try:
        s3 = boto3.client('s3')
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