story = "Once upon a time there is a good man who helped all poors and give shelter"
 #string fuctions 
# # 1. len()fuction = returns length of string 
# print(len(story))

# # 2. String.endswith("..") = returns true or false for your last word ends
# print(story.endswith("shelter"))

# # 3. string.count("i") = returns how many alphabets of number which you wanna search
# print(story.count("a"))

# # 4. string.capitalize = this fuction capatilizes the first character of a given string
# print(story.capitalize())

# # 5. string.find("word") = finds the word and returns the index of first occurence of the word in the string
# print(story.find("is"))

# # 6. string.replace(oldword, newword) = This function replace old word with newword in entire string
# print(story.replace("man" , "MAns"))

# 7. str(): Converts a value to a string.
# str(123)
# print(str)

# # 8 strip(): Removes any leading and trailing whitespace from a string./# Original string with leading and trailing whitespace

A= "   Hello, World!   "
# Using strip() to remove the whitespace
B= A.strip()
print(f"A:'{B}'") # f - ye NEW feature hai python ka jisme f ka use kr ke variable use kr skte hai print fun me


# 9 join(): Joins a list of strings into a single string with a specified separator.
words = ["Hello", "world", "this", "is", "Python"]
sentence = " ".join(words)
print(sentence)

A ="Hello", "World!"
B= ", ".join((A))  # Output: 'Hello, World!'
print(B)