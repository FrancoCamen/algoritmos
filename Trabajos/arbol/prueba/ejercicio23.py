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

#Show talos information
def search_talos():
    creatures_tree.search_talos("Trabajos/arbol/prueba/criaturas.txt")

#3 heroes who defeated the most number of creatures.
def tops_heroes():
    creatures_tree.contar_heroes("Trabajos/arbol/prueba/criaturas.txt")

#list creatures defeated by heracles
def kill_heracles():
    creatures_tree.kills_Heracles("Trabajos/arbol/prueba/criaturas.txt")

#list undefeated creatures
def undefeated():
    creatures_tree.undefeated_creatures("Trabajos/arbol/prueba/criaturas.txt")

#load captured field
def load_captured():
    creatures_tree.load_captured("Trabajos/arbol/prueba/criaturas.txt")

#modifies who defeated the creatures
def modifies_creatures():
    creatures = ["Cerbero", "Toro de Creta", "Cierva Cerinea", "Jabalí de Erimanto"]
    creatures_tree.modifies_creatures(creatures)

#search by coincidence
def search_coincidence(value):
    creatures_tree.search_by_coincidence(value)

#delete basilisco and sirenas
def delete_BandS():
    creatures_tree.delete_node("Basilisco")
    creatures_tree.delete_node("Sirenas")
    creatures_tree.inorden()

#modify the Aves del Estinfalo node
def modify_Aves():
    creatures_tree.modify_Aves()

#modify the Ladon node
def modify_Ladon():
    creatures_tree.modify_Ladon()

#sweep by level
def sweep_By_level():
    creatures_tree.by_level()

#creatures captured by Heracles
def defeated_by_Heracles():
    creatures_tree.defeated_by_Heracles()

condicion = True
while condicion:
    print("a. listado inorden de las criaturas y quienes la derrotaron")
    print("b. se debe permitir cargar una breve descripción sobre cada criatura")
    print("c. mostrar toda la información de la criatura Talos")
    print("d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;")
    print("e. listar las criaturas derrotadas por Heracles;")
    print("f. listar las criaturas que no han sido derrotadas;")
    print("g. además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe o dios que la capturo;")
    print("h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de Erimanto indicando que Heracles las atrapó;")
    print("i. se debe permitir búsquedas por coincidencia;")
    print("j. eliminar al Basilisco y a las Sirenas;")
    print("k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles derroto a varias;")
    print("l. modifique el nombre de la criatura Ladón por Dragón Ladón;")
    print("m. realizar un listado por nivel del árbol;")
    print("n. muestre las criaturas capturadas por Heracles")
    print("salir")

    point = input("Ingrese el punto que desea visualizar")

    if point == "a":
        list_inorden_creatures()
    elif point == "b":
        print("Se genera la decripcion automaticamente")
        _add_description()
    elif point == "c":
        search_talos()
    elif point == "d":
        tops_heroes()
    elif point == "e":
        kill_heracles()
    elif point == "f":
        undefeated()
    elif point == "g":
        load_captured()
    elif point == "h":
        modifies_creatures()
    elif point == "i":
        value = input("Ingrese valor a buscar")
        search_coincidence(value)
    elif point == "j":
        delete_BandS()
    elif point == "k":
        modify_Aves()
    elif point == "l":
        modify_Ladon()
    elif point == "m":
        sweep_By_level()
    elif point == "n":
        defeated_by_Heracles()
    elif point == "salir":
        condicion = False


        

        