from itertools import batched


def expand(a: str):
    b = ''.join(reversed(a))
    b = b.replace('1','2').replace('0','1').replace('2','0')
    return a + "0" + b

assert expand('1') == '100'
assert expand('0') == '001'
assert expand('11111') == '11111000000'


def expandto(a: str, n: int):
    while len(a) < n:
        a = expand(a)
    return a


assert expandto('10000', 20) == '10000011110010000111110'


def checksum(a: str):
    while len(a) % 2 == 0:
        a = ''.join('1' if a == b else '0' for a, b in batched(a, 2))
    return a

assert checksum('110010110100') == '100'


def solve(input: str, n: int):
    init = expandto(input, n)
    return checksum(init[:n])


assert solve('10000', 20) == '01100'
# solve('11101000110010100', 272)
# solve('11101000110010100', 35651584)
