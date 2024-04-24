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


        # ---------- START THE GAME ---------#

        # level=1, end_of_level=False, game_over=True
        game = Game()
        game.startNewGame()

        forest_confirmation = input('\nWould you like to enter the forest now? (y/n)\n')

        if forest_confirmation != 'y':
            print(f"Farewell, {player_name}. Come back when you're ready to tackle this challenge.")
        else:

            # ---------- ENTERING THE FOREST ---------#

            # let witch enter the start point
            print(witch.get_forest().enterCell())

            # ---------- START INTERACTION LOOP ---------#
            while not game.get_game_over():

                see_options = input('\nPress Enter to see your current options.')

                # ---------- PRESENT OPTIONS ---------#

                options_pet     = gameplay_snippets.input_list_with_pet
                options_no_pet  = gameplay_snippets.input_list_no_pet
                actions         = gameplay_snippets.output_list_with_pet

                # print prompt depending on whether the witch has a pet
                if witch.get_familiar() is None:
                    print('\nThis is what you could do now:')
                    for string in options_no_pet:
                        print(string)
                    action = input('\nChoose wisely: ')
                    action = action.strip().lower()
                else:
                    print('\nThis is what you could do now:')
                    for string in options_pet:
                        print(string)
                    action = input('\nChoose wisely:\n')
                    action = action.strip().lower()

                # ---------- EXECUTE ACTION ---------#

                # get the chosen method and its arguments from the actions list
                args = None
                method = actions[action]
                if type(method) == tuple:
                    method_name, args = method
                else:
                    method_name = method

                # create a reference of the method
                method_reference = lambda method: getattr(witch, method)
                method = method_reference(method_name)

                # call the method
                if args is None:
                    print(method())
                else:
                    print(method(args))






