# Generate character stats:
def charGen():
    from random import randint

    print(
        "Character builder\n\nCreate a character by choosing their name and species, and you'll get stats for them\n\n"
    )
    name = input("Choose your character's name: ")
    species = input(
        "Choose character type (e.g., human, wizard, thief, etc.)\nYou are: "
    )
    health = ((randint(1, 6) * randint(1, 12)) + 10) * randint(1, 4)
    attack = (((randint(1, 6) * randint(1, 12)) // 2) + 12) * randint(1, 5)
    speed = (health // randint(1, 12)) + randint(1, 4)
    defence = (health // 2) + randint(4, 16) // 2
    luck = (health + attack + speed + defence) // 5
    print(
        f"""
-- Stats --
- {name}
- {species}
- Health: {health}
- Attack power: {attack}
- Defence: {defence}
- Speed: {speed}
- Luck: {luck}"""
    )
    return health, attack, name, speed, defence, luck


# Player chose to attack:
def pick_attack():
    # char1_name, char2_name, char1_atk, char2_atk, char1_hp, char2_hp, turn):
    from random import random, randint
    from game2 import (
        char1_name,
        char2_name,
        char1_atk,
        char2_atk,
        char1_hp,
        char2_hp,
        turn,
    )

    if char1_atk > char2_atk:
        diff_atk = (char1_atk - char2_atk) + 1
    elif char2_atk > char1_atk:
        diff_atk = (char2_atk - char1_atk) + 1
    else:
        diff_atk = ((char1_atk // 2) + ((char1_hp + char2_hp) // 2)) // (
            random() * (1.5 + (randint(0, 25) // 10))
        )
    if diff_atk < 20:
        diff_atk += randint(-3, 3) - 1
    else:
        diff_atk += randint(-5, 1)
    if turn == 1:
        char2_hp -= diff_atk
        print(
            f"{char1_name} attacks {char2_name} for {diff_atk} damage! {char2_name} has {char2_hp} health remaining!"
        )
    elif turn == 2:
        char1_hp -= diff_atk
        print(
            f"{char2_name} attacks {char1_name} for {diff_atk} damage! {char1_name} has {char1_hp} health remaining!"
        )
    return char1_hp, char2_hp, turn


# Player chose to defend:
def pick_defend():
    # char1_defence, char1_hp, char2_atk, char1_name, turn):
    from game2 import char1_defence, char1_hp, char2_atk, char1_name, turn

    boost_defence = (char1_defence + char2_atk) // char1_hp
    print(
        f"{char1_name} is defending themselves! Their defence is increased to {boost_defence}"
    )
    if turn == 1:
        turn += 1
    else:
        turn -= 1
    return char1_defence + ((char1_defence + char2_atk) // char1_hp), turn


# Player chose to see their item list: (unfinished)
def pick_item():
    print("you have a super mushroom for 60hp i think")
    print("This feature has not been fully implemented yet, sorry.")


# The player wants to do.. nothing?
def pick_luigi():
    # char_luck, turn):
    from random import randint
    from game2 import char_luck, turn

    print(f"luck increased to {char_luck}")
    if turn == 1:
        turn += 1
    else:
        turn -= 1
    return char_luck + (char_luck * ((randint(0, 100) // 10) + 1)), turn


# The player chose to see their stats
def pick_stats(char_hp, char_defence, char_luck, char_name):
    print(
        f"""{char_name}'s stats:
          - {char_hp}hp
          - {char_defence} defence
          = {char_luck} luck"""
    )
