# 1. Write a program to reverse a string

# s = "ankit"
# print(s[::-1])

# Using for loop
# a = "Gaurav"
# rev = ""
# for i in range(0, a + 1):
#     rev = i + rev
# print(rev)

# a = "Gaurav"
# rev = ""
# for i in a:
#     rev = i + rev
# print(rev)

# -------------- 26/july/26 practice

# Write a program to reverse a string

st ="aman"
print(st[::-1])

# using For Loop

# | Iteration | `i` | Previous `rev` | New `rev` |
# | --------- | --- | -------------- | --------- |
# | Start     | -   | `""`           | `""`      |
# | 1         | G   | `""`           | `G`       |
# | 2         | a   | `G`            | `aG`      |
# | 3         | u   | `aG`           | `uaG`     |
# | 4         | r   | `uaG`          | `ruaG`    |
# | 5         | a   | `ruaG`         | `aruaG`   |
# | 6         | v   | `aruaG`        | `varuaG`  |

D = "Aman"
rev =""
for i in D:
    rev = i+rev
print(rev)



