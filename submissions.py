# Rank users by number of submissions

import boto3
import json
lambda_client = boto3.client('lambda','ap-southeast-1')
dynamodb = boto3.resource('dynamodb','ap-southeast-1')
problems_table = dynamodb.Table('codebreaker-problems')
subs_table=dynamodb.Table('codebreaker-submissions')

hist={}

resp = subs_table.scan()
subs = resp['Items']
for i in subs:
	un = i['username'].lower()
	try:
		hist[un]+=1
	except:
		hist[un]=1

while 'LastEvaluatedKey' in resp:
	resp = subs_table.scan(ExclusiveStartKey=resp['LastEvaluatedKey'])
	subs = resp['Items']
	print(len(subs))

	for i in subs:
		un = i['username'].lower()
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
