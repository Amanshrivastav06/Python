#Type hints are added using the colon (:) syntax for variables and the -> syntax for function return types.
# Variable type hint
age: int = 25 
# Function type hints
def greeting(name: str) -> str: 
    return f"Hello, {name}!" 

# Usage 
print(greeting('Aman'))
# # Output: Hello, Alice!

n: int = 8
y: int = 7
print(n + y)

def sum(a: int, b: int) -> int:  #ise use karne se user ko hint milta hai programmer ne ky data types use kiya hai.
    return a+b
print(sum(7,8))

# ADVANCED TYPE HINTS
from typing import List,Tuple, Dict , Union
# list of integer
n : List[int] = {4,5,6,6}

# Tuple of a string and an integer
person: Tuple[str, int] = ("Alice", 30) 

# Dictionary with string keys and integer values
scores: Dict[str, int] = {"Alice": 90, "Bob": 85} 

# Union type for variables that can hold multiple types
identifier: Union[int, str] = "ID123"

identifier = 12345 # Also valid

print(f"{n},{scores}")

