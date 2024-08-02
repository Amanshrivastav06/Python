#6. Write a program to mine a log file and find out whether it contains ‘python’.
with open("log.txt") as f:
    d = f.read()

if("python" in d):
    print("python yhi hai")
else:
    print("python nhi mila")