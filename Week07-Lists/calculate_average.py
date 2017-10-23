
def average(grades):
    """
    Helper function to calculate an average from a list of individual grades.
    :param grades: The list of grades.
    :return: The calculated average.
    """
    sum = 0
    for grade in grades:
        sum += grade
    return sum / len(grades)


def process_grades(filename):
    # open the file
    file = open(filename)

    # for each line in th efile...
    for line in file:
        # split on white space
        data = line.split()

        # slice off the grade strings, e.g. '98'
        numbers = data[2:]

        # for each grade string in the list...
        for i in range(len(numbers)):
            # convert it from a string to an int and write it back into the
            # list. Lists are mutable!
            numbers[i] = int(numbers[i])

        # print this student's first name, last name, and calculated average
        print(data[1], data[0], average(numbers))


def main():
    process_grades("data.txt")

main()

