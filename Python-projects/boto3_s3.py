import boto3

s3_client = boto3.client('s3') 

bucket_name = 'Moses-data-storage' 

response = s3_client.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={
        'LocatedConstraint': 'eu-north-1'
    }
)
print(response) 