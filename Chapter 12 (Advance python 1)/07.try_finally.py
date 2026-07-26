# TRY WITH FINALLY - ye error msg aane pe bhi chalega , FUCTIONS me agr use kare to bhi reurn karne pe chalega but finally na use kre to nhi chalega


try:
    a = int(input("Enter the number: "))
    print(a)

except ValueError as v:
    print("hey, enter a number not string ")


finally:
    print("Thank you")


def main():
    try:
        a = int(input("Enter the number: "))
        print(a)
        return

    except ValueError as v:
        print("hey, enter a number not string ")
        return


    finally:  # yha finally hata du to ye error aane pe nhi run karega
        print("Thank you")  

main()