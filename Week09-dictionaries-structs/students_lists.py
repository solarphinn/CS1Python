

def add_student(students, id, credits):
    """
    Adds the specified student to the list of students.
    :param students: The list of students.
    :param id: The id of the student to add.
    :param credits: The number of credits earned by the student.
    :return: None.
    """
    student = [id, credits]
    students += [student]


def get_student(students, id):
    """
    Performs a linear search in the list of students for the student with the
    specified id and returns the list containing that student's data or None
    if the id is not in the list.
    :param students: The list of students.
    :param id: The id of the student to fetch.
    :return: The student with the specified id, or None if no such student
    exists.
    """
    for student in students:  # linear search := O(n)
        if student[0] == id:
            return student
    return None


def get_credits(students, id):
    """
    Gets the credits earned by the student with the specified id.
    :param students: The list of students.
    :param id: The id of the student to fetch.
    :return: The credits earned by the student with the specified id, or 0 if
    no such student exists in the list.
    """
    student = get_student(students, id)  # this is a call to an O(n) function
    if student is not None:
        return student[1]
    else:
        return 0


def add_credits(students, id, credits):
    """
    Adds the given number of earned credits to the student with the specified
    id.
    :param students: The list of students.
    :param id: The id of the student that has earned credit.
    :param credits: The number of credits earned.
    :return: None.
    """
    student = get_student(students, id)  # this is a call to an O(n) function
    if student is not None:
        student[1] = student[1] + credits
    else:
        add_student(students, id, credits)

