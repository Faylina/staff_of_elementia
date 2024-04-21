#---------------------------------------#
#------------ POUCH CLASS --------------#
#---------------------------------------#

"""The class for the creation of a pouch for the witch"""

#---------- IMPORTS -----------#

from classes.Ingredient import Ingredient
from debugging import debug_functions


#---------- CLASS -----------#
class Pouch:
    """
        This class represents the characteristics of a pouch.
    """

    # ------ CONSTRUCTOR --------#
    def __init__(self, inventory=None):
        """
        Creates a Pouch object with information about its contents.

        :param __inventory  :list = None      list of ingredients in the pouch
        """
        debug_functions.debugClass(self)

        self.set_inventory(inventory)


    #------ GETTER & SETTER --------#

    def set_inventory(self, value):
        """Creates the pouch that the witch starts off with."""

        empty_list = []

        if value is not None and type(value) == list:
            self.__inventory = value

        else:
            # the witch starts the game with some basic ingredients that are added to her pouch
            # name = None, amount = None, rarity = None, effectiveness = None, effect = None
            small_mixed_herbs = Ingredient( 'small pouch of mixed herbs',
                                            'common',
                                            1,
                                            'health',
                                            3)
            vial_of_moonlight = Ingredient( 'vial of concentrated moonlight essence',
                                            'common',
                                            1,
                                            'magic',
                                            3)
            handful_of_soil = Ingredient('handful of enchanted soil from the heart of the forest',
                                         'common',
                                         2,
                                         'health',
                                         3)

            empty_list.append(small_mixed_herbs)
            empty_list.append(vial_of_moonlight)
            empty_list.append(handful_of_soil)

            self.__inventory = empty_list

    def get_inventory(self):
        """Fetches the inventory of the pouch."""
        try:
            return self.__inventory
        except AttributeError:
            print('ERROR: Failed to get inventory.')


    # ------ METHODS --------#

    def displayInventory(self) -> str:
        """Lists all ingredients in the pouch with their respective amounts."""
        debug_functions.debugMethod(self)
        current_inventory = '\nYour current inventory:'
        for item in self.get_inventory():
            current_inventory += f"\n\t{item.get_amount()}x {item.get_name()}"
        return current_inventory

    def addIngredient(self, ingredient: Ingredient) -> str:
        """Adds an ingredient to the pouch."""
        debug_functions.debugMethod(self)
        try:
            # check if the object is actually an ingredient
            if isinstance(ingredient, Ingredient):
                self.get_inventory().append(ingredient)
                return 'The item has been added to your inventory.'
            else:
                print('This is not an ingredient.')
        except AttributeError:
            print('\nERROR: Ingredient could not be added.')

    def removeIngredient(self, ingredient: Ingredient) -> str:
        """Removes an ingredient from the pouch."""
        debug_functions.debugMethod(self)
        try:
            # check if the object is actually an ingredient
            if isinstance(ingredient, Ingredient):
                self.get_inventory().remove(ingredient)
                return 'The item has been removed from your inventory.'
            else:
                print('This is not an ingredient.')
        except AttributeError:
            print('\nERROR: Ingredient could not be removed.')

