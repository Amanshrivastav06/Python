import random

'''
 1 - for snake
 -1 -for water
 0 - for gun
'''

computer = random.choice([-1, 0, 1]) # ye random no generate karega.
yourchoice = input("Enter your choice: ")
values = {"s":1 , "w":-1 , "g":0}
reversedvalues = {1:"Snake" , -1:"Water", 0:"Gun"}
you = values[yourchoice]

print(f"You choose {reversedvalues[you]}\nComputer Choose {reversedvalues[computer]}")

if(computer == you):
    print("Draw!!!")
else:
#     if(computer == -1 and you == 1):  #(computer - you) = -2
#          print("You Win!!!")
#     elif(computer == -1 and you == 0):#(computer - you) = -1
#          print("You Lose!!!!!")
#     elif(computer == 1 and you == -1):#(computer - you) = 2
#          print("You Lose!!!!!")
#     elif(computer == 1 and you == 0):#(computer - you) = 1
#          print("You Win!!!")
#     elif(computer == 0 and you == -1):#(computer - you) = 1
#          print("You Win!!!")
#     elif(computer == 0 and you == 1):#(computer - you) = -1
#          print("You Lose!!!!!")
#     else:
#          print("Something Went Wrong hua hai !!!! ")
    if((computer - you) == -1 or (computer - you)== 2):
        print("Lose!!!")
    else:
        print("You Win")
  
      


