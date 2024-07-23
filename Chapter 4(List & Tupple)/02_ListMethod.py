friends=["apple", "orange", 5, 438.9, False, "aman"]
print(friends)
# 1. append() = adding element at last means last me element ko add karna.
friends.append("hurray")
print(friends)

# 2.sort()= sorting the list
l=[3,5,7,8,0,2,4,7,88,]
# l.sort()
# print(l)
print(l[0]) # ye index value pe element return karta

# 3. reverse() - reverse the list 
l.reverse()
print(l)

# 4. insert(3,0) - this will add 0 at index 3
l.insert(3,0)
print(l)

# 5. pop(2)- will delete element at index 2 and return its value
l.pop(2)
print(l)

# 6. remove(88)- will remove 21 from the list
l.remove(88)
print(l)
