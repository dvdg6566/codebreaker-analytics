from pprint import pprint
import boto3
import json
dynamodb = boto3.resource('dynamodb','ap-southeast-1')
users_table=dynamodb.Table('codebreaker-users')

def updateUserInfo(email):
	users_table.update_item(
		Key = {'email':email},
		UpdateExpression = f'set theme=:a',
		ExpressionAttributeValues={':a':'light'}
	)

if __name__ == '__main__':
	updateUserInfo('czhdaniel@gmail.com')
	resp = users_table.scan(ProjectionExpression = 'email')
	items = resp['Items']
	usernames = [i['email'] for i in items if i['email'] != '']
	pprint(usernames)
	for i in usernames:
		updateUserInfo(i)
		print(i)