# Generate character stats:
def charGen():
    from random import randint

    print(
        "Character builder\n\nCreate a character by choosing their name and species, and you'll get stats for them\n\n"
    )
    name = input("Choose your character's name: ")
    species = input(
        "Choose tank, light, or a custom species name. Choosing tank/light species impacts your stats.\nYou are: "
    )
    health = randint(randint(140, 160), randint(190, 210))
    attack = randint(randint(15, 25), randint(30, 40))
    defence = randint(randint(25, 30), randint(40, 65))
    speed = randint(randint(30, 50), randint(50, 100))
    luck1 = randint(1, 1000)
    if luck1 == 1000:
        luck2 = randint(1, 1000)
        if luck2 == 1000:
            luck = 100
    else:
        luck = (randint(1, 100) + randint(1, 100)) // 2
    if species == "tank":
        defence += 30
        speed *= 0.35
    elif species == "light":
        defence *= 0.35
        speed += 20
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
    return health, attack, name, speed, defence, luck, species


# Player chose to attack:
def pick_attack(
    char1_name,
    char2_name,
    char1_atk,
    char2_atk,
    char1_hp,
    char2_hp,
    char1_defence,
    char2_defence,
    char1_speed,
    char2_speed,
    state_defend1,
    state_defend2,
    turn,
):
    from random import randint

    if turn == 2:
        if char1_speed > randint(40, 75):
            if randint(1, 4) == turn:
                print(
                    f"""{char1_name} dodges the attack!
                    They take no damage, how unfortunate for {char2_name}!"""
                )
                turn = 1
                return char1_hp, char2_hp, turn
    elif turn == 1:
        if char2_speed > randint(40, 75):
            if randint(1, 4) == turn:
                print(
                    f"""{char2_name} dodges the attack!
                    They take no damage. Better luck next time {char2_name}!"""
                )
                turn = 2
                return char1_hp, char2_hp, turn
    diff_atk1 = char1_atk + randint(-5, 8)
    damage_dealt1 = diff_atk1 // (char2_defence // 10)
    diff_atk2 = char2_atk + randint(-5, 8)
    damage_dealt2 = diff_atk2 // (char1_defence // 10)
    if turn == 1:
        char2_hp = char2_hp - (diff_atk1 * (char2_defence // 100))
        char2_defence -= state_defend2 * 30
        state_defend2 = 0
        print(
            f"{char1_name} attacks {char2_name} for {damage_dealt1} damage!"
            f" {char2_name} has {char2_hp} health remaining!"
        )
        turn = 2
        return char1_hp, char2_hp, turn
    elif turn == 2:
        char1_hp = char1_hp - (diff_atk2 * (char1_defence // 100))
        char1_defence -= state_defend1 * 30
        state_defend1 = 0
        print(
            f"{char2_name} attacks {char1_name} for {damage_dealt2} damage!"
            f" {char1_name} has {char1_hp} health remaining!"
        )
        turn = 1
        return char1_hp, char2_hp, turn
    return (
        char1_hp,
        char2_hp,
        state_defend1,
        state_defend2,
        char1_defence,
        char2_defence,
        turn,
    )


# Player chose to defend:
def pick_defend(char1_defence, char1_name, state_defend):
    char1_defence += 30
    state_defend += 1
    print(
        f"{char1_name} is defending themselves! Their defence is increased to {char1_defence}"
    )
    return char1_defence, state_defend


# Player chose to see their item list: (unfinished)
def pick_item():
    print("you have a super mushroom for 60hp i think")
    print("This feature has not been fully implemented yet, sorry.")


# The player wants to do.. nothing?
def pick_luigi(char_luck):
    char_luck = char_luck * 1.25
    print(f"luck increased to {char_luck}")
    return char_luck


# The player chose to see their stats
def pick_stats(
    char_hp, char_defence, char_luck, char_name, char_atk, char_speed, char_species
):
    print(
        f"""
-- Stats --
- {char_name}
- {char_species}
- {char_hp}hp
- {char_atk} attack power
- {char_speed} speed
- {char_defence} defence
= {char_luck} luck"""
    )
