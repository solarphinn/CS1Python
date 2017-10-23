import collections


a_tuple = (1 , 3.14, True, "a string", ["a", "list"])
print(a_tuple)

# crashes
# a_tuple[1] = 6.28

print(a_tuple[0])

for item in a_tuple:
    print(item)


# named tuples

card = collections.namedtuple("Card", ["suit", "value"])

aos = card("Spades", 1)

eoc = card("Clubs", 8)

print(eoc)
print(eoc.suit)
print(eoc.value)

eoh = card(True, [1, 2, 3])  # this is OK as far as Python is concerned

print(eoh.value)