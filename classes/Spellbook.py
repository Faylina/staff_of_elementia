#---------------------------------------#
#---------- SPELLBOOK CLASS ------------#
#---------------------------------------#

"""The class for the creation of a spellbook for the witch"""

#---------- IMPORTS -----------#

from classes.Spell import Spell
from debugging import debug_functions


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
        debug_functions.debugClass(self)

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
        debug_functions.debugMethod(self)
        current_arsenal = '\nYour current arsenal:'
        for spell in self.get_arsenal():
            current_arsenal += f"\n\t{spell.get_name()} (Element: {spell.get_element()})"
        return current_arsenal

    def addSpell(self, spell: Spell) -> None:
        """Adds a spell to the spellbook."""
        debug_functions.debugMethod(self)
        try:
            # check if the object is actually a spell
            if isinstance(spell, Spell):
                self.get_arsenal().append(spell)
                return 'The spell has been added to your arsenal.'
            else:
                print('This is not a spell.')
        except AttributeError:
            print('\nERROR: Spell could not be added.')