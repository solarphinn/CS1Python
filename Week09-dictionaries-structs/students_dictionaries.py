

def add_student(students, id, credits):
    """
    Adds the student to a dictionary using the student id as the key.
    :param students: The dictionary of students.
    :param id: The student's id.
    :param credits: The number of credits the student has earned.
    :return: None.
    """
    student = [id, credits]
    students[id] = [student]


def get_student(students, id):
    """
    Gets the student from the dictionary of students using the student's id.
    :param students: The dictionary of students.
    :param id: The id of the student to get.
    :return: The student, if a student with the same id is in the dictionary,
    or None if it is not.
    """

    # use the in keyword to check to see if the id is in the dictionary.
    # trying to use a key that is not in the dictionary causes an error
    if id in students:
        return students[id]
    else:
        # if the key is not in the dictionary, return None
        return None


def get_credits(students, id):
    """
    Get the credits earned so far by the student with the specified id.
    :param students: The dictionary of students.
    :param id: The id of the student.
    :return: The credits earned by the student, or 0 if the student is not in
    the dictionary.
    """
    student = get_student(students, id)
    if student is not None:
        return student[1]
    else:
        return 0


def add_credits(students, id, credits):
    """
    Adds earned credits to the student with the specified id.
    :param students: The dictionary of students.
    :param id: The id of the student that has earned credit.
    :param credits: The number of credits earned.
    :return: None.
    """
    student = get_student(students, id)
    if student is not None:
        # if the student exists, add credits to that student
        student[1] = student[1] + credits
    else:
        # if the student does not exist, add the student to the dictionary
        add_student(students, id, credits)

