#5. Repeat program 4 for a list of such words to be censored.
words = ["Donkey", "takla", "ganja"]
with open("file.txt", "r") as f:
    new = f.read()
for word in words:
    new = new.replace(word, "genius")
with open("file.txt", "w") as f:
    f.write(new)
    