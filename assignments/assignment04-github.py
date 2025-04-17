# assignment04-github.py
# write a program in python that will read a file from a repository
# the program should then replace all the instances of the text "Andrew" with your name
# author: Joseph Benkanoun

from github import Github
import requests
from config import githubkey as cfg

url = 'https://api.github.com/repos/JBnkn/misc/contents/'
filename = '2025/Andrew2Joseph.txt'

key = cfg
response = requests.get(url, auth = ('token', key))
print(response.status_code)

file = requests.get('https://github.com/JBnkn/misc/blob/main/Andrew2Joseph.txt')
print(file)

# struggling to get this to work
# Python keeps returning an error when I try to pip install Github