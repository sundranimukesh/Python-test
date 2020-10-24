import boto3
s3 = boto3.resource('s3')

#Print out bucket names
#for bucket in s3.buckets.all():
    #print(bucket.name)

#Upload a new file
data = open('muk_myfile.txt', 'rb')  # file mode = binary read
s3.Bucket('advpythonkukesh01').put_object(Key='muk_myfile.txt', Body=data)

# #download file
# s3client = boto3.client('s3')
# s3client.download_file('advpythonalisha01', 'muk_myfile.txt)
