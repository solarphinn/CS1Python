from rit_lib import *
import random


'''
The NestingDoll struct is a recursive structure that represents a Russian 
Nesting Doll. Each doll has:
- a size, which determines which dolls will fit into other dolls
- a link to another doll; the link may be a smaller doll, or None (if the
  doll does not contain another doll.
'''
NestingDoll = struct_type("NestingDoll",
                          (int, "size"),
                          ((NoneType, "NestingDoll"), "inner"))


def make_dolls(largest):
    """
    A convenience method that creates a shuffled list of nesting dolls for use
    in experimenting with the other functions.
    :param largest: The size of the largest doll; this also determines how
    many dolls will be returned.
    :return: A shuffled list of NestingDolls that includes one doll of each
    size from 1 to largest.
    """

    dolls = []

    for size in range(largest):
        doll = NestingDoll(size + 1, None)
        dolls += [doll]

    random.shuffle(dolls)
    return dolls


def nest(one, the_other):
    """
    Nests one doll inside of the other. Always returns the larger of the two
    dolls with the smaller inside of it. This function will fail spectacularly
    if the dolls are the same size.
    :param one: One of the two NestingDolls.
    :param the_other: The other NestingDoll.
    :return: The larger of the two dolls; the smaller doll will be nested
    inside of it.
    """
    # if one is the smaller doll...
    if the_other.size > one.size:
        # check to see if the_other already has a doll inside of it
        if the_other.inner is not None:
            # if so, make the recursive call with two smaller dolls. This
            # should nest the smaller of the two inside of the other, and
            # return the larger doll
            outer = nest(the_other.inner, one)
            # nest the larger of the two smaller dolls inside of the_other
            the_other.inner = outer
            # return the_other
            return the_other
        else:
            # if the_other doesn't have a doll inside of it already, just
            # nest one inside of it and return
            the_other.inner = one
            return the_other
    else:
        # if one is the larger doll, make a recursive call, but swap the
        # two dolls (so that the smaller doll is first)
        return nest(the_other, one)


def nest_all(dolls):
    """
    Nests all of the dolls inside of each other and returns the largest doll
    (with all of the others nested inside of it).
    :param dolls: The list of dolls; the list should not contain any two
    dolls that are the same size.
    :return:
    """
    # assume that the first doll is the largest
    largest = dolls[0]

    # for each of the other dolls (other than the first)
    for i in range(1, len(dolls)):
        # us the nest function to nest the smaller of the two in the larger.
        # nest will return the larger doll with the smaller doll inside of it.
        # for each pair of dolls, the largest "wins" and becomes the new
        # largest doll
        largest = nest(largest, dolls[i])
    # return the largest
    return largest


def print_dolls(doll, indent=""):
    """
    Prints each doll with an indent.
    :param doll:  The doll to print.
    :param indent: The indent to print before the doll such that each smaller
    doll is indented slightly more than its container.
    :return: None
    """
    if doll is None: # base case
        return
    else:
        print(indent, "A doll of size", doll.size)
        print_dolls(doll.inner, indent + " ")


def main():
    """
    Makes a list of shuffled dolls, prints it, nests them all, and then
    prints them.
    :return: None
    """
    dolls = make_dolls(10)
    print(dolls)
    biggest = nest_all(dolls)
    print_dolls(biggest)


if __name__ == '__main__':
    main()