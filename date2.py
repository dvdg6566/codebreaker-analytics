import boto3
import json
import datetime
from pprint import pprint
lambda_client = boto3.client('lambda','ap-southeast-1')
dynamodb = boto3.resource('dynamodb','ap-southeast-1')
subs_table=dynamodb.Table('codebreaker-submissions')

map = {}
def getSubmission(subId):
    if subId in map.keys():
        return map[subId]
        
    try:
        response = subs_table.get_item( 
            Key={"subId": subId },
            ProjectionExpression = 'submissionTime'
        )
        subDetails = response['Item']['submissionTime'].split(' ')[0]
        map[subId] = subDetails

        return subDetails
    except KeyError:
        map[subId] = '3023-00-00'
        return '3023-00-00'

time = 8
A = []

for i in range(time+1):
    x = datetime.datetime.now() - datetime.timedelta(days=i)
    query = x.strftime('%Y-%m-%d')
    # Looking for the LAST submission of the day
    low = 0 
    high = 100000
    while high > low:
        mid = int((low+high + 1)/2)
        submissionTime = getSubmission(mid)
        if query >= submissionTime:
            low=mid
        else:
            high=mid - 1
    A.append(low)

# A = A[::-1]

for i in range(time):
    x = datetime.datetime.now() - datetime.timedelta(days=i)
    query = x.strftime('%Y-%m-%d')
    print(f'{query}: {A[i] - A[i+1]}, from {A[i+1]+1} - {A[i]}')

# print(getSubmission(2121))