import os
import stat_classes
from dice import Dice
from dataclasses import dataclass
import ability_desc
import random

# Dice.dice()


def start():
    # Welcome message - (needs fonts, emojis, etc)
    print("Welcome to Wizard 102!!")
    print("Here is a list of classes!")
    print(
        """
        [Fire] - A Pyromancer that deals large damage and has a normal amount of health (the most rounded mage).
        [Ice] - A Cryomancer that can freeze enemies causing their turn to be skipped! 
        [Lightning] - An Electromancer that is fast and does a lot of damage. Starts off with 3 charge (lower health pools).
        [Earth] - A geomancer having increased hp and sustainability (deals less damage).
                                                                                                                      """
    )
    print("Keep in mind that you only get 1 heal from your cleric! Use it to your advantage.")

def winner(player1_list, player2_list, name1, name2):
    if player1_list[0].health <= 0:
        print(f"{name2.capitalize()} IS THE SUPERIOR WIZARD!!!!!")
    elif player2_list[0].health <= 0:
        print(f"{name1.capitalize()} IS THE SUPERIOR WIZARD!!!!!")
def wizard_ascii_art(): ## This function will be used when wizards are fighting just a cool art thing that shows a wizard casting a spell.
    print(
        """                             /\\
                            /  \\
                           |    |
                         --:'''':--
                           :'_' :
                            :"":\\___
            ' '      ____.' :::     '._
           . *=====<<=)           \\    :
            .  '      '-'-'\\_      /'._.'
                             \\====:_ ""
                            .'     \\\\
                           :       :
                          /   :    \\
                         :   .      '.
                         :  : :      :
                         :__:-:__.;--'
                         '-'   '-'
"""
    )


def cleric_ascii_art(): ## This function is called when healing, same thing as wizard except its just a cleric.
    print(
        """              _,._      
  .||,       /_ _\\\\     
 \\.`',/      |'L'| |    
 = ,. =      | -,| L    
 / || \\    ,-'\\"/,'`.   
   ||     ,'   `,,. `.  
   ,|____,' , ,;' \\| |  
  (3|\\    _/|/'   _| |  
   ||/,-''  | >-'' _,\\\\ 
   ||'      ==\\ ,-'  ,' 
   ||       |  V \\ ,|   
   ||       |    |` |   
   ||       |    |   \\  
   ||       |    \\    \\ 
   ||       |     |    \\
   ||       |      \\_,-'
   ||       |___,,--")_\\
   ||         |_|   ccc/
   ||        ccc/       
   ||\n"""
    )

def gandalf_winner():
    print("""                       ,---.
                       /    |
                      /     |
                     /      |
                    /       |
               ___,'        |
             <  -'          :
              `-.__..--'``-,_\\_
                 |o/ ` :,.)_`>
                 :/ `     ||/)
                 (_.).__,-` |\\
                 /( `.``   `| :
                 \\'`-.)  `  ; ;
                 | `       /-<
                 |     `  /   `.
 ,-_-..____     /|  `    :__..-'\\
/,'-.__\\\\  ``-./ :`      ;       \\
`\\ `\\  `\\\\  \\ :  (   `  /  ,   `. \\
  \\` \\   \\\\   |  | `   :  :     .\\ \\
   \\ `\\_  ))  :  ;     |  |      ): :
  (`-.-'\\ ||  |\\ \\   ` ;  ;       | |
   \\-_   `;;._   ( `  /  /_       | |
    `-.-.// ,'`-._\\__/_,'         ; |
       \\:: :     /     `     ,   /  |
        || |    (        ,' /   /   |
        ||                ,'   / SSt|""")

def rand_4():
    return int(random.uniform(1,4.9999999999999999999))

def spell_desc(): ## This function holds all of the descriptions for each ability!
    choose = input(
        "Which description would you want?\n[Fire], [Ice], [Earth], or [Lightning] "
    )
    if choose.lower() == "fire":
        fire_description = ability_desc.fire_desc()
        print("~" * os.get_terminal_size().columns)
        print(f"{fire_description[0]}\n{fire_description[1]}\n{fire_description[2]}")
        print("~" * os.get_terminal_size().columns)
    elif choose.lower() == "ice":
        ice_description = ability_desc.ice_desc()
        print("~" * os.get_terminal_size().columns)
        print(f"{ice_description[0]}\n{ice_description[1]}\n{ice_description[2]}")
        print("~" * os.get_terminal_size().columns)
    elif choose.lower() == "earth":
        earth_description = ability_desc.earth_desc()
        print("~" * os.get_terminal_size().columns)
        print(f"{earth_description[0]}\n{earth_description[1]}\n{earth_description[2]}")
        print("~" * os.get_terminal_size().columns)
    elif choose.lower() == "lightning":
        lightning_description = ability_desc.lightning_desc()
        print("~" * os.get_terminal_size().columns)
        print(f"{lightning_description[0]}\n{lightning_description[1]}\n{lightning_description[2]}")
        print("~" * os.get_terminal_size().columns)
    else:
        print("Invalid Input.")


def player1_choice(): ## This function grabs the players choice of mage types.
    while True:
        class_decider = input("Choose your class:")
        if class_decider.lower() == "fire":
            fire_mage = stat_classes.Fire(False)
            fire_desc = ability_desc.fire_desc()
            mage_type = "fire"
            print("You have chosen Fire Mage!\n")
            fire_list = [fire_mage, fire_desc, mage_type]
            return fire_list

        elif class_decider.lower() == "ice":
            ice_mage = stat_classes.Ice(False)
            ice_desc = ability_desc.ice_desc()
            mage_type = "ice"
            print("You have chosen Ice Mage!\n")
            ice_list = [ice_mage, ice_desc, mage_type]
            return ice_list

        elif class_decider.lower() == "lightning":
            lightning_mage = stat_classes.Lightning(False)
            lightning_desc = ability_desc.lightning_desc()
            mage_type = "lightning"
            print("You have chosen Lightning Mage!\n")
            lightning_list = [lightning_mage, lightning_desc, mage_type]
            return lightning_list

        elif class_decider.lower() == "earth":
            earth_mage = stat_classes.Earth(False)
            earth_desc = ability_desc.earth_desc()
            mage_type = "earth"
            print("You have chosen Earth Mage!\n")
            earth_list = [earth_mage, earth_desc, mage_type]
            return earth_list

        else:
            print(f"'{class_decider}' is not a valid mage type!!! ")


def player2_choice(): ## This is the same function as above but for player 2. (could be counter intuitive but it helped me seperate my thought proccess better.)
    while True:
        class_decider = input("Choose your class:")
        if class_decider.lower() == "fire":
            fire_mage = stat_classes.Fire(False)
            fire_desc = ability_desc.fire_desc()
            mage_type = "fire"
            print("You have chosen Fire Mage\n")
            fire_list = [fire_mage, fire_desc, mage_type]
            return fire_list

        elif class_decider.lower() == "ice":
            ice_mage = stat_classes.Ice(False)
            ice_desc = ability_desc.ice_desc()
            mage_type = "ice"
            print("You have chosen Ice Mage!\n")
            ice_list = [ice_mage, ice_desc, mage_type]
            return ice_list

        elif class_decider.lower() == "lightning":
            lightning_mage = stat_classes.Lightning(False)
            lightning_desc = ability_desc.lightning_desc()
            mage_type = "lightning"
            print("You have chosen Lightning Mage!\n")
            lightning_list = [lightning_mage, lightning_desc, mage_type]
            return lightning_list

        elif class_decider.lower() == "earth":
            earth_mage = stat_classes.Earth(False)
            earth_desc = ability_desc.earth_desc()
            mage_type = "earth"
            print("You have chosen Earth Mage!\n")
            mage_list = [earth_mage, earth_desc, mage_type]
            return mage_list

        else:
            print(f"'{class_decider}' is not a valid mage type!!! ")


## ALL CHARGE FUNCTIONS.
def charge(player1_list, player2_list):
    if player1_list[0].turn == True:
        player1_list[0].charge += 1
        
    elif player2_list[0].turn == True:
        player2_list[0].charge += 1

