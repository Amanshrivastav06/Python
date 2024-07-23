# Break - is used to come out of the loop when encountered . it instructs the loop to exit the loop now.
for i in range(100):
    if(i==34):
        break  # ye loop exit kr dega mtlb 33 tk print karega
    print(i)

# Countinue Statements::
for i in range(100):
    if(i==34):
        continue  # Skip the iteration mtlb 34 ko skip karega
    print(i)

# PASS STATEMENTS:
for i in range(100):
    pass # ye baad me kaam krne ya skip krne ke kaam aata hai.


i=0
while(i<5):
    print(i)
    i=i+1