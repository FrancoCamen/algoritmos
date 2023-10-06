from arbolFranco import BinaryTree, get_value_from_file
from random import randint

file_jedi = open("Trabajos/arbol/prueba/jedis.txt")
read_lines = file_jedi.readlines()
file_jedi.close()

# Creates and loads 3 trees with data
name_tree = BinaryTree()
specie_tree = BinaryTree()
ranking_tree = BinaryTree()

read_lines.pop(0)
for index, linea_jedi in enumerate(read_lines):
    jedi = linea_jedi.split(';')
    jedi.pop() 
    name_tree.insert_node(jedi[0], index+2)
    specie_tree.insert_node(jedi[2], index+2)
    ranking_tree.insert_node(jedi[1], index+2)


#Sweep inorden the tree names
def inorden_names_ranking():
    print("Names")
    name_tree.inorden()
    print()
    print("Rankings")
    ranking_tree.inorden()

#Sweep by level 
def bylevel_ranking_specie():
    print("             Rankings:")
    ranking_tree.by_level()
    print()
    print("             Species:")
    specie_tree.by_level()

#Show information about Yoda and Luke 
def info_Yoda_and_Luke():
    root = name_tree.search("yoda")
    info = get_value_from_file("Trabajos/arbol/prueba/jedis.txt", root.other_values)
    print("       Yoda information")
    print(info)
    root = name_tree.search("luke skywalker")
    info = get_value_from_file("Trabajos/arbol/prueba/jedis.txt", root.other_values)
    print("       LUke information")
    print(info)

#Show all Jedi with ranking "Jedi master"
def jedi_Master():
    ranking_tree.jedi_Master("Trabajos/arbol/prueba/jedis.txt")

#Jedi who used green lightsabers
def jedi_lightsabers():
    print("          Jedi who used green lightsabers")
    name_tree.jedi_lightsabersG("Trabajos/arbol/prueba/jedis.txt")

#Jedi whose masters are in the archive
def jedi_master():
    name_tree.jedi_with_Master("Trabajos/arbol/prueba/jedis.txt")

#Jedi with togruta or cerean species
def _jedi_specie():
    name_tree.jedi_especie("Trabajos/arbol/prueba/jedis.txt")

#jedi beginning with A
def jedi_with_A():
    name_tree.jedi_A()


    




    











