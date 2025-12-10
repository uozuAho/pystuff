import sys
import re
from aocd import get_data, submit

year, day = 2015, 5

raw = get_data(year=year, day=day)


def single1(line: str):
    if (
        line.count("a")
        + line.count("e")
        + line.count("i")
        + line.count("o")
        + line.count("u")
        < 3
    ):
        return False
    if not bool(re.search(r"(.)\1", line)):
        return False
    for x in ["ab", "cd", "pq", "xy"]:
        if x in line:
            return False
    return True


def single2(line: str):
    pairs = {}
    foundPair = False
    foundGap = False
    passrules = False
    for i in range(len(line)):
        if i > 0:
            pair = line[i - 1] + line[i]
            if pair in pairs:
                if pairs[pair] != i - 1:
                    foundPair = True
            else:
                pairs[pair] = i
        if i > 1:
            if line[i - 2] == line[i]:
                foundGap = True
        if foundPair and foundGap:
            passrules = True
            break
    return passrules


def solve(input: str):
    return sum(1 if single2(line) else 0 for line in input.splitlines())


if "print" in sys.argv:
    print(solve(raw))

elif "submit" in sys.argv:
    # submit works out what part to submit
    submit(solve(raw), year=year, day=day)

else:
    solve(raw)
    # breakpoint here to run/debug interactively
    # This is better in vscode than IDLE or python -i
    print("yo")


# single
# @pytest.mark.parametrize(
#     "input, expected",
#     [
#         ("xyxy", True),
#         ('abcdefeghiab', True),
#         ('aaaa', True),
#         ('qjhvhtzxzqqjkmpb', True),
#         ('xxyxx', True),
#         ('uurcxstgmygtbstg', False),
#         ('ieodomkazucvgmuy', False)
#     ]
# )
# def test_single(input, expected):
#     assert tmp.single(input) == expected
