"""
Author: Robby Stohel
File: binarysearchtree.py

Contains the Node and BinarySearchTree classes to build and modify
    binary search trees.
"""

from copy import deepcopy
from recursioncounter import RecursionCounter

class Node(): # 'object' removed from arg as per pylint
    """ A class used to build out base nodes. """
    def __init__(self, data, left_child=None, right_child=None):
        """
        Node class initilzer.
        Process:
            Receives data/left_child/right_child. If left_child/
                right_child are not provided, initialized to None.
        Args:
            self(Node): Obligatory self arguement
            data(int): Integer applied as node's data
            left_child(node/None): Smaller leaf node or None
            right_child(node/None): Larger leaf node or None
        Returns:
            None(None): No return
        """
        self.data = data
        self.left_child = left_child
        self.right_child = right_child
        self.height = 0

    def __str__(self):
        """
        Converts node data into a string.
        Process:
            Returns self.data as string.
        Args:
            self(Node): Obligatory self arguement
        Returns:
            self.data(str): Returns self.data after converting to string
        """
        return str(self.data)

    def is_leaf(self):
        """
        Checks if node is a leaf node.
        Process:
            Checks self.left_child/self.right_child. If both are None, returns True.
                Otherwise returns False.
        Args:
            self(Node): Obligatory self arguement
        Returns:
            bool(bool): Returns True if both children nodes are None. Otherwise
                returns False
        """
        return bool(self.left_child is None and self.right_child is None)

    def update_height(self):
        """
        Udpates node height value when created.
        Process:
            1. Verifies node isn't a leaf which initializes to 0
            2. Increments node height as called
        Args:
            self(Node): Obligatory self arguement
        Returns:
            None(None): No return
        """
        if self.is_leaf() is True:
            pass
        else:
            self.height += 1

