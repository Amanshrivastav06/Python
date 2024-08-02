#9. Write a program to find out whether a file is identical & matches the content of another file.
with open("log.txt") as f:
    content1 = f.read()

with open("logCopy.txt") as f:
    content2 = f.read()

if (content1 == content2):
    print("The contents are same: ")

else:
    print("The content are not same: ")


