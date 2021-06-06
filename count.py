# Output number of submissions by date
import boto3
import json
from time import time
from pprint import pprint
lambda_client = boto3.client('lambda','ap-southeast-1')
dynamodb = boto3.resource('dynamodb','ap-southeast-1')
problems_table = dynamodb.Table('codebreaker-problems')
subs_table=dynamodb.Table('codebreaker-submissions')
users_table=dynamodb.Table('codebreaker-users')
s3 = boto3.client('s3')

def credits_page():
	def find_length(table, primaryKey):
		ans = 0
		resp = table.scan(ProjectionExpression=f'primaryKey')
		subs = resp['Items']
		ans += len(subs)

		while 'LastEvaluatedKey' in resp:
			resp = table.scan(ExclusiveStartKey=resp['LastEvaluatedKey'],ProjectionExpression=f'primaryKey')
			subs = resp['Items']
			ans += len(subs)
		return ans

	def getSubmissionId():
		subId = s3.get_object(Bucket='codebreaker-submission-number',Key=f'submissionNumber.txt')['Body'].read().decode('utf-8')
		subId = int(subId)
		subId = 100*round(subId/100)
		return subId

	problems = find_length(problems_table,'')
	users = find_length(users_table,'')
	subs = getSubmissionId()

	return {'users':users,'problems':problems,'subs':subs}

print(credits_page())