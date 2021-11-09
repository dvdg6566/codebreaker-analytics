import boto3
import json
import awstools
from time import time
from pprint import pprint
import datetime
s3 = boto3.client('s3')
lambda_client = boto3.client('lambda','ap-southeast-1')
dynamodb = boto3.resource('dynamodb','ap-southeast-1')
problems_table = dynamodb.Table('codebreaker-problems')
subs_table=dynamodb.Table('codebreaker-submissions')
dates = {}
TIMEZERO = datetime.datetime(year=2026,month=1,day=18)

# def StringToDate(s):
#   return datetime.datetime.strptime(s,"%Y-%m-%d %X")

# problems = awstools.getAllProblemNames()
# for problem in problems:
#   name = problem['problemName']
#   dates[name] = TIMEZERO

# resp = subs_table.scan(ProjectionExpression='problemName,submissionTime')
# subs = resp['Items']
# for i in subs:
#   dates[i['problemName']] = min(dates[i['problemName']],StringToDate(i['submissionTime']))

# while 'LastEvaluatedKey' in resp:
#   print("HI")
#   resp = subs_table.scan(ExclusiveStartKey=resp['LastEvaluatedKey'],ProjectionExpression='problemName,submissionTime,username')
#   subs = resp['Items']
#   for i in subs:
#       try:
#           dates[i['problemName']] = min(dates[i['problemName']],StringToDate(i['submissionTime']))
#       except:
#           print(i)

# for problem in dates:
#   if dates[problem] == TIMEZERO:
#       dates[problem] = datetime.datetime(year=2005,month=1,day=18)

# for problem in dates:
#   dates[problem] = str(dates[problem])


with open('tmp.txt') as f:
    lines = f.readlines()[0]
    dates = json.loads(lines)

for problem in dates:
    print(f'{problem}')
    problems_table.update_item(
        Key = {'problemName' : problem},
        UpdateExpression = f'set createdTime=:a',
        ExpressionAttributeValues={':a':dates[problem]},
    )
