# assignment04-github.py
# write a program in python that will read a file from a repository
# the program should then replace all the instances of the text "Andrew" with your name
# author: Joseph Benkanoun

from github import Github
import requests
from config import githubkey as cfg
import base64

url = 'https://api.github.com/repos/JBnkn/misc/contents/'

key = cfg
response = requests.get(url, auth = ('token', key))
print(response.status_code)

file = requests.get('https://api.github.com/repos/JBnkn/misc/contents/Andrew2Joseph.txt', auth = ('token', key))
print(file.status_code)

file_data = file.json()

# asked for advice on my code from ChatGPT and it suggested using to return the file contents
# I'm not fully getting this put unfortunately am flying out for Easter this morning so don't have time to continue tweaking
# disappointed with this assignment - it just hasn't clicked for me
# the below seems to have worked but I'd like to take more time to work through it and fully understand why it is working
content_base64 = file_data['content']
content = base64.b64decode(content_base64).decode('utf-8')

updated_content = content.replace('Andrew', 'Joseph')

update_payload = {
        'message': 'Replace all instances of Andrew with Joseph',
        'content': base64.b64encode(updated_content.encode('utf-8')).decode('utf-8'),
        'sha': file_data['sha'] 
    }

update_response = requests.put('https://api.github.com/repos/JBnkn/misc/contents/Andrew2Joseph.txt', json=update_payload, auth=('token', key))
print(update_response.status_code)