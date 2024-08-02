#8. Write a program to make a copy of a text file “this. txt”
with open("log.txt") as f:
    lines = f.read()

with open("logCopy.txt" , "w")as f:
    f.write(lines)
