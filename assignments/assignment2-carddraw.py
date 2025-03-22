# assignment2-carddraw.py
# write a program that shuffles out five random playing cards using the Deck of Cards API
# author: Joseph Benkanoun

import requests
import json

url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
response = requests.get(url)
data = response.json()
deck = data["deck_id"]
print(deck)