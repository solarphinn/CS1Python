

def count_down(number):
    """
    Counts down from a number to 0 recursively.
    :param number: The number from which to count down.
    :return: None
    """
    if number >= 0:           # validate number >= 0
        print(number)         # print the number (one unit of work)
        count_down(number-1)  # make the recursive call for the rest


def count_up(number):
    """
    Counts up from 0 to number recursively.
    :param number: The number to which to count up.
    :return: None
    """
    if number >= 0:           # validate that number >= 0
        count_up(number-1)    # recursively handle number-1
        print(number)         # print number last


def main():
    print("counting down from 10 to 0...")
    count_down(10)
    print("counting up from 0 to 5...")
    count_up(5)


main()