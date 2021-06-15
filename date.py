# Output number of submissions by date
import boto3
import json
from pprint import pprint
lambda_client = boto3.client('lambda','ap-southeast-1')
dynamodb = boto3.resource('dynamodb','ap-southeast-1')
problems_table = dynamodb.Table('codebreaker-problems')
subs_table=dynamodb.Table('codebreaker-submissions')

hist = {}

def add(date):
	if date in hist:
		hist[date]+=1
	else:
		hist[date]=1

resp = subs_table.scan(,ProjectionExpression='submissionTime')
subs = resp['Items']
print(len(subs))
for i in subs:
	date = i['submissionTime'].split(' ')[0]
	add(date)

while 'LastEvaluatedKey' in resp:
	resp = subs_table.scan(ExclusiveStartKey=resp['LastEvaluatedKey'],ProjectionExpression='submissionTime')
	subs = resp['Items']
	print(len(subs))

	for i in subs:
		date = i['submissionTime'].split(' ')[0]
		add(date)

# print(hist)
# x = [[hist[i],i] for i in hist]
# x.sort()
# for i in x[-50:]:print(i[1],i[0])
# import json
# f = open("memo.json","w")
# f.write(json.dumps(hist))
pprint(hist)