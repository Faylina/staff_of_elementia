#---------------------------------------#
#--------- STAFF OF ELEMENTIA ----------#
#-------------- GAMEPLAY ---------------#
#---------------------------------------#

"""This is the main gameplay."""

#---------- IMPORTS -----------#

from debugging      import debug_functions
from texts          import gameplay_snippets
from classes.Game   import Game
from classes.Player import Player
from classes.Forest import Forest

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
