

def count_down(number):
    if number >= 0:
        print(number)
        count_down(number-1)

def count_up(number):
    if number >= 0:
        count_up(number-1)
        print(number)

count_up(5)