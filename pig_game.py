#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Julia Stein
"""
import random
"""
function: take_turn()
This function lets a player take a turn in the 1-die game.

Step 1) Make one roll: Roll = random.randInt(1-6)
Step 2) If the player rolls a 1: end turn, all points are lost.
        If player rolls anything else, roll is added to total score. 
        Player can choose to keep rolling or stop. When player 
        chooses to stop, he earns the sum of all rolls this turn.
Step 3) After each roll that is not a one, prompt the player to type 
        "r" or "R" to keep rolling; typing anything else ends the turn.
"""


def take_turn():
    points = 0
    keep_playing = True
    while keep_playing:
        dice_roll = random.randint(1, 6)
        if dice_roll == 1:
            print("Current player rolled 1 and lost all current points.")
            points = 0
            break
        else:
            points += dice_roll
            print("Current player rolled", dice_roll, "----> Score in turn is", points)
            roll = input("Keep rolling?: r/R ")
            if roll.lower() != "r":
                break
    return points

"""
function: play_one_turn_pig()
- This function lets a player play a very short Pig game, which
  ends after exactly 1 turn.
"""
def play_one_turn_pig():
    print('1-Turn Pig Time!')
    score = take_turn()
    print('You scored', score, "points.📈📈📈")


"""
function: play_solitaire_pig()
This function lets a player play a solitaire Pig game.
"""
def play_solitaire_pig():
    print('Solitaire Pig Time!')
    target_score = int(input("What is your target score?: "))
    while target_score <= 0:
        target_score = int(input("Target score must be greater than 0. What is your target score?: "))
    score = 0
    while True:
        score += take_turn()
        if score >= target_score:
            print("🐖You won solitaire pig!🐖")
            break
        print("----> Total Points Banked:", score, "points.")
        keep_playing = input("Keep playing? r/R: ")
        if keep_playing.lower() != "r":
            print("🃏You gave up on solitaire pig.🃏")
            break

"""
function: play_heads_up_pig()
This function lets 2 players play a heads-up Pig game.
This should proceed the same way as solitaire except alternating
between player 1 and player 2.  Again, don't allow negative target
scores. If player 1 exceeds the target score, then player 2 gets 
one more turn before the game ends.  If player 2 exceeds the target 
score, then the game ends right away.
"""
def play_heads_up_pig():
    print('Heads-up Pig Time!')
    i = 1
    round_num = 1
    scores = [0, 0]
    in_game = True

    target_score = int(input("Enter target score: "))
    while target_score <= 0:
        target_score = int(input("Target score must be greater than 0. Enter target score: "))
    print(" ")
    while in_game:
        for i in range(len(scores)):
            print("------- Round", round_num, "-------")
            print("Player", i + 1, "is rolling.")
            scores[i] += take_turn()
            if scores[i] >= target_score:
                print("----> Player", i + 1, "has reached target score.")
                in_game = False
            else:
                print("----> Player", i + 1, "banked", scores[i], "total points.")
                if input("Keep playing? r/R: ").lower() != "r":
                    print(" ")
                    print("Players have ended the game.")
                    in_game = False
                    break
        round_num += 1
        print(" ")
    if scores[0] > target_score > scores[1]:
        print("Player 1 wins!")
    elif scores[0] < target_score < scores[1]:
        print("Player 2 wins!")
    else:
        print("Players ended game in a draw.")


''' Change no code below here '''
''' Here be dragons '''
''' Don't change this '''

def start():
    games = {
        't': ('1-Turn Pig', play_one_turn_pig),
        's': ('Solitaire Pig', play_solitaire_pig),
        'h': ('Heads-up Pig', play_heads_up_pig),
    }
    print('Menu\n----')
    for (key, game) in games.items():
        print(key, ": ", game[0], sep='')
    choice = input('\nGame choice: ')
    if choice in games:
        games[choice][1]()
    else:
        print('Sorry, that is not a game choice')

if __name__ == '__main__':
    start()
