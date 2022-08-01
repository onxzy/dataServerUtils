import json
import requests
import os
from datetime import datetime

with open('config.json') as json_file:
    config = json.load(json_file)
serverUrl = config['serverUrl']
admin = config['admin']

# Check if server is online
try:
    requests.get(serverUrl)
except:
    exit('Server offline')

# Get Admin token
r = requests.get(serverUrl + 'api/auth/login', params=admin)
adminToken = r.json()['token']
headers = {'Authorization': 'Bearer ' + adminToken}
print('Authenticated')

# Get All Links
r = requests.get(serverUrl + 'api/healthData/datalink', headers=headers)
dataLinks = r.json()
print('Link number : ' + str(len(dataLinks)))

# Get ecg from one link
# r = requests.get(serverUrl + 'api/healthData/ecg', headers=headers, params={'link': dataLinks[0]['link']})
# ecgList = r.json() # ecgList[0]['value'] ecgList[0]['date'] ecgList[0]['sampling_frequency']
# # print(ecgList[0]['value'])

# Get all ECG
dirname = 'ecgs_' + datetime.now().strftime("%y-%m-%d_%H%M%S")
os.mkdir(dirname)

from concurrent.futures import as_completed
from requests_futures.sessions import FuturesSession

session = FuturesSession()

futures=[]
for dataLink in dataLinks:
    link = dataLink['link']
    print(link + ' | Getting ECGs')
    future = session.get(serverUrl + 'api/healthData/ecg', headers=headers, params={'link': link})
    future.link = link
    futures.append(future)

for future in as_completed(futures):
    r = future.result()
    print(future.link + ' | Saving ECGs')
    with open(dirname + '/' + future.link +'.json', 'w') as outfile:
        outfile.write(json.dumps((r.json()['list'])))
        print(future.link + ' | Saved')
