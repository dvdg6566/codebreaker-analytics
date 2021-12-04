STATEMENTS_BUCKET_NAME = 'codebreaker-statements'

import boto3
s3 = boto3.resource('s3')

def makePrivate(statement):
	object_acl = s3.ObjectAcl(STATEMENTS_BUCKET_NAME,'1821.pdf')
	response = object_acl.put(ACL='private')

def makePublic(statement):
	object_acl = s3.ObjectAcl(STATEMENTS_BUCKET_NAME,'1821.pdf')
	response = object_acl.put(ACL='public-read')

# Need to change when
# a) Problem is changed to analysisVisible
# b) Problem is changed to not analysisVisible
# c) When statement is uploaded and not analysisVisible