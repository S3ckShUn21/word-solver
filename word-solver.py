import re

search = re.compile("(?=(?:\w*l\w*){5})\w+")

with open("words_alpha.txt", "r") as file:
    text = file.read()
    matches = search.findall(text)

print(matches)