import random
import Zombie as z
import Human as h
import Boss as b
import csv

item_file= open("items/items.txt", "r")
item_list= item_file.readlines()
item_file.close()

special_item_file = open("items/special_items.txt", "r")
special_item_list = special_item_file.readlines()
special_item_file.close()

ultra_special_item_file = open("items/ultra_special_items.txt", "r")
ultra_special_item_list = ultra_special_item_file.readlines()
ultra_special_item_file.close()

boss_item_file= open("items/boss_items.txt", "r")
boss_item_list= boss_item_file.readlines()
boss_item_file.close()

zom_descriptions_file= open("descriptions/zombie_descriptions.txt", "r")
zom_description_list = zom_descriptions_file.readlines()
zom_descriptions_file.close()

raider_descriptions_file= open("descriptions/raider_descriptions.txt", "r")
raider_descriptions_list = raider_descriptions_file.readlines()
raider_descriptions_file.close()

survivor_descriptions_file= open("descriptions/survivor_descriptions.txt", "r")
survivor_descriptions_list = survivor_descriptions_file.readlines()
survivor_descriptions_file.close()

military_descriptions_file= open("descriptions/military_descriptions.txt", "r")
military_descriptions_list = military_descriptions_file.readlines()
military_descriptions_file.close()

survivors_male_file = open("descriptions/survivor_names_male.txt", "r")
survivors_male_list = survivors_male_file.readlines()
survivors_male_file.close()

items = item_list[0]
item_list = items.split(",")

count = 0
suits = ["D","C","H","S"]
card_list  = []
for i in range(4):
    suit = suits[count]
    for j in range(14):
        if j == 1:
            card_list.append("ACE" + suit)

        elif j == 11:
            card_list.append("KING" + suit)

        elif j == 12:
            card_list.append("QUEEN" + suit)

        elif j == 13:
            card_list.append("JACK" + suit)

        elif j != 0:
            card_list.append(str(j) + suit)

    count += 1

special_items = special_item_list[0]
special_item_list = special_items.split(",")

ultra_special_items = ultra_special_item_list[0]
ultra_special_item_list = ultra_special_items.split(",")

boss_items = boss_item_list[0]
boss_item_list = boss_items.split(",")

zom_descriptions = zom_description_list[0]
zom_description_list = zom_descriptions.split(",")

raider_descriptions = raider_descriptions_list[0]
raider_descriptions_list = raider_descriptions.split(",")

survivor_descriptions = survivor_descriptions_list[0]
survivor_descriptions_list = survivor_descriptions.split(",")

military_descriptions = military_descriptions_list[0]
military_description_list = military_descriptions.split(",")

survivors_male = survivors_male_list[0]
survivors_male_list = survivors_male.split(",")

raider_descriptions_list += survivor_descriptions_list

#0 HP, 1 Water, 2 Calories, 3 Food, 4 Weapons, 5 Meds, 6 Friends, 7 Home, 8 Bag, 9 Fuel, 10 Ammo
character = [[100], ["Hydrated"], [2000], [], ["hands"], [], [], [], ["Journal"], [0], [0, 0]]
#0 Head, 1 Torso, 2 Hands, 3 Legs, 4 Feet
current_clothing = [[],[],[],[],[]]
total_armour = 0

temp_items = []
afflictions = []
enemy_list = []
zombie_survivors = []
latest_events = []
journal = []

areas = ["Downtown","the Suburbs","the City Centre","the Industrial Estate"]
zom_types = ["weak zombie","zombie","strong zombie"]
explore_list = ["Radio Tower (5 Litres)"]
shelter = ["small shop","lonely house","secluded shack"]

head_armour = ["*motorbike helmet*","*army helmet*"]
torso_armour = ["***commander's armor***","***doctor's labcoat***","*body armour*","*leather jacket*","*police vest*","**combat armour**"]
leg_armour = ["*combat pants*"]
foot_armour = ["*work boots*"]
hand_armour = ["***flame gloves***","*leather gloves*"]

fight_list = []

game = True
day = 0
days_no_water = 0
zombies_killed = 0
water_drank = True

rifle_supp = False
pistol_supp = False

line_break = ("-" * 144)

def add_item(x):
    if x[0:2] == "(m":
        character[5].append(x[7:])

    elif x[0:3] == "(fu":
        character[9][0] += int(x[7])

    elif x[0:2] == "(f":
        character[3].append(x[7:])

    elif x[0:2] == "(w":
        character[4].append(x[9:])

    elif x[0:2] == "(c":
        character[8].append(x)

    elif x[0:3] == "(mo":
        character[8].append(x)

    elif x[0:3] == "(gu":
        character[4].append(x[6:])

    elif x[0:2] == "(a":
        if x[8] == "*":
            if x[10].isnumeric():
                character[10][1] += int(x[9:11])

            else:
                character[10][1] += int(x[9])

        else:
            if x[9].isnumeric():
                character[10][0] += int(x[8:10])

            else:
                character[10][0] += int(x[8])


def random_item(num1, num2, rarity, vers=None):
    temp_items = []
    for i in range(random.randint(num1,num2)):
        if rarity == "normal":
            temp_item = item_list[random.randint(0, len(item_list) - 1)]
            if vers == "meds":
                while temp_item[1:5] != "meds":
                    temp_item = item_list[random.randint(0, len(item_list) - 1)]

            elif vers == "food":
                while temp_item[1:5] != "food":
                    temp_item = item_list[random.randint(0, len(item_list) - 1)]

            elif vers == "fuel":
                while temp_item[1:5] != "fuel":
                    temp_item = item_list[random.randint(0, len(item_list) - 1)]

        elif rarity == "special":
            temp_item = special_item_list[random.randint(0, len(special_item_list) - 1)]

        elif rarity == "ultra special":
            temp_item = ultra_special_item_list[random.randint(0, len(ultra_special_item_list) - 1)]

        temp_items.append(temp_item)
        add_item(temp_item)
    for i in temp_items:
        print(i)


cal_list_100 = ["apple","banana","carrots"]
cal_list_300 = ["bag of peach rings","popcorn","cereal"]
cal_list_400 = ["protein bar","bread","flapjack","honey","tomato sauce","granola bar"]
cal_list_600 = ["canned soup","canned peaches","can of beans","can of tuna","biscuits","sausages","oats","bag of marshmallows"]
cal_list_800 = ["chicken","pasta","beef jerky","box of chocolates","can of whipped cream"]
cal_list_1000 = ["pre-made meal"]
cal_list_2000 = ["MRE"]

def get_cals(x):
    if x in cal_list_400:
        return 400

    elif x in cal_list_100:
        return 100

    elif x in cal_list_1000:
        return 1000

    elif x in cal_list_2000:
        return 2000

    elif x in cal_list_800:
        return 800

    elif x in cal_list_600:
        return 600

    elif x in cal_list_300:
        return 300

    else:
        if x == "chicken and pasta" or x == "chicken and beef sandwiches":
            cals = 2350

        elif x == "sausages and pasta":
            cals = 2150

        elif x == "fruit and cream" or "tuna sandwiches":
            cals = 1150

        elif x == "Mega-MRE":
            cals = 3750

        elif x == "peaches and cream":
            cals = 1650

        elif x == "cereal treats":
            cals = 1000

        if character[7][0] == "restaurant":
            cals += round(cals * 0.1)

        return cals


def make_choice():
    choice = input("Make your choice: ")

    not_choice = "abcdefghijklmnopqrstuvwxyz```-"
    not_choice2 = "1234567890"

    inc_entry = False

    for i in choice:
        if i in not_choice:
            inc_entry = True

    while inc_entry == True:
        choice = input("Make your choice: ")

        count = 0

        for i in choice:
            if i in not_choice or not_choice2:
                inc_entry = True

                if i in not_choice2:
                    count += 1

            else:
                count += 1

        if count == len(choice):
            inc_entry = False

    while choice == "":
        choice = input("Make your choice: ")

    print(line_break)
    return int(choice)


def choose_weapon():
    count = 1
    for i in character[4]:
        if i == "*pistol*":
            print(str(count) + ". " + i + " - ammo:", character[10][0])

        elif i == "**assault rifle**":
            print(str(count) + ". " + i + " - ammo:", character[10][1])

        else:
            print(str(count) + ". " + i)
        count += 1

    weapon_choice = make_choice()
    weapon_choice = character[4][weapon_choice - 1]

    while (weapon_choice == "*pistol*" and character[10][0] == 0) or (
            weapon_choice == "**assault rifle**" and character[10][1] < 3):
        if weapon_choice == "*pistol*" and character[10][0] == 0:
            print("You don't have any ammo for this gun\n")
            count = 1
            print("Choose again!")

            for i in character[4]:
                if i == "**assault rifle**":
                    print(str(count) + ". " + i + " - ammo:", character[10][1])

                elif i == "*pistol*":
                    count -= 1

                elif i != "*pistol*":
                    print(str(count) + ". " + i)
                count += 1

            weapon_choice = make_choice()
            weapon_choice = character[4][weapon_choice - 1]

        elif weapon_choice == "**assault rifle**" and character[10][1] < 3:
            print("\nYou don't have enough ammo for this gun")
            count = 1
            print("Choose again!")

            for i in character[4]:
                if i == "*pistol*":
                    print(str(count) + ". " + i + " - ammo:", character[10][0])

                elif i == "**assault rifle**":
                    count -= 1

                elif i != "**assault rifle**":
                    print(str(count) + ". " + i)
                count += 1

            weapon_choice = make_choice()
            weapon_choice = character[4][weapon_choice - 1]

    return weapon_choice

def ranged_attack(weapon, enemy, health):
    boss = False
    attack_missed = False

    if enemy == "Infected Commander" or enemy == "Diseased Doctor" or enemy == "Fuel Beast":
        enemy = "the " + enemy
        boss = True

    if weapon == "*pistol*":
        weapon = "pistol"
        ammo = character[10][0]
        chance = random.randint(1,3)

    elif weapon == "**assault rifle**":
        weapon = "assault rifle"
        ammo = character[10][1]
        chance = random.randint(1, 5)

    while (weapon == "pistol" and ammo > 0) or (weapon == "assault rifle" and ammo > 3):
        if weapon == "pistol":
            shots_fired = random.randint(1, 3)

            while shots_fired > character[10][0]:
                shots_fired = random.randint(1, 3)
            character[10][0] -= shots_fired

        elif weapon == "assault rifle":
            shots_fired = random.randint(3, 5)

            while shots_fired > character[10][1]:
                shots_fired = random.randint(3, 5)
            character[10][1] -= shots_fired

        if shots_fired == 1:
            round = "round is"
            hit = "hits"
            strike = "strikes"
            miss = "misses"

        else:
            round = "rounds are"
            hit = "hit"
            strike = "strike"
            miss = "miss"

        if shots_fired == 1:
            print("You fire a shot at", enemy, "with your", weapon)

        else:
            print("You fire a burst of", shots_fired, "shots at", enemy, "with your", weapon)

        if chance != 1:
            killshot = random.randint(1, 3)

            if killshot == 1:
                print("The", round, "on target and", hit + " " + enemy, "in the head!\n")
                if boss == True:
                    damage = health//2.5

                    if (damage + 100) < health:
                        crit_chance = random.randint(1, 3)
                        if crit_chance == 1:
                            damage += 100

                    elif (damage + 50) < health:
                        crit_chance = random.randint(1, 2)
                        if crit_chance == 1:
                            damage += 50

                    elif (damage + 25) < health:
                        damage += 25

                    else:
                        damage = health

                else:
                    damage = health

                if weapon == "**assault rifle**":
                    if (damage + 20) < health:
                        damage += 20

                print("Critical Hit! You hit", enemy, "for", damage, "damage")

            else:
                part_hit = random.randint(1, 3)
                if health < 40:
                    damage = health

                else:
                    if boss == True:
                        min_dam = health // 5
                        max_dam = health // 3.5

                        damage = random.randint(int(min_dam), int(max_dam))

                    else:
                        min_dam = health // 3
                        max_dam = health // 1.5

                        damage = random.randint(int(min_dam), int(max_dam))

                    if damage < 50 and health > 50 and (damage + 20) < health:
                        damage += 20

                    elif damage < 50 and health > 50 and (damage + 10) < health:
                        damage += 10

                if weapon == "**assault rifle**":
                    if (damage + 20) < health:
                        damage += 20

                if part_hit == 1:
                    print("The", round, "on target, but", strike + " " + enemy, "in the torso\n")
                    if (damage + 10) < health:
                        damage += 10

                    elif (damage + 5) < health:
                        damage += 5

                elif part_hit == 2:
                    print("The", round, "on target, but", strike + " " + enemy, "in the arm\n")

                else:
                    print("The", round, "on target, but", strike + " " + enemy, "in the leg\n")

                print("You hit the", enemy, "for", damage, "damage")

        else:
            attack_missed = True

            if shots_fired == 1:
                round = "round"

            else:
                round = "rounds"

            print("\nThe", round + " " + miss + " " + enemy + "!")

            damage = 0

        if attack_missed == False:
            print(enemy, "has", health - damage, "HP left")
            print()
            input("Press 1 to continue: ")
            if health != 0:
                print(line_break)
        return [damage, attack_missed]


def fight_zombie(zombie, weapon_choice, bonus_dam):
    swapped_weapon = False

    count = 0
    while not zombie.health <= 0:
        damage = 0
        if count != 0:
            print(line_break)

        print("You attack the",zombie.character)

        if weapon_choice == "*pistol*" or weapon_choice == "**assault rifle**":
            if weapon_choice == "*pistol*" and character[10][0] == 0 or weapon_choice == "**assault rifle**" and character[10][1] < 3:
                print("Looks like you don't have enough ammo!")
                print("You'll have to swap weapons\n")
                print("You back away from the zombie and find space to look in your bag")
                result = [0, False]

                weapon_choice = choose_weapon()
                swapped_weapon = True
            else:
                result = ranged_attack(weapon_choice, "the zombie", zombie.health)

            if result[1] == True:
                print("\nThe zombie strikes!")
                chance = random.randint(1, 7)

                if "*" in weapon_choice:
                    chance = random.randint(1, 9)                   
                if chance == 1:
                    print("The", zombie.character, "grabs you and bites!\nYOU ARE DEAD")
                    return False

                elif chance == 2:
                    print("The zombie charges forward, but you knock back its attack with your", weapon_choice)

                else:
                    print("The zombie lunges for you, but you dodge and the fight continues")

                input("Press 1 to continue: ")
                print(line_break)
                print()

            zombie.health -= result[0]
            if zombie.health < 0:
                zombie.health = 0

        else:
            if weapon_choice == "hands":
                miss_chance = random.randint(1,2)

            else:
                miss_chance = random.randint(1, 5)

            if miss_chance != 1:
                chance = random.randint(1, 2)
                if weapon_choice == "machete" or weapon_choice == "knife":
                    if chance == 1:
                        print("You stab the", zombie.character, "with your",weapon_choice)

                    else:
                        print("You slash the", zombie.character, "with your",weapon_choice)

                elif weapon_choice == "hands":
                    if chance == 1:
                        print("You swing and punch the", zombie.character, "in the head")

                    else:
                        print("You kick the", zombie.character, "as hard as you can")

                else:
                    if chance == 1:
                        print("You whack the", zombie.character, "with your", weapon_choice)

                    else:
                        print("You club the", zombie.character, "with your", weapon_choice)

                if zombie.health >= 40:
                    damage = random.randint(40, zombie.health) + bonus_dam

                else:
                    damage = zombie.health

                if weapon_choice == "hands":
                    if zombie.health > 10:
                        damage = random.randint(10, zombie.health) + bonus_dam
                        if damage == 0:
                            damage = 10

                    else:
                        damage = zombie.health

                if damage > zombie.health // 2:
                    print("Critical Hit! You hit the zombie for",damage,"damage")

                else:
                    print("You hit the zombie for",damage,"damage")

            else:
                print("You swing your",weapon_choice,"and miss")
                print("\nThe zombie strikes!")
                chance = random.randint(1,7)
                if chance == 1:
                    print("The",zombie.character,"grabs you and bites!\nYOU ARE DEAD")
                    return False

                elif chance == 2:
                    print("The zombie charges forward, but you block its attack with your",weapon_choice)

                else:
                    print("The zombie lunges for you, but you dodge and the fight continues")

            if miss_chance != 1:
                zombie.health -= damage
                if zombie.health < 0:
                    zombie.health = 0
                print("\nThe", zombie.character, "has", zombie.health, "HP left")

            input("Press 1 to continue: ")
            count += 1

    print("The zombie has been defeated!")
    chance = random.randint(1,5)
    if chance== 1:
        print("The zombie dropped",zombie.loot_drop)
        add_item(zombie.loot_drop)
    print(line_break)

    if swapped_weapon == True:
        return [True, weapon_choice]

    else:
        return [True, False]


def fight_boss(boss, weapon_choice, bonus_dam, armour):
    while boss.health > 0:
        print(line_break)
        boss.shout()
        print("You attack the", boss.name, "\n")
        miss_chance = random.randint(1, 4)

        if weapon_choice == "*pistol*" or weapon_choice == "**assault rifle**":
            if weapon_choice == "*pistol*" and character[10][0] == 0 or weapon_choice == "**assault rifle**" and character[10][1] < 3:
                print("Looks like you don't have enough ammo!")
                print("You'll have to swap weapons\n")
                print("You back away from the", boss.name, "and find space to look in your bag")
                result = [0, False]

                weapon_choice = choose_weapon()
            else:
                result = ranged_attack(weapon_choice, boss.name, boss.health)

            if result[1] == True:
                input("Press 1 to continue: ")
                print(line_break)
                print()

            damage = result[0]

        else:
            if weapon_choice == "hands":
                miss_chance = random.randint(1, 2)

            if miss_chance != 1:
                chance = random.randint(1, 2)
                if weapon_choice == "machete" or weapon_choice == "knife" or weapon_choice == "*katana*" or weapon_choice == "*butterfly knife*":
                    if chance == 1:
                        print("You stab it with your", weapon_choice)

                    else:
                        print("You slash the", boss.name,"with your", weapon_choice)

                elif weapon_choice == "hands":
                    if chance == 1:
                        print("You swing and punch the ", boss.name, "in the head")

                    else:
                        print("You kick the him as hard as you can")

                else:
                    if chance == 1:
                        print("You whack it with your", weapon_choice)

                    else:
                        print("You club the ", boss.name, "with your", weapon_choice)

                if "*" in weapon_choice:
                    bonus_dam += 20

                if boss.health >= 20:
                    damage = random.randint(20, 150) + bonus_dam

                else:
                    damage = boss.health

                if weapon_choice == "hands":
                    if boss.health > 10:
                        damage = random.randint(10, 100) + bonus_dam
                        if damage == 0:
                            damage = 10

                    else:
                        damage = boss.health

                if damage > boss.health // 2:
                    print("Critical Hit! You hit the", boss.name ,"for", damage, "damage\n")

                else:
                    print("You hit the", boss.name ,"for", damage, "damage")

                boss.health -= damage
                if boss.health < 0:
                    boss.health = 0

                print("It has", boss.health, "HP left\n")

            else:
                chance = random.randint(1,3)
                damage = 0
                if chance == 1:
                    print("You swing your",weapon_choice,"and miss\n")

                else:
                    boss.dodge()

        if boss.health > 0:
            enemy_chance = random.randint(1, 4)

            if enemy_chance != 1:
                boss.attack()
                print()
                if character[0][0] >= 20:
                    enemy_damage = random.randint(50, 100)

                else:
                    enemy_damage = character[0][0]

                if enemy_damage > character[0][0]:
                    enemy_damage = character[0][0]

                if enemy_damage > character[0][0] // 2:
                    print("Critical Hit! The", boss.name,"hit you for", enemy_damage, "damage")

                else:
                    print("The", boss.name,"hit you for", enemy_damage, "damage")

                if armour < enemy_damage and armour > 0:
                    print("Your armour blocked", armour, "damage")
                    enemy_damage -= armour
                    armour = 0
                    character[0][0] -= enemy_damage
                    if character[0][0] < 0:
                        character[0][0] = 0

                    print("\nYou have", armour, "armour left")

                elif armour > enemy_damage and armour > 0:
                    og_armour = armour
                    armour -= enemy_damage

                    print("Your armour blocked",og_armour - armour, "damage")
                    print("\nYou have", armour, "armour left")

                else:
                    character[0][0] -= enemy_damage

                if character[0][0] < 0:
                    character[0][0] = 0

                print("You have", character[0][0], "HP left")

            else:
                boss.miss()
                print()

            if character[0][0] == 0:
                print("\nThe", boss.name, "Has killed you!\nYOU ARE DEAD")
                return False

        if boss.health != 0:
            input("Press 1 to continue:")

    print("The", boss.name, "has been defeated!")
    print(line_break)
    return True


