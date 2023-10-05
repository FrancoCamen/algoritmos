from cola import Cola
import linecache

def get_value_from_file(file_name, index):
    line = linecache.getline(file_name, index)
    line_split = line.split(';')
    line_split.pop()
    return line_split

class NodeTree():

    def __init__(self, value, other_values=None):
        self.value = value
        self.other_values = other_values
        self.left = None
        self.right = None
        self.height = 0

class BinaryTree:

    def __init__(self):
        self.root = None

    def height(self, root):
        if root is None:
            return -1
        else:
            return root.height

    def update_height(self, root):
        if root is not None:
            left_height = self.height(root.left)
            right_height = self.height(root.right)
            root.height = (left_height if left_height > right_height else right_height) + 1

    def simple_rotation(self, root, control):
        if control:
            aux = root.left
            root.left = aux.right
            aux.right = root
        else:
            aux = root.right
            root.right = aux.left
            aux.left = root
        self.update_height(root)
        self.update_height(aux)
        root = aux
        return root

    def double_rotation(self, root, control):
        if control:
            root.left = self.simple_rotation(root.left, False)
            root = self.simple_rotation(root, True)
        else:
            root.right = self.simple_rotation(root.right, True)
            root = self.simple_rotation(root, False)
        return root

    def balancing(self, root):
        if root is not None:
            if self.height(root.left) - self.height(root.right) == 2:
                if self.height(root.left.left) >= self.height(root.left.right):
                    root = self.simple_rotation(root, True)
                else:
                    root = self.double_rotation(root, True)
            elif self.height(root.right) - self.height(root.left) == 2:
                if self.height(root.right.right) >= self.height(root.right.left):
                    root = self.simple_rotation(root, False)
                else:
                    root = self.double_rotation(root, False)
        return root

    def insert_node(self, value, other_values=None):

        def __insertar(root, value, other_values):
            if root is None:
                return NodeTree(value, other_values)
            elif value < root.value:
                root.left = __insertar(root.left, value, other_values)
            else:
                root.right = __insertar(root.right, value, other_values)
            root = self.balancing(root)
            self.update_height(root)
            return root

        self.root = __insertar(self.root, value, other_values)

    def by_level(self):
        if self.root is not None:
            cola_tree = Cola()
            cola_tree.arrive(self.root)
            while cola_tree.size() > 0:
                node = cola_tree.atention()
                print(node.value)
                if node.left is not None:
                    cola_tree.arrive(node.left)
                if node.right is not None:
                    cola_tree.arrive(node.right)

    def inorden(self):
        def __inorden(root):
            if root is not None:
                __inorden(root.left)
                print(root.value)
                __inorden(root.right)

        __inorden(self.root)

    def postorden(self):
            def __postorden(root):
                if root is not None:
                    __postorden(root.right)
                    print(root.value)
                    __postorden(root.left)

            __postorden(self.root)

    def preorden(self):
            def __preorden(root):
                if root is not None:
                    print(root.value, root.height)
                    __preorden(root.left)
                    __preorden(root.right)

            __preorden(self.root)

    def search(self, key):
        def __search(root, key):
            if root is not None:
                if root.value == key:
                    return root
                elif key < root.value:
                    return __search(root.left, key)
                else:
                    return __search(root.right, key)

        return __search(self.root, key)

    def delete_node(self, key):
        def __replace(root):
            if root.right is None:
                return root.left, root
            else:
                root.right, replace_node = __replace(root.right)
            return root, replace_node

        def __delete(root, key):
            value = None
            if root is not None:
                if key < root.value:
                    root.left, value = __delete(root.left, key)
                elif key > root.value:
                    root.right, value = __delete(root.right, key)
                else:
                    value = root.value
                    if root.left is None and root.right is not None:
                        return root.right, value
                    elif root.right is None and root.left is not None:
                        return root.left, value
                    elif root.left is None and root.right is None:
                        return None, value
                    else:
                        root.left, replace_node = __replace(root.left)
                        root.value = replace_node.value

            return root, value

        delete_value = None
        if self.root is not None:
            self.root, delete_value = __delete(self.root, key)
        return delete_value

    def contar(self, value):
        def __contar(root, value):
            count = 0
            if root is not None:
                if root.value == value:
                    count = 1
                count += __contar(root.left, value)
                count += __contar(root.right, value)
            return count

        return __contar(self.root, value)

    # Height of subtrees. Ejercice 1.d
    def height_subtree(self):
        def __point1_d(root):
            if root is not None:
                left_height = self.height(root.left)
                right_height = self.height(root.right)
                print(f"Height of left subtree : {left_height}. Height of right subtree: {right_height}")

        __point1_d(self.root)

    # counting odd and even. Ejercice 1.f
    def odd_even(self):
        def __odd_even(root):
            def __odd(root):
                count = 0
                if root is not None:
                    if root.value % 2 == 0:
                        count = 1
                    count += __odd(root.left)
                    count += __odd(root.right)
                return count
            odd = __odd(root)

            def __even(root):
                count = 0
                if root is not None:
                    if root.value % 2 != 0:
                        count = 1
                    count += __even(root.left)
                    count += __even(root.right)
                return count
            even = __even(root)

            return [odd, even]

        return __odd_even(self.root)

    # Inorder of characters. Ejercice 5.a
    def show_characters(self):
        def __show_characters(root):
            if root is not None:
                __show_characters(root.left)
                print(root.value, root.other_values)
                __show_characters(root.right)

        __show_characters(self.root)

    # Shows villains in alphabetical order. Ejercice 5.b
    def show_V_alphabetically(self):
        def __show_V_alphabetically(root):
            if root is not None:
                __show_V_alphabetically(root.left)
                if root.other_values == False:
                    print(root.value)
                __show_V_alphabetically(root.right)

        __show_V_alphabetically(self.root)

    # Shows superheroes beginning with C. Ejercice 5.c
    def show_S_withC(self):
        def __show_S(root):
            if root is not None:
                __show_S(root.left)
                if root.other_values == True and root.value[0] == "C":
                    print(root.value)
                __show_S(root.right)

        __show_S(self.root)

    # Determine how many superheroes are on the tree. 5.D
    def count_S(self):
        def __count_S(root):
            count = 0
            if root is not None:
                if root.other_values == True:
                    count = 1
                count += __count_S(root.left)
                count += __count_S(root.right)
            return count

        return __count_S(self.root)

    # Search Doctor Strange and update it. 5.E
    def search_Update(self, key, new_key):
        def __search(root, key, new_key):
            if root is not None:
                if root.value == key:
                    root.value = new_key
                elif key < root.value:
                    __search(root.left, key, new_key)
                else:
                    __search(root.right, key, new_key)

        return __search(self.root, key, new_key)

    # generate a forest, split the tree
    def split_V_S(self, villains, superh):
        def __inorden(root):
            if root is not None:
                __inorden(root.left)
                if root.other_values == False:
                    villains.insert_node(root.value)
                else:
                    superh.insert_node(root.value)
                __inorden(root.right)
            return villains, superh

        return __inorden(self.root)

    # Show all Jedi with ranking "Jedi master"
    def jedi_Master(self, file):
        def __jedi_Master(root, file):
            if root is not None:
                __jedi_Master(root.left, file)
                if root.value == "jedi master":
                    info = get_value_from_file(file, root.other_values)
                    print(info[0])
                __jedi_Master(root.right, file)
        __jedi_Master(self.root, file)

    #Jedi who used green lightsabers
    def jedi_lightsabersG(self, file):
        def __jedi_lightsabersG(root, file):
            if root is not None:
                __jedi_lightsabersG(root.left, file)
                pos = root.other_values
                info = get_value_from_file(file, pos)
                lightsaber_color = info[4]
                if lightsaber_color == "green":
                    print(root.value)
                __jedi_lightsabersG(root.right, file)
        __jedi_lightsabersG(self.root, file)

    #Jedi whose masters are in the archive
    def jedi_with_Master(self, file):
        master_tree = BinaryTree()

        def search_master(masters):
            masters = masters.split("/")
            for master in masters:
                value = self.search(master)
                if value is not None:
                    return True
        
        def __jedi_with_Master(root, file):
            if root is not None:
                __jedi_with_Master(root.left, file)
                pos = root.other_values
                info = get_value_from_file(file, pos)
                master = info[3]
                if search_master(master) == True:
                    print("---")
                    print("Jedi")
                    print(root.value)
                    print("Master")
                    print(master)
                    print("---")
                __jedi_with_Master(root.right, file)
        __jedi_with_Master(self.root, file)

    #Jedi with togruta or cerean species
    def jedi_especie(self, file):
        def __jedi_especie(root, file):
            if root is not None:
                __jedi_especie(root.left, file)
                pos = root.other_values
                info = get_value_from_file(file, pos)
                if info[2] == "togruta" or info[2] == "cerean":
                    print("---")
                    print("Jedi")
                    print(root.value)
                    print("Specie")
                    print(info[2])
                    print("---")
                __jedi_especie(root.right, file)
        __jedi_especie(self.root, file)








