import boto3

# Retrieve the list of existing buckets
s3 = boto3.client('s3', region_name="RegionOne", verify=False,
                        endpoint_url="https://localhost",
                        aws_access_key_id="2dff69e63984445c819a1a3c3328bf8b",
                        aws_secret_access_key="9bbe336440c94b079a19bb7b89aec749")
response = s3.list_buckets()
print response