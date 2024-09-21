logo = '''
 _____________________
|  _________________  |
| | Meliodas calctr | |
| |_________________| |
|  ___ ___ ___   ___  |                      _            _       _             
| | 7 | 8 | 9 | | + | |                     | |          | |     | |            
| |___|___|___| |___| |             ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
| | 4 | 5 | 6 | | - | | >>>>>>>>>  / __/ _` | |/ __| | | | |/ _` | __/ _ \\| '__|
| |___|___|___| |___| | >>>>>>>>> | (_| (_| | | (__| |_| | | (_| | || (_) | |   
| | 1 | 2 | 3 | | x | | >>>>>>>>>  \\___\\__,_|_|\\___|\\__,_|_|\\__,_|\\__\\___/|_|   
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
'''

def somme(num1,num2):
    return num1 + num2
def diff(num1,num2):
    return num1 - num2
def mul(num1,num2):
    return num1 * num2
def div(num1,num2):
    if num2 == 0:
        print("you can't devide by 0!")
        return
    else:
        return num1 / num2   
opperation={
    "+":somme,
    "-":diff,
    "*":mul,
    "/":div,
}

def calculator():
    print(logo)
    loop = True
    num1=float(input("enter the first number:      >>> "))

    while loop:
        opp =input("enter the opperation (+,-,*,/):  >>> ")
        num2=int(input("enter the second number:      >>> "))
        result = opperation[opp](num1,num2)
        print (f"{num1} {opp} {num2} = {result}")
        restart= input(f"\n\ndo you wanna continue with {result } as the first number? or start a new opperation ?\nprint:\n'y' to continue\n'n' to start a new opperation\nor an other key to end the programe: >>> ")
        if  restart == "y":
            num1=result
        elif restart == "n":
            loop = False
            print("\n"*20)
            calculator()
        else:
            return
calculator()
