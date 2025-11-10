import itertools
import sys
from aocd import get_data, submit

foundstuff = """children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1"""

# 373
def solve1(input: str):
    fstff = {}
    for line in foundstuff.splitlines():
        spl = line.split()
        fstff[spl[0][:-1]] = int(spl[1])

    aunthave = []
    cands = []
    for line in input.splitlines():
        if not line.strip(): continue
        aftername = ''.join(line.split(':')[1:])
        aftername = aftername.replace(',', '')
        aunthave.append({x: int(y) for x, y in itertools.batched(aftername.split(), 2)})
        cand = True
        for k in fstff.keys():
            if k in aunthave[-1] and aunthave[-1][k] != fstff[k]:
                cand = False
                break
        if cand:
            cands.append(len(aunthave))

    print(cands)

# 260
def solve2(input: str):
    fstff = {}
    for line in foundstuff.splitlines():
        spl = line.split()
        fstff[spl[0][:-1]] = int(spl[1])

    aunthave = []
    cands = []
    for line in input.splitlines():
        if not line.strip(): continue
        aftername = ''.join(line.split(':')[1:])
        aftername = aftername.replace(',', '')
        aunthave.append({x: int(y) for x, y in itertools.batched(aftername.split(), 2)})
        cand = True
        for k in fstff.keys():
            if k == 'cats' or k == 'trees':
                if k in aunthave[-1] and aunthave[-1][k] <= fstff[k]:
                    cand = False
                    break
            elif k == 'pomeranians' or k == 'goldfish':
                if k in aunthave[-1] and aunthave[-1][k] >= fstff[k]:
                    cand = False
                    break
            elif k in aunthave[-1] and aunthave[-1][k] != fstff[k]:
                cand = False
                break
        if cand:
            cands.append(len(aunthave))

    print(cands)

if __name__ == "__main__":
    year, day = 2015, 16
    real = get_data(year=year, day=day)
    samp = real

    if 'print' in sys.argv:
        print(solve1(samp))
    elif 'submit' in sys.argv:
        submit(solve1(real), year=year, day=day)
    else:
        solve1(samp)
