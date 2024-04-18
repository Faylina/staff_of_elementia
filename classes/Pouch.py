#---------------------------------------#
#------------ POUCH CLASS --------------#
#---------------------------------------#

"""The class for the creation of a pouch for the witch"""

#---------- IMPORTS -----------#

from classes.Ingredient import Ingredient

# importing DEBUG-constant from config file
import sys
import os

# getting the name of the directory where this file is located.
current = os.path.dirname(os.path.realpath(__file__))

# Getting the parent directory name where the current directory is located.
parent = os.path.dirname(current)

# adding the parent directory to the sys.path.
sys.path.append(parent)

# import
from config import DEBUG


#---------- CLASS -----------#
class Pouch():
    """
        This class represents the characteristics of a pouch.
    """

    # ------ CONSTRUCTOR --------#
    def __init__(self, inventory=[]):
        """
        Creates a Pouch object with information about its content.

        :param __inventory:int = []      list of ingredients in the pouch
        """
        if DEBUG:
            print('DEBUG: Pouch object is being created.')

        self.set_inventory(inventory)


    #------ GETTER & SETTER --------#

    def set_inventory(self, value):
        """Creates the pouch that the witch starts off with."""
        # the pouch needs to be empty when created
        if len(value) != 0:
            print('The inventory must be empty.')
        # the witch starts the game with some basic ingredients that are added to her pouch
        else:
            # name = None, amount = None, rarity = None, effectiveness = None, effect = None
            small_mixed_herbs = Ingredient('small pouch of mixed herbs',
                                                    3,
                                                    'common',
                                                    1,
                                                    'health')
            vial_of_moonlight = Ingredient('vial of concentrated moonlight essence',
                                                                3,
                                                                'common',
                                                                1,
                                                                'magic')
            handful_of_soil = Ingredient('handful of enchanted soil from the heart of the forest',
                                         3,
                                         'common',
                                         2,
                                         'health')

            value.append(small_mixed_herbs)
            value.append(vial_of_moonlight)
            value.append(handful_of_soil)

            self.__inventory = value

    def get_inventory(self):
        """Fetches the inventory of the pouch."""
        try:
            return self.__inventory
        except AttributeError:
            print('ERROR: Failed to get inventory.')


    # ------ METHODS --------#

    def displayInventory(self) -> str:
        """Lists all ingredients in the pouch with their respective amounts."""
        current_inventory = '\nYour current inventory:'
        for item in self.get_inventory():
            current_inventory += f"\n\t{item.get_amount()}x {item.get_name()}"
        return current_inventory

    def addIngredient(self, ingredient: Ingredient) -> None:
        """Adds an ingredient to the pouch."""
        try:
            # check if the object is actually an ingredient
            if isinstance(ingredient, Ingredient):
                self.get_inventory().append(ingredient)
                return 'The item has been added to your inventory.'
            else:
                print('This is not an ingredient.')
        except AttributeError:
            print('\nERROR: Ingredient could not be added.')

    def removeIngredient(self, ingredient: Ingredient) -> None:
        """Removes an ingredient from the pouch."""
        try:
            # check if the object is actually an ingredient
            if isinstance(ingredient, Ingredient):
                self.get_inventory().remove(ingredient)
                return 'The item has been removed from your inventory.'
            else:
                print('This is not an ingredient.')
        except AttributeError:
            print('\nERROR: Ingredient could not be removed.')

