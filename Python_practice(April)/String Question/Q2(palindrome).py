# 2. Check if a string is a palindrome.

# palindrome = "121" = "121"
# Examples of palindromes (words)

# "madam" → forward: madam, backward: madam ✅

# "level" → forward: level, backward: level ✅

# "racecar" → forward: racecar, backward: racecar ✅


# using simple method
text = input("Enter the text: ")
if text == text[::-1]:
    print("It is palindrome")
else:
    print("it is not")


# Using for loop
p = input("enter the word: ")
rev = ""
for i in p:
    rev = i + rev
if p == rev:
    print("It is palindrome")
else:
    print("it is not")
