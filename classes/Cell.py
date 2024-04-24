#---------------------------------------#
#------------ CELL CLASS ---------------#
#---------------------------------------#

"""The class for the creation of a cell in the forest's grid."""

#---------- IMPORTS -----------#
from debugging import debug_functions


#---------- CLASS -----------#
class Cell:
    """
        This class represents a cell in a forest's grid.
    """

    #------ CONSTRUCTOR --------#
    def __init__(self, coordinates=None, level=None, content=None, occupied=False, env_descriptions=None):
        """
        Creates a Cell object with information about its coordinates, level, content, whether the
         witch is currently there and a list of descriptions of all cell's environments.

        :param __coordinates      :tuple                          = None    The coordinates of the cell on the grid
        :param __level            :int                            = None    level of the world
        :param __content          :Ingredient or Enemy or None    = None    Content of the Cell
                                                                            (ingredient, enemy, scenery)
        :param __occupied         :bool                           = False   True if the witch is in this Cell
        :param __env_descriptions :dict                           = None    List of all description of the environment
        """
        debug_functions.debugClass(self)

        if coordinates != '' and coordinates is not None:
            self.set_coordinates(coordinates)
        if level != '' and level is not None:
            self.set_level(level)
        if content != '' and content is not None:
            self.set_content(content)
        if occupied != '' and occupied is not None:
            self.set_occupied(occupied)

        self.set_env_descriptions(env_descriptions)

    # ------ GETTER & SETTER --------#

    # coordinates
    def set_coordinates(self, value: tuple) -> None:
        """Defines the coordinates of the cell on the grid."""
        if type(value) is tuple:
            if type(value[0]) == int and type(value[1]) == int:
                self.__coordinates = value
            else:
                print('Those are not valid coordinates for a cell.')
        else:
            print('Those are not valid coordinates for a cell.')

    def get_coordinates(self) -> None or tuple:
        """Fetches the coordinates of the cell."""
        try:
            return self.__coordinates
        except AttributeError:
            print('ERROR: Failed to get cell coordinates.')


    # level
    def set_level(self, value: int or str) -> None:
        """Defines the world level of the cell."""
        try:
            value = int(value)
        except ValueError:
            print('The format of the cell level must be an integer.')
        else:
            if value < 1:
                print('This is not a valid cell level.')
            else:
                self.__level = value

    def get_level(self) -> None or int:
        """Fetches the world level of the cell."""
        try:
            return self.__level
        except AttributeError:
            print('ERROR: Failed to get cell level.')


    # content
    def set_content(self, value: str) -> None:
        """Defines what the witch will encounter in the cell."""
        value = value.strip().lower()
        if value != 'ingredient' and value != 'enemy' and value != 'scenery':
            print('This is not a valid content for the cell.')
        else:
            self.__content = value

    def get_content(self) -> None or str:
        """Fetches the content of the cell."""
        try:
            return self.__content
        except AttributeError:
            print('ERROR: Failed to get content of the cell.')


    # occupied
    def set_occupied(self, value: bool) -> None:
        """Defines whether the witch is in this cell."""
        self.__occupied = value

    def get_occupied(self) -> None or bool:
        """Indicates whether the witch is in the cell."""
        try:
            return self.__occupied
        except AttributeError:
            print("ERROR: Failed to get cell's occupied status.")


    # environment descriptions
    def set_env_descriptions(self, value) -> None:
        """Creates a list of possible descriptions for a cell's environment."""

        if value is not None and type(value) is dict:
            self.__env_descriptions = value
        else:
            level1_descriptions = {'1x1': 'You emerge into a sunlit glade, its grassy expanse shimmering with dew.\n'
                                          'In the center of the glade stands an ancient oak tree,\n'
                                          'its branches stretching towards the heavens like the arms of a wise old man.\n'
                                          'Beneath the oak tree, a family of rabbits huddles together,\n'
                                          'their soft fur glowing in the morning light.\n'
                                          'The glade is alive with the songs of birds and the buzzing of insects,\n'
                                          'and you feel a sense of peace and tranquility wash over you.',
                                   '1x2': "You encounter a dense thicket of brambles.\n"
                                          "The brambles twist and writhe,\n"
                                          "forming a maze-like barrier that blocks your path.\n"
                                          "The air is thick with the scent of ripe blackberries,\n"
                                          "tempting you to push through the tangled mess.\n"
                                          "However, the brambles are guarded by a territorial badger,\n"
                                          "its sharp claws and powerful jaws ready to defend its territory.\n"
                                          "You must carefully navigate the brambles, avoiding the badger's wrath,\n"
                                          "to discover what lies beyond.",
                                   '1x3': "You find a picturesque waterfall,\n"
                                          "its roar echoing through the tranquil forest.\n"
                                          "The waterfall is a magnificent sight,\n"
                                          "cascading down the rocky slope in a series of steps,\n"
                                          "each one creating a misty veil that hangs in the air.\n"
                                          "At the base of the falls, the water forms a small pool,\n"
                                          "crystal clear and reflecting the verdant surroundings.\n"
                                          "The sound of the water crashing against the rocks fills the air,\n"
                                          "harmonizing with the gentle rustle of the nearby trees.\n"
                                          "The waterfall seems to embody the very essence of nature,\n"
                                          "a testament to the beauty and power of the natural world.",
                                   '2x1': 'You discover a towering hillside covered in a blanket of wildflowers.\n'
                                          'The flowers dance in the wind,\n'
                                          'their vibrant petals painting the hillside with a rainbow of colors.\n'
                                          'Atop the hill, a wise old owl perches atop a weathered stone monument,\n'
                                          'its piercing gaze surveying the surrounding forest.\n'
                                          'The owl speaks in a haunting melody,\n'
                                          'sharing ancient wisdom and cryptic prophecies\n'
                                          'with any who dare to seek it out.',
                                   '2x2': 'You see a clearing in the enchanted forest.\n'
                                          'The sunlight filters through the dense canopy,\n'
                                          'illuminating the moss-covered stones and the vibrant leaves of the trees.\n'
                                          'In the center of the clearing, there is a majestic oak tree,\n'
                                          'its trunk thick and gnarled, its branches reaching towards the sky.\n'
                                          'As you look closer, you see that the oak tree\n'
                                          'is home to a family of squirrels,\n'
                                          'their fur fluffy and their eyes bright with curiosity.',
                                   '2x3': 'You come across a babbling brook that meanders its way through the forest.\n'
                                          'The water sparkles in the dappled light filtering through the trees,\n'
                                          'reflecting the colors of the surrounding foliage.\n'
                                          'The air is fresh and clean, carrying with it the scent of wildflowers\n'
                                          "growing along the brook's edges.",
                                   '3x1': 'You discover a hidden valley nestled within the forest.\n'
                                          'The valley is shrouded in mystery and surrounded by an ethereal fog. \n'
                                          'The air is charged with magic,\n'
                                          'and the whispers of ancient spirits fill the space.\n'
                                          'At the heart of the valley lies a mystical lake,\n'
                                          'its surface reflecting the stars in the night sky.\n'
                                          'The water glimmers with iridescent hues,\n'
                                          'inviting you to immerse yourself in its enchanting waters.',
                                   '3x2': 'Here lies an enigmatic forest of towering trees\n'
                                          'whose branches intertwine overhead, creating a labyrinth of shadows.\n'
                                          'The trees whisper secrets and riddles,\n'
                                          'challenging you to solve them in exchange for passage.\n'
                                          'Amidst the tangled roots, a serpent slithers,\n'
                                          'its scales shimmering with iridescent hues.\n'
                                          'If you are clever enough to answer the riddles,\n'
                                          'the serpent will lead you to a hidden portal,\n'
                                          'transporting you to a realm beyond you wildest dreams.',
                                   '3x3': "There is a towering cliff face that looks out over a vast, uncharted plain.\n"
                                          "The cliff face is home to a colony of peregrine falcons,\n"
                                          "their feathers a brilliant white contrasting with the cool blue of the sky.\n"
                                          "The falcons are protective of their territory,\n"
                                          "and their wingspan casts a shadow over your path.\n"
                                          "But those with a keen eye may notice something peculiar\n"
                                          "in the falcons' flight patterns."
                                   }
            self.__env_descriptions = level1_descriptions

    def get_env_descriptions(self) -> dict:
        """Fetches the list of the cell environment descriptions."""
        try:
            return self.__env_descriptions
        except AttributeError:
            print('ERROR: Failed to get environment descriptions.')

    # ------ METHODS --------#

    def enter(self) -> None:
        """Marks the cell as occupied when the witch enters it."""
        debug_functions.debugMethod(self)
        self.set_occupied(True)

    def leave(self) -> None:
        """Marks the cell as not occupied when the witch leaves it."""
        debug_functions.debugMethod(self)
        self.set_occupied(False)

    def describeEnvironment(self) -> str:
        """Describes the environment of the current cell."""
        debug_functions.debugMethod(self)

        current_coordinates = f"{self.get_coordinates()[0]}x{self.get_coordinates()[1]}"

        # pick the right description from the list according to the coordinates of this cell
        if current_coordinates in self.get_env_descriptions():
            return self.get_env_descriptions()[current_coordinates]
        else:
            return 'There is no description for this cell.'
