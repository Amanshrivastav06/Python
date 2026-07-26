# EXCEPTION HANDLING IN PYTHON  - Ye user experince ko shi karene ke liye use hota jaise code/program me koi error user ki wjah se ho to program 
# ek msg drop kre.

try:
    a = int(input("Enter the number: "))
    print(a)

except ValueError as v:
    print("hey, enter a number not string ")


except Exception as e:  # means user agr number ki jagah string enter karega to program user ko suggest krega.
    print(e)

print("Thank you")