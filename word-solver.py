import re

search = re.compile("^s..l.l....$", re.MULTILINE)

with open("words_alpha.txt", "r", encoding="utf-8") as file:
    text = file.read()
    matches = search.findall(text)

print(matches)