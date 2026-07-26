 # Q2 Write a program to fill in a letter template given below with name and date.
# letter ='''Dear <|Name|>,
# You are selected!
# <|Date|>
#  ''' 
# print(letter.replace("<|Name|>", "Aman").replace("<|Date|>", "03/07/2024"))

# if i want to entered name by user then 
letter ='''Dear <|Name|>,
You are selected!
<|Date|>
'''
A= input("Enter your Roll no: ")
print(letter.replace("<|Name|>",f"{A}").replace("<|Date|>", "03/07/2024"))