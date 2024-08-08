# Write __str__() method to print the vector as follows: 7i + 8j +10k
# Assume vector of dimension 3 for this problem

class vector:
    def __init__(self, i ,j , k):
        self.i = i
        self.j = j
        self.k = k
    def show(self):
        print(f"the vector is {self.i} + {self.j} + {self.k} ")
    
    def __str__(self):
        return f"{self.r}i + {self.i}j + {self.k}k"
    


v = vector(2,4,6)
v.show()
