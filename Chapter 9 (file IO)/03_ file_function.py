f = open("poem.txt")
# l = f.readlines() # ye list return karta hai lines ki file me se
# print(l, type(l))

line1 = f.readline() # ye one by one line ko print krta hai
print(line1, type(line1))

line2 = f.readline()
print(line2, type(line2))
f.close()