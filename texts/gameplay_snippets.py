#---------------------------------------#
#---------- GAMEPLAY SNIPPETS ----------#
#---------------------------------------#

"""Contains the texts necessary for the running the main gameplay"""

#---------- TEXT SNIPPETS -----------#

# Introduction

title  = "\n   _____ _         __  __          __   ______ _                           _   _ "
title += "\n  / ____| |       / _|/ _|        / _| |  ____| |                         | | (_) "
title += "\n | (___ | |_ __ _| |_| |_    ___ | |_  | |__  | | ___ _ __ ___   ___ _ __ | |_ _  _"
title += "\n  \___ \| __/ _` |  _|  _|  / _ \|  _| |  __| | |/ _ \ '_ ` _ \ / _ \ '_ \| __| |/ _` |"
title += "\n  ____) | || (_| | | | |   | (_) | |   | |____| |  __/ | | | | |  __/ | | | |_| | (_| |"
title += "\n |_____/ \__\__,_|_| |_|    \___/|_|   |______|_|\___|_| |_| |_|\___|_| |_|\__|_|\__,_|"

intro = ("\nWelcome, traveler, "
         "\nto a world teetering on the edge of chaos. "
         "\nIn this magical forest, a brave witch embarks on a journey to find the Staff of Elementia, "
         "\na powerful artifact capable of restoring balance to nature. "
         "\nAs you guide her, you'll encounter dangerous foes, solve puzzles, "
         "\nand gather valuable ingredients for potions and spells. "
         "\nWill you help the witch restore harmony to the realm, or will you succumb to darkness?")


# player options listed for the player to prompt input
input_list_with_pet = ['\tcheck inventory   = Check your inventory',
                       '\tread spellbook    = Read your spellbook',
                       '\tinteract with pet = Interact with your pet',
                       '\tmove north        = Walk north',
                       '\tmove south        = Walk south',
                       '\tmove east         = Walk east',
                       '\tmove west         = Walk west'
                       ]

# player options without pet listed for the player to prompt input
input_list_no_pet = ['\tcheck inventory   = Check your inventory',
                     '\tread spellbook    = Read your spellbook',
                     '\tmove north        = Walk north',
                     '\tmove south        = Walk south',
                     '\tmove east         = Walk east',
                     '\tmove west         = Walk west'
                     ]

# map of corresponding methods to the player's input
output_list_with_pet = {'check inventory'   : 'checkInventory',
                        'read spellbook'    : 'readSpellbook',
                        'interact with pet' : 'interactWithPet',
                        'move north'        : ('walk', 'north'),
                        'move south'        : ('walk', 'south'),
                        'move east'         : ('walk', 'east'),
                        'move west'         : ('walk', 'west')
                        }

# player options listed for the player to prompt input for pet interaction
input_pet_interaction_list = [  '\tcall pet       = Call your pet',
                                '\tlook at pet    = Look at your pet',
                                '\tpet pet        = Pet your pet',
                                '\tplay with pet  = Play with your pet',
                                '\tfeed pet       = Feed your pet',
                                '\tcheck hunger   = Check if your pet is hungry'
                             ]

# map of corresponding methods to the player's input for pet interaction
output_pet_interaction_list = { 'call pet'      : 'callPet',
                                'look at pet'   : 'lookAtPet',
                                'pet pet'       : 'petPet',
                                'play with pet' : 'playWithPet',
                                'feed pet'     : 'feedPet',
                                'check hunger'  : 'checkPetsHunger'
                               }

