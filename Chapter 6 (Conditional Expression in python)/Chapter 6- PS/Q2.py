#2. Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. 
# \Assume 3 subjects and take marks as an int(input from the user.)

math = int(input("Enter the  marks of math: "))
physics= int(input("Enter the  marks of physics: "))
sst = int(input("Enter the  marks of sst: "))
total_percentage = (100*(math + physics + sst))/300
if(math>=33 and physics>=33 and sst>=33 and total_percentage>= 40):
    print(" Great!!,you are passed,", total_percentage)
else:
    print("ohh!!, you arte failed,", total_percentage)