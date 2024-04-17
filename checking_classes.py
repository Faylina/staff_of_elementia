#---------------------------------------#
#---------- TESTING CLASSES -----------#
#---------------------------------------#

#---------- IMPORTS --------------------#

from classes.Ingredient import Ingredient
from classes.Pouch import Pouch


#---------- TESTING INGREDIENT ---------#
print('\n>>> Testing empty Ingredient object:')

ingredient1 = Ingredient()

print('\nEmpty Ingredient object:',
      '\nName:',           ingredient1.get_name(),
      '\nAmount:',         ingredient1.get_amount(),
      '\nRarity:',         ingredient1.get_rarity(),
      '\nEffectiveness:',  ingredient1.get_effectiveness(),
      '\nEffect:',         ingredient1.get_effect())


print('\n>>> Testing filled Ingredient object:')

# name=None, amount=None, rarity=None, effectiveness=None, effect=None
ingredient2 = Ingredient('dried herbs', 2, 'Common', 3, 'health')

print('\nFilled Ingredient object:',
      '\nName:',           ingredient2.get_name(),
      '\nAmount:',         ingredient2.get_amount(),
      '\nRarity:',         ingredient2.get_rarity(),
      '\nEffectiveness:',  ingredient2.get_effectiveness(),
      '\nEffect:',         ingredient2.get_effect())


print('\n>>> Testing faulty Ingredient object:')

# name=None, amount=None, rarity=None, effectiveness=None, effect=None
ingredient3 = Ingredient('dried herbs', -1, 'Commo', 12, 'stamina')

print('\nFaulty Ingredient object:',
      '\nName:',           ingredient3.get_name(),
      '\nAmount:',         ingredient3.get_amount(),
      '\nRarity:',         ingredient3.get_rarity(),
      '\nEffectiveness:',  ingredient3.get_effectiveness(),
      '\nEffect:',         ingredient3.get_effect())

print('\n>>> Testing Ingredient method checkEffect():')
print('\nFilled Ingredient object:', ingredient2.checkEffect())
print('\nFaulty Ingredient object:', ingredient3.checkEffect())



#---------- TESTING POUCH ---------#
print('\n>>> Testing filled Pouch object:')
# inventory=[]
pouch1 = Pouch()
print('\nFilled Pouch object:',
      '\nInventory:', pouch1.get_inventory())


print('\n>>> Testing faulty Pouch object:')
# inventory=[]
pouch2 = Pouch(['herbs'])
print('\nFaulty Pouch object:',
      '\nInventory:', pouch2.get_inventory())

print('\n>>> Testing Pouch method displayInventory():')
print(pouch1.displayInventory())

print('\n>>> Testing Pouch method addIngredient():')
herbs = Ingredient('herbs', 1, 'common', 2, 'magic')
pouch1.addIngredient(herbs)
print('Testing valid object: Add herbs', pouch1.displayInventory())

herb = 'herb'
pouch1.addIngredient(herb)
print('Testing invalid object: Add herb', pouch1.displayInventory())


print('\n>>> Testing Pouch method removeIngredient():')
pouch1.removeIngredient(herbs)
print('Testing removing indredient:', pouch1.displayInventory())
