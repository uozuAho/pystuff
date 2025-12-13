import re

year, day = 2015, 11

# real = get_data(year=year, day=day)

# samp = real


# increment one character
def incr_one(str, i):
    nextchar = ord(str[i]) + 1
    if nextchar == 105 or nextchar == 108 or nextchar == 111:
        nextchar += 1
    if nextchar == 123:
        nextchar = 97
    return str[:i] + chr(nextchar) + str[i + 1 :]


# increment a string
def incr(str, i=None):
    if i == -1:
        return "a" + str
    if not i:
        i = len(str) - 1
    str = incr_one(str, i)
    if str[i] == "a":
        return incr(str, i - 1)
    return str


def has3(x: str):
    for i in range(2, len(x)):
        o = ord(x[i])
        if ord(x[i - 2]) == o - 2 and ord(x[i - 1]) == o - 1:
            return True
    return False


def has2pair(x):
    return len(re.findall(r"(.)\1", x)) > 1


def isvalid(passw: str):
    return has3(passw) and not any(x in passw for x in "iol") and has2pair(passw)


def solve(input: str):
    incr_count = 0
    try:
        while not isvalid(input):
            input = incr(input)
            incr_count += 1
    except KeyboardInterrupt:
        pass
    print()
    print(incr_count)
    return input


if __name__ == "__main__":
    assert not isvalid("hijklmmn")
    assert not isvalid("abbceffg")
    assert not isvalid("abbcegjk")
    assert isvalid("abcdffaa")
    assert isvalid("ghjaabcc")
    assert solve("abcdefgh") == "abcdffaa"

    # if "print" in sys.argv:
    #     print(solve(samp))
    # elif "submit" in sys.argv:
    #     submit(solve(real), year=year, day=day)
    # else:
    #     solve(samp)
