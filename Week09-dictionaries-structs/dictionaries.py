

my_dict = {}

my_dict[10] = "foo"

my_dict["bar"] = True

my_dict[3.14] = "A Butterfly"

print(my_dict)

print(my_dict[3.14])

for key in my_dict:
    print(my_dict[key])

# crashes with KeyError
# print(my_dict["not there"])

