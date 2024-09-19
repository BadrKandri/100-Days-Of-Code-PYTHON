import os

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)

names ={}
starting='yes'
bide=0
while starting == 'yes':
    name=input("what is your name? >>> ")
    bide1=int(input("what is your bide? >>> $"))
    if bide1>bide:
      bide=bide1
    names[name] = bide
    starting=input("are there any other bidders?\n print 'yes' or 'no' >>> ").lower()
    os.system("cls")
    print(logo)
winner=max(names, key =names.get) #this function give us the key of the maximum of the dictionary
print(F">>>>>>>>>>>>>>>>>>>>>>>  THE WINNER IS : {winner} with a bide of {bide} $\n\n")
