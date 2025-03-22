# assignment2-carddraw.py
# write a program that shuffles out five random playing cards using the Deck of Cards API
# author: Joseph Benkanoun

import requests
import json

url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
response = requests.get(url)
data = response.json()
deck = data["deck_id"]

url2 = f"https://deckofcardsapi.com/api/deck/{deck}/draw/?count=5"
response2 = requests.get(url2)
data2 = response2.json()
print(data2)

with open ("assignment2-pokerhand.json", "w") as fp:
    json.dump(data2, fp)