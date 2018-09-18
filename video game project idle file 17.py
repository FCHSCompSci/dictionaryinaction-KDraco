input random

game_stats: {
    'player_power': [1, 2, 3, 4, 5]
    'enemy_power': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    'enemy_numbers': [1, 2, 3]
    'lives': 3
    'enemy_exp': [50, 100, 150, 200, 250, 300]
    'player_exp': 0
    'player_level': 1
    }
ship_power = input("please input your ships attacking power as a number 1-5")
game_difficulty = input("please input the difficulty you want to play at as a number 1-5")
print("Time to begin your epic space battle!!!")
    while lives > 0:
        while again != strip(no):
            troops = random.choice(game_stats['enemy_numbers'])
            print("you face off against %s enemy ships lets see if our strong enough to win" %s troops)
            while troops > 0:
                Epower = random.choice(game_stats['enemy_power']) + game_difficulty
                Ppower = random.choice(game_stats['player_power']) + ship_power
                    if Ppower >= Epower:
                    print("you were able to defeate a enemy unit lets keep going and beat the rest")
                    troops = troops - 1
                    player_exp = player_exp + random.choice(game_stats['enemy_exp']
                    if player_exp = 1000:
                                        player_level = player_level + 1
                                        print("you have leveled up you are now level %s" %s player_level)
                    else:
                        print("you have gained some exp from the enemies you defeated good job")
                else:
                    lives = lives - 1
                    print("you have been defeated but dont worry you still have %s lives left" %s lives)
        again = input("you have defeated all the enemies in this wave would you like to continue? 'yes' or 'no'")
print("thank you for playing we hope that you will play again soon")
