import re


def exp1(chars: str):
    chars = re.sub(r"\s+", "", chars)
    out = []
    i = 0
    while i < len(chars):
        c = chars[i]
        if c != "(":
            out.append(c)
            i += 1
        else:
            m = re.search(r"(\d+)x(\d+)", chars[i:])
            numchars, repeat = [int(x) for x in m.groups()]
            i += m.end() + 1
            out.extend(chars[i : i + numchars] * repeat)
            i += numchars
    return "".join(out)


exp1("as  df  ")
exp1("A(1x5)BC")
exp1("(3x3)XYZ")
exp1("A(2x2)BCD(2x2)EFG")
exp1("(6x1)(1x3)A")
len(exp1("X(8x2)(3x3)ABCY"))


# part 1
# len(exp1(pyperclip.paste()))


def expfull(chars: str):
    chars = re.sub(r"\s+", "", chars)
    outlen = 0
    i = 0
    while i < len(chars):
        c = chars[i]
        if c != "(":
            outlen += 1
            i += 1
        else:
            m = re.search(r"(\d+)x(\d+)", chars[i:])
            numchars, repeat = [int(x) for x in m.groups()]
            i += m.end() + 1
            outlen += repeat * expfull(chars[i : i + numchars])
            i += numchars
    return outlen


expfull("(3x3)XYZ")
expfull("X(8x2)(3x3)ABCY")
expfull("(27x12)(20x12)(13x14)(7x10)(1x12)A")
expfull("(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN")

# pt2
# expfull(pyperclip.paste())