def secondary_charge(player1_list, player2_list):
    if player1_list[0].turn == True:
        player1_list[0].charge -= 2
    elif player2_list[0].turn == True:
        player2_list[0].charge -= 2


def ultimate_charge(player1_list, player2_list):
    if player1_list[0].turn == True:
        player1_list[0].charge -= 5
    elif player2_list[0].turn == True:
        player2_list[0].charge -= 5


## Decides who's turn it will be next.
def change_turn(player1_list, player2_list):
    if player1_list[0].turn == True:
        player1_list[0].turn = False
        player2_list[0].turn = True

    elif player2_list[0].turn == True:
        player2_list[0].turn = False
        player1_list[0].turn = True


# Fight function will run off of who's turn it is and let them attack or heal.
def fight(name1, name2, player1_list, player2_list):
    # If its your turn and you use an ability you must lose or gain whatever charge for that ability and set the new users turn true.
    # PLAYER 1 FIGHT CODE-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    if player1_list[0].turn == True:
        while True:
            if player1_list[0].health > 0 and player2_list[0].health > 0:
                print(f"{name1.capitalize()}'s turn to do damage!")
                print(
                    f"{name1.capitalize()}\nHEALTH: {player1_list[0].health:.2f}\nCHARGE: {player1_list[0].charge}"
                )
                print(
                    f"{name2.capitalize()}\nHEALTH: {player2_list[0].health:.2f}\nCHARGE: {player2_list[0].charge}"
                )
                game_option = input("Would you like to [fight] or [heal]")
                if game_option == "fight":
                    print(f"Choose your spell {name1.capitalize()}")
                    print(
                        f"[1] Basic Attack: [{player1_list[0].ability1}] - Takes 0 charge\n[2] Secondary Attack: [{player1_list[0].ability2}]- Takes 2 charge\n[3] Ultimate Attack: [{player1_list[0].ability3}]- Takes 5 charge"
                    )

                    ability_choice = input(">> ")
                    if ability_choice == "1":  ## ABIILITY 1
                        dmg_decider = Dice.dice()
                        print(
                            f"{name1.capitalize()} decided to use {player1_list[0].ability1}!"
                        )

                        match dmg_decider: ## FOR ALL match dmg_decider REFER BACK TO NOTES (damage is affected by a dice roll, values specified in notes.)
                            case 1:
                                wizard_ascii_art()
                                turn_damage = player1_list[0].damage * 0.50
                                turn_damage *= 0.50
                                player2_list[0].health -= turn_damage
                                charge(player1_list, player2_list)
                                change_turn(player1_list, player2_list)
                                print(
                                    f"You dealt {turn_damage:.2f} with {player1_list[0].ability1} to {name2.capitalize()}!"
                                )
                                if player1_list[0].ability1 == "Ice Bolt": ## This logic checks if they are using an ice ability and if they are the enemies will have a chance to be frozen!
                                    chance = rand_4()
                                    match chance:
                                        case 1:
                                            print(f"{player1_list[0].ability1} froze {name2.capitalize()} with a 25% chance to freeze! ({name2.capitalize()}'s turn will be skipped.)")
                                            change_turn(player1_list,player2_list)
                                            print(
                                                "~" * os.get_terminal_size().columns
                                            )
                                            break
                                        case 2:
                                            print(
                                                "~" * os.get_terminal_size().columns
                                            )
                                            break
                                        
                                        case 3:
                                            print(
                                                "~" * os.get_terminal_size().columns
                                            )
                                            break

                                        case 4:
                                            print(
                                                "~" * os.get_terminal_size().columns
                                            )
                                            break
                                else:
                                    print(
                                            "~" * os.get_terminal_size().columns
                                    )
                                    break

                                
                            case 2:
                                wizard_ascii_art()
                                turn_damage = player1_list[0].damage * 0.50
                                turn_damage *= 1.00
                                player2_list[0].health -= turn_damage
                                charge(player1_list, player2_list)
                                change_turn(player1_list, player2_list)
                                print(
                                    f"You dealt {turn_damage:.2f} with {player1_list[0].ability1} to {name2.capitalize()}!"
                                )
                                if player1_list[0].ability1 == "Ice Bolt": ## This logic checks if they are using an ice ability and if they are the enemies will have a chance to be frozen!
                                    chance = rand_4()
                                    match chance:
                                        case 1:
                                            print(f"{player1_list[0].ability1} froze {name2.capitalize()} with a 25% chance to freeze! ({name2.capitalize()}'s turn will be skipped.)")
                                            change_turn(player1_list,player2_list)
                                            print(
                                                "~" * os.get_terminal_size().columns
                                            )
                                            break
                                        case 2:
                                            print(
                                                "~" * os.get_terminal_size().columns
                                            )
                                            break
                                        
                                        case 3:
                                            print(
                                                "~" * os.get_terminal_size().columns
                                            )
                                            break

                                        case 4:
                                            print(
                                                "~" * os.get_terminal_size().columns
                                            )
                                            break
                                else:
                                    print(
                                            "~" * os.get_terminal_size().columns
                                    )
                                    break

                            case 3:
                                wizard_ascii_art()
                                turn_damage = player1_list[0].damage * 0.50
                                turn_damage *= 1.50
                                player2_list[0].health -= turn_damage
                                charge(player1_list, player2_list)
                                change_turn(player1_list, player2_list)
                                print(
                                    f"You dealt {turn_damage:.2f} with {player1_list[0].ability1} to {name2.capitalize()}!"
                                )
                                if player1_list[0].ability1 == "Ice Bolt": ## This logic checks if they are using an ice ability and if they are the enemies will have a chance to be frozen!
                                    chance = rand_4()
                                    match chance:
                                        case 1:
                                            print(f"{player1_list[0].ability1} froze {name2.capitalize()} with a 25% chance to freeze! ({name2.capitalize()}'s turn will be skipped.)")
                                            change_turn(player1_list,player2_list)
                                            print(
                                                "~" * os.get_terminal_size().columns
                                            )
                                            break
                                        case 2:
                                            print(
                                                "~" * os.get_terminal_size().columns
                                            )
                                            break
                                        
                                        case 3:
                                            print(
                                                "~" * os.get_terminal_size().columns
                                            )
                                            break

                                        case 4:
                                            print(
                                                "~" * os.get_terminal_size().columns
                                            )
                                            break
                                else:
                                    print(
                                            "~" * os.get_terminal_size().columns
                                    )
                                    break
                            case 4:
                                wizard_ascii_art()
                                turn_damage = player1_list[0].damage * 0.50
                                turn_damage *= 2.00
                                player2_list[0].health -= turn_damage
                                charge(player1_list, player2_list)
                                change_turn(player1_list, player2_list)
                                print(
                                    f"You dealt {turn_damage:.2f} with {player1_list[0].ability1} to {name2.capitalize()}!"
                                )
                                if player1_list[0].ability1 == "Ice Bolt": ## This logic checks if they are using an ice ability and if they are the enemies will have a chance to be frozen!
                                    chance = rand_4()
                                    match chance:
                                        case 1:
                                            print(f"{player1_list[0].ability1} froze {name2.capitalize()} with a 25% chance to freeze! ({name2.capitalize()}'s turn will be skipped.)")
                                            change_turn(player1_list,player2_list)
                                            print(
                                                "~" * os.get_terminal_size().columns
                                            )
                                            break
                                        case 2:
                                            print(
                                                "~" * os.get_terminal_size().columns
                                            )
                                            break
                                        
                                        case 3:
                                            print(
                                                "~" * os.get_terminal_size().columns
                                            )
                                            break

                                        case 4:
                                            print(
                                                "~" * os.get_terminal_size().columns
                                            )
                                            break
                                else:
                                    print(
                                            "~" * os.get_terminal_size().columns
                                    )
                                    break
                            case 5:
                                wizard_ascii_art()
                                turn_damage = player1_list[0].damage * 0.50
                                turn_damage *= 2.50
                                player2_list[0].health -= turn_damage
                                charge(player1_list, player2_list)
                                change_turn(player1_list, player2_list)
                                print(
                                    f"You dealt {turn_damage:.2f} with {player1_list[0].ability1} to {name2.capitalize()}!"
                                )
                                if player1_list[0].ability1 == "Ice Bolt": ## This logic checks if they are using an ice ability and if they are the enemies will have a chance to be frozen!
                                    chance = rand_4()
                                    match chance:
                                        case 1:
                                            print(f"{player1_list[0].ability1} froze {name2.capitalize()} with a 25% chance to freeze! ({name2.capitalize()}'s turn will be skipped.)")
                                            change_turn(player1_list,player2_list)
                                            print(
                                                "~" * os.get_terminal_size().columns
                                            )
                                            break
                                        case 2:
                                            print(
                                                "~" * os.get_terminal_size().columns
                                            )
                                            break
                                        
                                        case 3:
                                            print(
                                                "~" * os.get_terminal_size().columns
                                            )
                                            break

                                        case 4:
                                            print(
                                                "~" * os.get_terminal_size().columns
                                            )
                                            break
                                else:
                                    print(
                                        "~" * os.get_terminal_size().columns
                                    )
                                    break
                            case 6:
                                wizard_ascii_art()
                                turn_damage = player1_list[0].damage * 0.50
                                turn_damage *= 3.00
                                player2_list[0].health -= turn_damage
                                charge(player1_list, player2_list)
                                change_turn(player1_list, player2_list)
                                print(
                                    f"You dealt {turn_damage:.2f} with {player1_list[0].ability1} to {name2.capitalize()}!"
                                )
                                if player1_list[0].ability1 == "Ice Bolt": ## This logic checks if they are using an ice ability and if they are the enemies will have a chance to be frozen!
                                    chance = rand_4()
                                    match chance:
                                        case 1:
                                            print(f"{player1_list[0].ability1} froze {name2.capitalize()} with a 25% chance to freeze! ({name2.capitalize()}'s turn will be skipped.)")
                                            change_turn(player1_list,player2_list)
                                            print(
                                                "~" * os.get_terminal_size().columns
                                            )
                                            break
                                        case 2:
                                            print(
                                                "~" * os.get_terminal_size().columns
                                            )
                                            break
                                        
                                        case 3:
                                            print(
                                                "~" * os.get_terminal_size().columns
                                            )
                                            break

                                        case 4:
                                            print(
                                                "~" * os.get_terminal_size().columns
                                            )
                                            break
                                else:
                                    print(
                                        "~" * os.get_terminal_size().columns
                                    )
                                    break

                    elif ability_choice == "2":  ## ABILITY TWO
                        if player1_list[0].charge >= 2:
                            dmg_decider = Dice.dice()
                            print(f"{name1.capitalize()} decided to use {player1_list[0].ability2}!")
                            match dmg_decider:
                                case 1:
                                    wizard_ascii_art()
                                    turn_damage = player1_list[0].damage * 0.75
                                    turn_damage *= 0.50
                                    player2_list[0].health -= turn_damage
                                    secondary_charge(player1_list, player2_list)
                                    change_turn(player1_list, player2_list)
                                    print(
                                        f"You dealt {turn_damage:.2f} with {player1_list[0].ability2} to {name2.capitalize()}!"
                                    )
                                    if player1_list[0].ability2 == "Ice Wall": ## This logic checks if they are using an ice ability and if they are the enemies will have a chance to be frozen!
                                        chance = rand_4()
                                        match chance:
                                            case 1:
                                                print(f"{player1_list[0].ability2} froze {name2.capitalize()} with a 25% chance to freeze! ({name2.capitalize()}'s turn will be skipped.)")
                                                change_turn(player1_list,player2_list)
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break
                                            case 2:
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break
                                            
                                            case 3:
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break

                                            case 4:
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break
                                    else:
                                        print(
                                            "~" * os.get_terminal_size().columns
                                        )
                                        break
                        
                                case 2:
                                    wizard_ascii_art()
                                    turn_damage = player1_list[0].damage * 0.75
                                    turn_damage *= 1.00
                                    player2_list[0].health -= turn_damage
                                    secondary_charge(player1_list, player2_list)
                                    change_turn(player1_list, player2_list)
                                    print(
                                        f"You dealt {turn_damage:.2f} with {player1_list[0].ability2} to {name2.capitalize()}!"
                                    )
                                    if player1_list[0].ability2 == "Ice Wall": ## This logic checks if they are using an ice ability and if they are the enemies will have a chance to be frozen!
                                        chance = rand_4()
                                        match chance:
                                            case 1:
                                                print(f"{player1_list[0].ability2} froze {name2.capitalize()} with a 25% chance to freeze! ({name2.capitalize()}'s turn will be skipped.)")
                                                change_turn(player1_list,player2_list)
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break
                                            case 2:
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break
                                            
                                            case 3:
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break

                                            case 4:
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break
                                    else:
                                        print(
                                            "~" * os.get_terminal_size().columns
                                        )
                                        break

                                case 3:
                                    wizard_ascii_art()
                                    turn_damage = player1_list[0].damage * 0.75
                                    turn_damage *= 1.50
                                    player2_list[0].health -= turn_damage
                                    secondary_charge(player1_list, player2_list)
                                    change_turn(player1_list, player2_list)
                                    print(
                                        f"You dealt {turn_damage:.2f} with {player1_list[0].ability2} to {name2.capitalize()}!"
                                    )
                                    if player1_list[0].ability2 == "Ice Wall": ## This logic checks if they are using an ice ability and if they are the enemies will have a chance to be frozen!
                                        chance = rand_4()
                                        match chance:
                                            case 1:
                                                print(f"{player1_list[0].ability2} froze {name2.capitalize()} with a 25% chance to freeze! ({name2.capitalize()}'s turn will be skipped.)")
                                                change_turn(player1_list,player2_list)
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break
                                            case 2:
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break
                                            
                                            case 3:
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break

                                            case 4:
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break
                                    else:
                                        print(
                                            "~" * os.get_terminal_size().columns
                                        )
                                        break

                                case 4:
                                    wizard_ascii_art()
                                    turn_damage = player1_list[0].damage * 0.75
                                    turn_damage *= 2.00
                                    player2_list[0].health -= turn_damage
                                    secondary_charge(player1_list, player2_list)
                                    change_turn(player1_list, player2_list)
                                    print(
                                        f"You dealt {turn_damage:.2f} with {player1_list[0].ability2} to {name2.capitalize()}!"
                                    )
                                    if player1_list[0].ability2 == "Ice Wall": ## This logic checks if they are using an ice ability and if they are the enemies will have a chance to be frozen!
                                        chance = rand_4()
                                        match chance:
                                            case 1:
                                                print(f"{player1_list[0].ability2} froze {name2.capitalize()} with a 25% chance to freeze! ({name2.capitalize()}'s turn will be skipped.)")
                                                change_turn(player1_list,player2_list)
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break
                                            case 2:
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break
                                            
                                            case 3:
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break

                                            case 4:
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break
                                    else:
                                        print(
                                            "~" * os.get_terminal_size().columns
                                        )
                                        break

                                case 5:
                                    wizard_ascii_art()
                                    turn_damage = player1_list[0].damage * 0.75
                                    turn_damage *= 2.50
                                    player2_list[0].health -= turn_damage
                                    secondary_charge(player1_list, player2_list)
                                    change_turn(player1_list, player2_list)
                                    print(
                                        f"You dealt {turn_damage:.2f} with {player1_list[0].ability2} to {name2.capitalize()}!"
                                    )
                                    if player1_list[0].ability2 == "Ice Wall": ## This logic checks if they are using an ice ability and if they are the enemies will have a chance to be frozen!
                                        chance = rand_4()
                                        match chance:
                                            case 1:
                                                print(f"{player1_list[0].ability2} froze {name2.capitalize()} with a 25% chance to freeze! ({name2.capitalize()}'s turn will be skipped.)")
                                                change_turn(player1_list,player2_list)
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break
                                            case 2:
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break
                                            
                                            case 3:
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break

                                            case 4:
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break
                                    else:
                                        print(
                                            "~" * os.get_terminal_size().columns
                                        )
                                        break

                                case 6:
                                    wizard_ascii_art()
                                    turn_damage = player1_list[0].damage * 0.75
                                    turn_damage *= 3.00
                                    player2_list[0].health -= turn_damage
                                    secondary_charge(player1_list, player2_list)
                                    change_turn(player1_list, player2_list)
                                    print(
                                        f"You dealt {turn_damage:.2f} with {player1_list[0].ability2} to {name2.capitalize()}!"
                                    )
                                    if player1_list[0].ability2 == "Ice Wall": ## This logic checks if they are using an ice ability and if they are the enemies will have a chance to be frozen!
                                        chance = rand_4()
                                        match chance:
                                            case 1:
                                                print(f"{player1_list[0].ability2} froze {name2.capitalize()} with a 25% chance to freeze! ({name2.capitalize()}'s turn will be skipped.)")
                                                change_turn(player1_list,player2_list)
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break
                                            case 2:
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break
                                            
                                            case 3:
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break

                                            case 4:
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break
                                    else:
                                        print(
                                            "~" * os.get_terminal_size().columns
                                        )
                                        break

                        else:
                            print(
                                "~" * os.get_terminal_size().columns
                            )
                            print("You don't have enough charge!")
                            print(
                                "~" * os.get_terminal_size().columns
                            )

                    elif ability_choice == "3":  ## ABILITY 3 (ULTIMATE)
                        if player1_list[0].charge >= 5:
                            dmg_decider = Dice.dice()
                            print(f"You decided to use {player1_list[0].ability3}!")
                            match dmg_decider:
                                case 1:
                                    wizard_ascii_art()
                                    turn_damage = player1_list[0].damage * 1.05
                                    turn_damage *= 0.50
                                    player2_list[0].health -= turn_damage
                                    ultimate_charge(player1_list, player2_list)
                                    change_turn(player1_list, player2_list)
                                    print(
                                        f"You dealt {turn_damage:.2f} with {player1_list[0].ability3} to {name2.capitalize()}!"
                                    )
                                    if player1_list[0].ability3 == "Blizzard": ## This logic checks if they are using an ice ability and if they are the enemies will have a chance to be frozen!
                                        chance = rand_4()
                                        match chance:
                                            case 1:
                                                print(f"{player1_list[0].ability2} froze {name2.capitalize()} with a 75% chance to freeze! ({name2.capitalize()}'s turn will be skipped.)")
                                                change_turn(player1_list,player2_list)
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break
                                            case 2:
                                                print(f"{player1_list[0].ability2} froze {name2.capitalize()} with a 75% chance to freeze! ({name2.capitalize()}'s turn will be skipped.)")
                                                change_turn(player1_list,player2_list)
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break
                                            case 3:
                                                print(f"{player1_list[0].ability2} froze {name2.capitalize()} with a 75% chance to freeze! ({name2.capitalize()}'s turn will be skipped.)")
                                                change_turn(player1_list,player2_list)
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break
                                            case 4:
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break
                                    else:
                                         print(
                                                "~" * os.get_terminal_size().columns
                                                )
                                         break


                                case 2:
                                    wizard_ascii_art()
                                    turn_damage = player1_list[0].damage * 1.05
                                    turn_damage *= 1.00
                                    player2_list[0].health -= turn_damage
                                    ultimate_charge(player1_list, player2_list)
                                    change_turn(player1_list, player2_list)
                                    print(
                                        f"You dealt {turn_damage:.2f} with {player1_list[0].ability3} to {name2.capitalize()}!"
                                    )
                                    if player1_list[0].ability3 == "Blizzard": ## This logic checks if they are using an ice ability and if they are the enemies will have a chance to be frozen!
                                        chance = rand_4()
                                        match chance:
                                            case 1:
                                                print(f"{player1_list[0].ability2} froze {name2.capitalize()} with a 75% chance to freeze! ({name2.capitalize()}'s turn will be skipped.)")
                                                change_turn(player1_list,player2_list)
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break
                                            case 2:
                                                print(f"{player1_list[0].ability2} froze {name2.capitalize()} with a 75% chance to freeze! ({name2.capitalize()}'s turn will be skipped.)")
                                                change_turn(player1_list,player2_list)
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break
                                            case 3:
                                                print(f"{player1_list[0].ability2} froze {name2.capitalize()} with a 75% chance to freeze! ({name2.capitalize()}'s turn will be skipped.)")
                                                change_turn(player1_list,player2_list)
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break
                                            case 4:
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break
                                    else:
                                         print(
                                                "~" * os.get_terminal_size().columns
                                                )
                                         break

                                case 3:
                                    wizard_ascii_art()
                                    turn_damage = player1_list[0].damage * 1.05
                                    turn_damage *= 1.50
                                    player2_list[0].health -= turn_damage
                                    ultimate_charge(player1_list, player2_list)
                                    change_turn(player1_list, player2_list)
                                    print(
                                        f"You dealt {turn_damage:.2f} with {player1_list[0].ability3} to {name2.capitalize()}!"
                                    )
                                    if player1_list[0].ability3 == "Blizzard": ## This logic checks if they are using an ice ability and if they are the enemies will have a chance to be frozen!
                                        chance = rand_4()
                                        match chance:
                                            case 1:
                                                print(f"{player1_list[0].ability2} froze {name2.capitalize()} with a 75% chance to freeze! ({name2.capitalize()}'s turn will be skipped.)")
                                                change_turn(player1_list,player2_list)
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break
                                            case 2:
                                                print(f"{player1_list[0].ability2} froze {name2.capitalize()} with a 75% chance to freeze! ({name2.capitalize()}'s turn will be skipped.)")
                                                change_turn(player1_list,player2_list)
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break
                                            case 3:
                                                print(f"{player1_list[0].ability2} froze {name2.capitalize()} with a 75% chance to freeze! ({name2.capitalize()}'s turn will be skipped.)")
                                                change_turn(player1_list,player2_list)
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break
                                            case 4:
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break
                                    else:
                                         print(
                                                "~" * os.get_terminal_size().columns
                                                )
                                         break
                                case 4:
                                    wizard_ascii_art()
                                    turn_damage = player1_list[0].damage * 1.05
                                    turn_damage *= 2.00
                                    player2_list[0].health -= turn_damage
                                    ultimate_charge(player1_list, player2_list)
                                    change_turn(player1_list, player2_list)
                                    print(
                                        f"You dealt {turn_damage:.2f} with {player1_list[0].ability3} to {name2.capitalize()}!"
                                    )
                                    if player1_list[0].ability3 == "Blizzard": ## This logic checks if they are using an ice ability and if they are the enemies will have a chance to be frozen!
                                        chance = rand_4()
                                        match chance:
                                            case 1:
                                                print(f"{player1_list[0].ability2} froze {name2.capitalize()} with a 75% chance to freeze! ({name2.capitalize()}'s turn will be skipped.)")
                                                change_turn(player1_list,player2_list)
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break
                                            case 2:
                                                print(f"{player1_list[0].ability2} froze {name2.capitalize()} with a 75% chance to freeze! ({name2.capitalize()}'s turn will be skipped.)")
                                                change_turn(player1_list,player2_list)
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break
                                            case 3:
                                                print(f"{player1_list[0].ability2} froze {name2.capitalize()} with a 75% chance to freeze! ({name2.capitalize()}'s turn will be skipped.)")
                                                change_turn(player1_list,player2_list)
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break
                                            case 4:
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break
                                    else:
                                         print(
                                                "~" * os.get_terminal_size().columns
                                                )
                                         break

                                case 5:
                                    wizard_ascii_art()
                                    turn_damage = player1_list[0].damage * 1.05
                                    turn_damage *= 2.50
                                    player2_list[0].health -= turn_damage
                                    ultimate_charge(player1_list, player2_list)
                                    change_turn(player1_list, player2_list)
                                    print(
                                        f"You dealt {turn_damage:.2f} with {player1_list[0].ability3} to {name2.capitalize()}!"
                                    )
                                    if player1_list[0].ability3 == "Blizzard": ## This logic checks if they are using an ice ability and if they are the enemies will have a chance to be frozen!
                                        chance = rand_4()
                                        match chance:
                                            case 1:
                                                print(f"{player1_list[0].ability2} froze {name2.capitalize()} with a 75% chance to freeze! ({name2.capitalize()}'s turn will be skipped.)")
                                                change_turn(player1_list,player2_list)
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break
                                            case 2:
                                                print(f"{player1_list[0].ability2} froze {name2.capitalize()} with a 75% chance to freeze! ({name2.capitalize()}'s turn will be skipped.)")
                                                change_turn(player1_list,player2_list)
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break
                                            case 3:
                                                print(f"{player1_list[0].ability2} froze {name2.capitalize()} with a 75% chance to freeze! ({name2.capitalize()}'s turn will be skipped.)")
                                                change_turn(player1_list,player2_list)
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break
                                            case 4:
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break
                                    else:
                                         print(
                                                "~" * os.get_terminal_size().columns
                                                )
                                         break

                                case 6:
                                    wizard_ascii_art()
                                    turn_damage = player1_list[0].damage * 1.05
                                    turn_damage *= 3.00
                                    player2_list[0].health -= turn_damage
                                    ultimate_charge(player1_list, player2_list)
                                    change_turn(player1_list, player2_list)
                                    print(
                                        f"You dealt {turn_damage:.2f} with {player1_list[0].ability3} to {name2.capitalize()}!"
                                    )
                                    if player1_list[0].ability3 == "Blizzard": ## This logic checks if they are using an ice ability and if they are the enemies will have a chance to be frozen!
                                        chance = rand_4()
                                        match chance:
                                            case 1:
                                                print(f"{player1_list[0].ability2} froze {name2.capitalize()} with a 75% chance to freeze! ({name2.capitalize()}'s turn will be skipped.)")
                                                change_turn(player1_list,player2_list)
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break
                                            case 2:
                                                print(f"{player1_list[0].ability2} froze {name2.capitalize()} with a 75% chance to freeze! ({name2.capitalize()}'s turn will be skipped.)")
                                                change_turn(player1_list,player2_list)
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break
                                            case 3:
                                                print(f"{player1_list[0].ability2} froze {name2.capitalize()} with a 75% chance to freeze! ({name2.capitalize()}'s turn will be skipped.)")
                                                change_turn(player1_list,player2_list)
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break
                                            case 4:
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break
                                    else:
                                         print(
                                                "~" * os.get_terminal_size().columns
                                                )
                                         break
                        else:
                            print(
                                "~" * os.get_terminal_size().columns
                            )
                            print("You don't have enough charge!")
                            print(
                                "~" * os.get_terminal_size().columns
                            ) 
                elif game_option == "heal":
                    if player1_list[0].potion == 1:
                        player1_list[0].potion -= 1
                        player1_list[0].health += 50
                        if player1_list[0].health > player1_list[0].original_health:
                            player1_list[0].health = player1_list[0].original_health
                            cleric_ascii_art()
                            print(
                                f"{name1.capitalize()} was healed back to {player1_list[0].original_health} health by their cleric! (You healed to the maximum health!)"
                            )
                            print(
                                "~" * os.get_terminal_size().columns
                            )
                            change_turn(player1_list, player2_list)
                            break

                        elif player1_list[0].health <= player1_list[0].original_health:
                            print(
                                f"{name1.capitalize()} was healed back to {player1_list[0].health} health by their cleric! "
                            )
                            cleric_ascii_art()
                            print(
                                "~" * os.get_terminal_size().columns
                            )
                            change_turn(player1_list, player2_list)
                            break
                    else:
                        print(
                            "~" * os.get_terminal_size().columns
                        )
                        print("Your cleric is out of mana!")
                        print(
                            "~" * os.get_terminal_size().columns
                        )
                        break

    # PLAYER 2 FIGHT CODE -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    elif player2_list[0].turn == True:
        while True:
            if player2_list[0].health > 0 and player1_list[0].health > 0:
                print(f"{name2.capitalize()}'s turn to do damage!")
                print(
                    f"{name1.capitalize()}\nHEALTH: {player1_list[0].health:.2f}\nCHARGE: {player1_list[0].charge}"
                )
                print(
                    f"{name2.capitalize()}\nHEALTH: {player2_list[0].health:.2f}\nCHARGE: {player2_list[0].charge}"
                )
                game_option = input("Would you like to [fight] or [heal]")
                if game_option == "fight":
                    print(f"Choose your spell {name2.capitalize()}")
                    print(
                        f"[1] Basic Attack: [{player2_list[0].ability1}] - Takes 0 charge\n[2] Secondary Attack: [{player2_list[0].ability2}]- Takes 2 charge\n[3] Ultimate Attack: [{player2_list[0].ability3}]- Takes 5 charge"
                    )
                    ability_choice = input(">> ")
                    if ability_choice == "1":  ## ABILITY 1
                        dmg_decider = Dice.dice()
                        print(
                            f"{name2.capitalize()} decided to use {player2_list[0].ability1}!"
                        )
                        match dmg_decider:
                            case 1:
                                wizard_ascii_art()
                                turn_damage = player2_list[0].damage * 0.50
                                turn_damage *= 0.50
                                player1_list[0].health -= turn_damage
                                charge(player1_list, player2_list)
                                change_turn(player1_list, player2_list)
                                print(
                                    f"You dealt {turn_damage:.2f} with {player2_list[0].ability1} to {name1.capitalize()}!"
                                )
                                if player2_list[0].ability1 == "Ice Bolt": ## This logic checks if they are using an ice ability and if they are the enemies will have a chance to be frozen!
                                    chance = rand_4()
                                    match chance:
                                        case 1:
                                            print(f"{player2_list[0].ability1} froze {name1.capitalize()} with a 25% chance to freeze! ({name1.capitalize()}'s turn will be skipped.)")
                                            change_turn(player1_list,player2_list)
                                            print(
                                                "~" * os.get_terminal_size().columns
                                            )
                                            break
                                        case 2:
                                            print(
                                                "~" * os.get_terminal_size().columns
                                            )
                                            break
                                        
                                        case 3:
                                            print(
                                                "~" * os.get_terminal_size().columns
                                            )
                                            break

                                        case 4:
                                            print(
                                                "~" * os.get_terminal_size().columns
                                            )
                                            break
                                else:
                                    print(
                                        "~" * os.get_terminal_size().columns
                                        )
                                    break

                            case 2:
                                wizard_ascii_art()
                                turn_damage = player2_list[0].damage * 0.50
                                turn_damage *= 1.00
                                player1_list[0].health -= turn_damage
                                charge(player1_list, player2_list)
                                change_turn(player1_list, player2_list)
                                print(
                                    f"You dealt {turn_damage:.2f} with {player2_list[0].ability1} to {name1.capitalize()}!"
                                )
                                if player2_list[0].ability1 == "Ice Bolt": ## This logic checks if they are using an ice ability and if they are the enemies will have a chance to be frozen!
                                    chance = rand_4()
                                    match chance:
                                        case 1:
                                            print(f"{player2_list[0].ability1} froze {name1.capitalize()} with a 25% chance to freeze! ({name1.capitalize()}'s turn will be skipped.)")
                                            change_turn(player1_list,player2_list)
                                            print(
                                                "~" * os.get_terminal_size().columns
                                            )
                                            break
                                        case 2:
                                            print(
                                                "~" * os.get_terminal_size().columns
                                            )
                                            break
                                        
                                        case 3:
                                            print(
                                                "~" * os.get_terminal_size().columns
                                            )
                                            break

                                        case 4:
                                            print(
                                                "~" * os.get_terminal_size().columns
                                            )
                                            break
                                else:
                                    print(
                                        "~" * os.get_terminal_size().columns
                                        )
                                    break
                            case 3:
                                wizard_ascii_art()
                                turn_damage = player2_list[0].damage * 0.50
                                turn_damage *= 1.50
                                player1_list[0].health -= turn_damage
                                charge(player1_list, player2_list)
                                change_turn(player1_list, player2_list)
                                print(
                                    f"You dealt {turn_damage:.2f} with {player2_list[0].ability1} to {name1.capitalize()}!"
                                )
                                if player2_list[0].ability1 == "Ice Bolt": ## This logic checks if they are using an ice ability and if they are the enemies will have a chance to be frozen!
                                    chance = rand_4() 
                                    match chance:
                                        case 1:
                                            print(f"{player2_list[0].ability1} froze {name1.capitalize()} with a 25% chance to freeze! ({name1.capitalize()}'s turn will be skipped.)")
                                            change_turn(player1_list,player2_list)
                                            print(
                                                "~" * os.get_terminal_size().columns
                                            )
                                            break
                                        case 2:
                                            print(
                                                "~" * os.get_terminal_size().columns
                                            )
                                            break
                                        
                                        case 3:
                                            print(
                                                "~" * os.get_terminal_size().columns
                                            )
                                            break

                                        case 4:
                                            print(
                                                "~" * os.get_terminal_size().columns
                                            )
                                            break
                                else:
                                    print(
                                        "~" * os.get_terminal_size().columns
                                        )
                                    break
                            case 4:
                                wizard_ascii_art()
                                turn_damage = player2_list[0].damage * 0.50
                                turn_damage *= 2.00
                                player1_list[0].health -= turn_damage
                                charge(player1_list, player2_list)
                                change_turn(player1_list, player2_list)
                                print(
                                    f"You dealt {turn_damage:.2f} with {player2_list[0].ability1} to {name1.capitalize()}!"
                                )
                                if player2_list[0].ability1 == "Ice Bolt": ## This logic checks if they are using an ice ability and if they are the enemies will have a chance to be frozen!
                                    chance = rand_4()
                                    match chance:
                                        case 1:
                                            print(f"{player2_list[0].ability1} froze {name1.capitalize()} with a 25% chance to freeze! ({name1.capitalize()}'s turn will be skipped.)")
                                            change_turn(player1_list,player2_list)
                                            print(
                                                "~" * os.get_terminal_size().columns
                                            )
                                            break
                                        case 2:
                                            print(
                                                "~" * os.get_terminal_size().columns
                                            )
                                            break
                                        
                                        case 3:
                                            print(
                                                "~" * os.get_terminal_size().columns
                                            )
                                            break

                                        case 4:
                                            print(
                                                "~" * os.get_terminal_size().columns
                                            )
                                            break
                                else:
                                    print(
                                        "~" * os.get_terminal_size().columns
                                        )
                                    break
                            case 5:
                                wizard_ascii_art()
                                turn_damage = player2_list[0].damage * 0.50
                                turn_damage *= 2.50
                                player1_list[0].health -= turn_damage
                                charge(player1_list, player2_list)
                                change_turn(player1_list, player2_list)
                                print(
                                    f"You dealt {turn_damage:.2f} with {player2_list[0].ability1} to {name1.capitalize()}!"
                                )
                                if player2_list[0].ability1 == "Ice Bolt": ## This logic checks if they are using an ice ability and if they are the enemies will have a chance to be frozen!
                                    chance = rand_4()
                                    match chance:
                                        case 1:
                                            print(f"{player2_list[0].ability1} froze {name1.capitalize()} with a 25% chance to freeze! ({name1.capitalize()}'s turn will be skipped.)")
                                            change_turn(player1_list,player2_list)
                                            print(
                                                "~" * os.get_terminal_size().columns
                                            )
                                            break
                                        case 2:
                                            print(
                                                "~" * os.get_terminal_size().columns
                                            )
                                            break
                                        
                                        case 3:
                                            print(
                                                "~" * os.get_terminal_size().columns
                                            )
                                            break

                                        case 4:
                                            print(
                                                "~" * os.get_terminal_size().columns
                                            )
                                else:
                                    print(
                                        "~" * os.get_terminal_size().columns
                                        )
                                    break
                            case 6:
                                wizard_ascii_art()
                                turn_damage = player2_list[0].damage * 0.50
                                turn_damage *= 3.00
                                player1_list[0].health -= turn_damage
                                charge(player1_list, player2_list)
                                change_turn(player1_list, player2_list)
                                print(
                                    f"You dealt {turn_damage:.2f} with {player2_list[0].ability1} to {name1.capitalize()}!"
                                )
                                if player2_list[0].ability1 == "Ice Bolt": ## This logic checks if they are using an ice ability and if they are the enemies will have a chance to be frozen!
                                    chance = rand_4()
                                    match chance:
                                        case 1:
                                            print(f"{player2_list[0].ability1} froze {name1.capitalize()} with a 25% chance to freeze! ({name1.capitalize()}'s turn will be skipped.)")
                                            change_turn(player1_list,player2_list)
                                            print(
                                                "~" * os.get_terminal_size().columns
                                            )
                                            break
                                        case 2:
                                            print(
                                                "~" * os.get_terminal_size().columns
                                            )
                                            break
                                        
                                        case 3:
                                            print(
                                                "~" * os.get_terminal_size().columns
                                            )
                                            break

                                        case 4:
                                            print(
                                                "~" * os.get_terminal_size().columns
                                            )
                                else:
                                    print(
                                        "~" * os.get_terminal_size().columns
                                        )
                                    break

                    elif ability_choice == "2":  ## ABILITY TWO
                        if player2_list[0].charge >= 2:
                            dmg_decider = Dice.dice()
                            print(f"{name2.capitalize()} decided to use {player2_list[0].ability2}!")
                            match dmg_decider:
                                case 1:
                                    wizard_ascii_art()
                                    turn_damage = player2_list[0].damage * 0.75
                                    turn_damage *= 0.50
                                    player1_list[0].health -= turn_damage
                                    secondary_charge(player1_list, player2_list)
                                    change_turn(player1_list, player2_list)
                                    print(
                                        f"You dealt {turn_damage:.2f} with {player2_list[0].ability2} to {name1.capitalize()}!"
                                    )
                                    if player2_list[0].ability2 == "Ice Wall": ## This logic checks if they are using an ice ability and if they are the enemies will have a chance to be frozen!
                                        chance = rand_4()
                                        match chance:
                                            case 1:
                                                print(f"{player2_list[0].ability2} froze {name1.capitalize()} with a 50% chance to freeze! ({name1.capitalize()}'s turn will be skipped.)")
                                                change_turn(player1_list,player2_list)
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break
                                            case 2:
                                                print(f"{player2_list[0].ability2} froze {name1.capitalize()} with a 50% chance to freeze! ({name1.capitalize()}'s turn will be skipped.)")
                                                change_turn(player1_list,player2_list)
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break
                                            case 3:
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break

                                            case 4:
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break
                                    else:
                                        print(
                                            "~" * os.get_terminal_size().columns
                                            )
                                        break
                                case 2:
                                    wizard_ascii_art()
                                    turn_damage = player2_list[0].damage * 0.75
                                    turn_damage *= 1.00
                                    player1_list[0].health -= turn_damage
                                    secondary_charge(player1_list, player2_list)
                                    change_turn(player1_list, player2_list)
                                    print(
                                        f"You dealt {turn_damage:.2f} with {player2_list[0].ability2} to {name1.capitalize()}!"
                                    )
                                    if player2_list[0].ability2 == "Ice Wall": ## This logic checks if they are using an ice ability and if they are the enemies will have a chance to be frozen!
                                        chance = rand_4()
                                        match chance:
                                            case 1:
                                                print(f"{player2_list[0].ability2} froze {name1.capitalize()} with a 25% chance to freeze! ({name1.capitalize()}'s turn will be skipped.)")
                                                change_turn(player1_list,player2_list)
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break
                                            case 2:
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break
                                            
                                            case 3:
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break

                                            case 4:
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break
                                    else:
                                        print(
                                            "~" * os.get_terminal_size().columns
                                            )
                                        break
                                case 3:
                                    wizard_ascii_art()
                                    turn_damage = player2_list[0].damage * 0.75
                                    turn_damage *= 1.50
                                    player1_list[0].health -= turn_damage
                                    secondary_charge(player1_list, player2_list)
                                    change_turn(player1_list, player2_list)
                                    print(
                                        f"You dealt {turn_damage:.2f} with {player2_list[0].ability2} to {name1.capitalize()}!"
                                    )
                                    if player2_list[0].ability2 == "Ice Wall": ## This logic checks if they are using an ice ability and if they are the enemies will have a chance to be frozen!
                                        chance = rand_4()
                                        match chance:
                                            case 1:
                                                print(f"{player2_list[0].ability2} froze {name1.capitalize()} with a 25% chance to freeze! ({name1.capitalize()}'s turn will be skipped.)")
                                                change_turn(player1_list,player2_list)
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break
                                            case 2:
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break
                                            
                                            case 3:
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break

                                            case 4:
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break
                                    else:
                                        print(
                                            "~" * os.get_terminal_size().columns
                                            )
                                        break
                                case 4:
                                    wizard_ascii_art()
                                    turn_damage = player2_list[0].damage * 0.75
                                    turn_damage *= 2.00
                                    player1_list[0].health -= turn_damage
                                    secondary_charge(player1_list, player2_list)
                                    change_turn(player1_list, player2_list)
                                    print(
                                        f"You dealt {turn_damage:.2f} with {player2_list[0].ability2} to {name1.capitalize()}!"
                                    )
                                    if player2_list[0].ability2 == "Ice Wall": ## This logic checks if they are using an ice ability and if they are the enemies will have a chance to be frozen!
                                        chance = rand_4()
                                        match chance:
                                            case 1:
                                                print(f"{player2_list[0].ability2} froze {name1.capitalize()} with a 25% chance to freeze! ({name1.capitalize()}'s turn will be skipped.)")
                                                change_turn(player1_list,player2_list)
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break
                                            case 2:
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break
                                            
                                            case 3:
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break

                                            case 4:
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break
                                    else:
                                        print(
                                            "~" * os.get_terminal_size().columns
                                            )
                                        break
                                case 5:
                                    wizard_ascii_art()
                                    turn_damage = player2_list[0].damage * 0.75
                                    turn_damage *= 2.50
                                    player1_list[0].health -= turn_damage
                                    secondary_charge(player1_list, player2_list)
                                    change_turn(player1_list, player2_list)
                                    print(
                                        f"You dealt {turn_damage:.2f} with {player2_list[0].ability2} to {name1.capitalize()}!"
                                    )
                                    if player2_list[0].ability2 == "Ice Wall": ## This logic checks if they are using an ice ability and if they are the enemies will have a chance to be frozen!
                                        chance = rand_4()
                                        match chance:
                                            case 1:
                                                print(f"{player2_list[0].ability2} froze {name1.capitalize()} with a 25% chance to freeze! ({name1.capitalize()}'s turn will be skipped.)")
                                                change_turn(player1_list,player2_list)
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break
                                            case 2:
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break
                                            
                                            case 3:
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break

                                            case 4:
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break
                                    else:
                                        print(
                                            "~" * os.get_terminal_size().columns
                                            )
                                        break
                                case 6:
                                    wizard_ascii_art()
                                    turn_damage = player2_list[0].damage * 0.75
                                    turn_damage *= 3.00
                                    player1_list[0].health -= turn_damage
                                    secondary_charge(player1_list, player2_list)
                                    change_turn(player1_list, player2_list)
                                    print(
                                        f"You dealt {turn_damage:.2f} with {player2_list[0].ability2} to {name1.capitalize()}!"
                                    )
                                    if player2_list[0].ability2 == "Ice Wall": ## This logic checks if they are using an ice ability and if they are the enemies will have a chance to be frozen!
                                        chance = rand_4()
                                        match chance:
                                            case 1:
                                                print(f"{player2_list[0].ability2} froze {name1.capitalize()} with a 25% chance to freeze! ({name1.capitalize()}'s turn will be skipped.)")
                                                change_turn(player1_list,player2_list)
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break
                                            case 2:
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break
                                            
                                            case 3:
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break

                                            case 4:
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break
                                    else:
                                        print(
                                            "~" * os.get_terminal_size().columns
                                            )
                                        break
                        else:
                            print(
                                "~" * os.get_terminal_size().columns
                            )
                            print("You don't have enough charge!")
                            print(
                                "~" * os.get_terminal_size().columns
                            )
                    elif ability_choice == "3":  ## ABILITY 3 (ULTIMATE)
                        if player2_list[0].charge >= 5:
                            dmg_decider = Dice.dice()
                            print(f"You decided to use {player2_list[0].ability3}!")
                            match dmg_decider:
                                case 1:
                                    wizard_ascii_art()
                                    turn_damage = player2_list[0].damage * 1.05
                                    turn_damage *= 0.50
                                    player1_list[0].health -= turn_damage
                                    ultimate_charge(player1_list, player2_list)
                                    change_turn(player1_list, player2_list)
                                    print(
                                        f"You dealt {turn_damage:.2f} with {player2_list[0].ability3} to {name1.capitalize()}!"
                                    )
                                    if player2_list[0].ability3 == "Blizzard": ## This logic checks if they are using an ice ability and if they are the enemies will have a chance to be frozen!
                                        chance = rand_4()
                                        match chance:
                                            case 1:
                                                print(f"{player2_list[0].ability3} froze {name1.capitalize()} with a 75% chance to freeze! ({name1.capitalize()}'s turn will be skipped.)")
                                                change_turn(player1_list,player2_list)
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break
                                            case 2:
                                                print(f"{player2_list[0].ability3} froze {name1.capitalize()} with a 75% chance to freeze! ({name1.capitalize()}'s turn will be skipped.)")
                                                change_turn(player1_list,player2_list)
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break
                                            case 3:
                                                print(f"{player2_list[0].ability3} froze {name1.capitalize()} with a 75% chance to freeze! ({name1.capitalize()}'s turn will be skipped.)")
                                                change_turn(player1_list,player2_list)
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break
                                            case 4:
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break
                                    else:
                                        print(
                                            "~" * os.get_terminal_size().columns
                                            )
                                        break
                                case 2:
                                    wizard_ascii_art()
                                    turn_damage = player2_list[0].damage * 1.05
                                    turn_damage *= 1.00
                                    player1_list[0].health -= turn_damage
                                    ultimate_charge(player1_list, player2_list)
                                    change_turn(player1_list, player2_list)
                                    print(
                                        f"You dealt {turn_damage:.2f} with {player2_list[0].ability3} to {name1.capitalize()}!"
                                    )
                                    if player2_list[0].ability3 == "Blizzard": ## This logic checks if they are using an ice ability and if they are the enemies will have a chance to be frozen!
                                        chance = rand_4()
                                        match chance:
                                            case 1:
                                                print(f"{player2_list[0].ability3} froze {name1.capitalize()} with a 75% chance to freeze! ({name1.capitalize()}'s turn will be skipped.)")
                                                change_turn(player1_list,player2_list)
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break
                                            case 2:
                                                print(f"{player2_list[0].ability3} froze {name1.capitalize()} with a 75% chance to freeze! ({name1.capitalize()}'s turn will be skipped.)")
                                                change_turn(player1_list,player2_list)
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break
                                            case 3:
                                                print(f"{player2_list[0].ability3} froze {name1.capitalize()} with a 75% chance to freeze! ({name1.capitalize()}'s turn will be skipped.)")
                                                change_turn(player1_list,player2_list)
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break
                                            case 4:
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break
                                    else:
                                        print(
                                            "~" * os.get_terminal_size().columns
                                            )
                                        break

                                case 3:
                                    wizard_ascii_art()
                                    turn_damage = player2_list[0].damage * 1.05
                                    turn_damage *= 1.50
                                    player1_list[0].health -= turn_damage
                                    ultimate_charge(player1_list, player2_list)
                                    change_turn(player1_list, player2_list)
                                    print(
                                        f"You dealt {turn_damage:.2f} with {player2_list[0].ability3} to {name1.capitalize()}!"
                                    )
                                    if player2_list[0].ability3 == "Blizzard": ## This logic checks if they are using an ice ability and if they are the enemies will have a chance to be frozen!
                                        chance = rand_4()
                                        match chance:
                                            case 1:
                                                print(f"{player2_list[0].ability3} froze {name1.capitalize()} with a 75% chance to freeze! ({name1.capitalize()}'s turn will be skipped.)")
                                                change_turn(player1_list,player2_list)
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break
                                            case 2:
                                                print(f"{player2_list[0].ability3} froze {name1.capitalize()} with a 75% chance to freeze! ({name1.capitalize()}'s turn will be skipped.)")
                                                change_turn(player1_list,player2_list)
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break
                                            case 3:
                                                print(f"{player2_list[0].ability3} froze {name1.capitalize()} with a 75% chance to freeze! ({name1.capitalize()}'s turn will be skipped.)")
                                                change_turn(player1_list,player2_list)
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break
                                            case 4:
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break
                                    else:
                                        print(
                                            "~" * os.get_terminal_size().columns
                                            )
                                        break

                                case 4:
                                    wizard_ascii_art()
                                    turn_damage = player2_list[0].damage * 1.05
                                    turn_damage *= 2.00
                                    player1_list[0].health -= turn_damage
                                    ultimate_charge(player1_list, player2_list)
                                    change_turn(player1_list, player2_list)
                                    print(
                                        f"You dealt {turn_damage:.2f} with {player2_list[0].ability3} to {name1.capitalize()}!"
                                    )
                                    if player2_list[0].ability3 == "Blizzard": ## This logic checks if they are using an ice ability and if they are the enemies will have a chance to be frozen!
                                        chance = rand_4()
                                        match chance:
                                            case 1:
                                                print(f"{player2_list[0].ability3} froze {name1.capitalize()} with a 75% chance to freeze! ({name1.capitalize()}'s turn will be skipped.)")
                                                change_turn(player1_list,player2_list)
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break
                                            case 2:
                                                print(f"{player2_list[0].ability3} froze {name1.capitalize()} with a 75% chance to freeze! ({name1.capitalize()}'s turn will be skipped.)")
                                                change_turn(player1_list,player2_list)
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break
                                            case 3:
                                                print(f"{player2_list[0].ability3} froze {name1.capitalize()} with a 75% chance to freeze! ({name1.capitalize()}'s turn will be skipped.)")
                                                change_turn(player1_list,player2_list)
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break
                                            case 4:
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break
                                    else:
                                        print(
                                            "~" * os.get_terminal_size().columns
                                            )
                                        break
                                case 5:
                                    wizard_ascii_art()
                                    turn_damage = player2_list[0].damage * 1.05
                                    turn_damage *= 2.50
                                    player1_list[0].health -= turn_damage
                                    ultimate_charge(player1_list, player2_list)
                                    change_turn(player1_list, player2_list)
                                    print(
                                        f"You dealt {turn_damage:.2f} with {player2_list[0].ability3} to {name1.capitalize()}!"
                                    )
                                    if player2_list[0].ability3 == "Blizzard": ## This logic checks if they are using an ice ability and if they are the enemies will have a chance to be frozen!
                                        chance = rand_4()
                                        match chance:
                                            case 1:
                                                print(f"{player2_list[0].ability3} froze {name1.capitalize()} with a 75% chance to freeze! ({name1.capitalize()}'s turn will be skipped.)")
                                                change_turn(player1_list,player2_list)
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break
                                            case 2:
                                                print(f"{player2_list[0].ability3} froze {name1.capitalize()} with a 75% chance to freeze! ({name1.capitalize()}'s turn will be skipped.)")
                                                change_turn(player1_list,player2_list)
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break
                                            case 3:
                                                print(f"{player2_list[0].ability3} froze {name1.capitalize()} with a 75% chance to freeze! ({name1.capitalize()}'s turn will be skipped.)")
                                                change_turn(player1_list,player2_list)
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break
                                            case 4:
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break
                                    else:
                                        print(
                                            "~" * os.get_terminal_size().columns
                                            )
                                        break
                                case 6:
                                    wizard_ascii_art()
                                    turn_damage = player2_list[0].damage * 1.05
                                    turn_damage *= 3.00
                                    player1_list[0].health -= turn_damage
                                    ultimate_charge(player1_list, player2_list)
                                    change_turn(player1_list, player2_list)
                                    print(
                                        f"You dealt {turn_damage:.2f} with {player2_list[0].ability3} to {name1.capitalize()}!"
                                    )
                                    if player2_list[0].ability3 == "Blizzard": ## This logic checks if they are using an ice ability and if they are the enemies will have a chance to be frozen!
                                        chance = rand_4()
                                        match chance:
                                            case 1:
                                                print(f"{player2_list[0].ability3} froze {name1.capitalize()} with a 75% chance to freeze! ({name1.capitalize()}'s turn will be skipped.)")
                                                change_turn(player1_list,player2_list)
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break
                                            case 2:
                                                print(f"{player2_list[0].ability3} froze {name1.capitalize()} with a 75% chance to freeze! ({name1.capitalize()}'s turn will be skipped.)")
                                                change_turn(player1_list,player2_list)
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break
                                            case 3:
                                                print(f"{player2_list[0].ability3} froze {name1.capitalize()} with a 75% chance to freeze! ({name1.capitalize()}'s turn will be skipped.)")
                                                change_turn(player1_list,player2_list)
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break
                                            case 4:
                                                print(
                                                    "~" * os.get_terminal_size().columns
                                                )
                                                break
                                    else:
                                        print(
                                            "~" * os.get_terminal_size().columns
                                            )
                                        break
                        else:
                            print(
                                "~" * os.get_terminal_size().columns
                            )
                            print("You don't have enough charge!")
                            print(
                                "~" * os.get_terminal_size().columns
                            )

                elif game_option == "heal": ## If they decide to heal we will run the cleric ascii art and figure out the logic behind how much they heal.
                    if player2_list[0].potion == 1:
                        player2_list[0].potion -= 1
                        player2_list[0].health += 50
                        if player2_list[0].health > player2_list[0].original_health:
                            player2_list[0].health = player2_list[0].original_health
                            cleric_ascii_art()
                            print(
                                f"{name2.capitalize()} was healed back to {player2_list[0].original_health} health by their cleric! (You healed to the maximum health!)"
                            )
                            print(
                                "~" * os.get_terminal_size().columns
                            )
                            change_turn(player1_list, player2_list)
                            break

                        elif player2_list[0].health <= player2_list[0].original_health:
                            cleric_ascii_art()
                            print(
                                f"{name2.capitalize()} was healed back to {player2_list[0].health} health by their cleric!"
                            )
                            print(
                                "~" * os.get_terminal_size().columns
                            )
                            change_turn(player1_list, player2_list)
                            break
                    else:
                        print(
                            "~" * os.get_terminal_size().columns
                        )
                        print("Your cleric is out of mana!")
                        print(
                            "~" * os.get_terminal_size().columns
                        )
                        break


