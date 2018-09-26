import random
import time

game_stats = {
    'player_power': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'enemy_power': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'enemy_numbers': [1, 2, 3, 4, 5],
    'lives': 3,
    'enemy_exp': [50, 100, 150, 200, 250, 300],
    'player_exp': 0,
    'player_level': 1,
    'again': "yes",
    'wave_num': -1
    }
ship_power = int(input("please input your ships attacking power as a number 1-5 ")) + int(game_stats['player_level']) -1
time.sleep(1)
game_difficulty = int(input("please input the starting enemy difficulty you want as a number 1-5 ")) + int(game_stats['wave_num']) * 0.5
time.sleep(1)
print("Time to begin your epic space battle!!!")
time.sleep(2)
while game_stats['again'] != "no":
        game_stats['wave_num'] += 1
        troops = random.choice(game_stats['enemy_numbers'])
        print("you face off against %s enemy ships this wave lets see if we can win" % troops)
        time.sleep(2)
        while troops > 0 and game_stats['lives'] > 0:
                    if int(random.choice(game_stats['player_power'])) + int(ship_power) >= int(random.choice(game_stats['enemy_power'])) + int(game_difficulty):
                                print("A enemy ship was defeated")
                                troops -= 1
                                exp_needed = int(game_stats['player_level']) * 100 + 1000
                                gained_exp = random.choice(game_stats['enemy_exp'])
                                game_stats['player_exp'] += gained_exp
                                time.sleep(2)
                                print("you have gained %s exp from the enemy you beat" % gained_exp)
                                time.sleep(2)
                                print("your current exp is %s" % game_stats['player_exp'])
                                time.sleep(2)
                                if game_stats['player_exp'] >= exp_needed:
                                        game_stats['player_exp'] = game_stats['player_exp'] - exp_needed
                                        game_stats['player_level'] += 1
                                        print("the ship has leveled up you are now level %s" % game_stats['player_level'])
                                else:
                                        exp_left = int(exp_needed) - int(game_stats['player_exp'])
                                        print("you need %s exp to level up" % exp_left)
                    else:
                        game_stats['lives'] -= 1
                        time.sleep(2)
                        print("you have lost and your ship has been damaged you now have %s lives left" % game_stats['lives'])
        if game_stats['lives'] > 0: 
                time.sleep(2)
                game_stats['again'] = input("you have defeated all enemy ships in this wave do you want to continue to the next wave the next wave remeber they will get harder as you go along? 'yes' or 'no'")
        else:
                break
if game_stats['lives'] > 0:
        print("thank you for playing we hope that you will play again soon")
else:
        print("you have lost all your lives GAME OVER")