class BinarySearchTree(): # 'object' removed from arg as per pylint
    """ A class to build and modify binary trees. """
    def __init__(self, node=None):
        """
        Initializes the binary search tree.
        Process:
            If a tree is not provided a node, the tree is created as
                node.root = None. Otherwise the node is started with the
                provided node data.
        Args:
            self(BinarySearchTree): Obligatory self arguement
            node(Node): The initial node for the tree. Initialized to
                None if no node is provided.
        Returns:
            None(None): No return
        """
        self.root = node
        self.hgt = -1

    def __str__(self):
        """
        Provides a string depiction of the tree.
        Process:
            Initially calls the str_helper method for string creation. Returns result.
        Args:
            self(BinarySearchTree): Obligatory self arguement
        Returns:
            str_helper(string): The result of the recursive method calls 
        """
        def str_helper(node, hgt):
            """
            Assists with producing a string representation of the tree.
            Process:
                1. Initializes string
                2. Recursively prints path down each branch, printing nodes
                3. Includes leaf height
                4. Prints [Empty] for empty child nodes (unless parent node is a leaf)
                4. Prints [leaf] when node is a leaf node
            Args:
                node(Node): ArgDescription
                hgt(int): Used to determin blank spacing in print
            Returns:
                string(string): The result of the recursive method calls 
            """
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

        return str_helper(self.root, self.root.height)

    def __len__(self):
        """
        Counts nodes in tree.
        Process:
            Initially calls len_helper method to begin count. Returns result.
        Args:
            self(BinarySearchTree): Obligatory self arguement
        Returns:
            len_helper(int): Returns the final result of the function call
        """
        def len_helper(node, hgt):
            """
            Assists with counting nodes in tree.
            Process:
                Recursively calls the len_helper method to count nodes.
            Args:
                hgt(int): The height if each level accessed
            Returns:
                count(int): The total node count
            """
            RecursionCounter()
            count = 0

            if node is not None:
                count += len_helper(node.left_child, hgt + 1)
                count += len_helper(node.right_child, hgt + 1)
                count += 1
            return count

        return len_helper(self.root, 0)

    def is_empty(self):
        """
        Checks to see if tree is empty.
        Process:
            Check if self.root is None. Returns True if true, and
                False if false.
        Args:
            self(BinarySearchTree): Obligatory self arguement
        Returns:
            bool(bool): True if self.root is None, false otherwise
        """
        return bool(self.root is None)

    def add(self, data):
        """
        Adds provided to node.data, then inserts the node appropriately.
        Process:
            1. Verifies the tree isn't empty
            2. Initially calls the add_helper method
        Args:
            self(BinarySearchTree): Obligatory self arguement
            data(int): The data to be added as a node
        Returns:
            None(None): No return
        """
        def add_helper(node, data):
            """
            Recursively assists with adding nodes in their proper order.
            Process:
                Recursively calls add_helper method, locating position for
                    new node, then inserting. Updates node height as it inserts.
            Args:
                node(Node): Subsequent nodes called for add
                data(int): The data to be added to an inserted node
            Returns:
                None(None): No return
            """
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

        present = self.find(data)

        if self.root is None:
            self.root = Node(data)
        elif present is not None:
            raise ValueError("Value already in tree")
        else:
            add_helper(self.root, data)

    def find(self, data):
        """
        Finds the node with the desired data value.
        Process:
            Initially calls and returns the response from finder_helper method.
        Args:
            self(BinarySearchTree): Obligatory self arguement
            data(int): The value to be located
        Returns:
            node(Node): The node containing the desired value
        """
        def find_helper(node, data):
            """
            Recursively assists with finding node containing specified data.
            Process:
                Recursively calls find_helper method separating search across
                    the entire tree till the proper node is located.
            Args:
                node(Node): Subsequent nodes called for search
                data(int): The value to be located
            Returns:
                node(Node): The node containing the desired value
            """
            RecursionCounter()

            if node is not None:
                if node.data == data:
                    return node
                else:
                    if find_helper(node.left_child, data) is None:
                        return find_helper(node.right_child, data)
                    return find_helper(node.left_child, data)

        return find_helper(self.root, data)

    def remove(self, data):
        """
        Removes nodes with predetermined values..
        Process:
            1. Verifies the tree isn't empty
            2. Initially calls the remove_helper method
            3. Corrects tree node height values.
        Args:
            self(BinarySearchTree): Obligatory self arguement
            data(int): Data value to be found and removed
        Returns:
            None(None): No return
        """
        temp = list()

        def remove_helper(node, data):
            """
            Recursively assists with removing nodes with predetermined values.
            Process:
                1. Locates node containing value
                2. Passes right_child for recursion
                3. Recursively passes left_child till predecessor is found
                4. Replaces top node data with predecessor data
                5. Shifts affected nodes as necessary
            Args:
                node(Node): Recursively passed nodes for tree arrangement
                data(int): Data value to be found and removed
            Returns:
                None(None): No return
            """
            RecursionCounter()
            if node is not None:
                if data == node.data:
                    temp.append(node)
                    if node.right_child is None:
                        if node.left_child is None:
                            pass

                        else:
                            node.data = node.left_child.data
                            node.height = node.left_child.height
                            node.right_child = node.left_child.right_child
                            node.left_child = node.left_child.left_child
                            temp.pop()
                    elif node.right_child is not None:
                        remove_helper(node.right_child, data)

                        if (node.right_child is not None
                                and len(temp) != 0
                                and node.right_child.data == temp[0].data):
                            node.right_child = None
                            temp.pop()

                    else:
                        node = None
                elif data > node.data:
                    remove_helper(node.right_child, data)

                    if (node.right_child is not None
                            and len(temp) != 0
                            and node.right_child.data == temp[0].data):
                        node.right_child = None
                        temp.pop()

                elif data < node.data:
                    remove_helper(node.left_child, data)

                    if node.left_child is None and len(temp) != 0:
                        temp[0].data = deepcopy(node.data)
                        if node.right_child is not None:
                            node.data = node.right_child.data
                            node.height = node.right_child.height
                            node.left_child = node.right_child.left_child
                            node.right_child = node.right_child.right_child

                    if (node.left_child is not None
                            and len(temp) != 0
                            and node.left_child.data == temp[0].data):
                        node.left_child = None
                        temp.pop()

        if self.is_empty():
            return None
        else:
            remove_helper(self.root, data)

        def hgt_update(node):
            """ Correct's node heights after removal. """
            if node is not None:
                hgt_update(node.left_child)
                hgt_update(node.right_child)
                if node.is_leaf():
                    node.height = 0
                else:
                    temp1 = 0
                    temp2 = 0
                    if node.left_child is not None:
                        temp1 = node.left_child.height + 1
                    if node.right_child is not None:
                        temp2 = node.right_child.height + 1

                    if temp1 > temp2:
                        node.height = temp1
                    else:
                        node.height = temp2

        hgt_update(self.root)

    def preorder(self):
        """
        Creates an preordered list of the tree's values.
        Process:
            Calls preorder_helper method recursively, applying the data to the
                order data list value.
        Args:
            self(BinarySearchTree): Obligatory self arguement
        Returns:
            order(list): The list type, preorder tree data
        """
        order = list()

        def preorder_helper(node):
            """
            Retrieves tree data in pre-order.
            Process:
                Recursively adds tree data to order list.
            Args:
                node(Node): Successive nodes for ordering
            Returns:
                None(None): Does not return
            """
            RecursionCounter()

            if node is not None:
                order.append(node.data)
                preorder_helper(node.left_child)
                preorder_helper(node.right_child)

        preorder_helper(self.root)
        return order

    def inorder(self):
        """
        Creates an preordered list of the tree's values.
        Process:
            Calls preorder_helper method recursively, applying the data to the
                order data list value.
        Args:
            self(BinarySearchTree): Obligatory self arguement
        Returns:
            order(list): The list type, preorder tree data
        """
        order = list()

        def inorder_helper(node):
            """
            Retrieves tree data in in-order.
            Process:
                Recursively adds tree data to order list.
            Args:
                node(Node): Successive nodes for ordering
            Returns:
                None(None): Does not return
            """
            RecursionCounter()

            if node is not None:
                inorder_helper(node.left_child)
                order.append(node.data)
                inorder_helper(node.right_child)

        inorder_helper(self.root)
        return order

    def rebalance_tree(self):
        temp_list = self.inorder()
        temp_tree = BinarySearchTree()

        def rebalance_helper(tmp_list):
            if len(tmp_list) != 0:
                mid = round(len(tmp_list) / 2)
                temp_tree.add(tmp_list[mid])
                rebalance_helper(tmp_list[:mid])
                rebalance_helper(tmp_list[mid+1:])

        if self is not None:
            rebalance_helper(temp_list)
            self.root = temp_tree.root

    def height(self):
        """
        Check object height.
        Process:
            From self.root, increments per level recursively, skipping incrementation
                if the present node height is already recorded.
        Args:
            self(BinarySearchTree): Obligatory self arguement
        Returns:
            hgt(int): Final object height
        """
        self.hgt = -1

        def height_helper(node, height):
            if node is not None:
                if height <= self.hgt:
                    self.hgt = height + 1
                    height_helper(node.left_child, height + 1)
                    height_helper(node.right_child, height + 1)
        
        if self.is_empty is True:
            return self.hgt
        else:
            height_helper(self.root, self.hgt)
            return self.hgt
