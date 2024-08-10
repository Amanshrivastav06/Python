#4. Write a program to filter a list of numbers which are divisible by 5.

l = [5 , 10, 12, 2, 4, 35 , 20 , 150]

def div(n):
    if(n%5 == 0):
        return True
    return False

divby5 = filter(div, l)
print(list(divby5))