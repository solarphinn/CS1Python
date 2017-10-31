from rit_lib import *

'''
A simple Node. Each node contains:
- a value - The Python object type is used so that the Node can hold any kind
  of value.
- a link to another Node - The link may be another Node or None.
'''
Node = struct_type("Node",
                   (object, "value"),
                   ((NoneType, "Node"), "next"))


def append(lst, value):
    """
    Returns a copy of the lst with a Node with the specified value appended
    onto the end of it. This is done non-destructively, so the original list
    is not modified.
    :param lst: The list to copy and append the new Node onto.
    :param value: The value to store inside of the new Node.
    :return: A copy of the list with the additional Node at the end.
    """
    if lst is None:
        return Node(value, None)
    else:
        copy = Node(lst.value, None)
        rest = append(lst.next, value)
        copy.next = rest
        return copy


def length(lst):
    """
    Uses iteration to count the number of nodes in the list.
    :param lst: The list for which to calculate the length.
    :return: The length of the list (i.e. the number of Nodes in the list).
    """

    # assume that the length is 0
    list_length = 0

    # while the list is not None (we have not reached the end yet)...
    while lst is not None:
        # increment the length by 1
        list_length += 1
        # move to the next Node in the list.
        lst = lst.next

    # return the length
    return list_length


def lengthRec(lst, list_length=0):
    """
    Uses tail recursion to count the number of nodes in the list.
    :param lst: The list for which the length should be calculated.
    :param list_length: The number of nodes counted so far (default of 0)
    :return: The number of nodes in the list.
    """
    # base case: if the list is None, return 0 (the length of the empty list)
    if lst is None:
        return list_length
    # recursive case
    else:
        list_length += 1
        # make the recursive call with length+1 and return the result
        return lengthRec(lst.next, list_length + 1)


def lengthGen(lst):
    """
    Uses general recursion to count the number of nodes in the list.
    :param lst: The list for which the length should be calculated.
    :return: The number of nodes in the list.
    """
    if lst is None:
        return 0
    else:
        return 1 + lengthGen(lst.next)


def catDestructive(front, back):
    """
    A destructive version of the cat function (alters the original list so
    that it contains the nodes from the second list).
    :param front: The list that should be in the front of the concatenated
    list.
    :param back: The list that should be in the back of the concatenated list.
    :return: The concatenated list (a list comprising all of the nodes in
    front and back).
    """
    if front is None:
        # base case: if front is the empty list, return back
        return back
    elif front.next is None:
        # if the end of front has been reached, set front.next to back. This
        # "destroys" the original front (the original list is gone and can't
        # be recovered), which is what makes this a destructive implementation
        # of the cat function
        front.next = back
    else:
        # make the recursive call with the next Node in front.
        catDestructive(front.next, back)


def cat(front, back):
    """
    A non-destructive version of the cat function (does not alter either of
    the original parameter lists, but instead creates a new list that contains
    copies of all of the nodes in the front and back lists).
    :param front: The list that should be in the front of the concatenated
    list.
    :param back: The list that should be in the back of the concatenated list.
    :return: The concatenated list; contains copies of all of the nodes in the
    front and back lists.
    """
    if front is None:
        # base case: if front is the empty list, return back
        return back
    else:
        # make a copy of the first node in front
        copy = Node(front.value, None)
        # make the recursive call to the cat function to concatenate
        # the remaining nodes in the front list with the back list.
        concat = cat(front.next, back)
        # set copy.next to the result returned by cat
        copy.next = concat
        # return the copy
        return copy


def get(lst, index):
    """
    Retrieves the value in the node at the specified index in the list.
    :param lst: The list that contains the desired value.
    :param index: The index of the desired value.
    :return: The value at the specified index in the list.
    """
    if lst is None:
        # if we have reached the end of the list, the index was larger than
        # the number of nodes in the list, so raise an error
        raise IndexError("invalid index")
    elif index == 0:
        # if the index is 0, we have reached the right location in the list,
        # so return the value
        return lst.value
    else:
        # if the index is not 0, make the recursive call with the next node
        # in the list and decrement index.
        return get(lst.next, index-1)

