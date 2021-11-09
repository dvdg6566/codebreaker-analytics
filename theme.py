# Output number of submissions by date
import boto3
import json
from time import time
from pprint import pprint
dynamodb = boto3.resource('dynamodb','ap-southeast-1')
users_table=dynamodb.Table('codebreaker-users')

def stats():
	resp = users_table.scan(ProjectionExpression='username,theme')
	items=resp['Items']
	items = [i for i in items if i['username'] != '']
	res = {}
	for i in items:
		theme = i['theme']
		username = i['username']
		if theme in res:
			res[theme].append(username)
		else:
			res[theme] = [username]
	return res


if __name__ == '__main__':
	s = stats()
	for i in s:
		print(f'{i} mode has {len(s[i])} users')
		pprint(s[i][:10])
	print(s['pink'])