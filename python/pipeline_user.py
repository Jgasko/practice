import boto3

# make client connection
iam = boto3.client('iam')

# create iam user
response = iam.create_user(
    UserName='github_pipeline_actions',
)

print(response)
