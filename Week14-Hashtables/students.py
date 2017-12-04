from rit_lib import *

'''
RIT-style struct representing a student with a unique ID and a number of earned 
credits.
'''
Student = struct_type("Student",
                      (str, "id"),
                      (int, "credits"))


##############################################################################
#                                                                            #
# List-based operations                                                      #
#                                                                            #
##############################################################################

def find_student_lst(students, id):
    """
    Finds the student with the specified ID in the list of students, if it
    exists. Does this using a linear search.
    :param students: The Python list of students.
    :param id: The ID of the student to retrieve.
    :return: The student with the specified ID if it exists. Otherwise None.
    """
    for student in students:
        if student.id == id:
            return student
    return None


def add_student_lst(students, id, credits):
    """
    Appends a new student to the given list.
    :param students: The Python list of students.
    :param id: The unique ID for the new student.
    :param credits: The credits earned by the student (so far).
    :return: None
    """
    if find_student_lst(students, id) is None:
        student = Student(id, credits)
        students += [student]


def add_credits_lst(students, id, credits):
    """
    Adds the specified number of credits to the student with the given ID.
    :param students: The Python list of students.
    :param id: The ID of the student to which the credits should be added.
    :param credits: The number of credits to add.
    :return: None
    """
    student = find_student_lst(students, id)
    if student is not None:
        student.credits += credits
    else:
        add_student_lst(students, id, credits)


def get_credits_lst(students, id):
    """
    Returns the number of credits earned by the student with the specified ID.
    :param students: The Python list of students.
    :param id: The ID of the student.
    :return: The number of credits earned by the student. Returns o if the
    student is not found in the list of students.
    """
    student = find_student_lst(students, id)
    if student is not None:
        return student.credits
    else:
        return 0


def id_to_number(id):  # hashing function
    """
    Trnslates a student ID into a number.
    :param id: The ID to translate into a number.
    :return: The resulting index.
    """
    number = 0

    # the first 3 characters are capital letters
    for i in range(3):
        value = ord(id[i]) - ord("A")
        number *= 26
        number += value

    # the remaining characters are digits
    for i in range(3, 7):
        number *= 10
        number += int(id[i])

    return number


def make_it_fit(a_big_number, a_list):  # indexing function
    """
    Translates a portentially very large number into an index that will fit
    into an array of the given size.
    :param a_big_number: The very big number.
    :param a_list: The list used to determine the valid range of indices (a
    number between 0 and the current length of the list).
    :return: A valid index in an array of the given size.
    """
    index = a_big_number % len(a_list)
    return index

##############################################################################
#                                                                            #
# Hashtable-based operations                                                 #
#                                                                            #
##############################################################################


def make_list(size):
    """
    A helper function that creates a Python list of the specified size,
    pre-populated with None values.
    :param size: The size of the list to create.
    :return: A Python list with the specified number of elements, all of which
    have a value of None.
    """
    return [None for _ in range(size)]


def hash_func(id):
    """
    A hashing function that is capable of computing the hashcode for a student
    based with the specified ID.
    :param id: The student ID to hash.
    :return: The hashcode computed for the specified ID.
    """
    number = 0

    # the first 3 characters are capital letters
    for i in range(3):
        value = ord(id[i]) - ord("A")
        number *= 26
        number += value

    # the remaining characters are digits
    for i in range(3, 7):
        number *= 10
        number += int(id[i])

    return number


def indexing_func(hashcode, a_list):
    """
    Given the specified hashcode, computes a valid index for the given list.
    :param hashcode: The hashcode for which an index should be computed.
    :param a_list: The list, the size of which determines the range of
    valid indices.
    :return: A valid index for the specified list.
    """
    index = hashcode % len(a_list)
    return index


def find_student_bad(students, id):
    """
    Finds the student with the specified ID in the list and returns it. Does
    not handle collisions.
    :param students: The list of students.
    :param id: The ID of the student to find.
    :return: The student, or None if the student isn't already in the list.
    """
    hashcode = hash_func(id)
    index = indexing_func(hashcode, students)
    return students[index]


def add_student_bad(students, id, credits=0):
    """
    Adds a new student to the list of students as long as a student with the
    same ID is not already present in the list. Does not handle collisions.
    :param students: The list of students.
    :param id: The ID of the student to add.
    :param credits: The number of credits earned by the student (so far).
    :return: None
    """
    if find_student(id) is None:
        hashcode = hash_func(id)
        index = indexing_func(hashcode, students)
        student = Student(id, credits)
        students[index] = student


def add_student(students, id, credits=0):
    """
    Adds a new student to the list of students as long as a student with the
    same ID is not already present in the list. Handles collisions using open
    addressing.
    :param students: The list of students.
    :param id: The ID of the student to add.
    :param credits: The number of credits earned by the student (so far).
    :return: None
    """
    size = len(students)
    hashcode = hash_func(id)
    start_index = indexing_func(hashcode, students)
    index = start_index
    while students[index] is not None and students[index].id != id:
        index = (index + 1) % size
        if index == start_index:
            raise IndexError("No more room!")

    students[index] = Student(id, credits)


def find_student(students, id):
    """
    Finds the student with the specified ID in the list and returns it. Handles
    collisions.
    :param students: The list of students.
    :param id: The ID of the student to find.
    :return: The student, or None if the student isn't already in the list.
    """
    size = len(students)
    hashcode = hash_func(id)
    start_index = indexing_func(hashcode, students)
    index = start_index
    while students[index] is not None and students[index].id != id:
        index = (index +1) % size
        if index == start_index:
            raise IndexError("ID not found!")

    return students[index]



def add_credits(students, id, credits):
    """
    Adds the specified number of credits to the student with the given ID.
    :param students: The Python list of students.
    :param id: The ID of the student to which the credits should be added.
    :param credits: The number of credits to add.
    :return: None
    """
    student = find_student(students, id)
    if student is not None:
        student.credits += credits
    else:
        add_student_lst(students, id, credits)


def get_credits(students, id):
    """
    Returns the number of credits earned by the student with the specified ID.
    :param students: The Python list of students.
    :param id: The ID of the student.
    :return: The number of credits earned by the student. Returns o if the
    student is not found in the list of students.
    """
    student = find_student(students, id)
    if student is not None:
        return student.credits
    else:
        return 0

