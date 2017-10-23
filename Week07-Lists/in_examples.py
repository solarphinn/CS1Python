def is_it_in(sequence, target):
    if target in sequence:
        print(target, "is in", sequence)
    else:
        print(target, "not found in", sequence)


def test_is_it_in():
    string = "abcdef"
    is_it_in(string, "a")  # single character; beginning
    is_it_in(string, "b")  # single character; middle
    is_it_in(string, "f")  # single character, end
    is_it_in(string, "bcd")  # multiple characters
    is_it_in(string, "bdf")  # multiple characters

    a_list = [1, 2, 3, 4, 5]
    is_it_in(a_list, 1)  # single element; beginning
    is_it_in(a_list, 3)  # single element; middle
    is_it_in(a_list, 5)  # single element; end
    is_it_in(a_list, [1, 2, 3])  # multiple elements


def main():
    test_is_it_in()


main()