def fight_human(human_enemy, weapon_choice, bonus_dam, armour):
    swapped_weapon = False

    while human_enemy.health > 0:
        print(line_break)
        print("You attack", human_enemy.name, "\n")
        miss_chance = random.randint(1, 4)

        if weapon_choice == "*pistol*" or weapon_choice == "**assault rifle**":
            if (weapon_choice == "*pistol*" and character[10][0] == 0) or (weapon_choice == "**assault rifle**" and character[10][1] < 3):
                print("Looks like you don't have enough ammo!")
                print("You'll have to swap weapons\n")
                print("You back away from", human_enemy.name, "and find space to look in your bag")
                result = [0, False]

                weapon_choice = choose_weapon()
                swapped_weapon = True
            else:
                result = ranged_attack(weapon_choice, human_enemy.name, human_enemy.health)

            if result[1] == True:
                input("Press 1 to continue: ")
                print(line_break)

            damage = result[0]

        else:
            finisher = 0

            if weapon_choice == "hands":
                miss_chance = random.randint(1, 2)

            elif "*" in weapon_choice:
                if human_enemy.health >= 30:
                        finisher = random.randint(1, 7)

                else:
                    finisher = random.randint(1, 3)

            if miss_chance != 1:
                if finisher != 1:
                    chance = random.randint(1, 2)
                    if weapon_choice == "machete" or weapon_choice == "knife" or weapon_choice == "*katana*" or weapon_choice == "*butterfly knife*":
                        if chance == 1:
                            print("You stab him with your", weapon_choice)

                        else:
                            print("You slash", human_enemy.name,"with your", weapon_choice)

                    elif weapon_choice == "hands":
                        if chance == 1:
                            print("You swing and punch", human_enemy.name, "in the head")

                        else:
                            print("You kick the him as hard as you can")

                    else:
                        if chance == 1:
                            print("You whack him with your", weapon_choice)

                        else:
                            print("You club", human_enemy.name, "with your", weapon_choice)

                    if human_enemy.health >= 20:
                        damage = random.randint(20, human_enemy.health) + bonus_dam

                    else:
                        damage = human_enemy.health

                    if weapon_choice == "hands":
                        if human_enemy.health > 15:
                            damage = random.randint(15, 50) + bonus_dam
                            if damage == 0:
                                damage = 15

                            elif damage > human_enemy.health:
                                damage = human_enemy.health

                        else:
                            damage = human_enemy.health

                    if "*" in weapon_choice:
                        if damage + 10 <= human_enemy.health:
                            damage += 10

                else:
                    if finisher == 1:
                        damage = human_enemy.health + human_enemy.armour_val

                        if weapon_choice == "*katana*":
                            print("Your *katana* glints as it slices through the air,", human_enemy.name, "has no time to react before he is cut in half")

                        elif weapon_choice == "*sledgehammer*":
                            print("You bring your sledgehammer crashing down on his head, hearing bone splinter and crack")

                        elif weapon_choice == "*butterfly knife*":
                            print("Your *butterfly knife* blurs and dances as you slice at", human_enemy.name + ",", "and he falls back clutching his throat")

                    else:
                        if human_enemy.health >= 20:
                            damage = random.randint(20, human_enemy.health) + bonus_dam

                        else:
                            damage = human_enemy.health


                if damage > human_enemy.health // 2:
                    print("Critical Hit! You hit", human_enemy.name ,"for", damage, "damage")

                else:
                    print("You hit him for", damage, "damage\n")

            elif miss_chance == 1:
                chance = random.randint(1,3)
                if chance == 1:
                    print("You swing your",weapon_choice,"and miss\n")

                else:
                    human_enemy.dodge()

        if miss_chance != 1 or (weapon_choice == "*pistol*" or weapon_choice == "**assault rifle**"):
            if human_enemy.armour_val < damage and human_enemy.armour_val > 0:
                    print("His armour blocked", human_enemy.armour_val, "damage")
                    damage -= human_enemy.armour_val
                    human_enemy.armour_val = 0
                    human_enemy.health -= damage

                    print("\nHe has", human_enemy.armour_val, "armour left")

            elif human_enemy.armour_val > damage and human_enemy.armour_val > 0:
                og_enemy_armour = human_enemy.armour_val
                human_enemy.armour_val -= damage
                print("\nHe has", og_enemy_armour - human_enemy.armour_val, "armour left")

            else:
                human_enemy.health -= damage
                
            if human_enemy.health < 0:
                human_enemy.health = 0

            if weapon_choice != "*pistol*" and weapon_choice != "**assault rifle**":
                print("He has", human_enemy.health, "HP left\n")

        if human_enemy.health > 0:
            enemy_chance = random.randint(1, 4)

            if human_enemy.weapon == "hands":
                enemy_chance = random.randint(1, 2)

            if enemy_chance != 1:
                human_enemy.attack()
                if character[0][0] >= 20:
                    chance = random.randint(1, 3)
                    if chance == 1:
                        enemy_damage = random.randint(20, 80)

                    else:
                        enemy_damage = random.randint(20, 60)

                else:
                    enemy_damage = character[0][0]

                if human_enemy.weapon == "hands":
                    if character[0][0] >= 20:
                        chance = random.randint(1, 3)
                        if chance == 1:
                            enemy_damage = random.randint(20, 60)

                        else:
                            enemy_damage = random.randint(20, 40)

                    else:
                        enemy_damage = character[0][0]

                if enemy_damage > character[0][0] // 2:
                    print("Critical Hit!", human_enemy.name,"hit you for", enemy_damage, "damage")

                else:
                    print(human_enemy.name,"hit you for", enemy_damage, "damage")

                if armour < enemy_damage and armour > 0:
                    print("Your armour blocked", armour, "damage")
                    enemy_damage -= armour
                    armour = 0
                    character[0][0] -= enemy_damage
                    if character[0][0] < 0:
                        character[0][0] = 0

                    print("You have", armour, "armour left")

                elif armour > enemy_damage and armour > 0:
                    og_armour = armour
                    armour -= enemy_damage

                    print("Your armour blocked",og_armour - armour, "damage")
                    print("\nYou have", armour, "armour left")

                else:
                    character[0][0] -= enemy_damage

                if character[0][0] < 0:
                    character[0][0] = 0

                print("You have", character[0][0], "HP left")

            else:
                human_enemy.miss()

            if character[0][0] == 0:
                print(human_enemy.name, "Has killed you!\nYOU ARE DEAD")
                return [False, False]

        if human_enemy.health != 0:
            input("\nPress 1 to continue:")

    print(human_enemy.name, "has been killed!")
    print(line_break)
    if swapped_weapon == True:
        return [True, weapon_choice]

    else:
        return [True, False]


def fight(num, battle, boss=None):
    opp_list = []
    bonus_dam = 0
    if character[2][0] < 1500:
        print("You're low on energy and won't be able to fight as well")
        bonus_dam -= 10

    elif character[2][0] > 2000:
        print("You have plenty of energy and will fight well today")
        bonus_dam += 10

    if battle == "zombies":
        reg_count = 1
        strong_count = 1
        weak_count = 1

        for i in range(num):
            zom_type = zom_types[random.randint(0, len(zom_types) - 1)]
            fight_list.append("a " + zom_type)
            if "a " + zom_type not in opp_list:
                opp_list.append("a " + zom_type)

            else:
                if zom_type == "weak zombie":
                    weak_count += 1

                elif zom_type == "strong zombie":
                    strong_count += 1

                elif zom_type == "zombie":
                    reg_count += 1

        if weak_count > 1:
            opp_list.append(str(weak_count) + " weak zombies")
            for i in opp_list:
                if i == "a weak zombie":
                    opp_list.remove(i)

        if reg_count > 1:
            opp_list.append(str(reg_count) + " zombies")
            for i in opp_list:
                if i == "a zombie":
                    opp_list.remove(i)

        if strong_count > 1:
            opp_list.append(str(strong_count) + " strong zombies")
            for i in opp_list:
                if i == "a strong zombie":
                    opp_list.remove(i)

        count = 1
        if len(fight_list) == 1 and fight_list[0] == "a zombie":
            (fight_prompt) = "It looks like you'll be fighting a zombie"

        elif len(fight_list) > 1 or (len(fight_list) == 1 and (fight_list[0] == "a strong zombie" or fight_list[0] == "a weak zombie")):
            fight_prompt = "It looks like you'll be fighting "

            for i in opp_list:
                if count == 1:
                    fight_prompt += i

                elif count == len(opp_list):
                    fight_prompt += " and " + i

                else:
                    fight_prompt += ", " + i

                count += 1

    elif battle == "humans":
        if boss is None:
            for i in range(num):
                opp_list.append(survivors_male_list[random.randint(0, len(survivors_male_list) -1)])

            if num == 1:
                fight_prompt = "Looks like you'll be fighting 1 human, named " + opp_list[0]

            else:
                fight_prompt = "Looks like you'll be fighting " + str(len(opp_list)) + " humans, named "

                count = 0
                for i in opp_list:
                    if count < len(opp_list) - 2:
                        fight_prompt += str(opp_list[count]) + ", "

                    elif count == len(opp_list) - 2:
                        fight_prompt += str(opp_list[count]) + " and "

                    else:
                        fight_prompt += str(opp_list[count])

                    count += 1

        else:
            fight_prompt = "Looks like you'll be fighting 1 human, named " + boss
            opp_list.append(boss)


    elif battle == "boss":
        fight_prompt = "You're going to be fighting the " + boss

    elif battle == "military zombies":
        fight_prompt = "You're going to be fighting " + str(num) + "military zombies"


    print(fight_prompt)

    print("\nYou reach in your bag for a weapon:")
    if len(character[4]) == 1:
        print("But there's nothing there, you'll have to use your fists")

    weapon_choice = choose_weapon()

    if battle == "zombies":
        descriptor = zom_description_list[random.randint(0,len(zom_description_list)-1)]
        loot = item_list[random.randint(0,len(item_list) - 1)]
        count = 1
        while num > 0:
            print("Zombie #",count)
            zombie = fight_list[0]
            if zombie == "a weak zombie":
                zombie = z.Zombie(75,zombie[2:],descriptor,loot)

            elif zombie == "a strong zombie":
                zombie = z.Zombie(125,zombie[2:],descriptor,loot)

            elif zombie == "a zombie":
                zombie = z.Zombie(100,zombie[2:],descriptor,loot)
            chance = random.randint(1, 10)

            if boss is None:
                if chance == 1:
                    print("\nAs you prepare to fight, you notice this zombie", zombie.appearance)

                else:
                    print()

            else:
                print("Before you attack, you apologise to", boss, "wishing you had saved him...")

            result= fight_zombie(zombie, weapon_choice, bonus_dam)
            fight_list.remove(fight_list[0])
            if result:
                num -= 1
                count += 1

            else:
                return False

    elif battle == "military zombies":
        loot = item_list[random.randint(1, len(item_list))]
        count = 1
        while num > 0:
            print("Zombie #", count)
            zombie = "military zombie"
            descriptor = military_description_list[random.randint(0, len(military_description_list) - 1)]

            zombie = z.Zombie(150, zombie, descriptor, loot)

            chance = random.randint(1, 5)
            if boss is None:
                print("\nAs you prepare to fight, you notice this military zombie", zombie.appearance)

            else:
                print("Before you attack, you stop and thank", boss, "for what he did for you...")

            result = fight_zombie(zombie, weapon_choice, bonus_dam)
            fight_list.remove(fight_list[0])
            if result[0]:
                num -= 1
                count += 1

                if result[1] != False:
                    weapon_choice = result[1]

            else:
                return False

    elif battle == "humans":
        loot_list = []
        loot_counter = 0
        count = 1
        while num > 0:
            human_name = opp_list[0]
            print("Human Enemy #", count, "-", human_name)
            enemy_weapon = item_list[random.randint(0, len(item_list) - 1)]
            while enemy_weapon[1:7] != "weapon":
                enemy_weapon = item_list[random.randint(0, len(item_list) - 1)]

            weapon_chance = random.randint(1,5)
            if weapon_chance == 1:
                enemy_weapon = "hands"

            if enemy_weapon != "hands":
                loot_list.append(enemy_weapon)

            armour_chance = random.randint(1,5)

            if armour_chance == 1:
                enemy_armour = special_item_list[random.randint(0, len(special_item_list) - 1)]
                while enemy_armour[1:9] != "clothing":
                    enemy_armour = special_item_list[random.randint(0, len(special_item_list) - 1)]

                loot_list.append(enemy_armour)

            else:
                enemy_armour = None

            human_enemy = h.Human(human_name, enemy_weapon, enemy_armour)
            human_enemy.display_armour()

            if armour_chance == 1:
                print("He has", human_enemy.armour_val, "armour")

            result = fight_human(human_enemy, weapon_choice, bonus_dam, total_armour)
            opp_list.remove(opp_list[0])
            if result[0] == True:
                num -= 1
                count += 1
                loot_counter += 1

                if result[1] != False:
                    weapon_choice = result[1]

            else:
                return False
        for i in range(5 * loot_counter):
            loot_list.append(item_list[random.randint(0, len(item_list) -1)])

        print("It looks like they had some loot:")
        for i in range(loot_counter * 3):
            loot = loot_list[random.randint(0, len(loot_list) -1)]
            print(loot)
            add_item(loot)
            loot_list.remove(loot)
        print()

    elif battle == "boss":
        loot_list = []
        print("Boss Battle -",boss)

        if boss == "Infected Commander":
            boss_weapon = boss_item_list[0]
            boss_armour = boss_item_list[1]

        elif boss == "Diseased Doctor":
            boss_weapon = boss_item_list[2]
            boss_armour = boss_item_list[3]

        elif boss == "Fuel Beast":
            boss_weapon = boss_item_list[4]
            boss_armour = boss_item_list[5]

        loot_list.append(boss_weapon)
        loot_list.append(boss_armour)

        boss_battle = b.Boss(boss)
        result = fight_boss(boss_battle, weapon_choice, bonus_dam, total_armour)

        if not result:
            return False

        for i in range(28):
            chance = random.randint(1, 10)

            if chance != 1:
                chance = random.randint(1, 2)

                if chance == 1:
                    loot_list.append(special_item_list[random.randint(0, len(special_item_list) -1)])

                else:
                    loot_list.append(item_list[random.randint(0, len(item_list) - 1)])

            else:
                loot_list.append(ultra_special_item_list[random.randint(0, len(ultra_special_item_list) -1)])

        print("It looks like the boss dropped some loot:")
        for i in range(5):
            loot = loot_list[random.randint(0, len(loot_list) - 1)]
            print(loot)
            add_item(loot)
            loot_list.remove(loot)
        print()

    if (weapon_choice == "**assault rifle**" and rifle_supp == False) or (weapon_choice == "*pistol*" and pistol_supp == False):
        chance = random.randint(1, 3)

        if chance == 1:
            print("But it looks like the shooting attracted some zombies")
            zom_num = random.randint(2, 5)

            fight_result = fight(zom_num, "zombies")

            if fight_result:
                print("The zombies lie dead, and you really need to find a suppressor")

            else:
                game = False

    return True


def describe_human(human_type,human_count):
    if human_type == "raider":
        if human_count == 1:
            return "It looks like he is wearing " + raider_descriptions_list[random.randint(0, len(raider_descriptions_list)-1)]

        else:
            sentence = ""
            count = 0
            for i in range(human_count):
                count += 1
                if count == 1:
                    sentence += "It looks like one is wearing " + raider_descriptions_list[random.randint(0, len(raider_descriptions_list)-1)]

                else:
                    sentence += " and another is wearing " + raider_descriptions_list[random.randint(0, len(raider_descriptions_list)-1)]

            return sentence

    elif human_type == "survivor":
        if human_count == 1:
            return "It looks like he is wearing " + survivor_descriptions_list[random.randint(0, len(survivor_descriptions_list)-1)]

        else:
            sentence = ""
            count = 0
            for i in range(human_count):
                count += 1
                if count == 1:
                    sentence += "It looks like one is wearing " + survivor_descriptions_list[random.randint(0, len(survivor_descriptions_list)-1)]

                else:
                    sentence += " and another is wearing " + survivor_descriptions_list[random.randint(0, len(survivor_descriptions_list)-1)]

            return sentence


def select_random_item():
    chance = random.randint(1,10)
    armour_check = False
    your_item = "Journal"

    count = 30

    while your_item == "Journal" and count > 0:
        count -= 1

        for i in current_clothing:
            if len(i) > 0:
                armour_check == True

        if chance == 1 and armour_check == True:
            category = current_clothing[random.randint(0,4)]
            while len(category) == 0:
                category = current_clothing[random.randint(0, 4)]

        elif chance == 2 and len(character[8]) > 0:
            category = character[8]

        else:
            category = character[random.randint(3, 5)]
            while len(category) == 0:
                category = character[random.randint(3, 5)]

        if len(category) > 1:
            your_item = category[random.randint(0, len(category) - 1)]

        else:
            your_item = category[0]

        while your_item == "hands":
            category = character[random.randint(3, 5)]
            while len(category) == 0:
                category = character[random.randint(3, 5)]

            your_item = category[random.randint(0, len(category) - 1)]

        if category == character[3]:
            your_item = "(food) " + your_item

        elif len(character[4]) > 1 and category[0] == character[4][0]:
            your_item = "(weapon) " + your_item

        elif len(character[5]) > 0 and category[0] == character[5][0]:
            your_item = "(meds) " + your_item

        elif category[0] == character[9][0]:
            your_item = your_item

        elif category in current_clothing:
            your_item = "(clothing) " + your_item

    if count == 0:
        return None

    else:
        return your_item


def get_card(card):
    read_card = "The card is the "
    if card[0] == "A":
        read_card += "Ace of "
        value = 11

    elif card[0] == "K":
        read_card += "King of "
        value = 10

    elif card[0] == "Q":
        read_card += "Queen of "
        value = 10

    elif card[0] == "J":
        read_card += "Jack of "
        value = 10

    else:
        if card[0] == "1":
            read_card += "10 of "
            value = 10

        else:
            read_card += card[0] + " of "
            value = int(card[0])


    if card[-1] == "H":
        read_card += "Hearts"

    elif card[-1] == "C":
        read_card += "Clubs"

    elif card[-1] == "D":
        read_card += "Diamonds"

    elif card[-1] == "S":
        read_card += ("Spades")

    read_card += "\n"

    print(read_card)
    return(value)


def play_blackjack(name):
    print("You've chosen to play Blackjack with", name)
    line_break

    your_hand = 0
    opp_hand = 0

    print()
    print(name, "deals you a card")
    card = card_list[random.randint(0, len(card_list) - 1)]
    card_list.remove(card)
    value = get_card(card)
    your_hand += value

    print(name, "deals you another card")
    card = card_list[random.randint(0, len(card_list) - 1)]
    card_list.remove(card)
    value = get_card(card)
    if value == 11:
        if (your_hand + value) > 21:
            value = 1
    your_hand += value

    print("Your hand is now worth", your_hand)
    input("Press 1 to Continue:")
    print(line_break)

    print()
    print(name, "deals himself a card")
    card = card_list[random.randint(0, len(card_list) - 1)]
    card_list.remove(card)
    value = get_card(card)
    opp_hand += value

    print(name, "deals himself another card")
    card = card_list[random.randint(0, len(card_list) - 1)]
    card_list.remove(card)
    value = get_card(card)
    if value == 11:
        if (opp_hand + value) > 21:
            value = 1
    opp_hand += value

    print("His hand is now worth", opp_hand)
    input("Press 1 to Continue:")
    print(line_break)

    your_hit = True
    opp_hit = True
    win = None
    print_score = True

    while your_hit == True or opp_hit == True:
        if your_hit == True:
            print("\nYour hand is worth", your_hand)
            if opp_hit == False and print_score == True:
                print("His hand is worth", opp_hand)
            print("Will you:\n1. Hit\n2. Hold")
            choice = make_choice()

            if choice == 1:
                print("You choose to hit")
                print(name, "deals you another card")
                card = card_list[random.randint(0, len(card_list) - 1)]
                card_list.remove(card)
                value = get_card(card)
                if value == 11:
                    if (your_hand + value) > 21:
                        value = 1

                your_hand += value

                print("Your hand is now worth", your_hand)
                input("Press 1 to Continue:")
                print(line_break)
                if your_hand > opp_hand:
                    opp_hit = True

                if your_hand >= 21:
                    if your_hand > 21:
                        print("You've gone bust\n")

                        win = False
                        return win

            elif choice == 2:
                print("You choose to hold")
                your_hit = False

        if your_hand > opp_hand:
            opp_hit == True

        if opp_hit == True and win is None:
            if win != False:
                if your_hand > opp_hand:
                    hit_chance = 1

                elif opp_hand > 18:
                    hit_chance = 0

                elif opp_hand == 18:
                    hit_chance = random.randint(1, 20)

                elif 15 <= opp_hand < 18:
                    hit_chance = random.randint(1, 3)

                elif 12 <= opp_hand < 15:
                    hit_chance = random.randint(1, 2)
                    if hit_chance != 1:
                        hit_chance = random.randint(1, 3)

                else:
                    hit_chance = 1

                if hit_chance == 1:
                    print()
                    print(name, "deals himself another card")
                    card = card_list[random.randint(0, len(card_list) - 1)]
                    card_list.remove(card)
                    value = get_card(card)
                    if value == 11:
                        if (opp_hand + value) > 21:
                            value = 1
                    opp_hand += value

                    print("His hand is now worth", opp_hand)
                    print_score = False

                    if opp_hand >= 21:
                        if opp_hand > 21:
                            print("He's gone bust\n")
                            your_hit = False

                        opp_hit = False

                    elif opp_hand > your_hand and your_hit == False:
                        opp_hit = False
                        your_hit = False

                else:
                    if your_hand < 22:
                        print()
                        print(name, "chooses to hold")
                        opp_hit = False
                        print_score = True

        elif win is None:
            if your_hand < 22:
                print(name, "chooses to hold")
                opp_hit = False
                print_score = True

    input("Press 1 to Continue:")
    print(line_break)

    if your_hand == opp_hand:
        win = "Draw"

    elif your_hand > 21 or opp_hand > 21:
        if your_hand > 21:
            win = False

        else:
            win = True

    elif your_hand > opp_hand:
        win = True

    else:
        win = False

    return win


def armour_val(armour):
    if armour == head_armour[0]:
        return 20

    elif armour == head_armour[1]:
        return 30

    elif armour == torso_armour[0]:
        return 150

    elif armour == torso_armour[1]:
        return 60

    elif armour == torso_armour[2]:
        return 75

    elif armour == torso_armour[3]:
        return 15

    elif armour == torso_armour[4]:
        return 40

    elif armour == torso_armour[5]:
        return 125

    elif armour == leg_armour[0]:
        return 10

    elif armour == foot_armour[0]:
        return 15

    elif armour == hand_armour[0]:
        return 50

    elif armour == hand_armour[1]:
        return 5


def equip_armour(armour,total_armour):
    if armour in head_armour:
        if len(current_clothing[0]) > 0:
            character[8][0].append("(clothing) " + current_clothing[0][0])
            total_armour -= armour_val(current_clothing[0][0])
            print("Your", current_clothing[0][0], "has been placed in your inventory")
            current_clothing[0].remove(current_clothing[0][0])

        current_clothing[0].append(armour)

    elif armour in torso_armour:
        if len(current_clothing[1]) > 0:
            character[8].append("(clothing) " + current_clothing[1][0])
            total_armour -= armour_val(current_clothing[1][0])
            print("Your", current_clothing[1][0], "has been placed in your inventory")
            current_clothing[1].remove(current_clothing[1][0])

        current_clothing[1].append(armour)

    elif armour in leg_armour:
        if len(current_clothing[2]) > 0:
            character[8][0].append("(clothing) " + current_clothing[2][0])
            total_armour -= armour_val(current_clothing[2][0])
            print("Your", current_clothing[2][0], "has been placed in your inventory")
            current_clothing[2].remove(current_clothing[2][0])

        current_clothing[2].append(armour)

    elif armour in foot_armour:
        if len(current_clothing[3]) > 0:
            character[8][0].append("(clothing) " + current_clothing[3][0])
            total_armour -= armour_val(current_clothing[3][0])
            print("Your", current_clothing[3][0], "has been placed in your inventory")
            current_clothing[3].remove(current_clothing[3][0])

        current_clothing[3].append(armour)

    elif armour in hand_armour:
        if len(current_clothing[4]) > 0:
            character[8][0].append("(clothing) " + current_clothing[4][0])
            total_armour -= armour_val(current_clothing[4][0])
            print("Your", current_clothing[4][0], "has been placed in your inventory")
            current_clothing[4].remove(current_clothing[4][0])

        current_clothing[4].append(armour)

    armour_added = armour_val(armour)
    total_armour += armour_added

    print("You are now wearing the", armour, "for", armour_added, "armour")
    print("Your total armour is now", total_armour)
    character[8].remove("(clothing) " + armour)

    return total_armour


