from random import randint
# import turtle


# PRINT GAME INFORMATION

print("cli rpg game v2 by Nixenn")
print("report bugs and give suggestions @ github.com/Nixenn\n")
input("Press enter to begin.")

print("\nThis game uses the time.sleep() function for tiny delays between text, \
      but you may turn it off.")
sleepEnabled: str = str(input("Would you like to enable the time.sleep() function? (Y/n)\n> "))
if sleepEnabled.lower() == "n":
    def sleep(awawa):
        pass
else:
    from time import sleep


roundCount: int = 0
turn: int = randint(1, 2)
changeTurn: bool = False
game_over: bool = False


def character_creation():
    print("-- CHARACTER CREATION --")

    hp = randint(65, 75)
    defence = 0
    atk = randint(18, 24)
    luck = randint(1, 4)
    wtf = 0
    crit = 0
    isclass: str = "No class"
    # crit lets you do extra damage to certain armour types if you get lucky
    # crit 0 = no crits
    # crit 1 = plate
    # crit 2 = chainmail
    # crit 3 = armourless

    name = input("Your characters' name (leave blank for random)\n> ")
    if len(name) <= 0:
        diceroll_name = randint(1, 6)
        names: list = ["tesla cybertruck", "goblin warrior", "nintendo ninja",
                       "dell optiplex", "ford focus", "subject number five"]
        name = names[diceroll_name - 1]
        print(f"Your name is {name}")

    armour = input("""Your character can wear one of the following armour pieces.
                    1: Plate armour
                    2: Chainmail
                    3: No armour.
                    Your choice (leave blank for none)\n> """)
    if armour == 1 or armour == "1":
        armour = 1
        luck -= 2
        defence += 50
        hp += 10
        print("This is some very strong armour, but it's quite heavy.")
    elif armour == 2 or armour == "2":
        armour = 2
        luck += 1
        atk += 5
        defence += 35
        print("This set is lighter than plate. It's less resistant as a result, \
but you can move around a bit better.")
    else:
        armour = 3
        luck += 4
        hp += 40
        defence += 25
        print("Plot armour.")

    weapon = input("""Your character can use one of the following weapons.
                    1: Sword
                    2: Croc (sports mode)
                    3: Hunting bow
                    4: None. You make your own luck.
                    Your choice (leave blank for none)\n> """)
    if weapon == 1 or weapon == "1":
        weapon = 1
        atk += 5
        crit = 3
        print("Slash your way to victory.")
    elif weapon == 2 or weapon == "2":
        weapon = 2
        atk += 1
        luck += 2
        hp = hp // 1.15
        wtf += 1  # lol
        crit += 3
        print("...")
    elif weapon == 3 or weapon == "3":
        weapon = 3
        atk += 3
        luck += 1
        crit += 2
        print("Distance is key.")
    else:
        weapon = 4
        luck += 4
        defence += 5
        hp += 5
        atk += 2
        crit += 1
        print("I'm not so sure your fists will hold up against a sword.. maybe there's something \
good about simplicity?")

    # this determines whether has chosen a "class". the classes are melee, ranged, and pure.
    if armour == 1 and weapon == 1:
        luck -= 2
        hp // 1.15
        atk += 28
        isclass = "Knight"
        # this is the melee class, made using plate armour and a sword.
        # it deals very high damage, but doesnt survive easily.
        # pure classes deal critical damage to knights.
    if armour == 2 and weapon == 3:
        luck += 1
        hp += 50
        defence += 20
        atk += 10
        isclass = "Archer"
        # this is the ranged class, made using chainmail armour and a hunting bow.
        # this class is quite well rounded. it has better survivability than the knight,
        # and has consistent damage.
    elif armour == 3 and weapon == 4:
        luck = 10
        hp += 45
        defence += 10
        isclass = "Pure"
        # this is the pure class, running on 2 hours sleep, a cup of coffee, and a dream.
        # it has perfect luck, meaning it has the highest crit chance. however,
        # these crits only work on the knight class. the pure class is also very tanky.
        # perfectly balanced, i know.

    print(f"""{name}
HP: {hp}
Defence: {defence}
Attack power: {atk}""")
    if luck > 8 and isclass != "Pure":
        luck = 8
    elif luck < 0:
        luck = 0

    if weapon == 1:
        weapon_str = "Sword (+5 atk)"
    elif weapon == 2:
        weapon_str = "Croc (Sports Mode) (+1 atk)"
    elif weapon == 3:
        weapon_str = "Hunting Bow (+3 atk) "
    elif weapon == 4:
        weapon_str = "None (+2 atk)"
    if armour == 1:
        armour_str = "Plate (+10hp +25def)"
    elif armour == 2:
        armour_str = "Chainmail (+10 def)"
    elif armour == 3:
        armour_str = "None (+40hp)"
    hp *= 1.25
    hp // 1
    defence *= 1.1
    defence // 1

    return name, armour, weapon, hp, defence, atk, luck, crit, isclass, weapon_str, armour_str


