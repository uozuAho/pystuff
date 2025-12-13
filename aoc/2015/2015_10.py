year, day = 2015, 5

# real = get_data(year=year, day=day)

# samp = real
samp = """1"""


def one(chars: str):
    prev = None
    count = 0
    out = ""
    for c in chars:
        if not prev or prev == c:
            count += 1
        elif c != prev:
            out += str(count) + prev
            count = 1
        prev = c
    if count > 0:
        out += str(count) + str(prev)
    return out


def solve(input: str):
    out = "1113122113"
    for i in range(50):
        out = one(out)
    return len(out)


# if "print" in sys.argv:
#     print(solve(samp))

# elif "submit" in sys.argv:
#     submit(solve(real), year=year, day=day)

# else:
#     solve(samp)
#     # breakpoint here to run/debug interactively
#     # This is better in vscode than IDLE or python -i
#     print("yo")
