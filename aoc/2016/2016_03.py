import utils.pipe as p
import utils.grid as g
import itertools

samp = """
  330  143  338
  769  547   83
  930  625  317
  669  866  147
   15  881  210
  662   15   70
"""


def isvalid(trpl):
    s = sorted(trpl)
    return s[0] + s[1] > s[2]


p.pipe(
    g.parsegrid(samp, lambda line: [int(n) for n in line.split()]),
    g.cols,
    p.flatten,
    lambda x: itertools.batched(x, 3),
    # pprint,
    lambda x: map(isvalid, x),
    sum,
)
