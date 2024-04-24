#---------------------------------------#
#--------- STAFF OF ELEMENTIA ----------#
#-------------- GAMEPLAY ---------------#
#---------------------------------------#

"""This is the main gameplay."""

#---------- IMPORTS -----------#

from debugging          import debug_functions
from texts              import gameplay_snippets
from classes.Game       import Game
from classes.Player     import Player
from classes.Forest     import Forest
from classes.Witch      import Witch

#---------- INTRO ---------#

print(gameplay_snippets.title)
print(gameplay_snippets.intro)

confirmation = input('\nEnter your response (y = I want to help! / n = No, thanks...):\n')
confirmation = confirmation.strip().lower()
debug_functions.debugVariable('confirmation', confirmation)

if confirmation != 'y':
    print("Farewell, traveler. Come back when you're ready to tackle this challenge.")
else:

    #---------- CREATING A PLAYER ---------#

    player_name = input('\nThen state your name, brave traveler!\n')
    player_name = player_name.strip()
    debug_functions.debugVariable('player_name', player_name)

    # name = None
    player = Player(player_name)
    debug_functions.debugVariable('player.get_name()', player.get_name())

    # TODO: check if the player has played before

    # case: player has not played before
    new_game_confirmation = input(f'\nAre you ready to start a new adventure, {player_name}? (y/n)\n')
    new_game_confirmation = new_game_confirmation.strip().lower()
    debug_functions.debugVariable('new_game_confirmation', new_game_confirmation)

    if new_game_confirmation != 'y':
        print(f"Farewell, {player_name}. Come back when you're ready to tackle this challenge.")
    else:

        #---------- CREATING THE FOREST ---------#

        debug_functions.debugProcess('Creating the forest')

        # create the forest grid for level 1
        grid = Forest.createGrid(1)
        debug_functions.debugVariable('grid.get_grid()', grid.get_grid())

        # create the forest
        # grid_layout = None, position = None, grid = None)
        forest = Forest('3x3', [2, 2], grid)
        debug_functions.debugVariable('forest.get_grid()', forest.get_grid())


        # ---------- CREATING THE WITCH AND HER PET ---------#

        debug_functions.debugProcess('Creating the witch and her pet')

        # player customization of the witch and her pet
        print("\nLet's transform you into a witch!")
        witch_name = input('\nWhat would you like to be called as a witch?\n')
        debug_functions.debugVariable('witch_name', witch_name)

        pet_lover = input('\nWould you like to adopt a pet? (y/n)\n')
        pet_lover = pet_lover.strip().lower()
        debug_functions.debugVariable('pet_lover', pet_lover)

        if pet_lover == 'y':
            pet = None
            while pet == None:
                pet = Witch.choosePet()
        else:
            pet = None

        # creating a witch
        '''
         forest         = Forest(),
         familiar       = None,
         name           = 'Asciri',
         max_HP         = 20,
         current_HP     = 20,
         max_MP         = 0,
         current_MP     = 0,
         gold           = 30,
         pouch          = Pouch(),
         spellbook      = Spellbook(),
         action_list    = None
        '''

        witch = Witch(forest, pet, witch_name)
        debug_functions.debugVariable('witch.get_art()', witch.get_art())

        print(f'\nCongratulations! You were reborn as a witch named {witch.get_name()}!')
        print(witch.get_art())
        if witch.get_familiar() is not None:
            print(witch.adoptPet())