class characters():
    # new attributes (these fucking SUCK THE CODE IS SO BAD OML 4 DEEP NESTING)
    # you may also notice that luck works differently now.
    # it is a chance to decrease the damage you take by a significant amount,
    # rather than a chance to become a god and/or dodge everything like in v1
    name: str
    armour: str
    armour_str: str  # used to display armour in the stats section
    weapon: str
    weapon_str: str  # used to display weapon in the stats section
    hp: int
    defence: int
    atk: int
    luck: int  # chance to take reduced damage
    crit: int  # certain weapons have a chance to land critical hits on certain armour types.
    playerIsClass: str  # used to display player class in the stats section
    defenceBoost: int = 0  # this and isDefending are used for the action_defend calculation
    isDefending: int = 0

    def __init__(self):
        self.name, self.armour, self.weapon, self.hp, self.defence, self.atk, self.luck, \
            self.crit, self.playerIsClass, self.weapon_str, self.armour_str = character_creation()

    def action_attack(self, name, atk, crit, luck, name2, hp2, def2, armour2,
                      luck2, game_over, defenceBoost2, isDefending2):
        print(f"{name} is attacking {name2}!")
        sleep(0.2)
        critchance: int = 0
        # notes:
        # i feel like this whole "self.crit == self.armour2" thing is gonna break
        # edit: it didnt break but the fucking attack function broke just like in v1 (i think)
        # i also added a lazy nerf to the defend action: the defence boost is reduced by 1
        # every time it is used (unless you are attacked and the block is broken).
        # this does not stop at 0. it can reduce your defence. have fun.
        if crit == 0:
            critchance = 5
        elif crit != 0 and crit == armour2:
            critchance = 40
        diceroll = randint(0, 8)
        if diceroll > luck:
            critchance: int = randint(15, 22)
        damage_dealt = atk + (randint(1, 100) / 10)

        # damage modifiers (applied after initial calculation, defence goes last.)
        if randint(1, 100) <= critchance:
            print("A critical hit!")
            sleep(0.2)
            damage_dealt = damage_dealt / 0.6

        if randint(1, 7) < luck2:
            print(f"{name2} got lucky! The damage they take has been reduced!")
            sleep(0.2)
            damage_dealt / 1.8

        damage_dealt -= def2 / 3
        damage_dealt // 1
        damage_dealt += randint(1, 15)
        hp2 -= damage_dealt
        if hp2 > 0:
            print(f"{name} attacked {name2} for {damage_dealt} damage! Onwards!")
            if isDefending2 > 0:
                print(f"{name2}'s block was broken! Their defence boost has been reset!")
            game_over = False
        else:
            print(f"{name} atttacked {name2} for {damage_dealt} damage!")
            print(f"{name2}'s hp was reduced to 0! {name} wins!")
            game_over = True
        sleep(0.2)

        def2 -= defenceBoost2
        defenceBoost2 = 0
        isDefending2 = 0
        changeTurn = True
        return hp2, game_over, changeTurn, isDefending2, defenceBoost2, def2

    def action_defend(self, name, defence):
        if self.isDefending == 0:
            defence += 50
            self.defenceBoost = 50
            print(f"{name} is blocking the next attack, raising \
their defence by {50 - self.isDefending}! ({defence} defence)")
            self.isDefending += 2
            sleep(0.4)
        else:
            print("You already have an active block! Continuing to fortify \
                  it will give less defence.")
            defence += 50 - self.isDefending
            self.defenceBoost += (50 - self.isDefending)
            print(f"{name} is blocking the next attack, raising \
their defence by {20 - self.isDefending}! ({defence} defence)")
            self.isDefending += 2
            sleep(0.4)
        changeTurn = True
        return defence, changeTurn

    def action_item(self, isTurnOver):
        choice = str(input("""Pick the item you would like to use from the list.
    1. Super Mushroom
    2. Glass (literal glass. wtf.)
    3. A FUCKING ROCK.
    4. A magic potion, what could it do?
    5. Go back and do something else.
    Your choice (enter a corresponding number): """))
        print("")

        if choice == "1":
            self.hp += 50
            print("WOW!! you healed for 50hp!")
            sleep(0.3)
            isTurnOver = True
        elif choice == "2":
            self.hp -= 30
            self.atk += 15
            print("that was a dumb idea.")
            sleep(0.1)
            print("HP DOWN 30!!")
            sleep(0.15)
            print("ATK UP 15!!")
            sleep(0.15)
            if self.hp <= 0:
                print("...")
                sleep(1)
                print("You died by eating a shard of glass. Why would you do that?")
                input()
                exit()
            isTurnOver = True
        elif choice == "3":
            rockRoll = randint(1, 3)
            if rockRoll == 1:
                self.defence += 35
                print("tastes.. crunchy.")
                sleep(0.1)
                print("DEFENCE UP 35!!")
                sleep(0.2)
            else:
                self.hp -= 25
                self.defence += 30
                print("I think I chipped a tooth..")
                sleep(0.1)
                print("HP DOWN 25!!")
                sleep(0.2)
                print("DEFENCE UP 30!!")
                sleep(0.2)
                if self.hp <= 0:
                    print("...")
                    sleep(1)
                    print("You died to a rock. Well done.")
                    input()
                    exit(0)
            isTurnOver = True
        elif choice == "4":
            potionRoll = randint(1, 5)
            if potionRoll == 1:
                self.hp -= 10
                self.defence // 2
                self.luck += 1
                self.atk += 15
                print("Woah, you're a glass cannon!")
                sleep(0.1)
                print("HP DOWN 10!!")
                sleep(0.1)
                print("DEFENCE DOWN 50%!!")
                sleep(0.1)
                print("LUCK UP 1!!")
                sleep(0.1)
                print("ATK UP 15!!\n")
                sleep(0.1)
            elif potionRoll == 2:
                self.hp += 120
                print("It was a health potion! you healed for 120hp!")
                sleep(0.3)
            elif potionRoll == 3:
                self.isDefending = 0
                self.defenceBoost = 0
                print("BONUS!! Your block state was reset, \
                      keeping your bonus defence and rendering it indestructable!")
                sleep(0.3)
            elif potionRoll == 4:
                self.luck -= 8
                print("OHN O AN UNHEALTHY POTION")
                sleep(0.1)
                print("LUCK DOWN 8!!")
                sleep(0.2)
            else:
                self.atk += 5
                self.hp += 20
                self.luck += 1
                self.defence += 20
                self.isDefending -= 1
                self.defenceBoost -= (20 - self.isDefending)
                self.playerIsClass = (self.playerIsClass, " -- BRILLIANCE MIXTURE ACTIVE")
                print("You found a Brilliance Mixture! All stats boosted!")
            isTurnOver = True
        else:
            print("Cancelling item use as no item was selected!")
            sleep(0.2)
            isTurnOver = False
        return isTurnOver

    def action_viewstats(self, health, attack, defence, luck, player_class, changeTurn):
        print(f"""-- {self.name}'s stats --
    HP: {health}
    Attack power: {attack}
    Defence: {defence}
    Luck: {luck}
    Weapon: {self.weapon_str}
    Armour: {self.armour_str}
    Player class: {player_class}""")
        changeTurn = False
        return changeTurn


