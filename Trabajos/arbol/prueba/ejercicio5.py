from arbolFranco import BinaryTree
from random import randint

arbol = BinaryTree()

# Charge
mcu = {
    "Iron Man": True,
    "Capitán América": True,
    "Thor": True,
    "Hulk": True,
    "Viuda Negra": True,
    "Ojo de Halcón": True,
    "Black Panther": True,
    "Spider-Man": True,
    "Doctor Strange": True,
    "Scarlet Witch": True,
    "Loki": False,
    "Thanos": False,
    "Ultron": False,
    "Hela": False,
    "Vulture": False,
    "Killmonger": False,
    "Red Skull": False,
    "Ronan the Accuser": False,
    "The Mandarin": False,
    "Ego the Living Planet": False
}
for characters, bando in mcu.items():
    arbol.insert_node(characters, bando)

# Show characters
def list(arbol):
    arbol.show_characters()

# Show villains in alphabetical order
def view_Villains(arbol):
    arbol.show_V_alphabetically()

# Shows superheroes beginning with C
def view_S(arbol):
    arbol.show_S_withC()

# Determine how many superheroes are on the tree
def count_S(arbol):
    cant = arbol.count_S()
    if cant:
        print(f"there are {cant} superheroes on the tree")
    else:
        print("No superheroes on the tree")

# Search Doctor Strange and update it
def search_DS(arbol):
    arbol.search_Update("Doctor Strange", "Doctor Strange Update")

# list the superheroes in descending order
def list_S_descending(arbol):
    arbol.postorden()

#generate a forest, split the tree
def split_tree(arbol):
    villains = BinaryTree()
    superh = BinaryTree()
    villains , superh = arbol.split_V_S(villains, superh)
    print("Villains")
    villains.inorden()
    print()
    print("Superheroes")
    superh.inorden()








