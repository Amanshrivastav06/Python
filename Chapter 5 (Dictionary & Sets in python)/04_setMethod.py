s={23,32,65,4,8,7,7,"aman"} 
 
#1 s.add(1)- it add element in set
s.add(1)
print(s)

#2 len(s): returns length of set
print(len(s))

#3 s.remove(8): updates the set s and removes 8 from s.
s.remove(8)
print(s)

#4 s.pop(): removes an arbitrary element from the set and return the element removed.
s.pop()
print(s)

#5 s.clear(): empty the set

#6 s.union({8,11}): returns a new set with all items from both sets
a={1,2,3,4,55,55,67,67,8,4,3,1}
b={1,2,0,4,78,55,67,1}
print(a.union(b))

#7 s.intersection({8,11}): Return a set which contains only item in both sets
a={1,2,3,4,55,55,67,67,8,4,3,1}
b={1,2,0,4,78,55,67,1}
# print(a.intersection(b))
# r=a-b
r= a+b # a-b ka means sirf a ke element jo b me same honge use nhi likhenege , jo sirf a me different honge wo ans. a+b me jo b me 
print(r)
