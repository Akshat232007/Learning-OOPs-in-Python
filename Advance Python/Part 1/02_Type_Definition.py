# Type Hints (Type Annotations)

# We use type hints to indicate the expected datatype
# of variables, function parameters and return values.

# Variable Type Hints:
Name: str = "Akshat"
Age: int = 19

# Function Type Hints:
def greeting(name: str, age: int) -> str:
    return f"Hello, I am {name}\nMy age is {age}"

print("Tejas KritiKudve", 23)

def Sum(a : int, b : int) -> int:
    return a + b

print(Sum(23,-9))