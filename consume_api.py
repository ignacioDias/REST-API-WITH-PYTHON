import requests
import json

response = requests.get('https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow')
print(response) #should be 200
# print(response.json())

for data in response.json()['items']:
    if data['answer_count'] == 0: #get questions without answers!
        print(data['title'])
        print(data['link'])
        print()