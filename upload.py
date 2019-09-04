#!/usr/bin/env python

import os
import sys
import datetime
import boto3

S3_BUCKET_NAME = 'YOUR_S3_BUCKET_NAME'
S3_KEY_PREFIX  = '{}/'.format(datetime.date.today().isoformat())  # 'YYYY-MM-DD/'
S3_PRESIGNED_URL_EXPIRES_IN = 7 * 24 * 60 * 60

if len(sys.argv) != 2:
    print('{} FILE'.format(sys.argv[0]))
    exit(1)

filepath = sys.argv[1]
filename = os.path.basename(filepath)
s3key    = '{}{}'.format(S3_KEY_PREFIX, filename)

print('UPLOAD s3://{}/{}'.format(S3_BUCKET_NAME, s3key))

s3 = boto3.client('s3')
s3.upload_file(filepath, S3_BUCKET_NAME, s3key)
url = s3.generate_presigned_url(
    ClientMethod='get_object',
    Params={ 'Bucket': S3_BUCKET_NAME, 'Key': s3key },
    ExpiresIn=S3_PRESIGNED_URL_EXPIRES_IN,
    HttpMethod='GET',
)
print(url)
