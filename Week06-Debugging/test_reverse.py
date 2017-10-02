import reverse


def test_reverse(string, expected):
    rev = reverse.reverse(string)
    if rev != expected:
        print("reverse on '", string, "' failed; should have been:", expected,
              "but was: ", rev)


def test_empty():
    test_reverse("", "")


def test_single():
    test_reverse("a", "a")


def test_two():
    test_reverse("ab", "ba")


def test_lots():
    test_reverse("A man, a plan, a canal. Panama!",
                 "!amanaP .lanac a ,nalp a ,nam A")


def test_all():
    test_empty()
    test_single()
    test_two()
    test_lots()


def main():
    test_all()

main()