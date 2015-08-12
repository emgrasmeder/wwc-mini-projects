# written for python3

def get_input_integer():
    to_be_romanized = int(input("Please provide positive whole number: "))
    assert isinstance(to_be_romanized, int)
    assert to_be_romanized >= 0
    return to_be_romanized


def main(the_integer=0):
    """
    """
    assert the_integer != 0
    the_roman_num = ""
    codex = {1: "i",
             5: "v",
             10: "x",
             50: "l",
             100: "c",
             500: "d",
             1000: "m"}
    while the_integer > 0:
        for k in [1, 5, 10, 50, 100, 500, 1000][::-1]:
            while the_integer - k >= 0:
                the_integer = the_integer - k
                the_roman_num += codex[k]

    print("The roman numeral representation of {i} is: {r}"
          .format(i=the_integer, r=the_roman_num))


if __name__ == "__main__":
    the_integer = get_input_integer()
    main(the_integer)
