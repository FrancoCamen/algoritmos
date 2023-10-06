from arbolFranco import BinaryTree, get_value_from_file
from random import randint

file_creatures = open("Trabajos/arbol/prueba/criaturas.txt")
read_lines = file_creatures.readlines()
file_creatures.close()

# Creates and loads tree with data
creatures_tree = BinaryTree()
read_lines.pop(0)
for index, linea_creatures in enumerate(read_lines):
    creature = linea_creatures.split(';')
    creature.pop() 
    creatures_tree.insert_node(creature[0], index+2)

# inorden list of creatures and who defeated them
def list_inorden_creatures():
    creatures_tree.inorden_creatures("Trabajos/arbol/prueba/criaturas.txt")

#Add description for creatures
def _add_description():
    new_lines = creatures_tree.add_description("Trabajos/arbol/prueba/criaturas.txt")

    file_creatures_copy = open("Trabajos/arbol/prueba/criaturas.txt", "w")
    file_creatures_copy.writelines(new_lines)
    file_creatures_copy.close()

