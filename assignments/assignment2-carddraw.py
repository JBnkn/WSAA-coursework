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

suit_counts = {}
value_counts = {}

print("Your hand:\n")

for card in data2["cards"]:
    suit = card["suit"]
    value = card["value"]
    suit_counts[suit] = suit_counts.get(suit, 0) + 1
    value_counts[value] = value_counts.get(value, 0) + 1
    print(f"{value.capitalize()} of {suit.capitalize()}")

print("")

for value, count in value_counts.items():
    if count == 4:
        print(f"Congratulations! Four of a kind: {value.capitalize()}s.")
    elif count == 3:
        print(f"Congratulations! Three of a kind: {value.capitalize()}s.")
    elif count == 2:
        print(f"Congratulations! A pair of {value.capitalize()}s.")

for suit, count in suit_counts.items():
    if count == 5:
        print(f"Congratulations! A flush of {suit.capitalize()}.")
