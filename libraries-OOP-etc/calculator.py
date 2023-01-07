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

def add(num1,num2):
    return num1+num2

def sub(num1,num2):
    return num1-num2

def mult(num1,num2):
    return num1*num2

def div(num1,num2):
    return float(num1)/float(num2)


print(logo)

operations={
    "+":add,
    "-":sub,
    "*":mult,
    "/":div
    }

num1=float(input("What's the first number?: "))


continue_flag=True


for symbol in operations:
    print(symbol)



while continue_flag:

    user_symbol=input("Pick an operation:")
    num2=float(input("What's the next number?: "))
    calculation_function=operations[user_symbol]
    final_value=calculation_function(num1,num2)
    print(f"{num1} {user_symbol} {num2} = {final_value}")

    if input(f"Type 'y' to continue calculating with {final_value}, or type 'n' to exit.:")=="y":
        num1=final_value
    else:
        continue_flag=False









