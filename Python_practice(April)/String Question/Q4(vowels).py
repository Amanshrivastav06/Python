# 5. Count the number of vowels in a string.
# a = "gaurav is on the way that is"
# count = 0
# for i in a:
#     if i in ["a", "e", "i", "o", "u"]:
#         count = count + 1

# print(count)

# for constants -
b = "gaurav is on the way that is"
count = 0
for i in b:
    if i not in ["a", "e", "i", "o", "u"]:
        count = count + 1
print(count)
