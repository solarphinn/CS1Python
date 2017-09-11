def dog_years(years):
    """
    Calculate's a dog's age in dog years based on its age in human years.
    :param years: The age of the dog in human years.
    :return: The age of the dog in dog years.
    """
    # first year = 15
    # second year = 9
    # other years = +5 each

    if years == 1:
        return 15
    elif years == 2:
        return 9 + 15
    else:
        return 5 * (years - 2) + 15 + 9


def dog_years_rec(years):
    """
    Recursively calculate's a dog's age in dog years based on its age in human
    years using the formula:
    F(1) = 15
    F(2) = 9 + F(1)
    F(N) = 5 + F(N-1)
    :param years: The dog's age in human years.
    :return: The dog's age in dog years.
    """
    if years == 1:
        return 15
    elif years == 2:
        return 9 + dog_years_rec(years - 1)
    else:
        return 5 + dog_years_rec(years - 1)


def dog_years_tail(years, age):
    """
    Recursively calculates a dog's age in dog years using tail recursion.
    :param years: The dog's age in human years.
    :param age: The cumulative age in dog years at the current recursion depth.
    :return: The total age in dog years.
    """
    if years == 1:
        return 15 + age
    elif years == 2:
        return dog_years_tail(years - 1, 9 + age)
    else:
        return dog_years_tail(years - 1, 5 + age)


def main():
    print(dog_years(12))
    print(dog_years(6))
    print(dog_years_rec(12))
    print(dog_years_rec(6))
    print(dog_years_tail(12, 0))
    print(dog_years_tail(6, 0))

main()