def main(): ## Main function compiling all of our functions that we created and 
    player_turn_winner = ""
    print("Before you start we will need your names (only 2 players allowed).")
    name1 = input("Player 1: ")
    name2 = input("Player 2: ")
    while True:
      see_abilities_desc = input(f"Would you like to look at all abilities [ y(es) ] or [ any other key ] ")
      if see_abilities_desc != "y" and see_abilities_desc != "yes":
          break
      spell_desc()
    start()
    print(f"Choose your mage {name1.capitalize()}")
    player1_list = player1_choice()
    while True:
        print(f"Choose your mage {name2.capitalize()}")
        player2_list = player2_choice()
        if player2_list == player1_list:
            print("This class is taken.")
        else:
            break
    while player_turn_winner == "":
        print(f"{name1.capitalize()} rolls:")
        total1 = Dice.dice()
        print(f"{name2.capitalize()} rolls:")
        total2 = Dice.dice()
        if total1 > total2:
            player_turn_winner = name1
            player1_list[0].turn = True
        elif total1 < total2:
            player_turn_winner = name2
            player2_list[0].turn = True
        else:
            print("You must reroll! Both players rolled the same dice!")
            player_turn_winner = ""
    while True:
        if float("{:.2f}".format(player1_list[0].health)) > 0 and float("{:.2f}".format(player2_list[0].health)) > 0:
            fight(name1, name2, player1_list, player2_list)
        else:
            break
    winner(player1_list, player2_list, name1, name2)
    gandalf_winner()

if __name__ == "__main__":
    main()
