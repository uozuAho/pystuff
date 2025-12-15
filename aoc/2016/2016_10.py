from dataclasses import dataclass, field

from pipe import map, where, Pipe

from utils.basic import get_or_add
from utils.input import lines
from utils.assertions import assertt
import re

LOG_ENABLED = False

test = """
value 5 goes to bot 2
bot 2 gives low to bot 1 and high to bot 0
value 3 goes to bot 1
bot 1 gives low to output 1 and high to bot 0
bot 0 gives low to output 2 and high to output 0
value 2 goes to bot 2
"""


def log(*msg):
    if LOG_ENABLED:
        print(*msg)


@dataclass
class Node:
    label: str
    inputs: list[int] = field(default_factory=list)
    clo: Node | None = None
    chi: Node | None = None

    def __str__(self):
        clo = "" if self.clo is None else self.clo.label
        chi = "" if self.chi is None else self.chi.label
        return f"{self.label} {self.inputs} -{clo} -{chi}"


def find(input: str, goalbot: set[int] = None, goalouts: set[int] = None):
    conn: dict[str, Node] = {}
    goalnode = None

    def addval(node: Node, val: int):
        nonlocal goalnode
        assertt(len(node.inputs) < 2)
        node.inputs.append(val)
        if set(node.inputs) == goalbot:
            goalnode = node
            log("goal node", goalnode)
            return
        # log("addval", val, node)
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
        if goalouts and all("out-" + str(x) in conn for x in goalouts):
            outs = [conn["out-" + str(x)] for x in goalouts]
            if all(o.inputs for o in outs):
                return [o.inputs[0] for o in outs]


def test_part1():
    node = find(test, {2, 5})
    assert node.label == "2"


def test_part2():
    outvals = find(test, None, {0})
    assert outvals == [5]


# TODO: try functional/pipe? style
# I hate my solution. Took so much debugging and was hard to iterate.
# Will functional dev make it easier?


def parse_conn_labels(line: str):
    patt = r"bot (\d+) gives low to (\w+) (\d+) and high to (\w+) (\d+)"
    m = re.search(patt, line)
    assertt(m is not None)
    bfrom, lotype, lonum, hitype, hinum = m.groups()
    return (
        bfrom,
        lonum if lotype == "bot" else "out-" + lonum,
        hinum if hitype == "bot" else "out-" + hinum,
    )


def addconn(conn: dict[str, Node], fromname, loname, hiname):
    fromn = get_or_add(conn, fromname, Node(fromname))
    fromn.clo = get_or_add(conn, loname, Node(loname))
    fromn.chi = get_or_add(conn, hiname, Node(hiname))
    return conn


@Pipe
def reduce(iterable, acc, func):
    for i in iterable:
        acc = func(acc, i)
    return acc


def make_graph(input: str):
    return (
        lines(input)
        | where(lambda x: x.startswith("bot "))
        | map(parse_conn_labels)
        | reduce({}, lambda acc, x: addconn(acc, x[0], x[1], x[2]))
    )


def parseval(line: str):
    return re.findall(r"\d+", line)


def addval(conn: dict[str, Node], val: str, bot: str):
    node = get_or_add(conn, bot, Node(bot))
    assertt(len(node.inputs) < 2)
    node.inputs.append(int(val))
    return conn


(
    lines(test)
    | where(lambda x: x.startswith("value"))
    | map(parseval)
    | reduce(make_graph(test), lambda acc, x: addval(acc, x[0], x[1]))
)


# GIVE UP: The functional approach reads OK, but I think this is because
# I understand the problem better. Reduce works, but is hard to read.
# Eg. a less functional make_graph is still short and is easy to read:
def make_graph2(input: str):
    graph = {}
    for line in lines(input):
        if line.startswith("bot "):
            from_bot, to_low, to_high = parse_conn_labels(line)
            addconn(graph, from_bot, to_low, to_high)
