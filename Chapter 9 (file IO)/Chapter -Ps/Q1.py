#1. Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’.

with open("poems.txt") as f:
    content = f.read()
    print(f.read())
if("twinkle" in content):
    print("mil gyi bhai twinkle")
else:
    print("Nhi hai bhai.. teri twinkle")


# f = open("poems.txt")
# content = f.read()
# if("twinkle" in content):
#     print("mil gyi content")
# else:
#     print("nhi mili bhai twinkle!!")
# f.close()