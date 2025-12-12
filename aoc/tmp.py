import utils.grid as g
from pipe import map, chain, batched
from utils.pipefriends import add

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


def to_row(line: str):
    return [int(x) for x in line.split()]


(
    [g.parsegrid(samp, to_row)]
    | map(g.cols)
    | chain
    | chain
    | batched(3)
    | map(isvalid)
    # | tee
    | add
)  # type: ignore
