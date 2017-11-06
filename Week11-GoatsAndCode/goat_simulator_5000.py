from rit_lib import *
import random

#############################################################################
# Disclaimer: This class includes a modified version of the data structures #
# provided in this week's notes and code. There are several small           #
# differences. I am including it for reference purposes only. You will need #
# to use the official CS department versions for your homework and lab.     #
#############################################################################


'''
The Node, basic building block of stacks and queues. Redeclared here rather
than importing all of linked_code. 
'''
Node = struct_type("Node",
                   (object, 'value'),
                   ((NoneType, 'Node'), 'next'))

#############################################################################
#                                                                           #
# Stack Stuff                                                               #
#                                                                           #
#############################################################################

'''
Basic RIT-style struct for a stack. A stack has a size (the number of items
currently in the stack), and a reference to the top Node in the stack.
'''
Stack = struct_type("Stack",
                    (int, "size"),
                    ((NoneType, Node), "top"))


def make_empty_stack():
    """
    Maker function that hides the implementation details of a stack so that
    the user of the stack doesn't need to worry about the internal components
    of the stack.
    :return: An empty stack.
    """
    return Stack(0, None)


def empty_stack(stack):
    """
    Checks the specified stack to determine whether or not it is currently
    empty.
    :param stack: The stack to check.
    :return: True if the queue is currently empty, otherwise False.
    """
    if stack.top is None:
        return True
    else:
        return False


def push(stack, item):
    """
    Pushes the specified item onto the top of the stack.
    :param stack: The stack onto which the item should be pushed.
    :param item: The item to push onto the stack.
    :return: None.
    """
    new_node = Node(item, stack.top)
    stack.top = new_node
    stack.size = stack.size + 1


def top(stack):
    """
    Returns but does not remove the item currently at the top of the stack. If
    the stack is empty, an IndexError is raised.
    :param stack: The stack.
    :return: The item at the top of the stack.
    """
    if empty_stack(stack):
        raise IndexError("Stack is empty!")
    else:
        return stack.top.value


def pop(stack):
    """
    Removes and returns the item currently at the top of the stack. If the
    stack is empty, an IndexError is raised.
    :param stack: The stack.
    :return: The item at the top of the stack.
    """
    item = top(stack)
    stack.top = stack.top.next
    stack.size = stack.size - 1
    return item


#############################################################################
#                                                                           #
# Queue stuff                                                               #
#                                                                           #
#############################################################################

'''
Basic RIT-style struct for a queue. A queue has a size (the number of items
currently in the queue), a reference to the front Node, and a reference to the
back Node.
'''
Queue = struct_type("Queue",
                    (int, "size"),
                    ((NoneType, Node), "front"),
                    ((NoneType, Node), "back"))


def make_empty_queue():
    """
    Maker function that hides the implementation details of a queue so that
    the user of the queue doesn't need to worry about the internal components
    of the queue.
    :return: An empty queue.
    """
    return Queue(0, None, None)


def empty_queue(queue):
    """
    Checks the specified queue to determine whether or not it is currently
    empty.
    :param queue: The queue to check.
    :return: True if the queue is currently empty, otherwise False.
    """
    return queue.front is None


def front(queue):
    """
    Returns, but does not remove, the oldest item in the queue. Raises an
    IndexError if the queue is empty.
    :param queue: The queue.
    :return: The item at the front of the queue.
    """
    if empty_queue(queue):
        raise IndexError("Queue is empty!")
    else:
        return queue.front.value


def back(queue):
    """
    Returns, but does not remove, the most recently enqueued item. Raises an
    IndexError if the queue is empty.
    :param queue: The queue.
    :return: The item at the back of the queue.
    """
    if empty_queue(queue):
        raise IndexError("Queue is empty!")
    else:
        return queue.back.value


def enqueue(queue, item):
    """
    Adds an item to the back of the queue.
    :param queue: The queue.
    :param item: The item to add to the back of the queue.
    :return: None.
    """
    new_node = Node(item, None)
    if empty_queue(queue):
        queue.front = new_node
        queue.back = new_node
    else:
        queue.back.next = new_node
        queue.back = new_node
    queue.size = queue.size + 1


def dequeue(queue):
    """
    Removes and returns the oldest item in the queue. Raises an IndexError if
    the queue is empty.
    :param queue: The queue.
    :return: The oldest item in the queue.
    """
    item = front(queue)
    queue.front = queue.front.next
    if empty_queue(queue):
        queue.back = None

    queue.size = queue.size - 1

    return item


