from rit_lib import *


# the RIT-style struct to represent coins
Coin = struct_type("Coin",
                   (str, "name"),
                   (int, "value"))


# the RIT-style struct to represent coin rolls
CoinRoll = struct_type("CoinRoll",
                       (Coin, "coin"),
                       (int, "qty"))


def find_biggest_coin(coins, amount):
    """
    Finds the biggest coin that is smaller than the specified amount.
    :param coins: The coins from which to choose. Must be sorted from smallest
    to largest denomination.
    :param amount: The amount for which to make change.
    :return: The largest coin that is smaller than the amount.
    """
    biggest = coins[0]  # assume that the first coin is the biggest

    for i in range(1, len(coins)):
        coin = coins[i]  # get the next coin in the list
        if coin.value <= amount:  # if the value is less than the amount...
            biggest = coin        # ...it is now the biggest coin

    # make sure to return biggest (not coin...oops)
    return biggest


def make_change(coins, amount):
    """
    Given the coins, make change for the specified amount.
    :param coins: The coin denominations to use when making change.
    :param amount: The amount for which to make change.
    :return: The coin rolls containing the coins and quantities for the change.
    """
    rolls = {}  # an empty dictionary of coin denominations to coin rolls

    # continue while there is change left to be made
    while amount > 0:
        # find the biggest coin that is smaller than the amount
        coin = find_biggest_coin(coins, amount)

        # if a roll for that coin is already in the rolls dictionary
        if coin.value in rolls:
            # fetch the roll
            roll = rolls[coin.value]
        else:
            # otherwise create a new roll and add it to the dictionary with
            # the coin's value as the key (can't use the coin itself because
            # RIT-style structs can't be used as keys in a dictionary).
            roll = CoinRoll(coin, 0)
            rolls[coin.value] = roll

        # update the quantity of coins in the rolls
        roll.qty = roll.qty + 1
        # deduct the coin's value from the amount
        amount = amount - coin.value

    # copy the coin rolls into a list and return it
    new_rolls = []
    for coin in rolls:
        new_rolls += [rolls[coin]]
    return new_rolls


def main():
    """
    Prompts the user to enter a country to use for currency denomination and
    an amount for which to make change, then calculates the change and prints
    the result.
    :return:
    """

    # prompt the user for the country (coin data is in data/<country>.txt)
    coin_filename = "data/" + input("Enter country: ") + ".txt"

    # create an empty list to hold the coins
    coins = []
    # loop through the lines in the file
    coin_file = open(coin_filename, 'r')
    for line in coin_file:
        # use the coin data to create a new coin and add it to the list of
        # coins
        line = line.strip()    # name<space>value
        tokens = line.split()  # [name, value]
        coin = Coin(tokens[0], int(tokens[1]))
        coins += [coin]

    # at this point the coins should be sorted by value from smallest to
    # largest, but I'm cheating by putting them in the currency file in sorted
    # order to start.

    # prompt the user to enter the amount for which to make change
    amount = int(input("Enter amount: "))

    # make the change
    rolls = make_change(coins, amount)
    # print the rolls
    for roll in rolls:
        print(roll)


if __name__ == '__main__':
    main()