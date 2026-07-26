#5. Write a class vector representing a vector of n dimensions. 
# Overload the + and * operator which calculates the sum and the dot(.) product of them.

class vector:
    def __init__(self, i ,j):
        self.i = i
        self.j = j
    def show(self):
        print(f"the vector is {self.i}i + {self.j}j ")

    
    def __add__(self , c2):
        return complex(self.r + c2.r, self.i + c2.i)
    
    def __mul__(self , c2):
        real_part = self.r * c2.r - self.i * c2.i
        imag_part = self.r * c2.i + self.i * c2.r
        return complex(real_part, imag_part)
    
    def __str__(self):
        return f"{self.r} + {self.i}"
    


v = vector(2,4)
v.show()

