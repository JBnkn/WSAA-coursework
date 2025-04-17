# assignment04-github.py
# write a program in python that will read a file from a repository
# the program should then replace all the instances of the text "Andrew" with your name
# author: Joseph Benkanoun

from github import Github
import requests
from config import githubkey as cfg

url = 'https://api.github.com/repos/JBnkn/misc/contents/'

key = cfg
response = requests.get(url, auth = ('token', key))
print(response.status_code)

file = requests.get('https://api.github.com/repos/JBnkn/misc/contents/Andrew2Joseph.txt', auth = ('token', key))
content = file.json()
print(content)

# struggling to get this to work
# Python keeps returning an error when I try to pip install Github