#############################################################################
#                                                                           #
# Goat stuff                                                                #
#                                                                           #
#############################################################################

'''
Basic RIT-style struct for the Troll. Trolls have hit points.
'''
Troll = struct_type("Troll",
                    (int, "hit_points"))


'''
Basic RIT-style struct for the Goats. Goats have a name, a weight, and an
amount of insult damage.
'''
Goat = struct_type("Goat",
                   (str, "name"),
                   (int, "weight"),
                   (int, "insult_damage"))


def get_hit_points(min, max):
    """
    Helper function to generate a random number of hit points between the
    specified minimum and maximum values.
    :param min: The minimum number of hit points.
    :param max: The maximum number of hit points.
    :return: The randomly generated number of hit points.
    """
    return random.randint(min, max)


def create_troll():
    """
    Creates and returns a Troll with between 1000 and 2000 hit points.
    :return: A new Troll.
    """
    return Troll(get_hit_points(1000, 2000))


def create_goat(name):
    """
    Creates and returns a new Goat with the specified name, weighing between
    50 and 100 pounds, and an insult damage inversely proportionate to its
    weight.
    :param name: The name of the Goat.
    :return: The new Goat.
    """
    weight = random.randint(50, 100)
    insult_damage = 250 - weight

    return Goat(name, weight, insult_damage)


def populate_deli():
    """
    Prompts the user for a number of Goats, and then populates a deli with
    the specified number.
    :return: A stack representing the deli full of Goats.
    """
    num_goats = int(input("How many goats? "))
    deli = make_empty_stack()

    for i in range(1, num_goats + 1):
        goat = create_goat("Goat #" + str(i))
        push(deli, goat)

    return deli


def troll_fight():
    """
    Implementation for Goat Challenge #1: Defeat the Troll. Creates and
    populates a deli with Goats and then wages battle between the Goats and a
    Troll.
    :return: The deli (and any remaining Goats).
    """
    deli = populate_deli()
    troll = create_troll()

    while not empty_stack(deli) and troll.hit_points > 0:
        goat = pop(deli)
        print(goat.name, ", a", goat.weight, "pound goat insults the troll for",
              goat.insult_damage, "damage!")
        troll.hit_points = troll.hit_points - goat.insult_damage

        if troll.hit_points > 0:
            print("The troll eats", goat.name, "!")
        else:
            print("The troll has been defeated!")
            push(deli, goat)

    if empty_stack(deli):
        print("There are no goats left working in the deli!")
    else:
        print("There are", deli.size, "goats left in the deli!")

    return deli


def pick_berries(deli):
    """
    Assuming that any Goats survive the fight with the Troll, the surviving
    Goats will cross the rickety wooden bridge to the field to pick berries.
    :param deli: The deli containing any surviving Goats.
    :return: None.
    """
    bridge = make_empty_queue()
    field = make_empty_queue()

    total_weight = 0
    bridge_is_broken = False
    max_goats = 15
    max_weight = 1200

    while not bridge_is_broken and not empty_stack(deli):
        if bridge.size == max_goats:
            goat = dequeue(bridge)
            print("The bridge is full.", goat.name,
                  "finishes crossing it...")
            enqueue(field, goat)
            total_weight -= goat.weight

        goat = pop(deli)

        print(goat.name, "of weight", goat.weight,
              "steps onto the bridge.")
        enqueue(bridge, goat)
        total_weight += goat.weight
        print("Total weight on bridge:", total_weight)
        print("Number of goats on the bridge:", bridge.size)

        if total_weight > max_weight:
            print("OH NO! Fat goats broke the bridge!")
            bridge_is_broken = True

    if bridge_is_broken:
        while not empty_queue(bridge):
            croc_food = dequeue(bridge)
            print(croc_food.name,
                  "falls into the water below!")

        while not empty_stack(deli):
            starving = pop(deli)
            print(starving.name, "is trapped inside the deli!")
    else:
        while not empty_queue(bridge):
            goat = dequeue(bridge)
            print(goat.name, "finishes crossing the bridge...")
            enqueue(field, goat)

        print(field.size, "goat/s successfully picking berries!")


def main():
    """
    Runs the Goat simulator. Makes Goats, fights Trolls, picks berries.
    :return: None
    """
    deli = troll_fight()
    if not empty_stack(deli):
        pick_berries(deli)
    else:
        print("The Troll has defeated the Goats! /sadface")


if __name__ == '__main__':
    main()