# with statements = using with statements we can avoid f.close

f = open("m.txt")
print(f.read())
f.close()

# the same can be written using with statements like this:
with open("m.txt") as f:
    print(f.read())
