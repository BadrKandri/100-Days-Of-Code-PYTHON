print("\n\n********** TIP CALCULATOR ********** \n")
price=int(input("what was the total? \n TOTAL= $"))
tips=int(input("how much u wanna add to de total? \n we wanna add: %"))
people=int(input("how many are you? \n we are: "))

pourcentage = tips/100
price *= 1 + pourcentage
price /= people
price =round(price, 2)
print(f"everyone of you should pay {price} $")
