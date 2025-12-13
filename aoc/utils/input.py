def linesitr(input: str):
    for line in input.splitlines():
        if line.strip():
            yield line


def lines(input: str):
    return list(linesitr(input))


def transpose(lines: list):
    return zip(*lines)
