from random import randint
from game2lib import charGen

state_defend1 = 0
state_defend2 = 0
state_pass1 = 0
state_pass2 = 0
turn = randint(1, 2)
rounds = 0
game = -1
pick = 0
# pva = input("Choose between '2player' and 'vai' to play with a friend or against a computer (NOT YET IMPLEMENTED)")
print("\n(3. Item:) does nothing currently. sorry")
print("-- Character 1 creation --")
(
    char1_hp,
    char1_atk,
    char1_name,
    char1_speed,
    char1_defence,
    char1_luck,
    char1_species,
) = charGen()
print("-- Character 2 creation --")
(
    char2_hp,
    char2_atk,
    char2_name,
    char2_speed,
    char2_defence,
    char2_luck,
    char2_species,
) = charGen()


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
        global char1_hp, char2_hp, char1_defence1, char2_defence1
        global char1_speed, char2_speed, state_defend1, state_defend2, turn
        if pick == 1:
            (
                char1_hp,
                char2_hp,
                state_defend1,
                state_defend2,
                char1_defence,
                char2_defence,
                turn,
            ) = pick_attack(
                char1_name,
                char2_name,
                char1_atk,
                char2_atk,
                char1_hp,
                char2_hp,
                char1_defence1,
                char2_defence1,
                char1_speed,
                char2_speed,
                state_defend1,
                state_defend2,
                turn,
            )
        elif pick == 2:
            if turn == 1:
                # global char1_defence1, state_defend1
                char1_defence, state_defend1 = pick_defend(
                    char1_defence1, char1_name, state_defend1
                )
            else:
                # global char2_defence1, state_defend2
                char2_defence, state_defend2 = pick_defend(
                    char2_defence, char2_name, state_defend2
                )
        elif pick == 3:
            pick_item()
        elif pick == 4:
            if turn == 1:
                global char1_luck
                char1_luck = pick_luigi(char1_luck)
            else:
                global char2_luck
                char2_luck = pick_luigi(char2_luck)
        elif pick == 5:
            if turn == 1:
                pick_stats(
                    char1_hp,
                    char1_defence,
                    char1_luck,
                    char1_name,
                    char1_atk,
                    char1_speed,
                    char1_species,
                )
            else:
                pick_stats(
                    char2_hp,
                    char2_defence,
                    char2_luck,
                    char2_name,
                    char2_atk,
                    char2_speed,
                    char2_species,
                )
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


while char1_hp > 0 and char2_hp > 0:
    char1_defence1 = char1_defence
    char2_defence1 = char2_defence
    if char1_luck > 99:
        char1_defence += 99999
        char1_atk -= randint(0, 250)
    if char2_luck > 99:
        char2_atk -= 99999
        char2_defence += randint(-10, 30)
    rounds += 1
    if turn == 1:
        yourTurn(char1_name)
        turn = 2
    else:
        yourTurn(char2_name)
        turn = 1
    if char1_hp < 0:
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
elif game == 3:
    print(
        f"""Both characters died. What a shame.
          {char1_name} had {char1_hp}hp
          {char2_name} had {char2_hp}hp
          This might be a bug. Please report it on github."""
    )
