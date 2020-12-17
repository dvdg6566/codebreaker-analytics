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
	r = [0,0,0]
	res=0
	for i in y:
		if y[i]==100:r[0]+=1
		elif y[i]==0:r[2]+=1
		else: r[1]+=1
		res+=y[i]
	return [res,r]

def res(x):
	for ele in x:
		if ele['username'] == '':
			continue
		t = sm(ele['problemScores'])
		H.append([t,ele['username']])
		# print(ele['username'],t)

resp = users_table.scan()
users = resp['Items']
res(users)

while 'LastEvaluatedKey' in resp:
	resp = users_table.scan(ExclusiveStartKey=resp['LastEvaluatedKey'])
	users = resp['Items']
	res(users)

H.sort()
print("Score Username ACs Partials Failed")
def x(s):
	while(len(s)<15):s+=' '
	return s
for i in H:
	print(int(i[0][0]),x(i[1]),i[0][1][0],i[0][1][1],i[0][1][2])