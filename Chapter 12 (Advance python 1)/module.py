def fun():
    print("hello , hattt")

# fun()
# print(__name__)  # if i run here then it gives the file name "main" and same thing i run in main file then it give "module" name



# if ki condition ke baad
if __name__=="__main__":
    # If this code is directly executed by running the file its present in
    print("We directly running this code")
    fun()
    print(__name__)
