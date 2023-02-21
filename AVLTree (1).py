# Assignment 7, 2022/11/20

# In this assignment, you are asked to implement your own AVL Tree class.
# AVL Tree is a balanced binary search tree that satisfies both Binary-search property and AVL property.
# We use the design of an AVL tree from Lecture 20, and some methods are discussed in Lectures 17,18 and 19.

# static method
####################    DO NOT CHANGE THIS   ####################
def get_height(n):
    # Height of the node is the distance from itself to the farthest descending leaf.
    # We also artificially define the height of None to be -1.
    if n is None:
        return -1
    else:
        return n.height


# static method
####################    DO NOT CHANGE THIS   ####################
def get_balance(n):
    # For a node n, we artificially define a value called Balance to represent the difference between
    # the heights of left and right subtrees of n.
    # If Balance is greater than 1, then the height of right subtree is too large and AVL property is violated.
    # Similarly, if Balance is smaller than -1, then the height of the left subtree is too large.
    # We also define the Balance of None to be 0.
    if n is None:
        return 0
    else:
        return get_height(n.left) - get_height(n.right)


class AVLTree:
    class Node:
        # This is the Node class for an AVL Tree.
        # Please implement right_rotation method in this class.

        def __init__(self, val):
            # There are 4 attributes in each tree Node:
            # 1. A piece of data: self.val. (You may consider self.val is an integer here.)
            # 2. A pointer to its left child, which initially points to None.
            # 3. A pointer to its right child, which initially points to None.
            # 4. The height of this node: self.height.
            # Note that, since height is maintained in each node, remember to update this attribute when it's needed.

            ####################    DO NOT CHANGE THIS   ####################
            self.val = val
            self.left = None
            self.right = None
            self.height = 0

        def __str__(self):
            # This implements "str(AVLTree.Node)".

            ####################    DO NOT CHANGE THIS   ####################
            return str(self.val)

        def __repr__(self):
            # This implements "print(AVLTree.Node)

            ####################    DO NOT CHANGE THIS   ####################
            return str(self)

        def left_rotation(self):
            # Left rotate a node so that its right child becomes the new root of this subtree.

            ####################    DO NOT CHANGE THIS   ####################
            b = self.right
            alpha = self.left
            beta = b.left
            gamma = b.right

            b.left = alpha
            b.right = beta
            self.left = b
            self.right = gamma

            self.val, b.val = b.val, self.val
            b.height = 1 + max(get_height(alpha), get_height(beta))
            self.height = 1 + max(get_height(b), get_height(gamma))

        def right_rotation(self):
            # right rotate a node so that its left child becomes the new root of this subtree.
            # Please follow the right_rotation algorithm in Lecture 19 and consider the code for left_rotation
            # method (but you don't have to follow it exactly) while implementing.
            # Remember to update the height of some nodes if necessary.
            # Do not return anything in this method.
            b = self.left
            alpha = self.right
            beta = b.left
            gamma = b.right

            b.left = alpha
            b.right = beta
            self.left = b
            self.right = gamma

            self.val, b.val = b.val, self.val
            b.height = 1 + max(get_height(alpha), get_height(beta))
            self.height = 1 + max(get_height(b), get_height(gamma))

    # Please implement each of the following methods in class AVLTree following the guide.
    # Here, I've only implemented the construction method, a printing method: pprint
    # and the dunder __repr__ method. Do not change them.

    def __init__(self, root=None):
        # In most of the designs, a tree is just a pointer to its root.
        # We use the same design here.

        ####################    DO NOT CHANGE THIS   ####################
        self.root = root

    def __contains__(self, item):
        # This implements "item in AVLTree".
        # It returns whether item is in AVLTree as a Boolean value.
        # Please follow the tree_search algorithm in Lecture 18 and the
        # code for the __contains__ method in a BinarySearchTree while implementing.
        def rec_contains(x):
            if x is None:
                return False
            elif x.val == item:
                return True
            elif x.val > item:
                return rec_contains(x.left)
            else:
                return rec_contains(x.right)

        return rec_contains(self.root)

    def height(self):
        # The height of a tree equals to the height of its root.
        # Thus, here we can return the height of the root of a tree.
        return self.root.height

    def tree_minimum(self):
        # Return the minimum item stored in an AVL Tree.
        x = self.root
        while x.left is not None:
            x = x.left
        return x.val

    def tree_maximum(self):
        # Return the maximum item stored in an AVL Tree.
        x = self.root
        while x.right is not None:
            x = x.right
        return x.val

    def preorder_tree_walk(self) -> list:
        # Remind that, in a preorder tree walk, we visit a node first, then its left subtree, then its right subtree.
        # Please follow the preorder_tree_walk algorithm in Lecture 17 and the code for the preorder_tree_walk or
        # inorder_tree_walk method in a BinarySearchTree while implementing.
        # Return a list of nodes in the expected order.
        list1 = []

        def rec_preorder_tree_walk(x):
            if x is not None:
                list1.append(x)
                rec_preorder_tree_walk(x.left)
                rec_preorder_tree_walk(x.right)

        rec_preorder_tree_walk(self.root)
        return list1

    def postorder_tree_walk(self) -> list:
        # Remind that, in a postorder tree walk, we visit a node's left subtree first, then its right subtree,
        # and then the node itself.
        # Please follow the postorder_tree_walk algorithm in Lecture 17 and the code for the preorder_tree_walk or
        # inorder_tree_walk method in a BinarySearchTree while implementing.
        # Return a list of nodes in the expected order.
        list1 = []

        def rec_postorder_tree_walk(x):
            if x is not None:
                rec_postorder_tree_walk(x.right)
                rec_postorder_tree_walk(x.left)
                list1.append(x)

        rec_postorder_tree_walk(self.root)
        return list1

    # static method
    def rebalance(x: Node):
        # Use left_rotations and right_rotations to fix AVL property at Node x.
        # Please follow the rebalance algorithm in Lecture 20 while implementing.
        # Do not return anything in this method.
        if get_balance(x) < 0:
            if get_balance(x.right) > 0:
                x.right.right_rotation()
                x.left_rotation()
            else:
                x.left_rotation()
        elif get_balance(x) > 0:
            if get_balance(x.left) < 0:
                x.left.left_rotation()
                x.right_rotation()
            else:
                x.right_rotation()

    def insert(self, item):
        assert item not in self

        # Insert a new item into an AVLTree, and maintain the AVL property at the same time.
        # Please follow the AVL_tree_insertion algorithm and the partial code in Lecture 20 while implementing.
        # Do not return anything in this method.
        def rec_insert(x):
            if x is None:
                x = AVLTree.Node(item)
            elif item < x.val:
                x.left = rec_insert(x.left)
            else:
                x.right = rec_insert(x.right)
            x.height += 1
            AVLTree.rebalance(x)
            return x

        self.root = rec_insert(self.root)

    def __delitem__(self, item):
        assert item in self

        # This implements "del AVLTree[item]".
        # Delete an existing unique item from AVLTree and maintain AVL property at the same time.
        # You may follow the AVL_tree_deletion algorithm and the partial code in Lecture 20 while implementing.
        # You can also replace a node with its predecessor (instead of its successor like what we did)
        # in the case that the node has two children. (It will give different tree after deletion but the binary
        # search property will also be maintained.)
        # Do not return anything in this method.
        def rec_delete(x):
            if x is not None:
                if item < x.val:
                    x.left = rec_delete(x.left)
                elif item > x.val:
                    x.right = rec_delete(x.right)
                else:
                    if x.left is None and x.right is None:
                        x = None
                        return x
                    elif x.left is None:
                        x = x.right
                    elif x.right is None:
                        x = x.left
                    else:
                        y = x.right
                        while y.left is not None:
                            y = y.left
                        x.val, y.val = y.val, x.val
                        x.right = rec_delete(x.right)
                x.height -= 1
                AVLTree.rebalance(x)
                return x

        self.root = rec_delete(self.root)

    def __iter__(self):
        # This implements "for item in AVLTree"
        # Yield each item in increasing order from a AVLTree.
        # Remind that, an inorder tree walk can print out items in a binary search tree in non-decreasing order.
        # Please following the inorder_tree_walk algorithm in Lecture 17 and the __iter__ method in
        # a BinarySearchTree while implementing.
        def rec_iter(x):
            if x is not None:
                yield from rec_iter(x.left)
                yield x
                yield from rec_iter(x.right)

        return rec_iter(self.root)

    def __repr__(self):
        # This implements "print(AVLTree)"

        ####################    DO NOT CHANGE THIS  ####################
        return "[" + ", ".join(repr(n) for n in self) + "]"

    def pprint(self, width=64):
        # This is a helper method that prints a binary tree out.

        ####################    DO NOT CHANGE THIS  ####################
        height = self.height()
        nodes = [(self.root, 0)]
        prev_level = 0
        repr_str = ''
        while nodes:
            n, level = nodes.pop(0)
            if prev_level != level:
                prev_level = level
                repr_str += '\n'
            if not n:
                if level <= height - 1:
                    nodes.extend([(None, level + 1), (None, level + 1)])
                repr_str += '{val:^{width}}'.format(val='-', width=width // 2 ** level)
            elif n:
                if n.left or level <= height - 1:
                    nodes.append((n.left, level + 1))
                if n.right or level <= height - 1:
                    nodes.append((n.right, level + 1))
                repr_str += '{val:^{width}}'.format(val=n.val, width=width // 2 ** level)
        print(repr_str)


########################################################################################################################
######################################                                      ############################################
######################################     DO NOT CHANGE ANYTHING BELOW     ############################################
######################################                                      ############################################
########################################################################################################################
tree1 = AVLTree()
for n in range(1, 8):
    tree1.insert(n)
print("Let's start with an AVL Tree with numbers 1 to 7 stored in it.")
tree1.pprint()
print()

tree1.insert(17)
print("Insert number 17 to the tree:")
tree1.pprint()
print()

for n in range(16, 7, -1):
    tree1.insert(n)
print("Insert numbers 8 to 16 into the tree in reverse order:")
tree1.pprint()
print()

r = tree1.root.val
del tree1[r]
print("Delete the root of the current tree:")
tree1.pprint()
print()

r = tree1.root.val
del tree1[r]
print("Then we delete the root of the current tree again:")
tree1.pprint()
print()

# for _ in range(5):
#    mi = tree1.tree_minimum()
#    del tree1[mi]
# print("Delete the five minimum numbers from the tree:")
# tree1.pprint()
# print()

print("Print out numbers in the current tree in "
      "increasing order:", tree1, ", ""and the maximum number in the tree is", tree1.tree_maximum(), ".")
print("If we traverse the current tree in preorder, we get:", tree1.preorder_tree_walk(), ".")
print("If we traverse the current tree in postorder, we get:", tree1.postorder_tree_walk(), ".")