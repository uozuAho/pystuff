from dataclasses import dataclass, field
from utils.input import lines
from utils.assertions import assertt
import pyperclip
import re

test = """
value 5 goes to bot 2
bot 2 gives low to bot 1 and high to bot 0
value 3 goes to bot 1
bot 1 gives low to output 1 and high to bot 0
bot 0 gives low to output 2 and high to output 0
value 2 goes to bot 2
"""


def log(*msg):
    # print(*msg)
    pass


@dataclass
class Node:
    label: str
    inputs: list[int] = field(default_factory=list)
    clo: Node | None = None
    chi: Node | None = None


# TODO: add to utils
def get_or_add(d: dict, key, value=None):
    if key in d:
        return d[key]
    else:
        d[key] = value
    return value


def find(input: str, goal: set[int]):
    conn: dict[str, Node] = {}
    goalnode = None

    def addval(node: Node, val: int):
        nonlocal goalnode
        assertt(len(node.inputs) < 2)
        node.inputs.append(val)
        # if set(node.inputs) == goal:
        #     goalnode = node
        #     log("goal node", goalnode)
        #     return
        log("addval", val, node)
        if len(node.inputs) == 2:
            lo, hi = sorted(node.inputs)
            if node.clo:
                addval(node.clo, lo)
            if node.chi:
                addval(node.chi, hi)

    for i, line in enumerate(lines(input)):
        log(line)
        vals = re.findall(r"\d+", line)
        if len(vals) == 2:
            val, label = vals
            node = get_or_add(conn, label, Node(label))
            addval(node, int(val))
            log(node)
        elif len(vals) == 3:
            a, b, c = vals
            nodea = get_or_add(conn, a, Node(a))
            blabel = b if "low to bot" in line else "out-" + b
            clabel = c if "high to bot" in line else "out-" + c
            nodeb = get_or_add(conn, blabel, Node(blabel))
            nodec = get_or_add(conn, clabel, Node(clabel))
            log(nodea)
            assertt(nodea.clo is None)
            assertt(nodea.chi is None)
            nodea.clo = nodeb
            nodea.chi = nodec
            log(nodea)
            if nodea.clo and nodea.chi and len(nodea.inputs) == 2:
                lo, hi = sorted(nodea.inputs)
                addval(nodea.clo, lo)
                addval(nodea.chi, hi)
        # part 1
        if goalnode:
            return goalnode
        # part 2
        if all("out-" + str(x) in conn for x in (0, 1, 2)):
            print(conn["out-0"].inputs)
            print(conn["out-1"].inputs)
            print(conn["out-2"].inputs)


# FINALLLYYYYYY
# issue1: I'm dumb
# issue2: careful about printing recursive structures: can go forever
# find(test, {2, 5})
find(pyperclip.paste(), {61, 17})
# print(a.label, a.inputs)
# print("done")

# TODO: understand norvig's solution
# TODO: try functional/pipe? style
