#---------------------------------------#
#---------- SPELLBOOK CLASS ------------#
#---------------------------------------#

"""The class for the creation of a spellbook for the witch"""

#---------- IMPORTS -----------#

from classes.Spell import Spell

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
class Spellbook():
    """
        This class represents the characteristics of a spellbook.
    """

    # ------ CONSTRUCTOR --------#
    def __init__(self, arsenal=[]):
        """
        Creates a Spellbook object with information about its contents.

        :param __arsenal    : list = []      list of spells in the spellbook
        """
        if DEBUG:
            print('DEBUG: Spellbook object is being created.')

        self.set_arsenal(arsenal)


    #------ GETTER & SETTER --------#

    def set_arsenal(self, value):
        """Creates the list of spells that the witch starts off with."""
        # the arsenal needs to be empty when created
        if len(value) != 0:
            print('The inventory must be empty.')
        # the witch starts the game with some basic ingredients that are added to her pouch
        else:
            self.__arsenal = value

    def get_arsenal(self):
        """Fetches the arsenal of the spellbook."""
        try:
            return self.__arsenal
        except AttributeError:
            print('ERROR: Failed to get arsenal.')


    # ------ METHODS --------#

    def displayArsenal(self) -> str:
        """Lists all spells in the spellbook."""
        current_arsenal = '\nYour current arsenal:'
        for spell in self.get_arsenal():
            current_arsenal += f"\n\t{spell.get_name()} (Element: {spell.get_element()})"
        return current_arsenal

    def addSpell(self, spell: Spell) -> None:
        """Adds a spell to the spellbook."""
        try:
            # check if the object is actually a spell
            if isinstance(spell, Spell):
                self.get_arsenal().append(spell)
                return 'The spell has been added to your arsenal.'
            else:
                print('This is not a spell.')
        except AttributeError:
            print('\nERROR: Spell could not be added.')