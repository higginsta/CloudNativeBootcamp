import sys
import boto3

try:
    def main():
        create_s3bucket(bucket_name)

except Exception as e_:
    print(e_)

def create_s3bucket(bucket_name):
    s3_bucket=boto3.client(
        's3',
    )

    bucket = s3_bucket.create_bucket(
        Bucket=bucket_name,
        ACL='private',
        CreateBucketConfiguration={'LocationConstraint':'us-east-2'},
    )

    print(bucket)

bucket_name = sys.argv[1]

if __name__ == '__main__':
    main()
