import sys
from aocd import get_data, submit

samp = """asdf"""

def solve(input: str):
    return input

if __name__ == "__main__":
    year, day = 2015, 12
    real = get_data(year=year, day=day)

    if 'print' in sys.argv:
        print(solve(samp))
    elif 'submit' in sys.argv:
        submit(solve(real), year=year, day=day)
    else:
        solve(samp)
