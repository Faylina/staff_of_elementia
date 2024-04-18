#---------------------------------------#
#---------- TESTING CLASSES ------------#
#---------------------------------------#

#---------- IMPORTS --------------------#

from classes.Ingredient import Ingredient
from classes.Pouch import Pouch
# from classes.Pet import Pet
from classes.Dog import Dog
from classes.Cat import Cat
from classes.Spell import Spell
from classes.Spellbook import Spellbook



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
ingredient3 = Ingredient('dried herbs', -1, 'Commo', '12', 'stamina')

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


#---------- TESTING DOG ---------#
print('\n>>> Testing empty Dog object:')

dog1 = Dog()

print('\nEmpty Dog object:',
      '\nName:',    dog1.get_name(),
      '\nAge:',     dog1.get_age(),
      '\nColor:',   dog1.get_color(),
      '\nHungry:',  dog1.get_hungry(),
      '\nPronoun:', dog1.get_pronoun())


print('\n>>> Testing filled Dog object:')

# name=None, age=None, color=None, sex=None
dog2 = Dog('Puppy', 5, 'brown', 'male')

print('\nFilled Dog object:',
      '\nName:',    dog2.get_name(),
      '\nAge:',     dog2.get_age(),
      '\nColor:',   dog2.get_color(),
      '\nSex:',     dog2.get_sex(),
      '\nHungry:',  dog2.get_hungry(),
      '\nPronoun:', dog2.get_pronoun())


print('\n>>> Testing faulty Dog object:')

# name=None, age=None, color=None, sex=None
dog3 = Dog('dried herbs', -1, '12', 'something')

print('\nFaulty Dog object:',
      '\nName:',    dog3.get_name(),
      '\nAge:',     dog3.get_age(),
      '\nColor:',   dog3.get_color(),
      '\nSex:',     dog3.get_sex(),
      '\nHungry:',  dog3.get_hungry(),
      '\nPronoun:', dog3.get_pronoun())

print('\n>>> Testing Dog methods:')
print(dog2.adoptPet())
print(dog2.call())
print(dog2.pet())
print(dog2.checkIfHungry())
print(dog2.feed())
print(dog2.checkIfHungry())
print(dog2.play())
print(dog2.checkIfHungry())
print(dog2.look())


#---------- TESTING CAT ---------#
print('\n>>> Testing empty Cat object:')

cat1 = Cat()

print('\nEmpty Cat object:',
      '\nName:',    cat1.get_name(),
      '\nAge:',     cat1.get_age(),
      '\nColor:',   cat1.get_color(),
      '\nHungry:',  cat1.get_hungry(),
      '\nPronoun:', cat1.get_pronoun())


print('\n>>> Testing filled Cat object:')

# name=None, age=None, color=None, sex=None
cat2 = Cat('Kitty', 3, 'brown', 'female')

print('\nFilled Cat object:',
      '\nName:',    cat2.get_name(),
      '\nAge:',     cat2.get_age(),
      '\nColor:',   cat2.get_color(),
      '\nSex:',     cat2.get_sex(),
      '\nHungry:',  cat2.get_hungry(),
      '\nPronoun:', cat2.get_pronoun())


print('\n>>> Testing faulty Cat object:')

# name=None, age=None, color=None, sex=None
cat3 = Cat('dried herbs', -1, '12', 'something')

print('\nFaulty Cat object:',
      '\nName:',    cat3.get_name(),
      '\nAge:',     cat3.get_age(),
      '\nColor:',   cat3.get_color(),
      '\nSex:',     cat3.get_sex(),
      '\nHungry:',  cat3.get_hungry(),
      '\nPronoun:', cat3.get_pronoun())

print('\n>>> Testing Cat methods:')
print(cat2.adoptPet())
print(cat2.call())
print(cat2.pet())
print(cat2.checkIfHungry())
print(cat2.feed())
print(cat2.checkIfHungry())
print(cat2.play())
print(cat2.checkIfHungry())
print(cat2.look())



#---------- TESTING SPELL ---------#
print('\n>>> Testing empty Spell object:')

spell1 = Spell()

print('\nEmpty Spell object:',
      '\nName:',              spell1.get_name(),
      '\nDescription:',       spell1.get_description(),
      '\nElement:',           spell1.get_element(),
      '\nEffect:',            spell1.get_effect(),
      '\nEffectiveness:',     spell1.get_effectiveness(),
      '\nCost:',              spell1.get_cost())


print('\n>>> Testing filled Spell object:')

# name=None, description=None, effect=None, effectiveness=None, cost=None
spell2 = Spell('Windgust',
               'creates a powerful gust of wind that knocks back enemies',
               'Air',
               'offensive',
               10,
               5)

print('\nFilled Spell object:',
      '\nName:',              spell2.get_name(),
      '\nDescription:',       spell2.get_description(),
      '\nElement:',           spell2.get_element(),
      '\nEffect:',            spell2.get_effect(),
      '\nEffectiveness:',     spell2.get_effectiveness(),
      '\nCost:',              spell2.get_cost())


print('\n>>> Testing faulty Spell object:')

# name=None, description=None, effect=None, effectiveness=None, cost=None
spell3 = Spell('windgust', 'does something', 'water', 'healing', 'something', 'much')

print('\nFaulty Spell object:',
      '\nName:',              spell3.get_name(),
      '\nDescription:',       spell3.get_description(),
      '\nElement:',           spell3.get_element(),
      '\nEffect:',            spell3.get_effect(),
      '\nEffectiveness:',     spell3.get_effectiveness(),
      '\nCost:',              spell3.get_cost())

print('\n>>> Testing Spell methods:')
print(spell2.checkEffect())



#---------- TESTING SPELLBOOK ---------#
print('\n>>> Testing empty Spellbook object:')
# arsenal=[]
spellbook1 = Spellbook()
print('\nEmpty Spellbook object:',
      '\nArsenal:', spellbook1.get_arsenal())

print('\n>>> Testing faulty Spellbook object:')
# arsenal=[]
spellbook2 = Spellbook(['spell'])
print('\nFaulty Spellbook object:',
      '\nArsenal:', spellbook2.get_arsenal())

print('\n>>> Testing Spellbook method addSpell():')
print(spellbook1.addSpell(spell2))

print('\n>>> Testing Spellbook method displayArsenal():')
print('Filled Spellbook', spellbook1.displayArsenal())

herb = 'herb'
spellbook1.addSpell(herb)
print('Testing invalid object: Add herb', spellbook1.displayArsenal())


