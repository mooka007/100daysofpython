logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


print(logo)



def ad(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mult(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

op = {
    "+" : ad,
    "-" : sub,
    "*" : mult,
    "/" : div 
}
history = {}
loop = True
while loop:
    num1 = int(input("What is the first number? (Enter 0 to exit): "))
    if num1 == 0:
        break
    shouldContinue = True
    while shouldContinue:
        pickedSymbol = input("Enter the operation symbol: ")
        if pickedSymbol not in op:
            print("Invalid operation symbol. Please try again.")
            break
        num2 = int(input("What is the second number? : "))
        calculation_func = op.get(pickedSymbol)
        if calculation_func:
            answer = calculation_func(num1, num2)
            equation = f"{num1} {pickedSymbol} {num2}"
            print(f"{equation} = {answer}")
            history[equation] = answer    
        else:
            print("Invalid operation symbol.")
            break
        if input(f"Type 'y' to continue calculating with {answer}, or Type 'n' to start a new calculation: ") == 'y':
            num1 = answer
        else:
            shouldContinue = False
    print("History of calculations:")
    for equation, answer in history.items():
        print(f"{equation} = {answer}")
    loop = False