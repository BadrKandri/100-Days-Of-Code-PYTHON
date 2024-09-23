ROCK = '''
    _______  
---'   ____)
      (_____) 
      (_____)
      (____)
---.__(___)  '''

PAPER= '''
    ________       
---'    ____)____    
           ______)    
          _______)   
         _______)   
---.__________)    '''

SCISSORS = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)        '''

ROCK2= '''
  _______
 (____   '---
(_____)
(_____)
 (____)
  (___)__.---''' 
PAPER2='''
      _______
 ____(____   '----
(______
(_______
 (_______
    (_________.---'''
SCISSORS2='''
       _______
  ____(____   '---
 (______
(__________
      (____)
       (___)__.---'''  
            
import random
list =["ROCK","PAPER","SCISSORS"]
choice = int(input("choose:\n0 for ROCK\n1 for PAPER\n2 for SCISSORS\nyour answer: "))

if choice == 0 :
    a= "ROCK" 
elif choice == 1:
    a= "PAPER" 
elif choice ==2:
    a= "SCISSORS" 
else:
    print("ERROR 04")
    
b=random.choice(list)
3

if a == "ROCK" and b == "PAPER":
    print(ROCK)
    print(PAPER2)
    print("\n\nyou LOST\n\n")
elif a == "ROCK" and b == "SCISSORS":
    print(ROCK)
    print(SCISSORS2)
    print("\n\nyou WON\n\n")
elif a == "ROCK" and b == "ROCK":
    print(ROCK)
    print(ROCK2)
    print("\n\nTRY AGAIN\n\n")
elif a == "PAPER" and b == "ROCK":
    print(PAPER)
    print(ROCK2)
    print("\n\nyou WON\n\n")
elif a == "PAPER" and b == "SCISSORS":
    print(PAPER)
    print(SCISSORS2)
    print("\n\nyou LOST\n\n")
elif a == "PAPER" and b == "PAPER":
    print(PAPER)
    print(PAPER2)
    print("\n\nTRY AGAIN\n\n")
elif a == "SCISSORS" and b == "ROCK":
    print(SCISSORS)
    print(ROCK2)
    print("\n\nyou LOST\n\n")
elif a == "SCISSORS" and b == "PAPER":
    print(SCISSORS)
    print(PAPER2)
    print("\n\nyou WON\n\n")
elif a == "SCISSORS" and b == "SCISSORS":
    print(SCISSORS)
    print(SCISSORS2)
    print("\n\nTRTY AGAIN\n\n")

