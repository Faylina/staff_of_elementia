#---------------------------------------#
#------------ CAT CLASS ----------------#
#---------------------------------------#

"""The child class of Pet for the adoption of a cat"""

#---------- IMPORTS -----------#
from classes.Pet import Pet

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
class Cat(Pet):
    """
        This child class represents the characteristics of a cat.
    """

    # ------ CONSTRUCTOR --------#
    def __init__(self, name=None, age=None, color=None, sex=None):
        """
        Creates a Cat object with information about its traits.

        :param _name    : str    = None      name of the cat
        :param _age     : int    = None      age of the cat
        :param _color   : str    = None      color of the cat's fur
        :param _sex     : str    = None      the cat's sex
        :param _hungry  : bool   = True      indicates whether the cat is hungry
        :param _pronoun : str    = None      pronoun to use for the cat
        :param __cat_art: str    = string    cat art
        """
        if DEBUG:
            print('DEBUG: Cat object is being created.')

        super().__init__(name, age, color, sex)

        self.set_art()

    # ------ GETTER & SETTER --------#

    def set_art(self) -> None:
        """Creates the image of a dog."""
        cat_art = '\n  ╱|、'
        cat_art += '\n(˚ˎ 。7'
        cat_art += '\n |、˜〵'
        cat_art += '\nじしˍ,)ノ'
        self.__cat_art = cat_art

    def get_art(self) -> str:
        """Fetches the image of a dog."""
        return self.__cat_art

    # ------ METHODS --------#

    def look(self) -> str:
        """Look at the cat."""
        your_cat = self.get_art()
        your_cat += f"\n{self.get_name()} is a {self.get_color()}, {self.get_sex()} cat"
        your_cat += f"\nand is {self.get_age()} years old."
        return your_cat

    def pet(self) -> str:
        """Pets the cat."""
        return f"{self.get_name()} rolls on {self.get_pronoun()} back, purring."

    def sneakAttack(self):
        """Deals extra damage when used against unsuspecting enemies."""
        pass