# This program takes any amount of text and counts the amount of
# characters in the text.

import pprint

message = "It was the final Sunday of the season and the Cleveland Browns are once again not making the playoffs."
count = {}

for character in message.lower():
    # Set default value for each character to 0
    count.setdefault(character, 0)
    # Increase character count by 1
    count[character] += 1

pprint.pprint(count)