# GAME STARTS HERE

print("\n-- PLAYER 1 --")
player1 = characters()

print("\n-- PLAYER 2 --")
player2 = characters()

while not game_over:
    roundCount += 1

    # this code is making me paranoid LOL
    # PR is short for player_ref, i just couldnt be bothered
    # typing that so many times
    if turn == 1:
        PR = player1
        PR2 = player2
    elif turn == 2:
        PR = player2
        PR2 = player1
    else:
        print("""An error occurred.
              Error code: turn_not_12
              Please create an issue on the Github page for this game if you see this.""")
    try:
        print("")
        player_choice = str(input(f"""{PR.name}'s turn! ({PR.hp}hp remaining).
                    1: Attack
                    2: Defend (increases defence temporarily)
                    3: Items (opens menu, ends your turn on item use)
                    4: View stats (doesn't end your turn)
                    Your choice (enter a corresponding number): """))
        print("")
        if PR.hp <= 0 or PR2.hp <= 0:
            print("An error occured! Error code: both_players_dead")
            input()
            exit()
        if player_choice == "1":
            PR2.hp, game_over, changeTurn, PR2.defenceBoost, \
                PR2.isDefending, PR2.defence = \
                PR.action_attack(PR.name, PR.atk, PR.crit, PR.luck, PR2.name, PR2.hp,
                                 PR2.defence, PR2.armour, PR2.luck, game_over,
                                 PR2.defenceBoost, PR2.isDefending)
        elif player_choice == "2":
            PR.defence, changeTurn = PR.action_defend(PR.name, PR.defence)
        elif player_choice == "3":
            changeTurn = PR.action_item(changeTurn)
        elif player_choice == "4":
            changeTurn = PR.action_viewstats(PR.hp, PR.atk, PR.defence,
                                             PR.luck, PR.playerIsClass, changeTurn)
        else:
            print("That's not a valid option! Try again!")
            changeTurn = False
            continue
    except (TypeError):
        print("Something went wrong! But the game should continue just fine. \
              (Error code: turn_protection_failed)")
    finally:
        if changeTurn:
            if turn == 1:
                turn += 1
            else:
                turn -= 1
        else:
            continue
