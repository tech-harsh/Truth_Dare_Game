print('''
1. Welocome to the "truth" And "dare" Game.

2. Enter the Player Names.

3. Choose Truth or Dare.

4. At the end of the prograsm, computer gives you a Truth or Dare questions.
''')

import random

truth_item = ['What is your worst habit?','Do you sing in the shower?','Are you scared of the dark?']
dare_items = ['Dance on the street like cazy.','Bark like a Dog loudly','Take Your Shirt off spin it.']

number_of_players = int(input("How many people wants to play?\n==>"))
list_of_players = []

answer = "yes"

for i in range(number_of_players):
    player_names = input("Please enter the player's name.\n==>")
    list_of_players.append(player_names)

while answer == "yes" or answer =="y":
    player = random.choice(list_of_players)    
    print('its <<', player ,'>> turn')
    truth_dare = input('Please type "truth" to choose truth and "dare" to chose dare.\n==>')

    truth_dare = str(truth_dare)

    if truth_dare == 'truth' or truth_dare == 'Truth':
        print(random.choice(truth_item))

    if truth_dare == 'dare'or truth_dare == 'Dare':
        print(random.choice(dare_items))

    answer = input("Do you wanna continue the game?\n==>")
    



            
