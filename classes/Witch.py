#---------------------------------------#
#------------ WITCH CLASS --------------#
#---------------------------------------#

"""The class for the creation of a witch"""

#---------- IMPORTS -----------#

from debugging          import debug_functions
from classes.Pouch      import Pouch
from classes.Spellbook  import Spellbook
from classes.Cat        import Cat
from classes.Dog        import Dog
from classes.Ingredient import Ingredient
from classes.Spell      import Spell
from classes.Potion      import Potion


#---------- CLASS -----------#
class Witch:
    """
        This class represents the characteristics of a witch.
    """

    # ------ CONSTRUCTOR --------#
    def __init__(self,
                 familiar       = None,
                 name           = 'Asciri',
                 max_HP         = 20,
                 current_HP     = 20,
                 max_MP         = 0,
                 current_MP     = 0,
                 gold           = 30,
                 pouch          = Pouch(),
                 spellbook      = Spellbook(),
                 action_list    = None
                 ):
        """
        Creates a Witch object with information about her traits and possessions.

        :param __familiar    : Cat or Dog or str    = None         pet of the witch
        :param __name        : str                  = 'Asciri'     name of the witch
        :param __max_HP      : int                  = 20           maximum health points of the witch
        :param __current_HP  : int                  = 20           current health point of the witch
        :param __max_MP      : int                   = 0            maximum mana points of the witch
        :param __current_MP  : int                  = 0            current mana point of the witch
        :param __gold        : int                  = 30           gold in possession of the witch
        :param __pouch       : Pouch                = Pouch()      inventory of the witch
        :param __spellbook   : Spellbook            = Spellbook()  spellbook of the witch
        :param __action_list : list                 = None           list of currently available actions
        :param __witch_art   : str                  = string       image of the witch
        """
        debug_functions.debugClass(self)

        if familiar != '' and familiar is not None:
            self.set_familiar(familiar)
        if name != '' and name is not None:
            self.set_name(name)
        if max_HP != '' and max_HP is not None:
            self.set_max_HP(max_HP)
        if current_HP != '' and current_HP is not None:
            self.set_current_HP(current_HP)
        if max_MP != '' and max_MP is not None:
            self.set_max_MP(max_MP)
        if current_MP != '' and current_MP is not None:
            self.set_current_MP(current_MP)
        if gold != '' and gold is not None:
            self.set_gold(gold)
        if pouch != '' and pouch is not None:
            self.set_pouch(pouch)
        if spellbook != '' and spellbook is not None:
            self.set_spellbook(spellbook)

        self.set_action_list(action_list)
        self.set_art()

    # ------ GETTER & SETTER --------#

    # familiar
    def set_familiar(self, value: Cat or Dog or None) -> None:
        """Allows the witch to adopt a dog or cat if she chooses to."""

        if type(value) == Cat or type(value) == Dog or value is None:
            self.__familiar = value
        else:
            print('This is not a valid familiar.')

    def get_familiar(self) -> None or Cat or Dog:
        """Fetches the pet of the witch."""
        try:
            return self.__familiar
        except AttributeError:
            print('ERROR: Failed to get pet.')


    # name
    def set_name(self, value: str) -> None:
        """Defines the name of the witch and formats it."""
        try:
            value = value.strip().title()
            self.__name = value
        except AttributeError:
            print('This is not a valid name.')

    def get_name(self) -> None or str:
        """Fetches the formatted name of the witch."""
        try:
            return self.__name
        except AttributeError:
            print("ERROR: Failed to get the witch's name.")


    # max_HP
    def set_max_HP(self, value: int or str) -> None:
        """Defines the maximum amount of HP the witch can have at her disposal."""
        try:
            value = int(value)
        except ValueError:
            print('The format of the maximum HP must be an integer.')
        else:
            if value < 20:
                print('This is not a valid max HP amount.')
            else:
                self.__max_HP = value

    def get_max_HP(self) -> None or int:
        """Fetches the maximum HP of the witch."""
        try:
            return self.__max_HP
        except AttributeError:
            print('ERROR: Failed to get max HP.')


    # current_HP
    def set_current_HP(self, value: int or str) -> None:
        """Defines the current amount of HP of the witch."""
        try:
            value = int(value)
        except ValueError:
            print('The format of the current HP must be an integer.')
        else:
            if value < 0:
                print('This is not a valid current HP amount.')
            else:
                self.__current_HP = value

    def get_current_HP(self) -> None or int:
        """Fetches the current HP of the witch."""
        try:
            return self.__current_HP
        except AttributeError:
            print('ERROR: Failed to get current HP.')


    # max_MP
    def set_max_MP(self, value: int or str) -> None:
        """Defines the maximum amount of MP the witch can have at her disposal."""
        try:
            value = int(value)
        except ValueError:
            print('The format of the maximum MP must be an integer.')
        else:
            if value < 0:
                print('This is not a valid max MP amount.')
            else:
                self.__max_MP = value

    def get_max_MP(self) -> None or int:
        """Fetches the maximum MP of the witch."""
        try:
            return self.__max_MP
        except AttributeError:
            print('ERROR: Failed to get max MP.')


    # current_MP
    def set_current_MP(self, value: int or str) -> None:
        """Defines the current amount of MP of the witch."""
        try:
            value = int(value)
        except ValueError:
            print('The format of the current MP must be an integer.')
        else:
            if value < 0:
                print('This is not a valid current MP amount.')
            else:
                self.__current_MP = value

    def get_current_MP(self) -> None or int:
        """Fetches the current MP of the witch."""
        try:
            return self.__current_MP
        except AttributeError:
            print('ERROR: Failed to get current MP.')


    # gold
    def set_gold(self, value: int or str) -> None:
        """Defines the current amount of gold of the witch."""
        try:
            value = int(value)
        except ValueError:
            print('The format of gold must be an integer.')
        else:
            if value < 0:
                print('This is not a valid gold amount.')
            else:
                self.__gold = value

    def get_gold(self) -> None or int:
        """Fetches the current amount of gold of the witch."""
        try:
            return self.__gold
        except AttributeError:
            print('ERROR: Failed to get gold.')


    # pouch
    def set_pouch(self, value: Pouch) -> None:

        if isinstance(value, Pouch):
            self.__pouch = value
        else:
            print('This is not a pouch.')

    def get_pouch(self) -> Pouch:
        """Fetches the pouch of the witch."""
        try:
            return self.__pouch
        except AttributeError:
            print('ERROR: Failed to get the pouch.')


    # spellbook
    def set_spellbook(self, value: Spellbook) -> None:

        if isinstance(value, Spellbook):
            self.__spellbook = value
        else:
            print('This is not a spellbook.')

    def get_spellbook(self) -> Spellbook:
        """Fetches the spellbook of the witch."""
        try:
            return self.__spellbook
        except AttributeError:
            print('ERROR: Failed to get the spellbook.')


    # action_list
    def set_action_list(self, value):
        """Creates the list of action that the witch can perform."""

        if value is not None and type(value) == list:
            self.__action_list = value
        # the witch starts the game with some basic actions that are added to her action list
        else:

            initial_action_list = ['List actions you can perform',
                                   'Check your inventory',
                                   'Read your spellbook',
                                   'Brew a potion',
                                   'Drink a potion'
                                   'Cast a spell',
                                   'Walk through the forest',
                                   'Search for ingredient',
                                   'Flee from opponent',
                                   'Add ingredient to your pouch',
                                   'Remove ingredient from your pouch',
                                   'Add spell to your spellbook',
                                   'Call your pet',
                                   'Look at your pet',
                                   'Pet your pet',
                                   'Play with your pet',
                                   'Feed your pet',
                                   'Check if your pet is hungry'
                                   ]

            self.__action_list = initial_action_list

    def get_action_list(self):
        """Fetches the list of actions that the witch is able to perform."""
        try:
            return self.__action_list
        except AttributeError:
            print('ERROR: Failed to get action list.')


    # witch_art
    def set_art(self) -> None:
        """Creates the image of a witch."""
        witch_art =  '\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠'
        witch_art += '\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⢠⣿'
        witch_art += '\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⡆'
        witch_art += '\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⣼⣿⡇'
        witch_art += '\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⢣⣿⣿⡇'
        witch_art += '\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⡼⠏⣼⣿⣿⣿'
        witch_art += '\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⣿⣿⣿⢹⣿⢻⣿⣿⣿⣦⣄'
        witch_art += '\n⠀⣠⣤⣄⠀⠀⠀⠀⠀⠀⠀⣸⠟⠛⠿⠶⢾⣿⣿⣿⣿⡿⠗'
        witch_art += '\n⠘⢿⣿⣿⣿⣦⡀⠀⠀⠀⢀⣿⠐⡀⠀⠰⠘⣿⣿⣿⣿⡄'
        witch_art += '\n⠀⠀⠈⠉⠛⠻⠿⣶⣶⠄⢸⣿⣧⣄⣀⠀⢀⣿⣿⣿⣿⡇'
        witch_art += '\n⠀⠀⠀⠀⠀⠀⠀⠈⠁⠉⢞⣿⣿⣿⣧⣾⣶⣿⣿⣿⠿⠟'
        witch_art += '\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⣿⣿⣿⣿⣿⡿⠀'
        witch_art += '\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣷⣼⢄⡀'
        witch_art += '\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⠧⠈⠁'
        witch_art += '\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠈⠉'
        self.__witch_art = witch_art

    def get_art(self) -> str:
        """Fetches the image of a witch."""
        return self.__witch_art


    # ------ METHODS --------#

    def checkInventory(self) -> str:
        """Lists all ingredients in the pouch with their respective amounts."""
        debug_functions.debugMethod(self)
        return self.get_pouch().displayInventory()

    def readSpellbook(self) -> str:
        """Lists all spells in the spellbook."""
        debug_functions.debugMethod(self)
        return self.get_spellbook().displayArsenal()

    def listActions(self) -> str:
        """Lists all actions that the witch can perform."""
        debug_functions.debugMethod(self)

        current_action = '\nYou can do this:'
        for item in self.get_action_list():
            current_action += f"\n\t{item}"

        return current_action

    def addItemToPouch(self, item: Ingredient or Potion) -> str:
        """Adds an item to the pouch."""
        debug_functions.debugMethod(self)
        return self.get_pouch().addItem(item)

    def removeItemFromPouch(self, ingredient: Ingredient, amount: int) -> str:
        """Removes an item from the pouch."""
        debug_functions.debugMethod(self)
        return self.get_pouch().removeItem(ingredient, amount)

    def learnSpell(self, spell: Spell) -> str:
        """Adds a spell to the spellbook."""
        debug_functions.debugMethod(self)
        return self.get_spellbook().addSpell(spell)

    def adoptPet(self) -> str:
        """Congratulates the player for adopting their new pet."""
        debug_functions.debugMethod(self)
        return self.get_familiar().adoptPet()

    def callPet(self) -> str:
        """Calls your pet."""
        debug_functions.debugMethod(self)
        return self.get_familiar().call()

    def lookAtPet(self) -> str:
        """Look at your pet."""
        debug_functions.debugMethod(self)
        return self.get_familiar().look()

    def petPet(self) -> str:
        """Pet your pet."""
        debug_functions.debugMethod(self)
        return self.get_familiar().pet()

    def playWithPet(self) -> str:
        """Play with your pet."""
        debug_functions.debugMethod(self)
        return self.get_familiar().play()

    def feedPet(self) -> str:
        """Feed your pet."""
        debug_functions.debugMethod(self)
        return self.get_familiar().feed()

    def checkPetsHunger(self) -> str:
        """Checks if your pet is hungry."""
        debug_functions.debugMethod(self)
        return self.get_familiar().checkIfHungry()

    def brewPotion(self, ingredient1: Ingredient, ingredient2: Ingredient) -> str:
        debug_functions.debugMethod(self)

        # healing ingredients
        healing_ingredient1 = 'Small Pouch Of Mixed Herbs'

        # restoring ingredients
        restoring_ingredient1 = 'Vial Of Concentrated Moonlight Essence'

        # ingredients for learning spells
        spell_ingredient1 = 'Lumina Fungus'

        # base ingredients
        base_ingredient = 'Handful Of Enchanted Soil From The Heart Of The Forest'

        if (
                (ingredient1.get_name() == healing_ingredient1
                 and ingredient2.get_name() == base_ingredient)
                or
                (ingredient1.get_name() == base_ingredient
                 and ingredient2.get_name() == healing_ingredient1)
        ):
            # name = None, description = None, effect = None, effectiveness = None, element = None, amount = 1
            new_potion = Potion('Greenwood Healer',
                                'A thick, dark green liquid with small flecks of dirt suspended in it. '
                                'This potion is said to contain the life force of the enchanted forest itself, '
                                'granting the consumer a surge of energy and vitality.',
                                'healing',
                                ingredient1.get_effectiveness() + ingredient2.get_effectiveness(),
                                'earth'
                                )

            return self.addItemToPouch(new_potion)

        elif (
                (ingredient1.get_name() == restoring_ingredient1
                 and ingredient2.get_name() == base_ingredient)
                or
                (ingredient1.get_name() == base_ingredient
                 and ingredient2.get_name() == restoring_ingredient1)
        ):
            # name = None, description = None, effect = None, effectiveness = None, element = None, amount = 1
            new_potion = Potion('Lunar Restoration',
                                'This potion glows softly with a pale blue light, '
                                'and carries a faint scent of citrus. '
                                'When consumed, it immediately restores a portion of your mana.',
                                'restoring',
                                ingredient1.get_effectiveness() + ingredient2.get_effectiveness(),
                                'air'
                                )

            self.addItemToPouch(new_potion)

        elif (
                (ingredient1.get_name() == spell_ingredient1
                 and ingredient2.get_name() == base_ingredient)
                or
                (ingredient1.get_name() == base_ingredient
                 and ingredient2.get_name() == spell_ingredient1)
        ):
            # name=None, description=None, element=None, effect=None, effectiveness=None, cost=None
            new_spell = Spell('Elemental Infusion',
                              'This potion '
                              'is said to imbue the drinker with the power of a thousand suns. '
                              'Its golden, shimmering liquid appears to dance with the promise of magical knowledge. '
                              'Consuming it grants the drinker the ability to learn a devastating spell '
                              'to defeat their enemies.',
                              'air',
                              'offensive',
                              ingredient1.get_effectiveness() + ingredient2.get_effectiveness(),
                              5
                              )

            self.addItemToPouch(new_spell)

    def drinkPotion(self, potion: Potion) -> None or str:
        """Drink a potion."""
        debug_functions.debugMethod(self)

        if isinstance(potion, Potion):
            # TODO: effect

            return self.get_pouch().removeItem(potion)
        else:
            return 'This is not a potion.'

    def castSpell(self):
        debug_functions.debugMethod(self)

    def walk(self):
        debug_functions.debugMethod(self)

    def search(self):
        debug_functions.debugMethod(self)

    def flee(self):
        debug_functions.debugMethod(self)