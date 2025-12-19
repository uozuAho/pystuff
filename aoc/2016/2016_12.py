"""
- registers a,b,c,d hold any int, start at 0
- jnz x y: if x != 0, jump y instructions
"""

from utils.input import lines


def do(instrucs: list[str], pc: int, regs: dict[str, int]):
    "do the instruction at pc"
    instruc = instrucs[pc]
    nextpc = pc + 1
    try:
        match instruc.split():
            case "cpy", x, y:
                if x in "abcd":
                    regs[y] = regs[x]
                else:
                    regs[y] = int(x)
            case "inc", x:
                regs[x] += 1
            case "dec", x:
                regs[x] -= 1
            case "jnz", x, y:
                if x in "abcd":
                    if regs[x] != 0:
                        nextpc = pc + int(y)
                else:
                    if int(x) != 0:
                        nextpc = pc + int(y)
    except Exception as e:
        print(f"Exception at pc {pc}:", instruc)
        raise e
    return nextpc


def solve(input: str):
    instrucs = lines(input)
    pc = 0
    regs = {x: 0 for x in "abcd"}
    regs["c"] = 1
    while pc < len(instrucs):
        pc = do(instrucs, pc, regs)
    return regs


testinput = """
cpy 41 a
inc a
inc a
dec a
jnz a 2
dec a
"""

# regs = solve(testinput)
# regs = solve(pyperclip.paste())
# pprint(regs)
