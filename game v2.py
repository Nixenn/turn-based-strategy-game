from random import randint
from game2lib import charGen # game2lib.py is the library i made for this

turn = randint(1, 2) # effectively a dice roll to decide who goes first
rounds = 0 # each time a player makes a choice there is 1 added to this value
# it technically should be +1 round every time both players make their choice but whatever
game = -1 # this is changed when one or more characters are below 0 hp (determines winner)


# This function is defined in the main code as it was hell to code from-
# -the library due to how many functions and variables need to be pulled.
def yourTurn(char_name, turn):
    from game2lib import pick_attack, pick_defend, pick_item, pick_luigi, pick_stats

    pick = 0
    print(f"{char_name}'s turn!")
    while pick not in [1, 2, 3, 4, 5]: # this is the players choice of action
        pick = int(
            input(
                """
                1. Attack: Basic attack.
                2. Defend: Increases defence, but lowers speed.
                3. Item: Not yet implemented.
                4. Pass: Does nothing, at what cost?
                5. Stats: Prints your current stats. This ends your turn.
                You choose:"""
            )
        )
        if pick == 1:
            pick_attack(
                char1_name, char2_name, char1_atk, char2_atk, char1_hp, char2_hp, turn
            )
        elif pick == 2:
            if turn == 1:
                pick_defend(char1_defence, char1_hp, char2_atk, char1_name)
            else:
                pick_defend(char2_defence, char2_hp, char1_atk, char2_name)
        elif pick == 3:
            pick_item(turn)
        elif pick == 4:
            if turn == 1:
                pick_luigi(char1_luck)
            else:
                pick_luigi(char2_luck)
        elif pick == 5:
            if turn == 1:
                pick_stats(char1_hp, char1_defence, char1_luck, char1_name)
            else:
                pick_stats(char2_hp, char2_defence, char2_luck, char2_name)
        else:
            continue
        return (
            char1_hp,
            char2_hp,
            char1_defence,
            char2_defence,
            char1_luck,
            char2_luck,
        )


print("-- Character 1 creation --")
char1_hp, char1_atk, char1_name, char1_speed, char1_defence, char1_luck = charGen()
print("-- Character 2 creation --")
char2_hp, char2_atk, char2_name, char2_speed, char2_defence, char2_luck = charGen()
if char1_atk > char2_atk:
    diff_atk = char1_atk - char2_atk
elif char1_atk < char2_atk:
    diff_atk = char2_atk - char1_atk
else:
    diff_atk = randint(5, 25)
while char1_hp > 0 and char2_hp > 0:
    rounds += 1
    if char1_luck > 1000: # refer to game2lib.pick_Luigi()
        char1_hp += 250
        char1_atk += 150
        print(
            f"{char1_name}'s stats have been boosted! They received an extra 250 hp and 150 atk"
        )
    elif char2_luck > 1000: # refer to game2lib.pick_Luigi()
        char2_hp += 250
        char2_atk += 150
        print(
            f"{char2_name}'s stats have been boosted! They received an extra 250 hp and 150 atk"
        )
    if turn == 1:
        yourTurn(char1_name, turn)
        turn += 1
    else:
        yourTurn(char2_name, turn)
        turn -= 1
    if char1_hp < 0: # winner determinant
        game = 2
        break
    elif char2_hp < 0:
        game = 1
        break
    elif char1_hp < 0 and char2_hp < 0:
        game = 3
        break
    else:
        continue
if game == 1:
    print(f"{char1_name} won the game with {char1_hp}hp remaining.")
elif game == 2:
    print(f"{char2_name} won the game with {char2_hp}hp remaining.")
else: # temp debug, should be removed before release
    print(
        f"""Something broke, you shouldn't be here.
        {char1_name} {char2_name}
        {char1_hp} {char2_hp}
        {char1_atk} {char2_atk}
        {char1_defence} {char2_defence}
        {char1_speed} {char2_speed}
        {char1_luck} {char2_luck}"""
    )
