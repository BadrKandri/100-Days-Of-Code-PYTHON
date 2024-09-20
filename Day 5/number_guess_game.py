#guessing game
heart='''❤️'''
import random
again='y'
print("\nhello i am mr bot i choose a number\nyou have to guess the number\nyou can choose the level of difficulty here:\n")
while again == 'y':
    level=input("EASY: hearts = 5 and number between 0 and 10\nHARD: hearts = 10 and number between 0 and 100\n>>> ").lower()
    if level == 'easy':
        rang= 11
        hearts= 5
    elif level == 'hard':
        rang=101
        hearts=10
    else:
        ("ERROR_404")
    the_number = random.randint(1,rang)
    #print(the_number)
    rep =0
    game_over=False
    while not game_over:
            if hearts ==0:
                print(f"\nGAME OVER you lost all your hearts\nthe number was {the_number} try again\n")
                game_over = True
            else:
                for i in range(0,hearts):
                    print(heart, end=' ')
                guess=int(input("\nguess the number >>> "))
                if guess == the_number:
                    rep+=1
                    print(f"\ncongratulation!!! you found the number after {rep} attempts\n")
                    game_over = True
                elif guess > the_number:
                    rep += 1
                    hearts-=1
                    print(f"\nthe number is smaller than {guess}\nyou have {hearts} more hearts\n")
                else:
                    rep += 1
                    hearts-=1
                    print(f"\nthe number is bigger than {guess}\nyou have {hearts} more hearts\n")
    again=input("do you wanna play again?\ntype 'y' or 'n':>>> ")
    print("\n"*20)
