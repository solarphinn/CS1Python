def reverse(string):
    if string == "":
        return ""
    else:
        head = string[0]
        tail = string[1:]
        return reverse(tail) + head
