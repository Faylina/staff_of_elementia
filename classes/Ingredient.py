#---------------------------------------#
#---------- INGREDIENT CLASS -----------#
#---------------------------------------#

"""The class for the creation of all ingredients"""

#---------- IMPORTS -----------#

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
class Ingredient():
    """
        This class represents the characteristics of all ingredients.
    """

    #------ CONSTRUCTOR --------#
    def __init__(self, name=None, amount=None, rarity=None, effectiveness=None, effect=None):
        """
        Creates an Ingredient object with information about its amount, rarity and effectiveness.

        :param amount:int           = None      amount of the same ingredient
        :param rarity:str           = None      the rarity of the ingredient in the forest
        :param effectiveness:int    = None      the effectiveness of this ingredient in potions
        """
        if DEBUG:
            print('DEBUG: Ingredient object is being created.')

        if name != '' and name is not None:
            self.set_name(name)
        if amount != '' and amount is not None:
            self.set_amount(amount)
        if rarity != '' and rarity is not None:
            self.set_rarity(rarity)
        if effectiveness != '' and effectiveness is not None:
            self.set_effectiveness(effectiveness)
        if effect != '' and effect is not None:
            self.set_effect(effect)


    # ------ GETTER & SETTER --------#

    # name
    def set_name(self, value: str) -> None:
        """Defines the name of the ingredient and formats it."""
        value = value.strip().title()
        self.__name = value

    def get_name(self) -> None or str:
        """Fetches the formatted name of the ingredient."""
        try:
            return self.__name
        except AttributeError:
            print('ERROR: Failed to get ingredient name.')

    # amount
    def set_amount(self, value: int or str) -> None:
        """Defines the amount of the ingredient."""
        try:
            value = int(value)
        except TypeError:
            print('The data format of the ingredient amount is not an integer.')
        else:
            if value < 0:
                print('This is not a valid ingredient amount.')
            else:
                self.__amount = value

    def get_amount(self) -> None or int:
        """Fetches the amount of the ingredient."""
        try:
            return self.__amount
        except AttributeError:
            print('ERROR: Failed to get amount.')

    # rarity
    def set_rarity(self, value: str) -> None:
        """Defines the rarity of the ingredient."""
        value = value.strip().lower()
        if value != 'common' and value != 'rare' and value != 'legendary':
            print('This is not a valid rarity indicator for the ingredient.')
        else:
            self.__rarity = value

    def get_rarity(self) -> None or str:
        """Fetches the rarity of the ingredient."""
        try:
            return self.__rarity
        except AttributeError:
            print('ERROR: Failed to get rarity.')

    # effectiveness
    def set_effectiveness(self, value: int or str) -> None:
        """Defines the effectiveness of the ingredient."""
        try:
            value = int(value)
        except TypeError:
            print('The data format of the ingredient effectiveness is not an integer.')
        else:
            if value < 1 or value > 10:
                print('This is not a valid ingredient effectiveness.')
            else:
                self.__effectiveness = value

    def get_effectiveness(self) -> None or int:
        """Fetches the effectiveness of the ingredient."""
        try:
            return self.__effectiveness
        except AttributeError:
            print('ERROR: Failed to get effectiveness.')

    # effect
    def set_effect(self, value: str) -> None:
        """Defines the effect of the ingredient."""
        value = value.strip().lower()
        if value != 'health' and value != 'magic':
            print('This is not a valid effect for the ingredient.')
        else:
            self.__effect = value

    def get_effect(self) -> None or str:
        """Fetches the effect of the ingredient."""
        try:
            return self.__effect
        except AttributeError:
            print('ERROR: Failed to get effect.')


    # ------ METHODS --------#

    def checkEffect(self):
        """Returns which effect the ingredient has and how effective this effect is."""
        try:
            if self.get_effectiveness() is not None and self.get_effect() is not None:
                return (f"The ingredient {self.get_name()} has a {self.get_effect()}-effect "
                        f"with an effectiveness of {self.get_effectiveness()}.")
            else:
                print('ERROR: Failed to check effect.')
        except AttributeError:
            print('ERROR: Failed to check effect.')



