import boto3
s3 = boto3.resource('s3')

data = open('muk_myfile.txt', 'rb')  # file mode = binary read
s3.Bucket('advpythonmukesh01').put_object(Key='muk_myfile.txt', Body=data)
