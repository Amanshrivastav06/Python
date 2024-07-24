#7. Write a python function to remove a given word from a list ad strip it at the same time.
 # IT ONLY REMOVE THE WORD
# def list(l, word):
#     for item in l:
#       l.remove(word)
#       return l

# l = ["aman" , "ankit" , "gaurav" , "adi" , "dinesh", "a"]
# n = input("enter the word: ")
# print(f"The list is {l} after {list(l, n)})")


 # IT STRIP AND REMOVE THE WORD
def list(l, word):
    n =[]
    for item in l:
       if not(item == word):
          n.append(item.strip(word))
    return n


l = ["aman" , "ankit" , "gaurav" , "adi" , "dinesh", "a"]
print(list(l , "a"))
# s= input("enter the word: ")
# print(f"The list is {l} after strip word {list(l, s)})")