def remove_item(item):
    if item[0:2] == "(m":
        character[5].remove(item[7:])

    elif item[0:2] == "(f":
        character[3].remove(item[7:])

    elif item[0:2] == "(w":
        character[4].remove(item[9:])

    elif item[0:2] == "(c":
        if item in character[8]:
            character[8].remove(item)

        else:
            for i in current_clothing:
                for j in i:
                    if j == item[12:]:
                        i.remove(item[12:])

def cook_food():
    cook_check =  False
    cook_list = []
    if "chicken" in character[3] and "pasta" in character[3] and "tomato sauce" in character[3]:
        cook_check = True
        cook_list.append("chicken and pasta")

    if "sausages" in character[3] and "pasta" in character[3] and "tomato sauce" in character[3]:
        cook_check = True
        cook_list.append("sausages and pasta")

    if "apple" in character[3] and "banana" in character[3] and "can of whipped cream" in character[3]:
        cook_check = True
        cook_list.append("fruit and cream")

    if "can of tuna" in character[3] and "bread" in character[3]:
        cook_check = True
        cook_list.append("tuna sandwiches")

    if "chicken" in character[3] and "beef jerky" in character[3] and "bread" in character[3]:
        cook_check = True
        cook_list.append("chicken and beef sandwiches")

    if "chicken" in character[3] and "beef jerky" in character[3] and "MRE" in character[3]:
        cook_check = True
        cook_list.append("deluxe MRE")

    if "canned peaches" in character[3] and "can of whipped cream" in character[3]:
        cook_check = True
        cook_list.append("peaches and cream")

    if "cereal" in character[3] and "bag of marshmallows" in character[3]:
        cook_check = True
        cook_list.append("cereal treats")

    if cook_check == True:
        print("It looks like you have enough ingredients to do some cooking:\n1. Cook\n2. Don't cook")
        choice = make_choice()

        if choice == 1:
            count = 1
            print("What would you like to cook?")
            for i in cook_list:
                print(str(count) + ". " + i)
                count += 1
            print(str(count) + ". nothing")

            choice = make_choice()

            if choice != (count + 1):
                recipe = cook_list[choice - 1]

                if recipe == "chicken and pasta":
                    remove_list = ["chicken", "pasta", "tomato sauce"]

                elif recipe == "sausages and pasta":
                    remove_list = ["sausages", "pasta", "tomato sauce"]

                elif recipe == "fruit and cream":
                    remove_list = ["apple", "banana", "can of whipped cream"]

                elif recipe == "tuna sandwiches":
                    remove_list = ["can of tuna", "bread"]

                elif recipe == "chicken and beef sandwiches":
                    remove_list = ["chicken", "beef jerky", "bread"]

                elif recipe == "deluxe MRE":
                    remove_list = ["chicken", "beef jerky", "MRE"]

                elif recipe == "peaches and cream":
                    remove_list = ["canned peaches", "can of whipped cream"]

                elif recipe == "cereal treats":
                    remove_list = ["cereal", "bag of marshmallows"]

                for i in remove_list:
                    character[3].remove(i)

                character[3].append(recipe)
                print("Nice,",recipe,"has been added to your items\n")


                if character[7][0] == "restaurant":
                    print("Since you're cooking at the restaurant, your food is a little better than expected\n")


def take_rest():
    print("You'll be taking some rest today")

    if len(afflictions) > 0 or character[0][0] < 100:
        if len(afflictions) > 0:
            print("You lie down and try get some sleep")
            print("Hopefully your", medical_prompt, "will heal and you'll be able to go out tomorrow\n")

            if character[7][0] == "house":
                print("Since you're resting in your comfy bed, you should have a better chance of healing")

            for i in afflictions:
                if character[7][0] == "house":
                    chance = random.randint(1, 2)

                else:
                    chance = random.randint(1, 3)
                if chance == 1:
                    print("Your", i, "has healed")
                    afflictions.remove(i)

                else:
                    print("Your", i, "hasn't healed")

        if character[0][0] < 100:
            chance = random.randint(1, 2)
            if chance == 1:
                HP_healed = random.randint(1, 25)
                print("You gained", HP_healed, "HP")
                character[0][0] += HP_healed

                if character[0][0] > 100:
                    character[0][0] = 100

                print("You now have", character[0][0], "/ 100 HP")

    else:
        print("You don't quite know why you chose to rest today, but everyone deserves a day off...")


def journal_entry(info):
    journal_entry = "Day " + str(day) + " - " + info
    journal.append(journal_entry)


username_list = []

with open("scores.csv", "r") as prev_usernames:
    read_users = csv.reader(prev_usernames)
    for row in read_users:
        username_list.append(row[0])

prev_usernames.close()

for i in range(len(username_list)):
    username_list[i] = username_list[i].upper()

username = input("Enter your Username: ")

while username.upper() in username_list:
    print("That username is already taken\n")
    username = input("Enter your Username: ")

print("\nThis game is played with the number keys corresponding to each choice\n")
print("Are you ready to Try Survive?")
play = int(input("Click 1 to Play: "))

while play != 1:
    play = int(input("Click 1 to Play: "))

