from recursioncounter import RecursionCounter

class Node(object):

    def __init__(self, data, left_child=None, right_child=None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child
        self.height = 0
    
    def __str__(self):
        return str(self.data)

    def is_leaf(self):
        if self.left_child is None and self.right_child is None:
            return True
        else:
            return False

    def update_height(self):
        """
        Recieves a data value to assign as the height of the tree at this leaf.
        The URL didn't include a data value arguement, but the leaf is disconnected
        from the tree otherwise so it would be unable to obtain a value otherwise.
        Process:
            Receives a height data value when called at the tree level. Assigns
            this value to the tree height from this leaf.
        Args:
            data(int): The height of the tree when this leaf is added.
        Returns:
            ReturnValue(None): None
        """
        if self.is_leaf() is True:
            pass
        else:
            self.height += 1 


class BinarySearchTree(object):

    def __init__(self, node=None):
        self.root = node

    def __str__(self):

        def str_helper(node, hgt):
            RecursionCounter() 
            string = ""

            if node is not None:
                if node.left_child is None and node.right_child is None:
                    string += "   " * (self.root.height - hgt)
                    string += str(node.data) + " (" + str(node.height) + ") [leaf] \n"
                else:
                    string += "   " * (self.root.height - hgt)
                    string += str(node.data) + " (" + str(node.height) + ") \n"

                if node.left_child is None and node.right_child is not None:
                    string += "   " * (self.root.height - hgt + 1)
                    string += "[Empty] \n"
                    string += str_helper(node.right_child, hgt - 1)
                elif node.right_child is None and node.left_child is not None:
                    string += str_helper(node.left_child, hgt - 1)
                    string += "   " * (self.root.height - hgt + 1)
                    string += "[Empty] \n"
                else:
                    string += str_helper(node.left_child, hgt - 1)
                    string += str_helper(node.right_child, hgt - 1)

            return string

        string = ""

        for item in self.preorder():
            string += (str(item) + ", ")
        string += "\n"
        string += str_helper(self.root, self.root.height)
        return string

    def __len__(self):

        def len_helper(node, hgt):
            RecursionCounter() 
            count = 0

            if node is not None:
                count += len_helper(node.left_child, hgt + 1)
                count += len_helper(node.right_child, hgt + 1)
                count += 1
            return count
        
        return len_helper(self.root, 0)

    def is_empty(self):
        if self.root is None:
            return True
        else:
            return False

    def add(self, data):

        def add_helper(node, data):
            RecursionCounter() 
            if node.data > data:
                if node.left_child is None:
                    node.left_child = Node(data)
                else:
                    add_helper(node.left_child, data)
                if node.height <= node.left_child.height:
                    node.update_height()
            elif node.data < data:
                if node.right_child is None:
                    node.right_child = Node(data)
                else:
                    add_helper(node.right_child, data)
                if node.height <= node.right_child.height:
                    node.update_height()
        
        if self.root is None:
            self.root = Node(data)
        else:
            add_helper(self.root, data)

    def find(self, data):
        
        def find_helper(node, data):
            RecursionCounter() 
            
            if node is not None:
                if node.data == data:
                    return node.data
                else:
                    if find_helper(node.left_child, data) is None:
                        return find_helper(node.right_child, data)
                    return find_helper(node.left_child, data)

        return find_helper(self.root, data)

    def remove(self):
        pass

        def remove_helper():
            RecursionCounter() 
            pass

    def preorder(self):

        order = list()

        def preorder_helper(node):
            RecursionCounter()
            
            if node is not None:
                order.append(node.data)
                preorder_helper(node.left_child)
                preorder_helper(node.right_child)

        preorder_helper(self.root)
        return order

    def height(self):
        def recurse(node):
            RecursionCounter() 
            if node == None:
                return 0
            else:
                return 1 + max(recurse(node.left_child), recurse(node.right_child))
        hgt = recurse(self.root)
        if not self.is_empty():
            hgt -= 1
        return hgt
