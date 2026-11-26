def Calculaor(a : int, b : int, Operator : str):
    match Operator:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            return a / b
        case _:
            return "Unknow Operator"
        
        
while True:
    a = int(input("Enter Number a : "))
    Operator = input("Enter any one operator (+,-,*,/): ")
    b = int(input("Enter Number b : "))
    
    print(f"Output : {Calculaor(a, b, Operator)}")
    
    
# case _ is the default case in Python's match-case.
# It executes when none of the previously defined cases match the given value.