# TRY WITH ELSE - try block agr shi se chal gya to else run krega nhi to nhi chalega

try:
    a = int(input("Enter the number: "))
    print(a)

except ValueError as v:
    print("hey, enter a number not string ")


else:
    print("Thank you")