while game:
    calories_used = 0
    day += 1
    print(line_break)
    print("Day",str(day))
    print(line_break)
    if day == 1:
        print("You're driving home from work when the radio is interrupted by an emergency broadcast")
        print("The government is warning of a disease which makes the dead come back to life and attack the living\n")
        print("You realise you need to find shelter")
        print("Will you:\n1. Make your way home, but closer to the city\n2. Get back to the restaurant you work at\n3. Drive to the forest nearby and camp out in your car")
        choice = make_choice()

        if choice == 1:
            character[7].append("house")

            print("The city is in chaos but you manage to get back to your house in one piece")
            print("You hurry inside, but it seems the fighting hasn't reached this area, yet...\n")

            print("You have a glass of water and then get to work")
            print("You do a quick sweep of your house and find:")
            random_item(3, 5, "normal")

        elif choice == 2:
            character[7].append("restaurant")

            print("The city is in chaos but you manage to get back to the restaurant in one piece")
            print("You hurry inside but it seems everyone else has left, you wonder if you'll ever see them again...\n")

            print("You do a quick sweep of the restaurant and find:")
            random_item(3, 5, "normal")

        elif choice == 3:
            character[7].append("campground clearing")

            print("You drive out into the forest and it seems everyone else is still in the city")
            print("You pull up to a campground in a clearing, this will do nicely...\n")

            print("You find a spring nearby and have some water")
            print("You do a quick sweep of the campground and find:")
            random_item(1, 3, "normal")

        calories_used = random.randint(1400,2000)
        character[2][0] = character[2][0] - calories_used
        if character[2][0] < 0:
            character[2][0] = 0
        print("\nToday you used", calories_used, "calories")
        print("You have", character[2][0], "calories left\n")

        cook_food()

        print("Would you like to eat something?\n1. Yes\n2. No, it's time to sleep")
        choice = make_choice()

        if choice == 1:
            eat = True

            while character[2][0] < 5000 and eat is True and len(character[3])> 0:
                print("You have:")
                count = 1
                for i in character[3]:
                    print(str(count) + ". " + i + " - " + str(get_cals(i)) + " calories")
                    count += 1

                if len(character[3]) > 1:
                    print(str(count) + ". " + "Consume all")

                choice = make_choice()
                if choice == count:
                    total_cals = 0

                    for i in character[3]:
                        total_cals += get_cals(i)

                    character[3] = []

                    print("You consumed everything for", total_cals, "calories")
                    character[2][0] += total_cals
                    print("You now have:", character[2][0], "calories")
                    eat = False

                else:
                    character[2][0] += get_cals(character[3][choice - 1])
                    print("You consumed:", character[3][choice - 1], "for", get_cals(character[3][choice - 1]),"calories\n")
                    character[3].remove(character[3][choice - 1])
                    print("You now have:", character[2][0], "calories")
                    print("Do you want to eat more?\n1. Yes\n2. No, it's time to sleep")
                    choice = make_choice()
                    if choice == 2:
                        eat = False

            if len(character[3]) == 0 and eat == True:
                print("You have no food")

        print("You close your eyes and go to sleep")
    
        log = "I survived my first day at the " + character[7][0]
        journal_entry(log)

        input("\nPress 1 to continue to Day "  + str((day + 1)) + ": ")
        days_no_water = 0

    elif day > 1:
        count = 0
        card_list = []
        for i in range(4):
            suit = suits[count]
            for j in range(14):
                if j == 1:
                    card_list.append("ACE" + suit)

                elif j == 11:
                    card_list.append("KING" + suit)

                elif j == 12:
                    card_list.append("QUEEN" + suit)

                elif j == 13:
                    card_list.append("JACK" + suit)

                elif j != 0:
                    card_list.append(str(j) + suit)

            count += 1

        possible_locations = ["Military Base", "Fuel Depot", "Hospital", "Trader's Hideout"]
        water_drank = False
        print("You blink your eyes open and take a look around at your home at the",character[7][0])
        if character[7][0] == "campground clearing":
            print("You take a drink from the nearby spring")
            water_drank = True

        elif day == 2 and character[7][0] != "campground clearing":
            print("It looks like the electricity went out during the night, and the water's stopped too")

        if days_no_water == 0:
            character[1][0] = "Hydrated"

        elif days_no_water == 1:
            character[1][0] = "Thirsty"

        elif days_no_water == 2:
            character[1][0] = "Parched"

        elif days_no_water == 3:
            character[1][0] = "Dehydrated"

        elif days_no_water > 3:
            character[1][0] = "Severely Dehydrated"

        print("You feel", character[1][0])

        if len(character[6]) > 0:
            item_chance = random.randint(1,7)

            if item_chance == 1:
                friend = character[6][random.randint(0, len(character[6]) - 1)]
                if len(friend) == 1:
                    friend_grammar = "friend"
                    print("\nIt looks like", friend[0], "visited while you were asleep!")
                    print("He left you:")

                else:
                    friend_grammar = "friends"
                    print("\nIt looks like " + friend[0] + " and " + friend[1] + " visited while you were asleep!")
                    print("They left you:")

                rarity_chance = random.randint(1,8)
                random_item(1,3, "normal")

                if rarity_chance == 1:
                    random_item(1,2, "special")

                if len(enemy_list) > 0:
                    print("\nBut it looks like someone else was here too")
                    print("They've left you a warning message...")
                    print("They weren't able to get you today with your", friend_grammar, "around, but they'll find you again soon...")

        if character[9][0] == 1:
            print("\nYour car has 1 litre of fuel")

        else:
            print("\nYour car has", character[9][0], "litres of fuel")

        loop = True
        while loop:
            print("\nWhat will you choose to do today?\n1. Scavenge for supplies\n2. Explore\n3. Take some rest")
            choice = make_choice()
            if choice == 2 and len(afflictions) == 0:
                if character[9][0] < 5:
                    print("You don't have enough fuel to explore...")

                else:
                    loop = False

            else:
                loop = False

        if choice == 2 and len(afflictions) == 0:
            print("You decide to fuel up your car and explore")
            print("\nWhere will you travel to?")
            count = 1
            for i in explore_list:
                print(str(count) + ". " + i)
                count += 1
            choice = make_choice()

            temp_location = explore_list[choice - 1]
            location = temp_location[0:-11]
            fuel_needed = int(explore_list[choice - 1][-9])

            while character[9][0] < fuel_needed:
                print("You don't have enough fuel to go this far...")
                print("\nWhere will you travel to?")
                count = 1
                for i in explore_list:
                    print(str(count) + ". " + i)
                    count += 1
                choice = make_choice()

                location = explore_list[choice - 1][0:-11]
                fuel_needed = int(explore_list[choice - 1][-9])

            kilometres = random.randint(20, 50)
            chance = random.randint(1, 3)
            result = True
            print("You decide to explore the", location)
            character[9][0] -= fuel_needed

            if chance == 1:
                setting = "still daytime"

            elif chance == 2:
                setting = "getting late"

            else:
                setting = "the middle of the night"

            print("You drive around", kilometres, "kilometres, but when you arrive it's", setting)
            print("You're close by, but you park your car to avoid unwanted attention")
            if setting == "getting late":
                print("It'll be dangerous at night, so you better be quick")

            elif setting == "the middle of the night":
                print("You can't make out much in your pitch black surroundings")
                print("Will you:\n1. Push forward through the dark\n2. Take shelter till the morning")
                choice = make_choice()

                if choice == 1:
                    chance = random.randint(1, 2)
                    zombies = random.randint(3, 10)
                    if chance == 1:
                        print("You narrowly avoid a group of", zombies, "zombies, but you make it through without being seen")

                    elif chance == 2:
                        print("You make your way towards the", location, "but a group of",zombies, "cuts you off!")
                        print("They've seen you, and you'll have to fight them off")
                        result = fight(zombies, "zombies")

                        if not result:
                            game = False

                        if result:
                            zombies_killed += zombies
                            print("After making sure nothing is following you, you head towards the", location)

                elif choice == 2:
                    print("You decide to wait until morning to explore the", location)
                    chosen_shelter = shelter[random.randint(0, 2)]
                    print("You find a", chosen_shelter, "to sleep in till morning")

                    chance = random.randint(1, 2)
                    if chance == 1:
                        zombies = random.randint(2, 5)
                        print("But inside is", zombies, "zombies!")
                        print("You'll have to fight them off quick before they attract attention")
                        result = fight(zombies, "zombies")

                        if result:
                            zombies_killed += zombies
                            print("You manage to fight off the zombies and secure the", chosen_shelter,"for the night")
                            day += 1
                            journal_entry("Had to fight some zombies to secure shelter while exploring")

                        if not result:
                            game = False

                    elif chance == 2:
                        print("It's deserted thankfully, and you fall into a restless sleep")
                        journal_entry("Had to find shelter while exploring, will get there tomorrow")

                        day += 1

                    if result:
                        print("When you wake up, you head to the", location)

            if result:
                print("You walk for a bit, keeping your head low and your eyes up, but you meet nothing along the way")
                print("\nYou've arrived at the", location)
                print("It looks deserted, so you head inside")
                chance = random.randint(1, 2)
                if chance == 1:
                    human_amount = random.randint(1, 2)
                    if human_amount == 1:
                        print("You enter the", location, "but you hear someone moving around up ahead")

                    else:
                        print("As you enter the", location, "you hear some people talking up ahead")

                    chance = random.randint(1, 2)
                    if chance == 1:
                        human = "survivor"

                    elif chance == 2:
                        human = "raider"

                    print("As you get closer, you notice...")
                    print(describe_human(human, human_amount))
                    print()

                    print("Will you:\n1. Try sneak past\n2. Approach them")
                    choice = make_choice()

                    if choice == 1:
                        print("You stick to the shadows, hoping you aren't spotted")

                        chance = random.randint(1, 2)
                        if chance == 1:
                            print("As you pass by, they shout out and you come to a stop")
                            spotted = True

                        elif chance == 2:
                            print("Your attempt at stealth succeeds, and you sneak by undetected")
                            spotted = False

                    elif choice == 2:
                        print("You take a quick breath and then step out of your cover")
                        if human_amount == 1:
                            print("He spins around, alarmed at your presence and grabs for his weapon")

                        else:
                            print("They spin around, alarmed at your presence and grab for their weapons")
                        print("But you quickly explain you're not here to hurt anyone\n")
                        spotted = True

                    if spotted:
                        if human == "survivor":
                            print("You prepare for the worst but instead they smile and greet you")
                            survivor1 = survivors_male_list[random.randint(0, len(survivors_male_list) - 1)]
                            if human_amount == 1:
                                print("He introduces himself as", survivor1)
                            else:
                                survivor2 = survivors_male_list[random.randint(0, len(survivors_male_list) - 1)]
                                print("They introduce themselves as", survivor1, "and", survivor2)
                                print("\nThey don't have any problem with you being here")

                            print("But", survivor1, "has hurt himself and really needs medicine\n")
                            if len(character[5]) > 0:
                                print("Will you:\n1.Give", survivor1, "some medicine\n2.Refuse")
                                choice = make_choice()

                                if choice == 1:
                                    print("You choose to help", survivor1)
                                    print("Click the corresponding button to select an item")
                                    print("You have:")
                                    count = 1
                                    for i in character[5]:
                                        print(str(count) + ". " + i)
                                        count += 1
                                    choice = make_choice()
                                    print("You give him", character[5][choice - 1])
                                    character[5].remove(character[5][choice - 1])

                                    if human_amount == 1:
                                        print("He thanks you as you have saved his life")
                                        print("He promises to try help you in the future")
                                        survivor_group = [survivor1]
                                        character[6].append(survivor_group)
                                        print(survivor1, "is now your Friend")
                                        log = "Made a new friend named " + survivor1 + " while exploring"
                                        journal_entry(log)

                                    elif human_amount > 1:
                                        print("They thank you as you have saved", survivor1 + "'s", "life")
                                        print("They promise to try help you in the future")
                                        survivor_group = [survivor1, survivor2]
                                        character[6].append(survivor_group)
                                        print(survivor1, "and", survivor2, "are now your Friends")

                                        log = "Made some new friends named " + survivor1 + " and " + survivor2 + " while exploring"
                                        journal_entry(log)

                                    print("\nWith this good deed, you say goodbye and head on your way")

                                elif choice == 2:
                                    if human_amount == 1:
                                        print(survivor1, "looks at you sadly but doesn't speak")
                                        print("You turn and leave him to die, he will not last long...")

                                        journal_entry("Found a survivor needing medicine but left him to die")

                                    else:
                                        print(survivor2, "goes to shout at you but he's stopped by", survivor1)
                                        print("They look at you sadly as you walk away, he will not last long...")

                                        journal_entry("Found some survivors needing medicine but didn't help them")

                            else:
                                print("But you don't have any medicine and you cannot help")
                                print("You explain this to him and he nods, accepting his fate")
                                print("With nothing more to do or say, you leave him to die...")

                                journal_entry("A survivor was in need of medicine but I couldn't help him")

                        elif human == "raider":
                            print("You've fallen into a raider trap!")
                            fight_result = fight(human_amount, "humans")
                            if not fight_result:
                                game = False

                            else:
                                if character[0][0] > 20:
                                    journal_entry("Had to fight a raider while exploring")

                                else:
                                    journal_entry("Had to fight a raider while exploring, I barely survived")

                elif chance == 2:
                    print("You tread lightly through the", location, "but it looks like there's nobody else here")

                if game:
                    if location == "Radio Tower":
                        print("\nYou find the main terminal at the Radio Tower, and it's intact")
                        print("On the terminal you find two possible locations:")

                        temp_location_list = []
                        count = 1
                        for i in range(2):
                            new_location = ""
                            if new_location in temp_location_list:
                                while new_location in temp_location_list:
                                    new_location = possible_locations[random.randint(0,len(possible_locations) - 1)]

                                temp_location_list.append(new_location)

                            else:
                                new_location = possible_locations[random.randint(0, len(possible_locations) - 1)]
                                temp_location_list.append(new_location)
                            print(str(count) + ". " + new_location)
                            possible_locations.remove(new_location)
                            count += 1

                        choice = make_choice()
                        print("You have gathered info on the location of the",temp_location_list[choice - 1])
                        fuel_required = random.randint(5,9)
                        explore_list.append(temp_location_list[choice - 1] + " (" + str(fuel_required) + " Litres)")

                    elif location == "Military Base":
                        print("\nYou walk by deserted barracks and empty offices, but something doesn't feel right")
                        print("You make your way deeper and deeper into the complex")
                        print("But you can't shake the feeling that you're not alone")
                        chance = random.randint(1,3)

                        if chance == 1:
                            print("\nYou find yourself looking at a huge reinforced door, it's clearly hiding something...")
                            print("You investigate and find it's unlocked, the army must have left in a hurry")
                            print("As you struggle to open it you hear a roar and the door flies open!")

                            enemy = "Infected Commander"
                            fight_result = fight(1, "boss", enemy)
                            if not fight_result:
                                game = False

                        else:
                            print("\nYou find yourself at the storage depot")
                            zom_num = random.randint(5,10)
                            enemy = "military zombies"
                            print("But as you prepare to enter, a group of", str(zom_num) + " " + enemy, "swarms out!")
                            fight_result = fight(zom_num, "military zombies")

                            if not fight_result:
                                game = False

                            else:
                                zombies_killed += zom_num

                        if game:
                            print("With the", enemy, "dead, you're free to look around")
                            print("You scavenge around the area and find a chest of military loot!")
                            print("\nYou look inside and find:")
                            random_item(1,5,"normal")
                            random_item(1,3,"special")
                            random_item(0,1, "ultra special")

                            if chance == 1:
                                journal_entry("Had to fight an Infected Commander, but got some good loot for my trouble")

                            else:
                                journal_entry("Had to fight an some military zombies, but got some good loot for my trouble")

                    elif location == "Hospital":
                        print("There must have been a huge battle here recently, the hospital is in bad shape")
                        print("The smell of gunpowder is still in the air as you creep through the main building")
                        print("You follow the signs towards the storage rooms")

                        chance = random.randint(1, 3)

                        if chance == 1:
                            chance = random.randint(1, 2)
                            zom_num = random.randint(3,8)
                            print()

                            
                            print("You find yourself in the waiting room, and it's full of undead patients!")
                            enemy = "zombies"

                            print("Will you:\n1. Attack them head on\n2. Try sneak past")
                            choice = make_choice()

                            if choice == 1:
                                print("You sprint towards the group of",zom_num, "zombies and cut one down in a surprise attack")
                                fight_result = fight(zom_num - 1, enemy)

                                if not fight_result:
                                    game = False

                                else:
                                    zombies_killed += zom_num
                                    print("With the", enemy, "dead, you can loot the area")

                            elif choice == 2:
                                chance = random.randint(1,2)
                                print("You wait for a few minutes till you see a gap in the crowd, and then you move")

                                if chance == 1:
                                    print("As quietly as possible you begin to inch forward towards the door on the other side")
                                    print("You're obscured by the shadows the fresh blood and gunpowder covers your scent")
                                    print("You make it to the next room and continue on your way, unseen...")

                                else:
                                    print("You stick to the shadows and try navigate around the group unseen")
                                    print("But as you reach the door, your shoe squeaks in a pool of blood")
                                    print("The zombies jolt towards the sound in unison and you know you'll have to fight...")

                                    fight_result = fight(zom_num, enemy)

                                    if not fight_result:
                                        game = False

                                    else:
                                        zombies_killed += zom_num
                                        print("With the", enemy, "dead, you can loot the area")

                                        journal_entry("Had to kill some infected patients, but there were good meds at the hospital")

                        else:
                            print("You find the storage room and without a single zombie in your way")
                            if chance == 2:
                                print("As you push the door and it creaks open, you can't help but feel a sense of dread...")
                                print("You make your way in and thankfully it's not pitch black")
                                print("\nBut there's something else in here with you...")
                                print("A Diseased Doctor snarls and jumps out from the shadows!")

                                fight_result = fight(1, "boss", "Diseased Doctor")

                                if not fight_result:
                                    game = False

                                else:
                                    print("With the Diseased Doctor dead, you can loot the area")

                                    journal_entry("Had to kill a Diseased Doctor, but there were good meds at the hospital")

                            elif chance == 3:
                                print("It seems you've finally gotten lucky and there's nobody around")
                                journal_entry("Got lucky while exploring the hospital, nothing here but loot")

                        if game:
                            print("You scavenge the area and find a chest of medical loot!")
                            print("\nYou look inside and find:")
                            random_item(5, 8, "normal","meds")
                            random_item(1, 3, "special")

                    elif location == "Fuel Depot":
                        print("It looks like the", location, "has seen better days")
                        print("Most of the people in the area must have come here to scavenge for fuel")
                        print("You see burnt out cars and buses full of skeletons")
                        print("It looks like the military must have used the fuel as a last ditch weapon")
                        print("You'll have to hope there's some left")

                        print("\nAs you navigate the complex, you see more and more bodies")
                        print("You round the corner towards the centre of the depot and see an undamaged fuel tank")

                        chance = random.randint(1, 3)

                        if chance == 1:
                            print("But you're suddenly face to face with a burning zombie clad in flame-proof gear!")
                            print("If you want to scavenge at the", location, "you'll have to fight the Fuel Beast first...")

                            fight_result = fight(1, "boss", "Fuel Beast")

                            if not fight_result:
                                game = False

                            else:
                                print("With the Fuel Beast dead, you can loot the area")
                                journal_entry("Killed the Fuel Beast and found loads of fuel for my car")

                        elif chance == 2:
                            print("But as you move out from cover a horde of scorched zombies pours out into the open!")
                            print("You run for some containers and they give chase")
                            print("Will you:\n1. Hide and wait for them to pass\n2. Try lose them in the containers")
                            choice = make_choice()

                            if choice == 1:
                                print("You've got a head start on the horde and are able to duck into an open container")
                                chance = random.randint(1,4)

                                if chance == 1:
                                    print("But instead of passing by, the horde pours in and tears you to shreds...\nYOU HAVE DIED")
                                    game = False

                                else:
                                    print("As the horde passes by, you almost choke on the fumes and give yourself away")
                                    print("But you manage to hold yourself together and they don't notice you")
                                    print("You wait till they're long gone before you sneak back out and towards the fuel tank")

                                    journal_entry("Dodged a horde and found loads of fuel for my car")

                            elif choice == 2:
                                print("With the horde hot on your tail you run left and right between the stacks of containers")
                                chance = random.randint(1, 2)

                                if chance == 1:
                                    zom_num = random.randint(3,8)
                                    print("You look back and see", zom_num, "zombies are still behind you")
                                    print("You'll have to fight them here...")
                                    fight_result = fight(zom_num,"zombies")

                                    if not fight_result:
                                        game = False

                                    else:
                                        zombies_killed += zom_num
                                        print("With the horde gone and the zombies dealt with, you're free to scavenge")

                                        journal_entry("Fought some scorched zombies and found loads of fuel for my car")

                                elif chance == 2:
                                    print("You run as fast as you can, and when you finally look back, there's nothing there")
                                    print("Looks like you outpaced the horde, and you'll be able to loop around")

                                    journal_entry("Evaded a horde while exploring and found loads of fuel for my car")

                        if game:
                            print("You make it to the undamaged fuel tanks and find:")
                            random_item(5,8,"normal","fuel")

                    elif location == "Trader's Hideout":
                        print("You enter the", location, "and find the Trader himself waiting for you\n")
                        chance = random.randint(1, 2)

                        if chance == 1:
                            print("But he's not alone, looks like a Raider has taken him captive!")
                            raider = describe_human("raider", 1)
                            print(raider)

                            if raider[28:] in survivor_descriptions_list:
                                print("Perhaps this Raider can be reasoned with...")
                                print("Will you:\n1. Negotiate with the Raider\n2. Fight the Raider")
                                choice = make_choice()

                                if choice == 1:
                                    print("\nYou try and reason with the Raider and he considers your proposal")
                                    print("He asks for some food, and in exchange he will leave without conflict")
                                    print("Will you:\n1. Give him some food\n2. Deny his request")
                                    choice = make_choice()

                                    if choice == 1:
                                        print("\nClick the corresponding button to select an item")
                                        print("You have:")
                                        count = 1
                                        for i in character[3]:
                                            print(str(count) + ". " + i)
                                            count += 1
                                        choice = make_choice()
                                        print("You give him (food)", character[3][choice - 1])
                                        raider_hunger = random.randint(200, 800)

                                        if get_cals(character[3][choice - 1]) < raider_hunger:
                                            print("But the Raider is starving and unsatisfied with this offer")
                                            print("He'd prefer to have his choice from your corpse!")
                                            fight_result = fight(1, "humans")

                                            if not fight_result:
                                                game  = False

                                            else:
                                                print("After the battle you pick back up your", character[3][choice - 1])
                                                print("Seems you'll enjoy it more than him")

                                                journal_entry("Tried unsuccessfully to reason with a raider and met with the Trader")

                                        else:
                                            print("He seems happy with this, and nods at you before leaving")
                                            character[3].remove(character[3][choice - 1])

                                            journal_entry("Somehow managed to reason with a raider and met with the Trader")

                                    elif choice == 2:
                                        print("The Raider curses at you and his eyes narrow")
                                        print("It looks like he'd rather fight you for your food anyway...")
                                        fight_result = fight(1, "humans")

                                        if not fight_result:
                                            game = False

                                        journal_entry("Fought with a raider and met with a Trader")

                                elif choice == 2:
                                    print("You don't negotiate with Raiders, time for him to die!")
                                    fight_result = fight(1, "humans")

                                    if not fight_result:
                                        game = False

                                    journal_entry("Fought with a raider and met with a Trader")

                            else:
                                print("This Raider can't be reasoned with...\n")
                                print("You'll have to fight him instead")
                                fight_result = fight(1, "humans")

                                if not fight_result:
                                    game = False

                                journal_entry("Fought with a raider and met with a Trader")

                            if game:
                                print("\nWith the Raider dealt with, you're free to talk to the Trader")

                        if game:
                            print("He studies you for a second, then decides you're on his side\n")
                            print("With this out of the way, he proposes his trades:")
                            print(line_break)

                            trader_pool = []
                            for i in range(25):
                                trader_pool.append(item_list[random.randint(0,len(item_list) -1)])

                            for i in range(5):
                                trader_pool.append(special_item_list[random.randint(0, len(special_item_list) - 1)])

                            count = 1
                            none_count = 0
                            your_item_list = []
                            trader_item_list = []

                            for i in range(3):
                                your_item = select_random_item()
                                if your_item is not None:
                                    if your_item[7:] in character[3]:
                                        if your_item[7:] not in cal_list_800 and your_item[7:] not in cal_list_1000:
                                            if len(character[5]) > 0:
                                                category = character[5]
                                                your_item = character[5][random.randint(0, len(character[5]) - 1)]

                                            elif len(character[4]) > 1:
                                                category = character[4]
                                                your_item = character[4][random.randint(0, len(character[4]) - 1)]
                                                while your_item == "hands":
                                                    your_item = character[4][random.randint(0, len(character[4]) - 1)]

                                            else:
                                                your_item = None

                                            if your_item is not None:
                                                if category[0] == character[4][0]:
                                                    your_item = "(weapon) " + your_item

                                                elif category[0] == character[5][0]:
                                                    your_item = "(meds) " + your_item

                                if your_item is not None:
                                    your_item_list.append(your_item)

                                trader_item = trader_pool[random.randint(0, len(trader_pool) -1)]
                                trader_item_list.append(trader_item)
                                stored_trades = []
                                if your_item is not None:
                                    trade = "Your " + your_item + " for his " + trader_item
                                    if trade not in stored_trades:
                                        print(str(count) + ". " + trade)
                                        count += 1
                                    stored_trades.append(trade)

                                else:
                                    none_count += 1

                            if none_count == 3:
                                print("The Trader has no interest in your items")
                                print("Come back next time with a better selection")

                            else:
                                print(str(count) + ".", "Reject all")
                                line_break
                                print("\n(You may only choose one trade)")
                                choice = make_choice()

                                if choice != count:
                                    print("You trade your", your_item_list[choice - 1], "for the Trader's", trader_item_list[choice - 1])
                                    add_item(trader_item_list[choice - 1])

                                    your_item = your_item_list[choice - 1]

                                    if your_item[0:2] == "(m":
                                        character[5].remove(your_item[7:])

                                    elif your_item[0:2] == "(f":
                                        character[3].remove(your_item[7:])

                                    elif your_item[0:2] == "(w":
                                        character[4].remove(your_item[9:])

                                else:
                                    print("You choose to reject the Trader's offers")

                            print("\nBefore you leave, the Trader offers to play a game of Blackjack")

                            trader_pool = []
                            for i in range(20):
                                trader_pool.append(item_list[random.randint(0, len(item_list) - 1)])

                            for i in range(5):
                                trader_pool.append(special_item_list[random.randint(0, len(special_item_list) - 1)])

                            your_item = select_random_item()
                            trader_item = trader_pool[random.randint(0, len(trader_pool) - 1)]

                            while your_item == trader_item:
                                your_item = select_random_item()
                                trader_item = trader_pool[random.randint(0, len(trader_pool) - 1)]

                            print("He proposes his", trader_item, "for your", your_item)
                            print("Will you:\n1. Play Blackjack\n2. Head home")
                            choice = make_choice()

                            if choice == 1:
                                result = play_blackjack("The Trader")

                                if result == True:
                                    print("YOU WIN")
                                    print("You take the", trader_item, "and the Trader nods")
                                    print("He tells you he'll be sure to win next time, and you shake hands")
                                    add_item(trader_item)

                                elif result == False:
                                    print("TRADER WINS")
                                    print("The Trader takes the", your_item, "and smiles")
                                    print("You tell him you want a rematch next time and he nods agreeingly")
                                    if your_item[0:2] == "(m":
                                        character[5].remove(your_item[7:])

                                    elif your_item[0:2] == "(f":
                                        character[3].remove(your_item[7:])

                                    elif your_item[0:2] == "(w":
                                        character[4].remove(your_item[9:])

                                elif result == "Draw":
                                    print("DRAW")
                                    print("Looks like you've stalemated, but you'll be sure to play again next time")

            if game:
                print("\nWith this done, your mission is complete")
                print("You head back to your car and head back to the", character[7][0])

                if location != "Radio Tower":
                    explore_list.remove(temp_location)

            loop = False

        elif choice == 1 and len(afflictions) == 0:
            area = areas[random.randint(0,len(areas)-1)]
            print("You decide to go scavenge in",area,"today\n")
            chance = random.randint(1,10)

            if len(latest_events) >= 4:
                latest_events == []

            count = 20
            while chance in latest_events and count > 0:
                chance = random.randint(1, 10)
                count -= 1

            latest_events.append(chance)

            if chance == 1:
                chance = random.randint(1, 3)

                if chance != 1:
                    zom_chance = random.randint(1,5)
                    if zom_chance == 1:
                        zombie_grammar = "zombie"

                    else:
                        zombie_grammar = "zombies"

                    if zom_chance == 1:
                        print("On your way through",area,"you spot a zombie walking near a crate of supplies")
                        print("Will you:\n1. Fight the zombie\n2. Sneak away")

                    else:
                        print("On your way through the forest you spot",zom_chance,"zombies walking near a crate of supplies")
                        print("Will you:\n1. Fight the zombies\n2. Sneak away")
                    
                    fight_choice = make_choice()

                    if zom_chance == 1:
                        zombie_grammar = "a zombie"

                    else:
                        zombie_grammar = "some zombies"

                    if fight_choice == 1:
                        if zom_chance == 1:
                            zombie_grammar = "a zombie"
                            print("You approach the zombie and get ready to fight")

                        else:
                            zombie_grammar = "some zombies"
                            print("You approach the zombies and get ready to fight")

                        fight_result= fight(zom_chance,"zombies")
                        if not fight_result:
                            game = False

                        else:
                            zombies_killed += zom_chance

                    if game:
                        if fight_choice == 1:
                            print("After the battle, you go up and check the crate to see what's inside")

                            print("You crack open the crate and find:")
                            random_item(1,3,"normal")
                            random_item(1, 2, "normal", "food")

                            print()
                            chance = random.randint(1, 10)

                            if chance == 1:
                                print("You turn to head home, and see a desperate survivor standing behind you")
                                survivor_name = survivors_male_list[random.randint(0, len(survivors_male_list) - 1)]

                                print("He introduces himself as", survivor_name, "and begs you for some food\n")

                                if len(character[3]) > 0:
                                    print("Will you:\n1.Give", survivor_name, "some food\n2.Refuse")
                                    choice = make_choice()

                                    if choice == 1:
                                        print("You choose to help", survivor_name)
                                        print("Click the corresponding button to select an item")
                                        print("You have:")
                                        count = 1
                                        for i in character[3]:
                                            print(str(count) + ". " + i)
                                            count += 1
                                        choice = make_choice()
                                        print("You give him", character[3][choice - 1])
                                        character[3].remove(character[3][choice - 1])

                                        chance = random.randint(1, 2)

                                        if chance == 1:
                                            print("He shakes your hand vigorously and stuffs the food in his bag")
                                            print("Thanking you for his kindness, he promises to help you in the future")
                                            survivor_group = [survivor_name]
                                            character[6].append(survivor_group)
                                            print(survivor_name, "is now your Friend")
                                            print("\nWith this victory in hand and a new friend, you head home with a smile")

                                            log = "I Killed " + zombie_grammar + " and made a new friend named " + survivor_name
                                            journal_entry(log)

                                        else:
                                            print("He snatches the food from your hands and scurries away")
                                            print("You go to stop him, but with this kind of behaviour, he probably needs it more than you do...")
                                            print("You head home to the", character[7][0], "contemplating your decision...")

                                            log = "I Killed " + zombie_grammar + " and fed some wierdo"
                                            journal_entry(log)

                                    else:
                                        print("You refuse his request, but instead of attacking, he sobs and runs off")
                                        print("He won't last long out there, and on your way home you wonder if it was worth keeping the food...")
                                        zombie_survivor = [survivor_name]
                                        zombie_survivors.append(zombie_survivor)

                                        log = "I Killed " + zombie_grammar + " and didn't give a guy named " + survivor_name + "some food"
                                        journal_entry(log)

                            else:
                                print("With this victory in hand, you head home with a smile")

                                log = "Killed " + zombie_grammar + " and looted a crate"
                                journal_entry(log)

                        else:
                            print("You don't feel great about sneaking away, but it's better than dying")

                            log = "I ran into " + zombie_grammar + " but got away undetected"
                            journal_entry(log)

                else:
                    chance = random.randint(1, 2)
                    if chance == 1:
                        print("As you journey towards", area, "you get an unsettling feeling in your gut")
                        print("You decide to tread carefully today, avoiding that area for now")
                        print("Better than to risk a fatal mistake")
                        print("Maybe tomorrow...")

                    elif chance == 2:
                        print("It's too foggy to search for long, you can't risk a horde sneaking up on you")
                        print("Better safe than sorry...")

                    print("\nDespite your difficulties, you still manage to scrape up something:")
                    random_item(1, 2, "normal")

            elif chance == 2:
                chance = random.randint(1, 3)

                if chance == 1:
                    print("As you're walking through", area, "you hear the shuffling of many feet and a moaning of many mouths")

                    chance = random.randint(10, 100)
                    print("You've stumbled upon a horde of", chance, "zombies\n")
                    print("You know it's too many to fight even with weapons as strong as your",character[4][-1], "...")
                    print("Will you:\n1. Sneak past\n2. Run past\n3. Wait for them to pass")
                    choice = make_choice()

                    if choice == 1:
                        chance = random.randint(1, 2)
                        if chance == 1:
                            print("You sneak past the horde, silent as a ninja")
                            for i in range(1):
                                temp_item = item_list[random.randint(0, len(item_list) - 1)]
                                add_item(temp_item)

                            if len(zombie_survivors) > 1:
                                chance = random.randint(1, 3)

                                if chance == 1:
                                    print("But as you look back at the horde, you get a glance of a eerily familiar face")
                                    named_zombie = zombie_survivors[random.randint(0, len(zombie_survivors) - 1)][0]
                                    print("It almost looked like", named_zombie, "was in that horde...")

                                    journal_entry("Sneaked past a horde but I think I saw a familiar face")

                                else:
                                    print("With your good luck you stumble upon a",temp_item, "on your way home")

                                    log = "Sneaked past a horde and managed to grab a " + temp_item
                                    journal_entry(log)

                            else:
                                print("With your good luck you stumble upon a", temp_item, "on your way home")

                                log = "Sneaked past a horde and managed to grab a " + temp_item
                                journal_entry(log)

                        elif chance == 2:
                            print("You sneak past the horde, skirting on the edge of the street and almost out of sight")
                            print("Suddenly a zombie lunges out in front of you, you'll have to fight it!")

                            fight_result= fight(1,"zombies")

                            if fight_result:
                                zombies_killed += 1
                                print("With the zombie dead you hurry home, shaken but glad you only had to fight one")

                                if len(zombie_survivors) > 1:
                                    chance = random.randint(1, 2)

                                    if chance == 1:
                                        print("But as you look back at the horde, you get a glance of a eerily familiar face")
                                        named_zombie = zombie_survivors[random.randint(0, len(zombie_survivors) - 1)][0]
                                        print("It almost looked like", named_zombie, "was in that horde...")

                                        journal_entry("I had to escape a horde, fight a zombie and I think I saw a familiar face")

                                    else:
                                        journal_entry("I had to escape a horde and fight a zombie")

                                else:
                                    journal_entry("I had to escape a horde and fight a zombie")

                            else:
                                game = False

                    elif choice == 2:
                        print("With the horde nearing your location you make a break for it")
                        chance = random.randint(1,2)
                        if chance == 1:
                            print("The zombies notice you, but with your fast pace you easily speed by them")
                            for i in range(1):
                                temp_item = item_list[random.randint(0, len(item_list) - 1)]
                                add_item(temp_item)
                            print("In fact, you're so fast that you have time to grab a",temp_item,"off the ground.")
                            print("With a runner's high, you jog your way back to the",character[7][0])

                            if len(zombie_survivors) > 1:
                                chance = random.randint(1, 2)

                                if chance == 1:
                                    print("But as you look back at the horde, you get a glance of a eerily familiar face")
                                    named_zombie = zombie_survivors[random.randint(0, len(zombie_survivors) - 1)][0]
                                    print("It almost looked like", named_zombie, "was in that horde...")

                                    log = "I had to run past a horde and I think I saw " + named_zombie + " in it"
                                    journal_entry(log)

                                else:
                                    log = "I had to run past a horde but at least I grabbed a " + temp_item
                                    journal_entry(log)

                            else:
                                log = "I had to run past a horde but at least I grabbed a " + temp_item
                                journal_entry(log)


                        elif chance == 2:
                            print("Unfortunately, as you didn't take time to warm up, you trip and fall right in front of the horde!")
                            chance = random.randint(1,5)
                            if chance == 1:
                                print("You get up again only to realise you've broken your ankle")
                                print("Before you can escape, the horde catches you and you're torn apart...\nYOU ARE DEAD")
                                game = False

                            elif chance != 1:
                                print("You manage to get back up and somehow evade the horde, but you've sprained your ankle")
                                print("\nYou have lost 20HP")
                                character[0][0] -= 20
                                afflictions.append("sprained ankle")
                                print("You now have", character[0][0], "HP")

                                if character[0][0] <= 0:
                                    game = False
                                    print("\nYOU DIED")

                                if game:
                                    print("Defeated, you hobble back to the", character[7][0])
                                    journal_entry("I somehow got away from a horde but twisted my ankle like an idiot")

                    elif choice == 3:
                        print("You find a fire escape on the side of one of the buildings overlooking the street and climb up")
                        chance = random.randint(1, 2)
                        if chance == 1:
                            print("On your way back down you lose your grip and fall, landing on your shoulder")
                            print("\nYou have lost 20HP")
                            character[0][0] -= 20
                            afflictions.append("bruised shoulder")
                            print("You now have", character[0][0], "HP")

                            if character[0][0] <= 0:
                                game = False
                                print("\nYOU DIED")

                            journal_entry("Nearly got caught by a horde then proceeded to fall down a fire escape")

                        else:
                            journal_entry("Nearly got caught by a horde but managed to climb a fire escape")

                        if game:
                            print("The horde passes by, oblivious to you, and you sneak off back to the",character[7][0])

                else:
                    chance = random.randint(1, 3)

                    if chance == 1:
                        print("As you cross through a park on your way, you hear a horde nearby")
                        print("The sounds of moaning and shuffling remind you that your survival depends on more than just calories")
                        print("With that, your fear of being eaten beats out your hunger")
                        print("For now at least...")

                    elif chance == 2:
                        print("You don't scavenge for too long today, there looked to be a lot of undead activity")
                        print("Seems to be getting worse...")

                    else:
                        zombie_num = random.randint(3, 5)
                        print("You've nearly arrived at the", area, "when you spot a group of", zombie_num, "zombies gathered around a corpse")
                        print("They haven't noticed you yet, but that body might have some good loot on it...")
                        print("Will you:\n1. Fight the zombies\n2. Head home")
                        choice = make_choice()

                        if choice == 1:
                            print("You walk closer to the zombies and clear your throat, alerting them")
                            fight_result = fight(zombie_num, "zombies")

                            if fight_result:
                                print("After the fight, you turn over the mangled body of the survivor and check his pockets")
                                print("You find:")
                                random_item(2, 3, "normal")
                                chance = random.randint(1,3)
                                if chance == 1:
                                    random_item(0, 1, "special")

                                print("\nWith this victory in hand you head home, wondering who the survivor once was... ")
                                journal_entry("I fought some zombies and looted a survivor's body, RIP")

                            else:
                                game = False

                        else:
                            print("Choosing not to risk it, and potentially end up like that guy, you head home")
                            journal_entry("Saw a guy getting munched on and got out of there")

                    if chance != 3 and game:
                        print("\nDespite your difficulties, you still manage to scrape up something:")
                        random_item(1, 2, "normal")

            elif chance == 3:
                chance = random.randint(1, 3)

                if chance != 1:
                    print("As you walk through", area, "you notice a seemingly un-looted store")
                    print("You walk up and try the door, but it's locked")
                    print("Will you:\n1. Try force the door open with your",character[4][-1],"\n2. Try find another way in\n3. Smash the window\n4. Don't risk it")
                    choice = make_choice()

                    if choice == 1:
                        chance = random.randint(1,3)
                        if chance == 1:
                            print("\nYou force the door, and suddenly it cracks and gives way")
                            print("The store definitely isn't as untouched as you thought, but you'll make do\n")
                            print("You check the aisles and find:")
                            random_item(3, 10, "normal")

                            print("\nHappy with your score, you return home to the",character[7][0],"with a smile on your face")
                            journal_entry("Forced the door open and looted a store with no hassle")

                        if chance == 2:
                            print("As you force the door inwards, it suddenly heaves out and a dozen hands grab for your clothes")
                            print("You've stumbled upon a sleeping horde!")
                            print("Which way do you run:\n1. Left\n2. Right")
                            choice = make_choice()
                            chance = random.randint(1,2)
                            if choice == 1:
                                direction = "left"

                            elif choice == 2:
                                direction = "right"

                            print("You run to the",direction)
                            if chance == 1:
                                print("And straight into a mass of zombies!")
                                chance = random.randint(1, 2)
                                if chance == 1:
                                    print("Luckily you're quick on your feet and manage to turn around and make a quick getaway")
                                    if len(character[4]) > 2:
                                        lost_weapon = character[4][random.randint(1, len(character[4]) - 1)]
                                        print("But in the process you lose your",lost_weapon)
                                        character[4].remove(lost_weapon)
                                    print("When you get home to the",character[7][0],"you're just happy you're alive")

                                    journal_entry("Tried to loot a store and barely escaped a horde")

                                elif chance == 2:
                                    chance = random.randint(1, 2)

                                    if len(character[6]) == 0 or chance == 1:
                                        print("You slip as you try desperately to get away, and are pulled into the horde...\nYOU ARE DEAD")
                                        game = False

                                    else:
                                        friends = character[6][random.randint(0, len(character[6]) - 1)]
                                        friend1 = friends[0]

                                        if len(friends) > 1:
                                            friend2 = friends[1]
                                            print("You slip and arms reach out and grab you, but " + friend1 + " and " + friend2 + " cut through them and pull you away!")
                                            print("The three of you escape the horde, and they remind you of the favor they owed you")
                                            print("\nYou thank them profusely and say goodbye, returning home to the", character[7][0])

                                            log = "Almost died while looting but I was saved by my friends " + friend1 + " and " + friend2
                                            journal_entry(log)

                                        else:
                                            print("You slip and arms reach out and grab you, but suddenly you're pulled back away from the horde")
                                            print("It's", (friend1 + "!"), "he's rescued you!")
                                            print("The two of you escape the horde, and he reminds you of the favor he owed you")
                                            print("\nYou thank him profusely and say goodbye, returning home to the",character[7][0])

                                            log = "Almost died while looting but I was saved by my friend " + friend1
                                            journal_entry(log)

                            elif chance == 2:
                                print("You know you made the right choice by running to the",direction,"as you see a horde swarm through the street behind you")

                                journal_entry("I almost got caught by a horde while looting")

                        if chance == 3:
                            print("\nAs the door gives way the alarm activates")
                            chance = random.randint(1,2)
                            if chance == 1:
                                print("But your quick reflexes allow you to get away before a horde arrives")
                                print("Still terrified you sprint all the way home to the",character[7][0])

                                journal_entry("An alarm went off while I was looting, but I escaped easily")

                            elif chance == 2:
                                print("You jump back, hitting your head on the door frame and cutting it open")
                                print("Clutching your head, you make a run for it, but you'll need to do something about your injury later")
                                print("\nYou have lost 50HP")
                                character[0][0] -= 50
                                afflictions.append("laceration on your head")
                                print("You now have",character[0][0],"HP")

                                if character[0][0] <= 0:
                                    game = False
                                    print("\nYOU DIED")

                                if game:
                                    print("\nYour head is pounding when you reach the",character[7][0],"but it's a reminder you're alive")

                                    journal_entry("Made a mess of a scavenging trip and split my head open on a door frame")

                    elif choice == 2:
                        print("Not trying to make any noise messing with the locked door, you go look for a back entrance")
                        print("You walk down an alleyway to find your way around")
                        chance = random.randint(1,3)
                        if chance == 1:
                            print("You were correct and there is a back entrance, but it's been destroyed by a crashed van")
                            print("There's no way through")
                            print("\nYou turn to try the front door but a horde is coming down the street, it's too late now")
                            print("You make your way back to the",character[7][0],"wondering what might have been")

                            journal_entry("Tried looting a store but some idiot crashed his van and ruined it")

                        elif chance == 2:
                            print("You check the back, and there is indeed an unlocked door through to the store")

                            chance = random.randint(1, 3)

                            if chance == 1:
                                zom_num = random.randint(2, 3)

                                print("\nYou open the door but there are", zom_num, "zombies inside!")
                                print("You're going to have to fight for this loot!")
                                fight_result = fight(zom_num, "zombies")

                                if fight_result:
                                    print("With them out of the way, you're free to check out the store")

                                else:
                                    game = False
                            
                            if game:
                                print("It's definitely not as full as it looked but it's good enough for you\n")
                                print("You check the aisles and find:")
                                random_item(3,8,"normal")

                                print("Feeling smart and with your pockets full, you decide to head back to the",character[7][0])

                                journal_entry("Found the back door of an unlooted store and filled my pockets")

                        elif chance == 3:
                            print("You check around the corner of the alleyway, but it seems a bomb has gone off here")
                            print("Skeletons litter the pavement, and you get a sick feeling in your stomach")
                            print("You take another look and it seems a bag by the end of the alleyway has survived")
                            print("\nWill you:\n1. Climb over the rubble to reach it\n2. Move on")
                            choice = make_choice()
                            if choice == 1:
                                chance = random.randint(1,2)
                                if chance == 1:
                                    print("You climb up the mountain of rubble, bag in your sights")
                                    print("But your foot slips and you fall, slicing your arm on some exposed rebar")
                                    print("\nYou have lost 30HP")
                                    character[0][0] -= 30
                                    afflictions.append("gash on your arm")
                                    print("You now have", character[0][0], "HP")

                                    if character[0][0] <= 0:
                                        game = False
                                        print("\nYOU DIED")

                                    if game:
                                        print("\nYou clutch your arm, unable to climb anymore, and head back to the",character[7][0])

                                        journal_entry("Cut my arm open while climbing like an idiot, wasn't worth it")

                                elif chance == 2:
                                    print("You slowly climb your way up the pile of rubble")
                                    print("Once you reach the top, you slide your way down towards the bag")
                                    print("You check the bag and find:")
                                    random_item(1,3,"normal")

                                    print("Happy with this, you carefully climb back over and head home to the",character[7][0])

                                    journal_entry(" Spotted a bag and climbed over some rubble to get it, I'm basically spiderman now")

                            if choice == 2:
                                print("Sensibly, you decide all this rubble is too dangerous and head home to the",character[7][0])

                                journal_entry("Was scavenging and decided not to climb through rubble for a possibly empty bag")

                    elif choice == 3:
                        chance = random.randint(1,3)
                        if chance == 1:
                            print("As you go to smash the glass with your",character[4][-1],"you notice a spark plug on the ground")
                            print("Thinking quickly, you throw it at the window")
                            chance = random.randint(1,2)
                            if chance == 1:
                                print("The glass shatters instantly and better yet, there's no alarm")
                                print("You're now able to help yourself to the contents of the store\n")
                                print("You check the aisles and find:")
                                random_item(3,10,"normal")

                                journal_entry("Found a store and shattered the window with a spark plug, easy loot")

                            elif chance == 2:
                                print("The glass shatter perfectly, but suddenly the alarm blares")
                                print("A horde of zombies appears but you hide behind a car, far away after your throw")
                                print("You thank your quick thinking and head home to the",character[7][0])

                                journal_entry("Had my scavenging trip ruined by an alarm")

                        elif chance == 2:
                            print("You crack the glass with your weapon, but it's too loud and zombies start to appear from all around")
                            print("You can't risk looting the shop now with all these zombies nearby")
                            print("Cursing your stupidity you jog back to the",character[7][0] + ",", "sure to lose the zombies on your tail")

                            journal_entry("Was too loud while looting and rang the zombie dinner bell")

                        elif chance == 3:
                            print("You bring your weapon down hard on the glass, but it shatters and cuts your hand")
                            print("\nYou have lost 20HP")
                            character[0][0] -= 20
                            afflictions.append("cut on your palm")
                            print("You now have", character[0][0], "HP\n")

                            if character[0][0] <= 0:
                                game = False
                                print("\nYOU DIED")

                            if game:
                                print("A horde starts to form, and you know you have to get out of here")
                                chance = random.randint(1,2)
                                if chance == 1:
                                    print("You run for a gap in the crowd, but slip on your own blood and come crashing to the ground")
                                    print("The horde closes around you, there is no escape...\nYOU ARE DEAD")
                                    game = False

                                elif chance == 2:
                                    print("Holding your palm tight, you run for a gap in the growing number of zombies")
                                    print("You make it through by the skin of your teeth, and run all the way home to the",character[7][0])

                                    journal_entry("Cut my hand open like an idiot and nearly died")

                    if choice == 4:
                        print("Thinking there must be a reason this store hasn't been looted, you decide not to try it")
                        print("Though you feel like a bit of a coward, you don't entirely regret your decision as you head back to the",character[7][0])

                        journal_entry("Found an unlooted store but decided not to risk it")

                else:
                    chance = random.randint(1, 6)

                    if chance == 1:
                        print("One of your usual paths is a bridge across the nearby river, but it looks to have collapsed")
                        print("Upon closer inspection it seems someone blew it up during the night")
                        print("You're frustrated, but can't help but wonder what their motives were...")

                    elif chance == 2:
                        survivor_num = random.randint(3, 15)
                        print("You've nearly reached", area, "when a group of", survivor_num, "raggedy survivors race out of a nearby building")
                        print("You duck into cover trying to remain unseen, just as they're cornered by a squad of soldiers in gas masks\n")
                        print("You're too far away to hear much but the survivors appear to be trying to reason")
                        print("Suddenly the leader of the soldiers barks an order, and his men raise their guns")
                        print("You watch in sudden horror as the survivors are gunned down in cold blood, and their bodies searched")
                        print("The soldiers set the corpses alight, and you use the distraction to make your escape...")

                    else:
                        print("It rained heavily last night, and when you arrive at", area,"a flood has made the streets impassable")
                        print("Bodies float on the waters surface, and you don't even want to think about what lies below...")
                        print("You'll have to head home for today, but the flood should clear up soon")

                    print("\nDespite your difficulties, you still manage to scrape up something:")
                    random_item(1, 2, "normal")

            elif chance == 4:
                chance = random.randint(1,3)
                if chance != 1:
                    print("As you're busy checking the streets of",area,"you hear a commotion nearby")
                    event= random.randint(1,10)
                    if event == 1:
                        van = "Survivor's Van"

                    elif event == 2 or event == 3:
                        van = "Ambulance"

                    else:
                        van = "Food Truck"

                    print("You turn the corner, and spot an abandoned",van,"surrounded by dozens of zombies")
                    print("From this distance you can't see if it's been looted or not")
                    print("Will you:\n1. Distract the horde\n2. Lead the horde away\n3. Leave the horde alone")
                    choice = make_choice()

                    if choice == 1:
                        chance = random.randint(1,2)
                        print("You sneak behind a car and grab a rock from the pavement")
                        if chance == 1:
                            print("You throw the rock as far as you can and it strikes a window down the street")
                            print("The horde of zombies lift their heads as one, and trundle towards the sound")

                            print("\nWith them out of the way, you're free to check out the",van)
                            chance = random.randint(1,2)
                            if chance == 1:
                                print("The",van,"seems completely intact!")
                                print("You open the doors and find:")
                                if van == "Survivor's Van":
                                    random_item(1,2,"special")
                                    random_item(2,7,"normal")

                                    log = "Lured a horde away and looted a " + van
                                    journal_entry(log)

                                elif van == "Ambulance":
                                    random_item(5, 10, "normal", "meds")

                                    log = "Lured a horde away and looted an " + van
                                    journal_entry(log)

                                elif van == "Food Truck":
                                    random_item(5, 15, "normal", "food")

                                    log = "Lured a horde away and looted a " + van
                                    journal_entry(log)

                                print("\nHappy with today's score, you head home, wishing every day was like this")

                            elif chance == 2:
                                print("But it looks like the horde got to the van first")
                                print("Disappointed, you head back to the",character[7][0])

                                journal_entry("Found a promising van but a horde got to it first")

                        elif chance == 2:
                            print("You throw the rock and the window smashes, but suddenly the alarm blares, this is way too loud!")
                            print("Your distraction has worked too well and another horde of zombies appears from behind you")
                            print("You need to escape, and quickly!")
                            print("Will you:\n1. Fight your way through a weak spot in the hordes\n2. Make a run for a side street")
                            choice = make_choice()

                            if choice == 1:
                                chance = random.randint(1,2)
                                print("You run straight for the weakest zombies in the horde behind you")
                                if chance == 1:
                                    print("As they reach out to grab you, you use your",character[4][-1],"to fight them off")
                                    print("Somehow you fight your way through without a scratch and head back to the",character[7][0])

                                    journal_entry("Ended up fighting my way through a horde, wouldn't recommend")

                                elif chance == 2:
                                    print("But as you prepare to burst through, a zombie jumps out from behind a car")
                                    print("It throws you off balance and you tumble right into the horde...\nYOU ARE DEAD")
                                    game = False

                            elif choice == 2:
                                chance = random.randint(1,2)
                                print("You make a dash for the side street to your left, and through the hordes")
                                if chance == 1:
                                    print("The zombies at the front of both hordes reach out for you...")
                                    print("But you somehow make it through the gap")
                                    print("After this close call you decide to head home to the",character[7][0])

                                    journal_entry("Nearly died while trying to lure a horde")

                                elif chance == 2:
                                    print("You've almost made it through when a zombie gets hold of your bag")
                                    print("It yanks you back, and your head lashes back with it")
                                    print("With adrenaline rushing through you, you manage to wrestle free and escape")
                                    item_lost = ""
                                    if len(character[3]) > 1:
                                        lost_item = character[3][random.randint(1, len(character[4]) - 1)]
                                        item_lost = "and lost a " + lost_item

                                    elif len(character[5]) > 1:
                                        lost_item = character[5][random.randint(1, len(character[5]) - 1)]
                                        item_lost = "and lost a " + lost_item

                                    print("You make your way back, but you've hurt your neck " + item_lost)
                                    print("\nYou have lost 15HP")
                                    character[0][0] -= 15
                                    print("You now have", character[0][0], "HP")

                                    if character[0][0] <= 0:
                                        game = False
                                        print("\nYOU DIED")

                                    afflictions.append("sprained neck")

                                journal_entry("Nearly died while scavenging, sprained my neck instead")

                    elif choice == 2:
                        print("You decide to lead the horde away, shouting and waving your arms")
                        chance = random.randint(1, 2)
                        if chance == 1:
                            print("The horde gives chase, following you down the street and away from the",van)
                            print("Will you:\n1. Double back around\n2. Hide and wait for the horde to pass")
                            choice = make_choice()

                            if choice == 1:
                                print("You double back around through a dark alley")
                                chance = random.randint(1, 2)
                                if chance == 1:
                                    print("You were quick enough that the horde hasn't noticed and they trod straight past")
                                    print("You make your way back and find the",van,"now deserted\n")
                                    chance = random.randint(1, 2)

                                    if chance == 1:
                                        print("The", van, "looks like it hasn't been looted!")
                                        print("You open the doors and find:")
                                        if van == "Survivor's Van":
                                            random_item(1, 2, "special")
                                            random_item(2, 7, "normal")

                                            log = "Lured a horde away and looted a " + van
                                            journal_entry(log)

                                        elif van == "Ambulance":
                                            random_item(5, 10, "normal", "meds")

                                            log = "Lured a horde away and looted an " + van
                                            journal_entry(log)

                                        elif van == "Food Truck":
                                            random_item(5, 15, "normal", "food")

                                            log = "Lured a horde away and looted a " + van
                                            journal_entry(log)

                                        print("\nProud of your horde evading abilities, you head home with the loot")

                                    else:
                                        print("Looks like the horde got to the van first, but it was worth a try")
                                        print("Disappointed, you head back to the", character[7][0])

                                        journal_entry("Had my loot stolen from me by a horde")

                                elif chance == 2:
                                    print("You try and duck in quickly, but the horde spots you!")
                                    chance = random.randint(1,2)
                                    if chance == 1:
                                        print("You break into a sprint and manage to get away before it closes around you")
                                        print("But the horde heads back towards the",van,"and you've lost your chance")
                                        print("You head home, glad you escaped but annoyed about wasting this opportunity")

                                        journal_entry("Horde almost got me while looting")

                                    elif chance == 2:
                                        kills = random.randint(2,10)
                                        print("You try make your getaway but another group of zombies has circled around!")
                                        print("Trapped in the alley, you manage to kill",kills,"zombies with your", character[4][-1])
                                        print("But the numbers are overwhelming and the horde envelops you...\nYOU ARE DEAD")
                                        game = False

                            elif choice == 2:
                                print("With the horde closing in, you run for a damaged shop window to hide in")
                                print("You dive through the broken glass and take cover behind a display")
                                chance = random.randint(1,2)
                                if chance == 1:
                                    print("The horde passes by, oblivious to your hiding spot and you make your way back to the",van)
                                    print("It looks like you managed to lure the whole horde, the",van,"is now abandoned\n")
                                    chance = random.randint(1, 2)
                                    if chance == 1:
                                        print("It looks like it hasn't been looted!")
                                        print("You open the doors and find:")
                                        if van == "Survivor's Van":
                                            random_item(1, 2, "special")
                                            random_item(2, 7, "normal")

                                            log = "Lured a horde away and looted a " + van
                                            journal_entry(log)

                                        elif van == "Ambulance":
                                            random_item(5, 10, "normal", "meds")

                                            log = "Lured a horde away and looted an " + van
                                            journal_entry(log)

                                        elif van == "Food Truck":
                                            random_item(5, 15, "normal", "food")

                                            log = "Lured a horde away and looted a " + van
                                            journal_entry(log)

                                        print("\nProud of your horde evading abilities, you head home with the loot")

                                    else:
                                        print("Seems like the van has been picked clean, it's completely empty")
                                        print("Disappointed, you head back to the", character[7][0])

                                        journal_entry("Lured a horde away but they picked the place clean")

                                elif chance == 2:
                                    print("But you jump too short and catch yourself on the glass, cutting deep!")
                                    print("\nYou have lost 30HP")
                                    character[0][0] -= 30

                                    if character[0][0] <= 0:
                                        game = False
                                        print("\nYOU DIED")

                                    if game:
                                        chance = random.randint(1,2)
                                        if chance == 1:
                                            print("Practising extreme control, you don't make a sound and the horde goes by")
                                            print("But you've injured yourself and you decide to just head back to the", character[7][0])
                                            afflictions.append("deep cut")
                                            print("You now have", character[0][0], "HP")

                                            journal_entry("I cut myself on some glass and almost alerted a horde")

                                        elif chance == 2:
                                            print("You shout in pain, and the horde stops as they hear your cries")
                                            print("You raise your hands weakly to defend yourself")
                                            print("But the horde floods in and you're ripped apart almost instantly...\nYOU HAVE DIED")
                                            game = False

                        elif chance == 2:
                            print("The horde surrounding the",van,"gives chase, but so does another horde from the opposite direction")
                            print("It looks like you're pinned")
                            print("Will you:\n1.Make a run for it\n2.Fight your way out")
                            choice = make_choice()
                            if choice == 1:
                                print("You break into a sprint, trying to outpace the legions of undead")
                                chance = random.randint(1,2)
                                if chance == 1:
                                    print("Their undead flesh is no match for your speed and you get away unscathed")
                                    print("You loop back to the van but it's still covered in zombies")
                                    print("You'll have to leave before it gets dark,",van,"or not")

                                    journal_entry("Had to outrun a horde, scavenging run not successful")

                                elif chance == 2:
                                    print("You make a run for it but you aren't fast enough, you try fight back but there are too many...")
                                    print("YOU ARE DEAD")
                                    game = False

                            elif choice == 2:
                                zom_chance = random.randint(3,10)
                                print("You decide to fight your way out with",zom_chance,"zombies in your way")
                                fight_result = fight(zom_chance, "zombies")
                                if fight_result == False:
                                    game = False

                                else:
                                    zombies_killed += zom_chance
                                    print("With the zombies defeated, you make your escape, heading back to the",character[7][0])

                                    journal_entry("Got cornered by a horde but killed a good few zombies and escaped")

                    elif choice == 3:
                        print("You make the safe decision, telling yourself it's the smart one")
                        print("But as you head home to the",character[7][0],"you can't help but wonder what was in the",van)

                        journal_entry("Spotted a van surrounded by zombies but didn't test my luck")

                else:
                    zombies = random.randint(100,250)
                    print("As you leave the",character[7][0],"to head towards",area,"a huge horde of",zombies,"zombies walks in front of you")
                    print("You manage to avoid them and get away without being seen")
                    print("But you won't be able to scavenge in",area,"today")

                    print("\nDespite your difficulties, you still manage to scrape up something:")
                    random_item(1, 2, "normal")

            elif chance == 5:
                chance = random.randint(1, 3)

                if chance != 1:
                    print("You're walking through", area, "when something catches your eye")
                    print("It looks like someone is waving at you from the roof of a nearby building!")
                    survivor_num = random.randint(1, 2)
                    survivor1 = survivors_male_list[random.randint(0, len(survivors_male_list) - 1)]
                    if survivor_num == 1:
                        print("You make your way up, and sure enough there's a survivor waiting for you\n")
                        describe_human("survivor", 1)
                        print("He introduces himself as", survivor1)

                    elif survivor_num == 2:
                        print("You make your way up, and sure enough there are", survivor_num, "survivors waiting for you\n")
                        describe_human("survivor", 2)
                        survivor2 = survivors_male_list[random.randint(0, len(survivors_male_list) - 1)]
                        print("They introduce themselves as", survivor1, "and", survivor2)

                    if survivor_num == 1:
                        print(survivor1, "offers you some water and you accept it gratefully")

                    elif survivor_num == 2:
                        print(survivor2, "offers you some water and you accept it gratefully")

                    water_drank = True

                    print("You start up some conversation, and", survivor1, "brags about how great he is at blackjack")
                    item_check = False
                    if len(character[3]) > 0:
                        item_check = True

                    elif len(character[4]) > 1:
                        item_check = True

                    elif len(character[5]) > 0:
                        item_check = True

                    if item_check == True:
                        survivor_pool = []
                        for i in range(22):
                            survivor_pool.append(item_list[random.randint(0, len(item_list) - 1)])

                        for i in range(3):
                            survivor_pool.append(special_item_list[random.randint(0, len(special_item_list) - 1)])

                        your_item1 = select_random_item()
                        while your_item1 is None:
                            your_item1 = select_random_item()

                        survivor_item1 = survivor_pool[random.randint(0, len(survivor_pool) - 1)]

                        while your_item1 == survivor_item1:
                            your_item1 = select_random_item()
                            survivor_item1 = survivor_pool[random.randint(0, len(survivor_pool) - 1)]

                        print("He wants to play you, your", your_item1, "for his", survivor_item1)
                        print("Will you:\n1. Challenge him to a game\n2. Back down")
                        choice = make_choice()

                        if choice == 1:
                            result = play_blackjack(survivor1)

                            remove_item(your_item1)

                            survivor_pool.remove(survivor_item1)

                            second_game = True

                            item_check = False
                            if len(character[3]) > 0:
                                item_check = True

                            elif len(character[4]) > 1:
                                item_check = True

                            elif len(character[5]) > 0:
                                item_check = True

                            if item_check == True:
                                your_item2 = select_random_item()
                                survivor_item2 = survivor_pool[random.randint(0, len(survivor_pool) - 1)]

                                while your_item2 == survivor_item2:
                                    your_item2 = select_random_item()
                                    survivor_item2 = survivor_pool[random.randint(0, len(survivor_pool) - 1)]

                                if your_item2 is None:
                                    second_game = False

                            else:
                                second_game = False

                            if result == True:
                                print("YOU WIN")
                                if survivor_num == 1:
                                    print("You take the", survivor_item1, "and", survivor1, "nods")

                                elif survivor_num == 2:
                                    print("You take the", survivor_item1, "and", survivor1, "grimaces while", survivor2, "laughs")

                                if second_game:
                                    print("As you get up to leave, he stops you and challenges you to a double or nothing game")
                                    print("This time, you'll be staking your", your_item1, "and", your_item2, "against his",survivor_item1, "and", survivor_item2)
                                    print("Will you:\n1. Go double or nothing\n2. Take your victory and leave")

                            elif result == False:
                                print(survivor1.upper(), "WINS")
                                print(survivor1, "takes the", your_item1, "and smiles")

                                if second_game:
                                    print("As you get up to leave, he stops you and challenges you to a double or nothing game to win it back")
                                    print("This time, you'll be staking your", your_item1, "and", your_item2, "against his", survivor_item1, "and", survivor_item2)
                                    print("Will you:\n1. Go double or nothing\n2. Take the loss and leave")

                            elif result == "Draw":
                                print("DRAW")
                                second_game = True

                                print("As you get up to leave,", survivor1, "stops you and asks for another game")
                                print("Will you:\n1. Play another game\n2. Take the draw and leave")

                            if second_game:
                                choice = make_choice()

                            if choice == 1 and second_game:
                                result2 = play_blackjack(survivor1)

                                if result2 == True:
                                    print("YOU WIN")
                                    if result != "Draw":
                                        if survivor_num == 1:
                                            print("He gasps in disbelief as you take the", survivor_item1, "and the", survivor_item2)
                                            print("He looks at you sadly as you wish him farewell")

                                        elif survivor_num == 2:
                                            print("He looks on in dismay as you take the", survivor_item1, "and the", survivor_item2 + ",", "while", survivor2, "roars laughing")
                                            print("You wish them goodbye, and can still hear", survivor2, "laughing as you leave")

                                        add_item(survivor_item2)

                                        log = "Played some blackjack and won " + survivor_item1 + " and " + survivor_item2
                                        journal_entry(log)

                                    else:
                                        if survivor_num == 1:
                                            print("You take the", survivor_item1, "and", survivor1, "nods")
                                            print("He looks at you sadly as you wish him farewell")

                                        elif survivor_num == 2:
                                            print("You take the", survivor_item1, "and", survivor1, "grimaces while", survivor2, "laughs")
                                            print("You wish them goodbye, and can still hear", survivor2,"laughing as you leave")

                                        log = "Played some blackjack and won " + survivor_item1
                                        journal_entry(log)

                                    print("You smile to yourself as you head home, your bag heavier and your mood happier")
                                    add_item(survivor_item1)
                                    add_item(your_item1)


                                elif result2 == False:
                                    print(survivor1.upper(), "WINS")
                                    if result != "Draw":
                                        print(survivor1, "takes your", your_item1, "and your", your_item2, "and grins ear to ear")

                                        remove_item(your_item2)

                                        log = "Played some blackjack and lost both my " + your_item1 + " and my " + your_item2
                                        journal_entry(log)


                                    else:
                                        print(survivor1, "takes your", your_item1, "and grins")

                                        log = "Played some blackjack and lost my " + your_item1
                                        journal_entry(log)

                                    if survivor_num == 1:
                                        print("You get up with a lighter bag as he wishes you goodbye")

                                    elif survivor_num == 2:
                                        print(survivor2, "pats you on the back as you try not to think too much about the loss")
                                        print("You wish them both goodbye and head home")

                                    print("On your way back to the", character[7][0], "you promise to yourself to get better at blackjack...")


                                elif result2 == "Draw":
                                    print("DRAW")
                                    if result == "Draw":
                                        print("You look at eachother in confusion as you manage to stalemate again")
                                        print("He shakes your hand, thanks you for the games and you leave")
                                        print("You make your way back to the", character[7][0], "still trying to calculate the odds of that happening...")

                                        journal_entry("Drew two blackjack games in a row and called it quits")

                                    else:
                                        print("The game ends in a stalemate and the item stays with its winner")

                                        if result == True:
                                            print(survivor1, "looks at his", survivor_item1, "for the last time as you throw it in your bag")
                                            add_item(survivor_item1)

                                            log = "Played some blackjack and won " + survivor_item1
                                            journal_entry(log)


                                        elif result == False:
                                            print("You look at your", your_item1, "for the last time as he throws it in his bag")

                                            log = "Played some blackjack and lost my " + your_item1
                                            journal_entry(log)

                            elif choice == 2 or not second_game:
                                if result == True:
                                    print("You decide to take your victory and leave, saying goodbye on your way")
                                    add_item(your_item1)
                                    add_item(survivor_item1)

                                    log = "Played some blackjack and won " + survivor_item1
                                    journal_entry(log)

                                elif result == False:
                                    print("You decide to stop now before you lose something else, saying goodbye on your way")

                                    log = "Played some blackjack and lost my " + your_item1
                                    journal_entry(log)

                                else:
                                    print("You take the draw, glad you didn't lose your", your_item1, "but also thinking about his", survivor_item1)
                                    add_item(your_item1)
 
                                    journal_entry(log = "Played a game of blackjack and called it evens")

                                if second_game:
                                    print("You head home, wondering what would have happened if you played a second game...")

                        else:
                            print("You choose not to gamble, for today at least")
                            print(survivor1, "goes to argue but stops himself and nods")
                            if survivor_num == 1:
                                print("He says goodbye and wishes you good luck, even if you're not keen on testing it")

                            elif survivor_num == 2:
                                print("They say goodbye and wish you good luck, even if you're not keen on testing it")

                            print("But as you make your way back to the", character[7][0], "you wonder what could have happened if you played some blackjack...")
                            journal_entry("Was offered a game of blackjack but turned it down")

                    else:
                        print("\nHe offers to play you if you bet some items")
                        print("But you explain to him you don't really have enough to bet right now")
                        charity_item = item_list[random.randint(0, len(item_list) - 1)]
                        print("He nods understandingly and gives you a", charity_item, "in a gesture of charity")
                        print("You thank him and head home to the", character[7][0])
                        add_item(charity_item)

                        log = "Met some survivors and they gave me " + charity_item
                        journal_entry(log)

                else:
                    print("As you're walking towards", area, "you hear hoots and shouting")
                    print("You dash to cover and a band of raiders runs past")
                    print("It's a close call, and you can't risk scavenging out here today")
                    print("You'll have to head home and try tomorrow")

                    print("\nDespite your difficulties, you still manage to scrape up something:")
                    random_item(1, 2, "normal")

            elif chance == 6:
                chance = random.randint(1, 3)

                if chance != 1:
                    print("You're exploring", area, "when a small office building catches your eye")
                    print("Will you:\n1. Explore the building\n2. Head home")
                    choice = make_choice()

                    if choice == 1:
                        print("Unsure of why, you decide to head inside and check the building")
                        print("You go inside and head up a flight of stairs to a room above")
                        print("Opening the door, it looks like there's a huge safe in the wall")

                        chance = random.randint(1,3)

                        if chance == 1:
                            print("\nBut there's a raider waiting for you too!")
                            print("He doesn't appreciate your presence in his home and you'll have to fight")
                            describe_human("raider", 1)
                            fight_result = fight(1,"humans")

                            if not fight_result:
                                game = False

                            else:
                                print("With the fight over, you can take a look around")

                        elif chance == 2:
                            zom_num = random.randint(2, 5)
                            print("\nBut there are", zom_num, "zombies waiting for you too!")
                            fight_result = fight(zom_num, "zombies")

                            if not fight_result:
                                game = False

                            else:
                                zombies_killed += zom_num
                                print("With the fight over, you can take a look around")

                        if game:
                            print("\nYou take a closer look at the safe and it seems locked")
                            print("It looks like the lock needs a 3-digit code")
                            code_list = []
                            guess_list = []
                            for i in range(3):
                                num = random.randint(1, 9)
                                while num in code_list:
                                    num = random.randint(1, 9)
                                code_list.append(num)

                            code_list_sorted = sorted(code_list)

                            print("But the keypad is faded on the", str(code_list_sorted[0]) + ", " + str(code_list_sorted[1]) + " and " + str(code_list_sorted[2]) + " keys\n")
                            print("Seems like you'll only get one chance before the safe locks permanently")
                            print("Input the numbers one-by-one:")
                            for i in range(3):
                                num = int(input("Press a number: "))
                                guess_list.append(num)
                            print(line_break)

                            if guess_list == code_list:
                                print("CODE CORRECT!")
                                print("You open the safe and find:")
                                chance = random.randint(1,10)

                                if chance == 1:
                                    item = ultra_special_item_list[random.randint(0, len(ultra_special_item_list) - 1)]
                                    print(item)
                                    add_item(item)

                                else:
                                    random_item(2,3, "special")

                                print("\nLooks like you hit the jackpot!")
                                print("You head home to the", character[7][0],", excited with your find")

                                journal_entry("Cracked a safe open and found some great loot")

                            else:
                                print("CODE INCORRECT!")
                                print("Looks like you couldn't guess the code")
                                print("You head home, still wondering what was in the safe...")

                                journal_entry("Found a safe but couldn't crack the code")

                    else:
                        print("You decide not to risk it and head home to the", character[7][0])

                else:
                    chance = random.randint(1, 2)

                    if chance == 1:
                        print("You round the corner towards", area, "but it looks like there's been a huge battle")
                        print("There are bodies strewn around, and the only movement comes from the hordes of undead scavengers")
                        print("You manage to stay out of sight, but you'll have to head home")

                    else:
                        print("You arrive at", area, "with no hassle, but only because someone else beat you to it")
                        print("The promising area you marked on your map has already been looted")
                        print("It looks like it was recent enough, dead zombies lie here and there")
                        print("Doesn't look like they left anything interesting for you...")

                    print("\nDespite your difficulties, you still manage to scrape up something:")
                    random_item(1, 2, "normal")

            elif chance == 7 and day > 10:
                chance = random.randint(1, 3)

                if chance != 1:
                    print("As you walk through", area, "you begin to notice the signs of another survivor")
                    print("You spot some footprints leading off your usual path, and down a dark side street...")
                    print("Will you:\n1. Follow the footprints\n2. Head home")
                    choice = make_choice()

                    if choice == 1:
                        possible_hideouts = ["looted gunstore", "burnt out police station", "dismal house"]
                        chance = random.randint(1,3)

                        survivor_hideout = possible_hideouts[chance - 1]

                        print("You choose to follow the footprints and set off after this survivor")
                        print("Sticking to the shadows, you follow the trail to a", survivor_hideout)
                        print("You sneak up and take a look through the window")

                        survivor_type = random.randint(1,3)
                        infected_survivor = random.randint(1, 2)

                        if survivor_type != 1:
                            if survivor_type == 2:
                                human = "raider"

                            else:
                                human = "survivor"

                            print("As your eyes adjust, you notice there's someone inside!")
                            print(describe_human(human, 1))
                            print("\nWill you:\n1. Approach them\n2. Attack them")
                            choice = make_choice()

                            if choice == 1:
                                print("You take a deep breath, then stand up and walk in the door")

                                if human == "raider":
                                    print("It's a raider!")
                                    chance = random.randint(1, 2)

                                    if chance == 1 and human[28:] in survivor_descriptions_list:
                                        print("But to your surprise, the raider doesn't attack you")
                                        print("It looks like he's badly injured and can barely walk")

                                        raider_name = survivors_male_list[random.randint(0, len(survivors_male_list) - 1)]

                                        print("\nHe raises his hands and introduces himself as", raider_name)
                                        print("You keep your guard up, but he quickly informs you he's not interested in a fight")
                                        print("He tells you he got this wound from another raider after abandoning his group")
                                        print(raider_name, "asks for medicine, but realises you may not forgive his past...")

                                        if len(character[5]) > 0:
                                            print("Will you:\n1.Give", raider_name, "some medicine\n2.Refuse")
                                            choice = make_choice()

                                            if choice == 1:
                                                print("You choose to help", raider_name)
                                                print("Click the corresponding button to select an item")
                                                print("You have:")
                                                count = 1
                                                for i in character[5]:
                                                    print(str(count) + ". " + i)
                                                    count += 1
                                                choice = make_choice()
                                                print("You give him the", character[5][choice - 1])
                                                character[5].remove(character[5][choice - 1])

                                                print(raider_name, "thanks you as you have saved his life")
                                                print("He promises to make right with this second chance")
                                                survivor_group = [raider_name]
                                                character[6].append(survivor_group)
                                                print(raider_name, "is now your Friend")

                                                print("\nWith this good deed, you say goodbye and head on your way home")

                                                log = "Found an injured raider named " + raider_name + " and saved his life"
                                                journal_entry(log)

                                            elif choice == 2:
                                                print(raider_name, "looks at you with sad understanding")
                                                print("You turn and leave him to his fate, he will not last long...\n")

                                                journal_entry("Found an injured raider, but left him to his fate")

                                        else:
                                            print("But you don't have any medicine and you cannot help")
                                            print("You explain this to him and he nods, accepting his fate")
                                            print("With nothing more to do or say, you leave him to die...\n")

                                            journal_entry("Found an injured raider, but didn't have enough meds to save him")

                                    else:
                                        print("He snarls and glares at you")
                                        print("Looks like there'll be no negotiations here...")
                                        result = fight(1, "humans")

                                        if result:
                                            print("With this fight over, you're free to take a look around the", survivor_hideout)
                                            print("Looks like the raider had a stash of food:")
                                            random_item(2, 5, "normal", "food")
                                            print("\nWith the food in your bag you head home, wondering if things could have gone differently")

                                            journal_entry("Killed a raider and looted his stash")

                                        else:
                                            game = False

                                elif human == "survivor":
                                    print("You walk in and their head jolts towards you")
                                    print("Looks like they're a survivor")
                                    print("You quickly explain you mean no harm, and the survivor concurs")

                                    survivor_name = survivors_male_list[random.randint(0, len(survivors_male_list) - 1)]

                                    print("He shakes your hand and introduces himself as", survivor_name)

                                    if infected_survivor == 1:
                                        print("But he looks ill and it seems like he's injured")

                                    else:
                                        print("But it seems like he's injured")

                                    choice_line = "\nWill you:\n1. Ask about his wound"

                                    if len(character[5]) > 0:
                                        choice_line += "\n2. Offer him some medicine"

                                    print(choice_line)
                                    choice = make_choice()

                                    if choice == 2:
                                        print("You choose to offer medicine to", survivor_name)
                                        print("Click the corresponding button to select an item")
                                        print("You have:")
                                        count = 1
                                        for i in character[5]:
                                            print(str(count) + ". " + i)
                                            count += 1
                                        choice = make_choice()

                                        chosen_meds = character[5][choice - 1]
                                        print("You give him the", chosen_meds)
                                        character[5].remove(chosen_meds)

                                        if infected_survivor == 1:
                                                print("\nBut he looks at you strangely, the", chosen_meds, "may not be able to heal him")
                                                print("Suddenly he collapses to the ground in front of you and lays still")
                                                print("\nWill you:\n1. Check if he's ok\n2. Back away")

                                                if choice == 1:
                                                    print("You kneel beside", survivor_name, "and check his pulse")
                                                    print("Your heart drops, he's dead!")
                                                    print("You look at him solemnly and wish you had gotten here earlier\n")
                                                    print("But as you get up off the floor, something catches your eye")
                                                    print(survivor_name + "'s", "eyes are wide open and staring at you!")
                                                    print("He dives and tackles you, he must have been infected!")

                                                    if len(character[4][0]) > 1:
                                                        chance = random.randint(1,4)

                                                        weapon = character[4][random.randint(1, len(character[4]) -1)]

                                                        count = 20
                                                        while weapon == "**assault rifle**" or weapon == "*pistol*" or count > 0:
                                                            weapon = character[4][random.randint(1, len(character[4]) - 1)]
                                                            count -= 1

                                                    else:
                                                        chance = random.randint(1,2)
                                                        weapon = "hands"

                                                    if chance == 1:
                                                        if weapon == "hands":
                                                            print("You try push him off with your hands, but it's no use!")
                                                            print("He overpowers you and bites...\nYOU DIED")

                                                        else:
                                                            print("You try push him back with your", weapon, "but there's not enough space!")
                                                            print("He bites your arm and you shout in pain, before he lunges for your neck...\nYOU DIED")

                                                        game = False

                                                    else:
                                                        if weapon == "hands":
                                                            print("In a superhuman effort you heave his body off of you")
                                                            print("He rolls back and jumps again, but you catch him with a kick to the ribs")
                                                            print("He falls to the ground again and this time you stomp down, ending the fight...")

                                                        else:
                                                            print("He opens his mouth wide to bite you, but you stop his teeth with your", weapon)
                                                            print("Recoiling back, he swipes at you and misses")
                                                            print("You use this oppurtunity to put him down with your", weapon, "this time he won't get back up...")

                                                else:
                                                    print("You back away from", survivor_name, "as he lies still on the ground")
                                                    print("You can barely hear over your heartbeat, as you battle the urge to help him")
                                                    print("Suddenly he twitches, and slowly gets back up")

                                                    print("\nBut as he turns to look at you, you realise this isn't", survivor_name, "anymore...")
                                                    result = fight(1, "zombies")

                                                    if not result:
                                                        game = False

                                                if game:
                                                    print("\n Shaken but alive, you search his body, retrieving your", chosen_meds, "and finding:")
                                                    random_item(1, 3, "normal")
                                                    print("\n You return home to the", character[7][0], "but vow to be more cautious next time...")

                                                    journal_entry("Tried to help a dying survivor but he turned and attacked me")

                                        else:
                                            print(survivor_name, "thanks you for your generosity")
                                            print("He promises to pay you back someday, and shakes your hand again")
                                            survivor_group = [survivor_name]
                                            character[6].append(survivor_group)
                                            print(survivor_name, "is now your Friend")

                                            print("\nWith this done, you say goodbye and head on your way home")

                                            log = "Helped a survivor named " + survivor_name + " and made a new friend"
                                            journal_entry(log)

                                    else:
                                        print("You ask", survivor_name,"about his appearance mentioning your concerns about a wound")

                                        if infected_survivor == 1:
                                            print("He mutters something about a fall while scavenging for food")
                                            print("He seems feverish and could use some medical help")

                                            print("\nWill you:\n1. Check your bag for medical supplies\n2. Reach for a weapon")
                                            choice = make_choice()

                                            if choice == 1:
                                                print("You tell him you can help him, and he looks at you in thinly veiled disbelief")
                                                print("You place your bag down and begin to rummage through it for meds")
                                                print("But when you look back up he's disappeared")
                                                print("It seems he's run to a room in the back of the", survivor_hideout)

                                                print("\nWill you:\n1. Go make sure he's ok\n2. Leave the",survivor_hideout)
                                                choice = make_choice()

                                                if choice == 1:
                                                    print("You notice a door slightly ajar, but it's gloomy in here and the electricity is gone out")
                                                    print("You call out", survivor_name + "'s", "name, and get no response...")
                                                    print("You push the door open and see him standing in the dim light")
                                                    print("But it's not him anymore...")
                                                    result = fight(1, "zombies")

                                                    if result:
                                                        print("With the zombie dead you breathe a sigh of relief")
                                                        print("\n Shaken but alive, you search his body, finding:")
                                                        random_item(1, 3, "normal")

                                                        print("\n You return home to the", character[7][0], "but vow to be more cautious next time...")

                                                        journal_entry("Tried to help a survivor and nearly got killed when he turned")

                                                    else:
                                                        game = False

                                                else:
                                                    print("You're not taking any chances, and you take this opportunity to run for the door")
                                                    print("As you make your way home, you wonder what might have really happened to him...")
                                                    zombie_survivor = [survivor_name]
                                                    zombie_survivors.append(zombie_survivor)

                                                    log = "Met a survivor named " + survivor_name + "but he didn't seem right, had to make a run for it"
                                                    journal_entry(log)

                                            else:
                                                print("You make eye contact and he looks at you with an almost feral gaze")

                                                if len(character[4][0]) > 1:
                                                    weapon = character[4][random.randint(1, len(character[4]) - 1)]
                                                    print("You grab for your", weapon, "and he shrieks and runs")

                                                else:
                                                    print("You raise your hands and prepare to fight")
                                                    print("But instead of fighting he shrieks and runs")

                                                print("He's surprisingly fast, and you can't land a hit on him")
                                                print("Kicking open the back door, he dashes out of sight and away from you")
                                                print("\nThis escapade has made a lot of noise and to chase him would be too risky")
                                                print("You decide to head back to the", character[7][0], "wondering what he was hiding...")
                                                zombie_survivor = [survivor_name]
                                                zombie_survivors.append(zombie_survivor)

                                                log = "Met a survivor named " + survivor_name + "but he didn't seem right, when I reached for a weapon he bolted"

                                        else:
                                            chance = random.randint(1, 2)
                                            if chance == 1:
                                                print("He nods and tells you about his narrow escape with a group of masked soldiers")
                                                print("Lifting up his shirt, he shows you a bleeding gash, presumably left by a bullet")

                                            else:
                                                print("He nods and tells you about his narrow escape with a group of raiders")
                                                print("Lifting up his shirt, he shows you a deep slash, presumably left by a raider's machete")

                                            print("He notices your expression, and begs you for medical supplies")
                                            if len(character[5]) > 0:
                                                print("Will you:\n1.Give", survivor_name, "some medicine\n2.Refuse")
                                                choice = make_choice()

                                                if choice == 1:
                                                    print("You choose to help", survivor_name)
                                                    print("Click the corresponding button to select an item")
                                                    print("You have:")
                                                    count = 1
                                                    for i in character[5]:
                                                        print(str(count) + ". " + i)
                                                        count += 1
                                                    choice = make_choice()
                                                    print("You give him the", character[5][choice - 1])
                                                    character[5].remove(character[5][choice - 1])

                                                    print(survivor_name, "thanks you as you have saved his life")
                                                    print("He promises to return the favour if he sees you again")
                                                    survivor_group = [survivor_name]
                                                    character[6].append(survivor_group)
                                                    print(survivor_name, "is now your Friend")

                                                    print("\nWith this good deed, you say goodbye and head on your way home")

                                                    log = "Gave a survivor named " + survivor_name + " some meds and made a new friend"
                                                    journal_entry(log)

                                                elif choice == 2:
                                                    print(survivor_name, "looks at you with a mix of shock and fear")
                                                    print("You turn and leave as he begs you again, he will not last long...\n")

                                                    journal_entry("Chose to ignore a survivor's request for medicine, he won't last long")

                                            else:
                                                print("But you don't have any medicine and you cannot help")
                                                print("You explain this to him and tears appear in his eyes")
                                                print("With nothing more to do or say, you leave him alone in the", survivor_hideout, "...")

                                                journal_entry("A survivor needed medicine, but I couldn't help him")

                            else:
                                print("You take a deep breath, then burst through the door")

                                chance = random.randint(1, 2)

                                if chance == 1:
                                    if len(character[4][0]) > 1:
                                        weapon = character[4][random.randint(1, len(character[4]) - 1)]

                                    else:
                                        weapon = "fists"

                                    print("Taking them by surprise you land a lucky hit with your", weapon, "knocking them down")
                                    print("You follow up with another, and they lie still and dead")

                                    if human == "survivor":
                                        print("You check the body and it looks like he was just an injured survivor")
                                        journal_entry("Killed a survivor today, don't know if he would have done the same")

                                        if infected_survivor == 1:
                                            print("But on closer inspection, it looks like he was bitten and infected")
                                            print("Maybe it's for the better that you put him down")

                                            journal_entry("Killed a survivor today, he was infected anyway")

                                    elif human == "raider":
                                        print("You check the body and it looks like he was a raider")
                                        print("Good thing you took him out")

                                        journal_entry("Took a raider by surprise and killed him")

                                    print("\nIt looks like he had:")
                                    random_item(1, 3, "normal")
                                    random_item(0, 1, "special")

                                else:
                                    print("But when you enter the", survivor_hideout, "they're looking right at you!")

                                    if human == "survivor":
                                        print("They're just a survivor, but now you'll have to fight them to the death...")

                                    elif human == "raider":
                                        print("They're a raider, and raiders are always ready to fight!")
                                        journal_entry("Had to fight a raider to the death")

                                    result = fight(1, "humans")

                                    if result:
                                        if human == "survivor":
                                            print("You've won the battle, and now another survivor lies dead")

                                            if infected_survivor == 1:
                                                print("As you go to check his corpse, you find an infected bite")
                                                print("There isn't much he could have done anyway")

                                                journal_entry("Had to fight a survivor to the death, but turns out he was infected anyway")

                                            else:
                                                journal_entry("Had to fight a survivor to the death")

                                    else:
                                        game = False

                                if game:
                                    print("\nYou fill your bag, and head home...")

                        else:
                            print("It looks like there's a dead survivor on the floor!")
                            print("\nWill you:\n1. Go and check the body\n2. Leave the", survivor_hideout, "alone")
                            choice = make_choice()

                            if choice == 1:
                                print("The door creaks as you push it open and step inside")
                                print("The room is dimly lit, shadows playing tricks on your mind")
                                print("As you check your surroundings, you start wishing this survivor had picked a better place to die\n")
                                if infected_survivor == 1:
                                    print("When your gaze settle on the body again, a wave of cold fear washes over you")
                                    print("It's standing up, and it's shuffling towards you")
                                    print("Looks like it wasn't quite dead after all...\n")

                                    zombies = random.randint(2,4)
                                    print("You try and make a run for it, but", zombies, "more zombies have blocked your path")
                                    print("This is going to be a tough fight")

                                    result=fight(zombies, "zombies")

                                    if result:
                                        print("With the zombies dead, you're free to take a look around the room")
                                        print("You spot the dead survivor's backpack, and inside you find:")
                                        random_item(0, 1, "special")
                                        random_item(3, 6, "normal")

                                        journal_entry("Fought a recently deceased survivor and his friends")

                                    else:
                                        game = False

                                else:
                                    print("You go and check the body, it seems he died recently")
                                    print("As you check his pockets, you think about what type of person he could have been")
                                    print("You find nothing there, but spot a backpack in the corner")
                                    print("Inside the backpack you find:")
                                    random_item(3, 5, "normal")

                                    journal_entry("Found a dead survivor and looted his backpack")

                                print("With this, you head back home to the", character[7][0])

                    else:
                        print("You've seen enough horror movies to know this is a bad idea, and head home to the", character[7][0], "without risking it")
                        journal_entry("Saw some footprints but decided not to followe them")

                else:
                    chance = random.randint(1, 2)
                    if chance == 1 or len(character[6]) == 0:
                        print("You hear voices arguing up ahead, and while making sure to stay hidden, you take a look\n")
                        print("You peek over an overturned truck and see a two groups of raiders arguing!")
                        print("It looks like they were waiting to ambush unsuspecting survivors, but couldn't decide who gets what")
                        print("You count yourself thankful for their incompetence, and head home")

                    elif chance == 2 and len(character[6]) > 0:
                        chance = random.randint(1, 3)
                        if chance == 1:
                            friends = character[6][random.randint(0, len(character[6]) - 1)]
                            friend1 = friends[0]
                            friend_count = 1

                            if len(friends) > 1:
                                friend2 = friends[1]
                                friend_count = 2

                            character[6].remove(friends)

                            print("You're on-route to your destination when you hear a commotion ahead")
                            print("You peek around some cars and spot a large group of raiders")

                            if friend_count == 1:
                                print(
                                    "You inch closer, and it looks like they have a human head on the end of a pike...")

                            else:
                                print(
                                    "You inch closer, and it looks like they have two human head on the ends of pikes...")

                            print("Will you:\n1. Take a closer look\n2. Make a run for it")
                            choice = make_choice()

                            if choice == 1:
                                print(
                                    "You sneak closer, moving between burnt out cars until you're close enough to see properly...\n")

                                if friend_count == 1:
                                    print("It's", (friend1 + "'s"), "head on the pike")
                                    print("Your friend", friend1, "is dead, killed by raiders")

                                    log = "Raiders killed my friend " + friend1
                                    journal_entry(log)

                                else:
                                    print("The heads belong to", friend1, "and", friend2)
                                    print("The raiders have killed your friends")

                                    log = "Raiders killed my friends " + friend1 + " and " + friend2
                                    journal_entry(log)

                                print("Shaking with rage, you hold yourself back")
                                print("There's no way you could take this many raiders in a fight")
                                print("You walk home in the rain, plotting your revenge...")

                            else:
                                print("You don't risk the raiders spotting you, not wanting to end up on a pike, so you make your exit")
                                print("As you walk home, you hope those heads didn't belong to anyone you knew...")

                                journal_entry("Some raiders had heads on pikes, hope it was nobody I knew")

                        else:
                            print("You're making your way down to", area, "when you hear gunfire ahead")
                            print("It continues briefly before stopping, but the damage has been done")
                            print("Dozens of zombies emerge from the streets around you, and you dive into cover")
                            print("Scavenging here is going to be a no-go today...")

                    print("\nDespite your difficulties, you still manage to scrape up something:")
                    random_item(1, 2, "normal")

            elif chance == 8:
                if len(zombie_survivors) > 0 or day >= 20:
                    chance = random.randint(1, 2)

                    if chance == 1:
                        print("You make your way into", area + ",", "while keeping low and quiet")
                        print("You duck out of sight as a horde passes close by, but they're not looking for you")

                        survivor_amount = random.randint(1, 2)

                        if survivor_amount == 1:
                            survivor = "survivor"

                        else:
                            survivor = "pair of survivors"

                        print("You look to the end of the street and see a", survivor, "exit a building and begin desperately running away")
                        print("\nWill you:\n1. Try help the survivors\n2. Don't help them")
                        choice = make_choice()

                        if choice == 1:
                            print("You decide to at least try help the", survivor, "escape")
                            print("You circle around, trying to get ahead of the horde")
                            print("But you're not quick enough, and a zombie stumbles out in front of you")

                            if len(zombie_survivors) > 1:
                                named_zombie_group = zombie_survivors[random.randint(0, len(zombie_survivors) - 1)]
                                named_zombie = named_zombie_group[0]

                                if len(named_zombie_group) > 1:
                                    missing_friend = True
                                    named_zombie2 = named_zombie_group[1]

                                print("\nIt's", named_zombie + "!")
                                if missing_friend:
                                    print("Looks like", named_zombie2, "isn't here, though he probably met a similar fate...")

                                    enemy_group = [named_zombie2, named_zombie]
                                    enemy_list.append(enemy_group)

                                print("You look at him sadly, remembering when you last saw him")
                                print("But he doesn't share the same sentiment and shuffles towards you...")
                                fight_result = fight(1, "zombies", named_zombie)

                                if fight_result:
                                    zombie_survivors.remove(named_zombie_group)
                                    print("You look at", named_zombie, "for the last time, but it's time to go")
                                    print("You've still got a job to do")

                            else:
                                fight_result = fight(1, "zombies")

                            if fight_result:

                                if survivor_amount == 1:
                                    print("You run onto the street with the horde right in front of you")
                                    print("But the survivor is still alive!")
                                    print("You spot a zombie sneaking up behind him as he retreats")
                                    print("You jump fowards and take it out, joining his side")
                                    zombies_killed += 1

                                    survivor_name = survivors_male_list[random.randint(0, len(survivors_male_list) - 1)]
                                    print("\nHe smiles, glad to see a friendly face, and introduces himself as", survivor_name)
                                    print("But the fight isn't over yet, you'll each have to cut through the horde")
                                    print("You nod at eachother, then each make a dash for weakspots in the wall zombies!")
                                    print("This is going to be a tough fight!")

                                    zom_count = random.randint(3, 7)
                                    fight_result = fight(zom_count, "zombies")

                                    if fight_result:
                                        chance = random.randint(1, 3)
                                        print("Somehow you manage to battle through the horde unscathed")
                                        print("You dash forward, then spin around to look for", survivor_name)

                                        if chance == 1:
                                            print("\nHe appears from the horde and you cheer, but celebration doesn't last long")
                                            print("A hand grabs his ankle and teeth close around his leg, before he's pulled in, never to be seen again")
                                            print("As the futility of your good deed tears at your heart as you stare at the crowd of zombies")
                                            print("\nYou run all the way home, not wanting to think about", survivor_name, "ever again...")

                                            journal_entry("Almost saved a survivor but he was dragged into a horde")

                                        else:
                                            print("\nHe suddenly rolls out of the horde, dodging the sea of hands grabbing at him")
                                            print("He races up beside you and give you a high-five")
                                            print("As the two of you make your escape, he thanks you for saving him")
                                            print("Before he goes, he promises to repay you for this good deed someday")
                                            survivor_group = [survivor_name]
                                            character[6].append(survivor_group)
                                            print(survivor_name, "is now your Friend")

                                            print("\nWith this done, you say goodbye and head on your way home")

                                            log = "Saved a survivor named " + survivor_name + " and made a new friend"
                                            journal_entry(log)

                                    else:
                                        game = False

                                else:
                                    print("You run out onto the street, with the horde pouring towards you")
                                    print("But just in front are the two survivors!")
                                    print("It looks like one of them has sprained their ankle and is limping, but the zombies are catching up!")
                                    print("\nA rotting hand reaches out for the survivors, but you jump in to defend them")
                                    print("They see this and cheer, you'll be fighting out of this together")
                                    print("The horde has almost surrounded you, but you point towards a weak spot and they make a run for it")

                                    print("\nBut while the survivors make their escape, you'll have to defend their backs")
                                    zom_count = random.randint(4,8)
                                    fight_result = fight(zom_count, "zombies")

                                    if fight_result:
                                        print("With enough zombies dead, you're free to make a run for it")
                                        chance = random.randint(1, 2)

                                        survivor1_name = survivors_male_list[random.randint(0, len(survivors_male_list) - 1)]
                                        survivor2_name = survivors_male_list[random.randint(0, len(survivors_male_list) - 1)]

                                        if chance == 1:
                                            print("It looks like the two survivors were successful as well, there's a path out of here!")
                                            print("You sprint after them, catching up with them as they round a corner")
                                            print("Once you've made sure you're clear of the horde, they introduce themselves as",survivor1_name, "and", survivor2_name)
                                            print("\nThey're grateful for your rescue, knowing they wouldn't have made it without you")
                                            print("Before they go, they promise to repay you for this good deed someday")
                                            survivor_group = [survivor1_name, survivor2_name]
                                            character[6].append(survivor_group)
                                            print(survivor1_name + " and " + survivor2_name + " are now your Friends")

                                            print("\nWith this done, you say goodbye and head on your way home")

                                            log = "Saved a pair of survivors named " + survivor1_name + " and " + survivor2_name + " and made some new friends"
                                            journal_entry(log)

                                        else:
                                            print("As you run past the swarms of zombies, you search for the two survivors")
                                            print("You can't see them only the zombies milling like ants in the middle of the road")
                                            print("They're too busy to notice you, and you sneak away")
                                            print("\nRounding the corner onto the next street, you spot one of the survivors!")
                                            print("He introduces himself as", survivor1_name, "but explains his friend", survivor2_name, "didn't make it")
                                            print("You offer your sympathy, and he thanks you for saving his life and trying to help his friend")
                                            print("Before he goes, he promises to repay his debt someday")
                                            survivor_group = [survivor1_name]
                                            print(survivor1_name, "is now your Friend\n")

                                            chance = random.randint(1,2)

                                            if chance == 1:
                                                character[6].append(survivor_group)
                                                print("\nWith this done, you say goodbye and head on your way home")

                                                log = "Made a new friend named " + survivor1_name
                                                journal_entry(log)

                                            else:
                                                zombie_survivors.append(survivor_group)
                                                print("You say goodbye, and", survivor1_name, "walks away with a limp")
                                                print("But as you leave, you can't shake the feeling that it was", survivor2_name, "who was limping...")

                                                log = "Made a new friend named " + survivor1_name + " but something wasn't right"
                                                journal_entry(log)

                        else:
                            print("You decide not to help the", survivor, "escape, and instead watch as the horde closes in")
                            survivor1_name = survivors_male_list[random.randint(0, len(survivors_male_list) - 1)]
                            survivor2_name = survivors_male_list[random.randint(0, len(survivors_male_list) - 1)]

                            if survivor_amount == 1:
                                print("The survivor spins in circles, shouting the name", survivor1_name, "over and over")
                                print("Suddenly another survivor emerges from the building, shouting the name", survivor2_name)
                                print("\nThey try desperately to fight their way towards eachother, but it's no use")
                                print(survivor2_name, "runs back into the building and", survivor1_name, "makes a run for a sidestreet")
                                print("But", survivor1_name, "suddenly turns around and locks eyes with you, he's seen you but it's too late")
                                print("You lose sight of both of them in the mass of zombies, wondering if you could have saved them")

                                survivor_group = [survivor1_name, survivor2_name]
                                zombie_survivors.append(survivor_group)

                                print("\nYou decide this has been enough action for today, and head home...")

                                log = "Spotted two survivors running from a horde, I didn't help but one of them named " + survivor1_name + " spotted me"
                                journal_entry(log)

                    else:
                        print("You're on your way to", area, "when a chorus of shouts rings out")
                        print("You duck behind a billboard and watch a gang of raiders descend on a group of zombies")
                        print("They're brutal fighters, and you find yourself learning new moves as you watch them")
                        print("\nThere's only one casualty on the raiders side, and the zombies are dead")
                        print("With the action over, you stealthily creep away and head back to the", character[7][0])

                else:
                    chance = random.randint(1, 3)

                    if chance != 1:
                        print("You've nearly reach your destination when you hear alarms ring out ahead")
                        print("Someone must have set them off!")
                        print("Dozens of zombies pour out onto the street behind you, and you dive for cover\n")
                        chance = random.randint(1, 4)

                        if day < 10:
                            chance = 2

                        if chance != 1:
                            print("You roll behind a greasy black bin, and the zombies pass by")
                            print("Looks like they didn't spot you!")

                        else:
                            zombie_num = random.randint(2,3)
                            print("But in your effort to escape the horde, you've jumped in front of", zombie_num, "zombies!")
                            result = fight(zombie_num, "zombies")

                            if not result:
                                game = False

                        if game:
                            print("After this narrow escape, you head back to the", character[7][0])
                            print("\nDespite your difficulties, you still manage to scrape up something:")
                            random_item(1, 2, "normal")

                    else:
                        print("You've nearly arrived at", area, "when you see smoke rising ahead...")
                        print("Deciding to check it out, you find a burning pile of dozens of bodies")
                        print("You're glad to see someone is sorting out all these zombies\n")
                        print("But as you make your way around, you realise not all of these bodies were undead")
                        print("One of the smouldering bodies on the edge of the pile is a survivor")
                        print("It looks like he was shot, and you make a quick exit")
                        print("On your way home, you wonder what could have happened to him...")
                        print("\nDespite your difficulties, you still manage to scrape up something:")
                        random_item(1, 2, "normal")

            elif chance == 9:
                if len(enemy_list) > 0:
                    enemy_name = enemy_list[random.randint(0, len(enemy_list) - 1)]
                    enemy_list.remove(enemy_name)
                    print("You're on your way towards", area, "when a figure steps out in front of you")
                    print("It's hard to see, but it doesn't look to be a raider or a zombie")
                    print("He steps forward and you gasp, it's", enemy_name[0])

                    if len(enemy_name) == 1:
                        print("He glowers at you, and promises to punish your betrayal of him")

                    else:
                        print("He snarls, promising revenge for the death of his friend", enemy_name[1])

                    fight_result = fight(1, "humans", enemy_name[0])

                    if fight_result:
                        print("With", enemy_name[0], "dead, you turn back home")
                        print("You'll be thinking twice before you mess with survivors again...")

                        log = enemy_name[0] + " returned and I had to kill him or be killed"
                        journal_entry

                    else:
                        game = False

                else:
                    chance = random.randint(1, 10)

                    if chance == 1:
                        print("You're walking up towards", area, "when a barricade in the street catches your eye")
                        soldier_num = random.randint(4, 10)
                        print("It's being patrolled by", soldier_num, "soldiers!")
                        print("Hopeful of some order being restored to society you creep closer, sticking to the shadows")
                        print("\nThe soldiers are wearing gas masks, and as you get near you begin to hear bits of conversation")
                        print("You're just about to reveal yourself when you hear an order from the soldier in command...")
                        print("He reminds his men to kill anything that moves, and putting aside your hopes, you head home")

                    elif chance == 2:
                        print("Working your way carefully towards", area, "you start to smell something strange")
                        print("When you turn onto the main road, you see a murky yellow gas blocking your way")
                        print("It hisses as it spreads from building to building, and as it makes contact with a lone zombie, their skin begins to dissolve")
                        print("You won't be able to scavenge here today...")

                    else:
                        print("As you near", area,"the clouds above darken, and when you arrive it begins to pour rain")
                        print("You can barely see what's in front of you, and it'd be too dangerous to seek shelter")
                        print("You'll have to head back home for today...")

                    print("\nDespite your difficulties, you still manage to scrape up something:")
                    random_item(1, 2, "normal")

            elif chance == 10:
                chance = random.randint(1, 2)

                if chance == 1:
                    horde_time = random.randint(5, 40)

                    print("You're on your way towards", area, "when you spot a pretty much untouched row of houses")
                    print("It looks like the perfect opportunity to do some looting")
                    print("These houses should be full of stuff")
                    print("But as you check the place out, you hear the sound of an approaching horde...\n")

                    if horde_time >= 25:
                        print("The horde is still far off and you should have some time to look around")

                    elif horde_time >= 15:
                        print("The horde isn't too far off but you could definitely risk taking a look around")

                    else:
                        print("The horde is really close, it'd be very risky to loot here")

                    print("Will you:\n1. Loot one of the houses\n2. Leave and avoid the horde")
                    choice = make_choice()

                    if choice == 1:
                        ground_floor = ["kitchen", "stairs", "living room", "bathroom", "garage"]
                        first_floor = ["bedroom", "bedroom", "bathroom", "study"]

                        print("You try the front door on one of the houses, and it's open")
                        print("Luckily there's no alarm and you can make your way inside")
                        print("You're in the hallway and can start looting")

                        room_num = 1
                        floor = 1
                        exit_house = False

                        print(line_break)
                        while horde_time > 0 and exit_house == False:
                            print("Room #" + str(room_num) + ":")
                            input("Press 1 to Continue:")
                            print()

                            if floor == 1:
                                room = ground_floor[random.randint(0, len(ground_floor) - 1)]

                                if room == "stairs":
                                    print("You open a door and see stairs going up to the first floor")
                                    horde_time -= random.randint(1, 2)
                                    print("You walk up the stairs and are now on the first floor")

                                    floor = 2

                                else:
                                    horde_time -= random.randint(4, 8)

                                    if room == "kitchen":
                                        print("You open a door and find yourself in the kitchen")
                                        print("Spending a few minutes checking cupboards and shelves you find:")
                                        random_item(3, 5, "normal", "food")

                                    elif room == "bathroom":
                                        print("You open a door and find yourself in the bathroom")
                                        print("You check through the cabinets and find:")
                                        random_item(1, 2, "normal", "meds")
                                    
                                    elif room == "living room":
                                        print("You open a door and find yourself in the living room")
                                        print("You check in drawers and behind couches and find:")
                                        random_item(2, 3, "normal")

                                    elif room == "garage":
                                        print("You open a door and find yourself in a dusty garage")
                                        chance = random.randint(1, 5)

                                        if chance == 1:
                                            garage_items = ["(weapon) *sledgehammer*", "(clothing) *motorbike helmet*", "(clothing) *work boots*"]

                                            garage_loot = garage_items[random.randint(0, len(garage_items) - 1)]

                                            print("\nYou take a look around the murky room, and spot a", garage_loot, "in the corner!")
                                            add_item(garage_loot)

                                            print("It seems like it was a good idea to loot here after all")

                                        else:
                                            print("\nYou around in the murky light, and find some fuel:")
                                            random_item(1, 2, "normal", "fuel")

                                ground_floor.remove(room)

                            elif floor == 2:
                                room = first_floor[random.randint(0, len(first_floor) - 1)]
                                horde_time -= random.randint(6, 10)
                                
                                if room == "study":
                                    chance = random.randint(1, 7)
                                    print("You open a door and find yourself in the study")

                                    if chance == 1:
                                        print("You rifle through drawers and check under the desk, until something catches your eye")
                                        print("There's a gun case under the desk!\n")
                                        print("Inside it you find:")
                                        print("(gun) *pistol*")
                                        print("(ammo) *5 pistol bullets*\n")

                                        add_item("(gun) *pistol*")
                                        add_item("(ammo) *5 pistol bullets*")

                                    else:
                                        print("You check in drawers and between plant pots and find:")
                                        random_item(3, 5, "normal")
                                
                                elif room == "bathroom":
                                        print("You open a door and find yourself in the bathroom")
                                        print("You check through the cabinets and find:")
                                        random_item(1, 3, "normal", "meds")

                                elif room == "bedroom":
                                        print("You open a door and find yourself in a bedroom")
                                        chance = random.randint(1, 5)

                                        if chance == 1:
                                            print("You check under the bed, then the wardrobe")
                                            
                                            bedroom_items = ["(clothing) *leather jacket*", "(clothing) *combat pants*", "(clothing) *body armour*", "(weapon) *katana*"]
                                            bedroom_loot = bedroom_items[random.randint(0, len(bedroom_items) - 1)]

                                            print("Looking through the wardrobe you see a", bedroom_loot, "in the back!")
                                            add_item(bedroom_loot)

                                        else:
                                            print("You check shelves, drawers and under the bed and find:")
                                            random_item(1, 3, "normal")

                                first_floor.remove(room)

                            if room != "stairs":
                                print("\nYou're satisfied you've looted everything in this room and can move on")

                        
                            if len(first_floor) > 0:
                                print("\nWill you:\n1. Check another room\n2. Leave and avoid the horde")
                                choice = make_choice()

                            else:
                                if len(ground_floor) == 0:
                                    print("Looks like you've checked everywhere, it's time to leave")
                                    choice = 2
                                    print(line_break)

                                else:
                                    print("Looks like you've checked the first floor, you'll head back downstairs")
                                    floor = 1

                                    print("\nWill you:\n1. Check another room\n2. Leave and avoid the horde")
                                    choice = make_choice()
                            
                            if choice == 2:
                                exit_house = True

                            else:
                                room_num += 1

                        if horde_time <= 0:
                            if exit_house == False:
                                print("But as you go to check the next room, you hear the front door cave in")
                            
                            else:
                                print("But as you go to leave, you hear the front door cave in")

                            print("You took too long and the horde has arrived!")

                            if floor == 1:
                                print("Will you:\n1. Try escape through the back door")
                                choice = make_choice()

                            else:
                                print("Will you:\n1. Try escape through a window")
                                choice = make_choice()

                            chance = random.randint(1, 3)
                            if choice == 1 and floor == 1:
                                print("You get to the kitchen and run for the back door")

                                if chance == 1:
                                    print("It's open!")
                                    print("As you dash out into the garden, you look back and see zombies pouring into the kitchen after you")
                                    print("You hop over the fence and head home, shocked by this lucky escape")

                                    journal_entry("Got greedy while looting but somehow escaped unharmed")

                                else:
                                    chance = random.randint(1, 2)
                                    print("It's locked!")

                                    if chance == 1:
                                        print("You kick the door desperately and it gives in, but a shock goes through your knee")
                                        print("You've injured your knee!")
                                        print("\nYou have lost 20HP")
                                        character[0][0] -= 20
                                        afflictions.append("injured knee")
                                        print("You now have", character[0][0], "HP")

                                        print("\nYou manage to make it out the door and slam it behind you as the horde pours into the kitchen")
                                        print("Somehow you get over the garden fence before you get pulled into the mass of zombies")
                                        print("As you hobble home, you curse yourself for being so greedy")

                                        journal_entry("Escaped a horde while looting but badly hurt my knee")

                                    else:
                                        print("You kick the door, but it doesn't budge")
                                        print("As you go to kick it again, zombies pour into the kitchen!")
                                        print("Undead hands grab you and drag you into the horde...\n YOU DIED")

                                        game = False

                            elif choice == 1 and floor == 2:
                                print("You rush to one of the bedrooms and spot a window facing the back of the house")

                                if chance == 1:
                                    print("It's unlocked!")
                                    print("You hear the horde coming up the stairs, and without a second thought you jump out the window")

                                    chance = random.randint(1, 2)

                                    if chance == 1:
                                        print("You roll as you land, avoiding injury and keeping your speed")
                                        print("\nAs the horde of zombies pour out of the house, you hop the garden fence and escape")
                                        print("As you head back to the", character[7][0], "you wonder what might have happened if the window was locked...")

                                        journal_entry("Had to jump out a window to escape a horde, but made it out okay")

                                    else:
                                        print("You land badly, hurting your ankle as you hit the ground")
                                        print("You've sprained your ankle!")
                                        print("\nYou have lost 20HP")
                                        character[0][0] -= 20
                                        afflictions.append("sprained ankle")
                                        print("You now have", character[0][0], "HP")

                                        chance = random.randint(1, 2)

                                        if chance == 1:
                                            print("Somehow you manage to get over the garden fence before the zombies, but it's too close")
                                            print("You can still feel their hands grabbing at your legs as you make your way home...")

                                            journal_entry("Sprained my ankle while escaping a horde and nearly died")

                                        else:
                                            print("You hobble towards the garden fence, but you're too slow!")
                                            print("You lunge desperately forward and trip, the horde closes around you and it's over...\nYOU DIED")

                                            game = False

                                else:
                                    print("The window's locked!")
                                    print("You'll have no choice but to smash it\n")

                                    chance = random.randint(1, 2)

                                    if chance == 1:
                                        print("You punch your hand through the window shattering it, but cutting open your hand")
                                        print("\nYou have lost 20HP")
                                        character[0][0] -= 20
                                        afflictions.append("laceration on hand")
                                        print("You now have", character[0][0], "HP")

                                        print("\nClutching your hand, you hop out the window and land in the grass")
                                        print("Zombies crawl out the window after you, but you manage to clear the fence and get away")
                                        print("As you head back to the", character[7][0], "you nurse your hand and curse your greediness")

                                        journal_entry("Cut my hand open while looting a house and almost died")

                                    else:
                                        print("You punch through the glass but it doesn't shatter fully and blood sprays from your hand")
                                        print("Clutching your hand, you look for another way out, but it's too late")
                                        print("Zombies rush into the room and you're torn apart...\nYOU DIED")

                                        game = False

                        else:
                            print("You gather your loot and open the door to head home")

                            if horde_time <= 3:
                                print("But when you leave the house, the horde is right in front of you!")
                                print("They've spotted you and you'll have to make a run for it")
                                print("You get to the end of the street but a some zombies have cut you off")

                                zom_num = random.randint(3, 6)

                                fight_result = fight(zom_num, "zombies")

                                if fight_result:
                                    print("With the zombies dead, you're free to escape the horde and head home")
                                    journal_entry("Ran into some zombies while looting but managed to kill them all")

                                    zombies_killed += zom_num

                                else:
                                    game = False

                            elif horde_time < 10:
                                print("You leave the house and check down the street, the horde is close but they won't reach you")

                                chance = random.randint(1, 3)

                                if chance == 1:
                                    zom_num = random.randint(2, 4)

                                    print("But as you go to escape down a side street,", zom_num, "zombies stumble in front of you")
                                    print("If you want to avoid the horde, you'll have to take them out!")

                                    zom_num = random.randint(3, 6)

                                    fight_result = fight(zom_num, "zombies")

                                    if fight_result:
                                        print("With the zombies dead, you're free to escape the horde and head home")
                                        journal_entry("Had to escape a horde and killed some zombies in my way")
                                        zombies_killed += zom_num

                                    else:
                                        game = False

                                else:
                                    print("There looks to be a lot of zombie activity from the horde, but you're able to slip through undetected")
                                    print("You make it all the way back to the", character[7][0], "without anymore trouble")
                                    journal_entry("Saw a lot of zombies while looting a house, but they didn't see me")

                            else:
                                print("You exit the house and see you had time to spare, the horde is nowhere near")
                                print("You head back without any hassle, but you wonder if you could've taken a bit more loot with you...")
                                journal_entry("Looted a house and escaped a horde without being seen")
                else:
                    chance = random.randint(1, 2)

                    if chance == 1:
                        print("You saw a huge shadow go by in the night, you'd want to lay low until it's definitely gone")
                        print("You won't go far today, no reason to attract unnecessary attention")
                        print("Whatever it was...")

                    else:
                        print("As you head down your usual road towards", area, "the smell of smoke drifts towards you")
                        print("You climb onto the roof of a smashed up store, and see a huge fire raging ahead")
                        print("The noise is drawing hundreds of zombies from all directions, you'll have to head home...")

                    print("\nDespite your difficulties, you still manage to scrape up something:")
                    random_item(1,2,"normal")

            else:
                chance = random.randint(1, 6)

                if chance == 1:
                    print("You're keeping an eye out for zombies when a horde passes across the street ahead")
                    print("You watch as zombies trickle in from side streets and head towards it")
                    print("As you turn to head back home something catches your eye")
                    print("\nA huge zombie, about 10 feet tall and clad in riot gear is lumbering around in the centre of the horde")
                    print("Could it be possible that the zombies can mutate?")

                elif chance == 2 or chance == 3:
                    print("You're on your way towards", area, "when a commotion ahead makes you stop and duck down")
                    print("Peering around the corner, you can't believe your eyes...")
                    print("A tank is being swarmed by zombies, and as you watch a soldier is dragged out and pulled into the horde")
                    print("With the hatch open, the zombies climb into the tank")
                    print("\nThe world belongs to them now")
                    print("As you head home, you wonder if that was the last remnant of the army you'll see...")

                else:
                    print("You journey out to scavenge in", area, "but something isn't right")
                    print("It feels like someone, or something is watching you...\n")

                    chance = random.randint(1, 3)

                    if chance == 1:
                        print("You keep walking straight, then dash off to the side")
                        print("Sprinting through sidestreets, you're taking a big risk, but your mind tells you it's the right decision")

                    elif chance == 2:
                        print("As you scavenge through some cars, you jump behind a van and run down a neighbouring alley")
                        print("You don't know what was watching you, but you've lost it")

                    else:
                        print("You keep moving towards your destination, when you feel a strange presence behind you")
                        print("Adrenaline fills your veins as you leap and jump over a fence, circling back down a different street")

                    print("As you head back to the", character[7][0], "you no longer feel that uneasy sensation...")

                print("\nDespite your difficulties, you still manage to scrape up something:")
                random_item(1,2,"normal")

            if game:
                water_chance = random.randint(1,3)

                if water_chance == 1 and character[7][0] != "campground clearing":

                    if not water_drank:
                        print("\nYou find some water on your way home, enough for today")
                        water_drank = True

        elif choice == 3:
            take_rest()

        elif len(afflictions) > 0:
            count = 0
            medical_prompt = ""
            for i in afflictions:
                if count == 0:
                    medical_prompt += i

                elif count + 1 == len(afflictions):
                    medical_prompt += " and a " + i

                else:
                    medical_prompt += ", " + i

                    count += 1

            print("You wont be able to go out today because of your",medical_prompt)
            print("Will you?\n1. Take some rest")
            choice = make_choice()

            take_rest()

        if game:
            print(line_break)
            count= 0
            medical_prompt= ""
            if len(afflictions) > 0 or character[0][0] < 100:
                if len(afflictions) > 0:
                    medical_prompt= "You have a "
                for i in afflictions:
                    if count == 0:
                        medical_prompt += i

                    elif count+1 == len(afflictions):
                        medical_prompt += " and a " + i

                    else:
                        medical_prompt += ", " + i

                    count += 1

                if medical_prompt != "":
                    print(medical_prompt)

                if character[0][0] < 100 or len(afflictions) > 0:
                    print("You have", character[0][0], "HP")
                print("Would you like to heal your wounds?\n1. Yes\n2. No")
                choice = make_choice()

                if choice == 1:
                    if len(character[5]) > 0:
                        print("\nWhat do you need to heal?")
                        count= 1
                        for i in afflictions:
                            print(str(count) + ". " + i)
                            count += 1
                        if character[0][0] < 100:
                            print(str(count) + ". " + "HP at " + str(character[0][0]))

                        print(str(count + 1) + ". Don't heal anything")

                        heal_choice = make_choice()

                        if heal_choice != count + 1:
                            print("What item will you use?")
                            if heal_choice!= count or character[0][0] == 100:
                                count= 1
                                for i in character[5]:
                                    if i == "bandages":
                                        heal_chance= "75%"

                                    elif i == "first aid kit":
                                        heal_chance= "100%"

                                    elif i == "painkillers":
                                        heal_chance= "50%"
                                    print(str(count) + ". " + i + " - chance of healing " + heal_chance)
                                    count += 1

                                choice = make_choice()

                                if character[5][choice - 1] == "bandages":
                                    chance = random.randint(1, 4)
                                    print("Your", afflictions[heal_choice - 1], "has been bandaged")

                                    if chance != 1:
                                        print("Your",afflictions[heal_choice-1],"has been healed")
                                        afflictions.remove(afflictions[heal_choice - 1])

                                    else:
                                        print("Your", afflictions[heal_choice - 1], "hasn't healed")

                                elif character[5][choice - 1] == "painkillers":
                                    chance = random.randint(1, 2)
                                    print("You have taken some painkillers")

                                    if chance != 1:
                                        print("Your", afflictions[heal_choice - 1], "has been healed")
                                        afflictions.remove(afflictions[heal_choice - 1])

                                    else:
                                        print("Your", afflictions[heal_choice - 1], "hasn't healed")

                                elif character[5][choice - 1] == "first aid kit":
                                    print("Your", afflictions[heal_choice - 1], "has been treated with a first aid kit")

                                    print("Your", afflictions[heal_choice - 1], "has been healed")
                                    afflictions.remove(afflictions[heal_choice - 1])

                                    character[5].remove(character[5][choice - 1])

                            else:
                                count = 0
                                for i in character[5]:
                                    count += 1
                                    if i == "bandages":
                                        hp_healed = 50

                                    elif i == "first aid kit":
                                        hp_healed = 100

                                    elif i == "painkillers":
                                        hp_healed = 25
                                    print(str(count) + ". " + i + " - HP healed: " + str(hp_healed))

                                choice = make_choice()

                                if character[5][choice-1] == "bandages":
                                    print("You have used some bandages")
                                    hp_healed = 50

                                elif character[5][choice-1] == "first aid kit":
                                    print("You have used a first aid kit")
                                    hp_healed = 100

                                elif character[5][choice-1] == "painkillers":
                                    print("You have taken some painkillers")
                                    hp_healed = 25

                                character[0][0] += hp_healed
                                if character[0][0] > 100:
                                    character[0][0] = 100
                                    print("You gained", hp_healed, "HP")

                                print("You now have", character[0][0], "/ 100 HP")
                                character[5].remove(character[5][choice -1])
                            print()

                        else:
                            print("You chose not to heal anything\n")

                    else:
                        print("You don't have any medicine\n")

            if len(character[8]) > 0:
                print("Would you like to open your inventory?\n1. Yes\n2. No")
                choice = make_choice()
                if choice == 1:
                    loop = True
                    while loop:
                        if len(character[8]) > 0:
                            print("Click the corresponding button to select an item")
                            print("You have:")
                            count = 1
                            for i in character[8]:
                                print(str(count) + ". " + i)
                                count += 1
                            print(str(count) + ". " + "Exit")
                            choice = make_choice()

                            if choice != count:
                                item_chosen = character[8][choice - 1]
                                if item_chosen[0:2] == "(c":
                                    total_armour = equip_armour(item_chosen[11:],total_armour)

                                elif item_chosen == "Journal":
                                    print("Important Events:")
                                    if len(journal) > 0:
                                        for entry in journal:
                                            print(entry)

                                    else:
                                        print("You haven't written anything in your journal yet")

                                elif item_chosen == "(mod) **suppressor**":
                                    mod_options = []

                                    for weapon in character[4]:
                                        if weapon[0:3] == "**a" or weapon[0:3] == "*pi":
                                            mod_options.append(weapon)

                                    if len(mod_options) == 0:
                                        print("No guns in your inventory")

                                    else:
                                        print("Choose a weapon to add the suppressor to:")
                                        count = 1
                                        for i in mod_options:
                                            print(str(count) + ". " + i)
                                            count += 1
                                        print(str(count) + ". " + "Exit")
                                        choice = make_choice()

                                        if mod_options[choice -1] == "**assault rifle**":
                                            rifle_supp = True
                                            print("Your **assault rifle** is now suppressed")
                                        
                                        else:
                                            pistol_supp = True
                                            print("Your *pistol* is now suppressed")

                                        character[9].remove("(mod) **suppressor**")

                                print(line_break)

                            elif choice == count:
                                loop = False

                        else:
                            loop = False


            calories_used = random.randint(1400, 2000)
            character[2][0] = character[2][0] - calories_used
            if character[2][0] < 0:
                character[2][0] = 0
            print("Today you used", calories_used, "calories")
            print("You have", character[2][0], "calories left\n")

            cook_food()

            print("Would you like to eat something?\n1. Yes\n2. No, it's time to sleep")
            choice = make_choice()

            if choice == 1:
                eat = True

                while character[2][0] < 5000 and eat is True and len(character[3]) > 0:
                    print("You have:")
                    count = 1
                    for i in character[3]:
                        print(str(count) + ". " + i + " - " + str(get_cals(i)) + " calories")
                        count += 1

                    if len(character[3]) > 1:
                        print(str(count) + ". " + "Consume all")

                    choice = make_choice()
                    if choice == count:
                        total_cals = 0

                        for i in character[3]:
                            total_cals += get_cals(i)

                        character[3] = []

                        print("You consumed everything for", total_cals,"calories")
                        character[2][0] += total_cals
                        print("You now have:", character[2][0], "calories")
                        eat = False
                    else:
                        character[2][0] += get_cals(character[3][choice - 1])
                        print("You consumed:", character[3][choice - 1], "for", get_cals(character[3][choice - 1]),"calories\n")
                        character[3].remove(character[3][choice - 1])
                        print("You now have:", character[2][0], "calories")
                        print("Do you want to eat more?\n1. Yes\n2. No, it's time to sleep")
                        choice = make_choice()
                        if choice == 2:
                            eat = False

                if len(character[3]) == 0 and eat == True:
                    print("You have no food")

            if character[2][0] == 0:
                print("You are now starving")
                print("You have lost 5 HP, find some food soon...")
                character[0][0] -= 5
                print("\nYou now have", character[0][0], "HP")

            if not water_drank:
                if character[1][0] == "Dehydrated":
                    print("\nYou are now dehydrated")
                    print("You have lost 10 HP, find some water soon...")
                    character[0][0] -= 10
                    print("\nYou now have", character[0][0], "HP")

                elif character[1][0] == "Severely Dehydrated":
                    print("\nYou are now severely dehydrated")
                    print("You have lost 20 HP, find some water URGENTLY...")
                    character[0][0] -= 20
                    print("\nYou now have", character[0][0], "HP")

            if character[0][0] < 0:
                character[0][0] = 0

            print("You close your eyes and go to sleep")
            input("\nPress 1 to continue to Day "  + str((day + 1)) + ": ")

            if character[0][0] == 0:
                print("Your body couldn't take it any more and in your sleep...\nYOU DIED")
                game= False

            if not water_drank:
                days_no_water += 1

            else:
                days_no_water = 0

            loop = False

record = []
scoreboard = []

record.append(username)
record.append(day - 1)
record.append(zombies_killed)

with open("scores.csv", "a", newline = "") as score:
    add_score = csv.writer(score)
    add_score.writerow(record)

with open("scores.csv", "r") as prev_scores:
    read_scores = csv.reader(prev_scores)
    for row in read_scores:
        scoreboard.append(row)

scoreboard = scoreboard[1:]

for i in range(1, len(scoreboard)):
    key = scoreboard[i]
    count = i - 1

    while count >= 0 and int(key[1]) > int(scoreboard[count][1]):
        scoreboard[count + 1] = scoreboard[count]
        count -= 1

    scoreboard[count + 1] = key

scoreboard = scoreboard[:11]
print()
print("{:-^46}".format("HIGH SCORES"))
print("{0:15}".format("Player:"), ("Days Survived:"), ("Zombies Killed:"))
for index, player in enumerate(scoreboard):
    print("{0:15}".format(player[0]), "{0:14}".format(player[1]), player[2])
print("-" * 46)
