class num:
    def __init__(self, n):
        self.n = n

    def __add__(self, number):
        return self.n + number.n
    
n = num(1)
m = num(4)
print(n + m)