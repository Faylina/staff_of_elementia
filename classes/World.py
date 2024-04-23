#---------------------------------------#
#------------ WORLD CLASS --------------#
#---------------------------------------#

"""The class for the creation of the world."""

#---------- IMPORTS -----------#
from debugging import debug_functions


#---------- CLASS -----------#
class World:
    """
        This class represents the forest of the witch.
    """

    #------ CONSTRUCTOR --------#
    def __init__(self, grid_layout=None, position=None, grid=None):
        """
        Creates an Ingredient object with information about its amount, rarity and effectiveness.

        :param __grid_layout    :str    = None      grid layout of the world (e.g. 3x3)
        :param __position       :list   = None      the current coordinates if the witch (e.g. [2,2])
        :param __grid           :dict   = None      a collection of all Cells in the grid of this world
        """
        debug_functions.debugClass(self)