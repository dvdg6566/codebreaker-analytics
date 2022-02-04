# Rank users by number of submissions

import boto3
import json
lambda_client = boto3.client('lambda','ap-southeast-1')
dynamodb = boto3.resource('dynamodb','ap-southeast-1')
problems_table = dynamodb.Table('codebreaker-problems')
subs_table=dynamodb.Table('codebreaker-submissions')
KEY = 'problemName'
PE = 'problemName,username'
hist={}
BLOCKED = ['ryangohca', 'kym', 'JustAWallaby', '0rang3', 'jamessng', 'jamielim', 'bensonlzl', 'oolimry', 'shenxy13']

resp = subs_table.scan(ProjectionExpression=PE)
subs = resp['Items']
for i in subs:
	un = i[KEY].lower()
	if i['username'] in BLOCKED:
		continue
	try:
		hist[un]+=1
	except:
		hist[un]=1

while 'LastEvaluatedKey' in resp:
	resp = subs_table.scan(ExclusiveStartKey=resp['LastEvaluatedKey'],ProjectionExpression=PE)
	subs = resp['Items']
	print(len(subs))
	
	for i in subs:
		un = i[KEY].lower()
		if i['username'] in BLOCKED:
			continue
		try:
			hist[un]+=1
		except:
			hist[un]=1

# print(hist)
x = [[hist[i],i] for i in hist]
x.sort()
for i in x[-50:]:print(i[1],i[0])
import json
f = open("memo.json","w")
f.write(json.dumps(hist))
