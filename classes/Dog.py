#---------------------------------------#
#------------ DOG CLASS ----------------#
#---------------------------------------#

"""The child class of Pet for the adoption of a dog"""

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
class Dog(Pet):
    """
        This child class represents the characteristics of a dog.
    """

    # ------ CONSTRUCTOR --------#
    def __init__(self, name=None, age=None, color=None, sex=None):
        """
        Creates a Dog object with information about its traits.

        :param _name    : str    = None      name of the dog
        :param _age     : int    = None      age of the dog
        :param _color   : str    = None      color of the dog's fur
        :param _sex     : str    = None      the dog's sex
        :param _hungry  : bool   = True      indicates whether the dog is hungry
        :param _pronoun : str    = None      pronoun to use for the dog
        :param __dog_art: str    = string    dog art
        """
        if DEBUG:
            print('DEBUG: Dog object is being created.')

        super().__init__(name, age, color, sex)

        self.set_art()

    # ------ GETTER & SETTER --------#
    def set_art(self) -> None:
        """Creates the image of a dog."""
        dog_art = '\n  .-"-.'
        dog_art += '\n /|6 6|\\'
        dog_art += '\n{/(_0_)\}'
        dog_art += '\n _/ ^ \_'
        dog_art += "\n(/ /^\ \)-'"
        dog_art += '\n ""   ""'
        self.__dog_art = dog_art

    def get_art(self) -> str:
        """Fetches the image of a dog."""
        return self.__dog_art

    # ------ METHODS --------#

    def look(self) -> str:
        """Look at the dog."""
        your_dog = self.get_art()
        your_dog += f"\n{self.get_name()} is a {self.get_color()}, {self.get_sex()} dog"
        your_dog += f"\nand is {self.get_age()} years old."
        return your_dog

    def givePaw(self) -> str:
        """Dog give paw."""
        return f"{self.get_name()} puts {self.get_pronoun()} paw in your hand, looking cheerful."

    def fetchItem(self):
        """
            Allows the player to retrieve distant objects
            without having to physically go and grab them.
        """
        pass