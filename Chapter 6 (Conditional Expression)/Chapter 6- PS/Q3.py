#3. A spam comment is defined as a text containing following keywords:
#“Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.
p1="Make a lot of money"
p2="buy now"
p3="subscribe this" 
p4="click this"

s=input("Enter the comment: ")

if((p1 in s) or (p2 in s) or (p3 in s) or (p4 in s )):
    print("This comment is spam")
else:
    print("this message is not sapm")