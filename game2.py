from random import randint
from game2lib import charGen

turn = randint(1, 2)
rounds = 0
game = -1
pick = 0


# This function is defined in the main code as it was hell to code from-
# -the library due to how many functions and variables need to be pulled.
def yourTurn(char_name):
    from game2lib import pick_attack, pick_defend, pick_item, pick_luigi, pick_stats

    pick = 0
    print(f"{char_name}'s turn!")
    while pick not in [1, 2, 3, 4, 5]:
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
            char1_hp, char2_hp, turn = pick_attack()
            # char1_name, char2_name, char1_atk, char2_atk, char1_hp, char2_hp, turn):
        elif pick == 2:
            if turn == 1:
                char1_defence, turn = pick_defend()
                # char1_defence, char1_hp, char2_atk, char1_name, turn):
            else:
                char2_defence, turn = pick_defend()
                # char2_defence, char2_hp, char1_atk, char2_name, turn):
        elif pick == 3:
            pick_item(turn)
        elif pick == 4:
            if turn == 1:
                char1_luck, turn = pick_luigi()
                # char1_luck, turn)
            else:
                char2_luck, turn = pick_luigi()
                # char2_luck, turn)
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
            pick,
        )


print("(3. Item:) and (4. Pass:) don't work currently. sorry")
print("-- Character 1 creation --")
char1_hp, char1_atk, char1_name, char1_speed, char1_defence, char1_luck = charGen()
print("-- Character 2 creation --")
char2_hp, char2_atk, char2_name, char2_speed, char2_defence, char2_luck = charGen()
# if char1_atk > char2_atk:
#    diff_atk = char1_atk - char2_atk
# elif char1_atk < char2_atk:
#    diff_atk = char2_atk - char1_atk
# else:
#    diff_atk = randint(5, 25)
while char1_hp > 0 and char2_hp > 0:
    rounds += 1
    if turn == 1:
        pick = yourTurn(char1_name)
    else:
        yourTurn(char2_name)
        turn -= 1
    if char1_hp < 0:
        game = 2
        break
    elif char2_hp < 0:
        game = 1
        break
if game == 1:
    print(f"{char1_name} won the game with {char1_hp}hp remaining.")
elif game == 2:
    print(f"{char2_name} won the game with {char2_hp}hp remaining.")
else:
    print(
        f"""Something broke, you shouldn't be here.
        {char1_name} {char2_name}
        {char1_hp} {char2_hp}
        {char1_atk} {char2_atk}
        {char1_defence} {char2_defence}
        {char1_speed} {char2_speed}
        {char1_luck} {char2_luck}"""
    )
