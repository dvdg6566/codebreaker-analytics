# Analysis mode rankings

import boto3
import json
lambda_client = boto3.client('lambda','ap-southeast-1')
dynamodb = boto3.resource('dynamodb','ap-southeast-1')
problems_table = dynamodb.Table('codebreaker-problems')
subs_table=dynamodb.Table('codebreaker-submissions')
users_table=dynamodb.Table('codebreaker-users')

H = []

def sm(y):
	res=0
	for i in y:
		res+=y[i]
	return res

def res(x):
	for ele in x:
		if ele['username'] == '':
			continue
		t = sm(ele['problemScores'])
		H.append([t,ele['username']])
		print(ele['username'],t)

resp = users_table.scan()
users = resp['Items']
res(users)

while 'LastEvaluatedKey' in resp:
	resp = users_table.scan(ExclusiveStartKey=resp['LastEvaluatedKey'])
	users = resp['Items']
	res(users)
H.sort()
for i in H:
	print(int(i[0]),i[1])