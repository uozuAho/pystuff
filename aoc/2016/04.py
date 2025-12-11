from typing import Counter
from pipe import where, map


samp = """
aaaaa-bbb-z-y-x-123[abxyz]
a-b-c-d-e-f-g-h-987[abcde]
not-a-real-room-404[oarel]
totally-real-room-200[decoy]
"""


def tobits(line):
    spl = line.split("-")
    num, check = spl[-1].split("[")
    check = check.replace("]", "")
    return spl[:-1] + [int(num), check]


def checksum(bits):
    abc = "".join(list(bits)[:-2])
    c = Counter(abc)
    srt = sorted(c.items(), key=lambda kv: (kv[1], -ord(kv[0])), reverse=True)
    return "".join(x[0] for x in srt)[:5]


def isreal(bits):
    return bits[-1] == checksum(bits)


# list comprehesions read nice but
# - u have to name each temp result
# - they don't read like other language's pipelines
# - they don't have easy print/debugging
# sum(bits[-2]
#     for line in samp.splitlines() if line
#     for bits in tobits(line) if isreal(bits)
#     )

# I made a very simple pipe lib. it's ok but:
# - it's annoying to have to wrap it in a func
# - it's annoying to have to wrap map/filter etc in lambdas
# p.pipe(
#     samp.splitlines(),
#     lambda x: filter(lambda line: line.strip(), x),
#     lambda x: map(tobits, x),
#     lambda x: filter(isreal, x),
#     lambda x: map(lambda b: b[-2], x),
#     # p.pprint,
#     sum,
# )


def notempty(thing):
    return bool(thing)


# OK pipe is pretty sweet
sum(
    samp.splitlines()
    | where(notempty)
    | map(tobits)
    # | tee
    | where(isreal)
    | map(lambda x: x[-2])
)
