# assignment03-cso.py
# write a program that retrieves the dataset for the "exchequer account (historical series)" from the CSO, and stores it into a file called "cso.json"
# author: Joseph Benkanoun

import requests

data = requests.get("https://data.cso.ie/table/FIQ02")
print(data.status_code)
print(data)