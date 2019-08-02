import boto3

s3 = boto3.resource('s3',
                  endpoint_url='http://192.168.2.92:10000',
                  aws_access_key_id='minio',
                  aws_secret_access_key='minio123',
                  region_name='us-east-1')



# Create a new bucket
# s3.create_bucket(Bucket='demo-bucket')


# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)


# Upload a new file
# data = open('hej', 'rb')
# s3.Bucket('demo-bucket').put_object(Key='hej', Body=data)



# Boto 3
#key.put(Metadata={'meta1': 'This is my metadata value'})
#print(key.metadata['meta1'])


object = s3.Object('demo-bucket','hejda.txt')
print (object.key)
print (object.last_modified)
print (object.metadata)
print (object.version_id)


# Add object with metadata
#s3.Object('demo-bucket', 'hejda.txt').put(Body='hello world2', Metadata={'fiiiiioo': 'booooooar'})


#bucket = s3.Bucket('demo-bucket')
#for obj in bucket.objects.all():
#    print(obj.key)
