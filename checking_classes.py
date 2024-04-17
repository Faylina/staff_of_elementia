#---------------------------------------#
#---------- TESTING CLASSES ------------#
#---------------------------------------#

#---------- TESTING INGREDIENT ---------#
from classes.Ingredient import Ingredient

print('\n>>> Testing empty Ingredient object:')

ingredient1 = Ingredient()

print('\nEmpty Ingredient object:',
      '\nAmount:',         ingredient1.get_amount(),
      '\nRarity:',         ingredient1.get_rarity(),
      '\nEffectiveness:',  ingredient1.get_effectiveness(),
      '\nEffect:',         ingredient1.get_effect())


print('\n>>> Testing filled Ingredient object:')

# amount=None, rarity=None, effectiveness=None, effect=None
ingredient2 = Ingredient(2, 'Common', 3, 'health')

print('\nFilled Ingredient object:',
      '\nAmount:',        ingredient2.get_amount(),
      '\nRarity:',        ingredient2.get_rarity(),
      '\nEffectiveness:', ingredient2.get_effectiveness(),
      '\nEffect:',        ingredient2.get_effect())


print('\n>>> Testing faulty Ingredient object:')

# amount=None, rarity=None, effectiveness=None, effect=None
ingredient3 = Ingredient(-1, 'Commo', 12, 'stamina')

print('\nFaulty Ingredient object:',
      '\nAmount',         ingredient3.get_amount(),
      '\nRarity',         ingredient3.get_rarity(),
      '\nEffectiveness',  ingredient3.get_effectiveness(),
      '\nEffect',         ingredient3.get_effect())

print('\n>>> Testing Ingredient method checkEffect():')
print('\nFilled Ingredient object:', ingredient2.checkEffect())
print('\nFaulty Ingredient object:', ingredient3.checkEffect())

