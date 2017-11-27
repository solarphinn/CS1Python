from rit_lib import *

##############################################################################
#                                                                            #
# Binary Tree and Basic Functions                                            #
#                                                                            #
##############################################################################


BinaryTree = struct_type("BinaryTree",
                         ((NoneType,"BinaryTree"), "left"),
                         (object, "value"),
                         ((NoneType, "BinaryTree"), "right"))


def tree_to_string(tree):
    """
    Converts a binary search tree into a string with the numbers in order.
    :param tree: The tree to convert into a string.
    :return: The stringified version of the tree.
    """
    if tree is None:
        return ""
    else:
        return tree_to_string(tree.left) + \
               str(tree.value) + \
               tree_to_string(tree.right)


def search(tree, value):
    """
    Searches the tree for the specified value.
    :param tree: The tree to search.
    :param value: The value for which to search.
    :return: True if the value is in the tree, False if it is not.
    """
    if tree is None:
        return False
    elif tree.value == value:
        return True
    elif value > tree.value:
        return search(tree.right, value)
    else:
        return search(tree.left, value)


def insert(tree, value):
    """
    Inserts a new value into the tree. Ignores duplicate values.
    :param tree: The tree into which the value should be inserted.
    :param value: The value to insert.
    :return: The tree with the
    """
    if tree is None:
        return BinaryTree(None, value, None)
    elif value < tree.value:
        tree.left = insert(tree.left, value)
    elif value > tree.value:
        tree.right = insert(tree.right, value)

    return tree

##############################################################################
#                                                                            #
# Binary Tree Traversal Examples                                             #
#                                                                            #
##############################################################################


def sum_infix(tree):
    """
    Demonstrates an infix traversal of the nodes in the tree by calculating
    and returning the sum of all of the values in the tree.
    :param tree: The tree containing the values to sum.
    :return: The sum of all of the values in the tree.
    """
    if tree is None:
        return 0
    else:
        return sum_infix(tree.left) + \
               tree.value + \
               sum_infix(tree.right)


def sum_prefix(tree):
    """
    Demonstrates a prefix traversal of the nodes in the tree by calculating
    and returning the sum of all of the values in the tree.
    :param tree: The tree containing the values to sum.
    :return: The sum of all of the values in the tree.
    """
    if tree is None:
        return 0
    else:
        return tree.value + \
               sum_prefix(tree.left) + \
               sum_prefix(tree.right)


def sum_postfix(tree):
    """
    Demonstrates a postfix traversal of the nodes in the tree by calculating
    and returning the sum of all of the values in the tree.
    :param tree: The tree containing the values to sum.
    :return: The sum of all of the values in the tree.
    :param tree:
    :return:
    """
    if tree is None:
        return 0
    else:
        return sum_postfix(tree.left) + \
               sum_postfix(tree.right) + \
               tree.value


##############################################################################
#                                                                            #
# main                                                                       #
#                                                                            #
##############################################################################


def main():
    # a tree always starts as the empty tree (None)
    tree = None
    # insert a bunch of values into the tree
    tree = insert(tree, 5)
    tree = insert(tree, 2)
    tree = insert(tree, 1)
    tree = insert(tree, 3)
    tree = insert(tree, 7)
    tree = insert(tree, 6)
    tree = insert(tree, 9)

    # print the tree
    print(tree_to_string(tree))

    # search for values in the tree
    for i in range(10):
        print(i, "is in the tree:", search(tree, i))

    # calculate the sum of the values in the tree using an infix traversal
    print(sum_infix(tree))
    # calculate the sum of the values in the tree using a prefix traversal
    print(sum_prefix(tree))
    # calculate the sum of the values in the tree using a postfix traversal
    print(sum_postfix(tree))


if __name__ == '__main__':
    main()
