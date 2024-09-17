#  _                                              #
# | |                                             #
# | |__   __ _ _ __   __ _ _ __ ___   __ _ _ ___  #
# | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_  \ #
# | | | | (_| | | | | (_| | | | | | | (_| | | | | #
# |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_| #
#                     __/ |                       #
#                    |___/                        #
import random
import hangman_list
gameover = '''
⠀⠀⠀⠀⠀⠀⢀⣤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⢤⣤⣀⣀⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⡼⠋⠀⣀⠄⡂⠍⣀⣒⣒⠂⠀⠬⠤⠤⠬⠍⠉⠝⠲⣄⡀⠀⠀
⠀⠀⠀⢀⡾⠁⠀⠊⢔⠕⠈⣀⣀⡀⠈⠆⠀⠀⠀⡍⠁⠀⠁⢂⠀⠈⣷⠀⠀
⠀⠀⣠⣾⠥⠀⠀⣠⢠⣞⣿⣿⣿⣉⠳⣄⠀⠀⣀⣤⣶⣶⣶⡄⠀⠀⣘⢦⡀
⢀⡞⡍⣠⠞⢋⡛⠶⠤⣤⠴⠚⠀⠈⠙⠁⠀⠀⢹⡏⠁⠀⣀⣠⠤⢤⡕⠱⣷
⠘⡇⠇⣯⠤⢾⡙⠲⢤⣀⡀⠤⠀⢲⡖⣂⣀⠀⠀⢙⣶⣄⠈⠉⣸⡄⠠⣠⡿
⠀⠹⣜⡪⠀⠈⢷⣦⣬⣏⠉⠛⠲⣮⣧⣁⣀⣀⠶⠞⢁⣀⣨⢶⢿⣧⠉⡼⠁
⠀⠀⠈⢷⡀⠀⠀⠳⣌⡟⠻⠷⣶⣧⣀⣀⣹⣉⣉⣿⣉⣉⣇⣼⣾⣿⠀⡇⠀
⠀⠀⠀⠈⢳⡄⠀⠀⠘⠳⣄⡀⡼⠈⠉⠛⡿⠿⠿⡿⠿⣿⢿⣿⣿⡇⠀⡇⠀
⠀⠀⠀⠀⠀⠙⢦⣕⠠⣒⠌⡙⠓⠶⠤⣤⣧⣀⣸⣇⣴⣧⠾⠾⠋⠀⠀⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠙⠶⣭⣒⠩⠖⢠⣤⠄⠀⠀⠀⠀⠀⠠⠔⠁⡰⠀⣧⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠲⢤⣀⣀⠉⠉⠀⠀⠀⠀⠀⠁⠀⣠⠏⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠛⠒⠲⠶⠤⠴⠒⠚⠁⠀⠀'''
levels = ['''
  _______
 |       |
 |      
 |      
 |       
 |      
 |
_|___ 
''','''
  _______
 |       |
 |      (_)
 |      
 |       
 |      
 |
_|___
''','''
  _______
 |       |
 |      (_)
 |       |
 |       
 |      
 |
_|___
''','''
  _______
 |       |
 |      (_)
 |      /|\\
 |       
 |      
 |
_|___
''','''
  _______
 |       |
 |      (_)
 |      /|\\
 |       |
 |      
 |
_|___
''','''
  _______
 |       |
 |      (_)
 |      /|\\
 |       |
 |      / \\
 |
_|___
''']
#STAR:
#chosen_word = random.choice(random.choice(hangman_list.words)).lower()
#part (1) : import all lists from hangman list then selecting a random word from a random list and save it in "chose_word"
import hangman_list

attributes = dir(hangman_list)
lists_in_hangman_list = []

for attr in attributes:
    value = getattr(hangman_list, attr)    
    if isinstance(value, list):
        lists_in_hangman_list.append(attr)

random_list_name = random.choice(lists_in_hangman_list)
random_list = getattr(hangman_list, random_list_name)
chosen_word = random.choice(random_list)
#part (2) : intro
hangman_list = ''
#if u wanna show the word that the computer choose remove the (#) from the next line
#print(chosen_word)
for i in range (0,len(chosen_word)):    
    hangman_list += "_"
game_over = False
correct=[]
q=0
l=5
print(f"\ni choose a word from {random_list_name}\n{hangman_list}\n\nguess the letter :")
#part (2) : body and function
while not game_over:
    guess=input("\nprint your choice here----->  ").lower()
    if guess in correct:
      print(f"YOU ALREADY CHOOSE THE LETTRE {guess}")  
    result= ""
    
    for letter in chosen_word:
        if letter == guess:
            result += letter
            correct.append(guess)
        elif letter in correct:
            result += letter
        else:
            result += "_"
                      
    print(result)
#part (3) : output the result       
    if "_" not in result:
        game_over = True
        print("\n*******************YOU WON*******************")
    elif guess not in chosen_word:
        q+=1
        l-=1
        print(f"\n**********you have {l} more lives***********")    
    elif guess not in correct:
        print("\n*************good continue*************")    
    print(levels[q])
    if q>4:
        game_over = True
        print(f"\n************* G_A_M_E  O_V_E_R **************{gameover}\nTHE WORD WAS---------------------> {chosen_word.upper()}\n********************************************* \n")
# THE END     
#test
