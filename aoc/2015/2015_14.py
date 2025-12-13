from collections import Counter, defaultdict
import re

samp = """
asdf can fly 22 km/s for 8 seconds, but then must rest for 165 seconds.
"""

# better solutions used reinder class that could update each second


def solve1(input: str, time_s=2503):
    trvl = {}
    for line in input.splitlines():
        if not line.strip():
            continue
        m = re.match(
            r"(.+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.",
            line,
        )
        if not m:
            raise NameError("no!")
        else:
            n, spd, dur, rest_dur = m.groups()
            t_full = int(dur) + int(rest_dur)
            num_full = time_s // t_full
            trvl[n] = num_full * int(dur) * int(spd) + int(spd) * min(
                time_s % t_full, int(dur)
            )
    return max(trvl.values())


def solve2(input: str, time_s=2503):
    stats = {}
    for line in input.splitlines():
        if not line.strip():
            continue
        m = re.match(
            r"(.+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.",
            line,
        )
        if not m:
            raise NameError("no!")
        else:
            n, spd, dur, rest_dur = m.groups()
            stats[n] = [int(x) for x in (spd, dur, rest_dur)]
    scores = Counter()
    travelled = defaultdict(int)

    def did_travel(n, s):
        dur = stats[n][1]
        rest = stats[n][2]
        total = dur + rest
        return 1 <= s % total <= dur

    for i in range(1, time_s + 1):
        for n in stats.keys():
            if did_travel(n, i):
                travelled[n] += stats[n][0]
        maxkv = max(travelled.items(), key=lambda x: x[1])
        scores[maxkv[0]] += 1
    return max(scores.values())


# if __name__ == "__main__":
#     year, day = 2015, 14
#     real = get_data(year=year, day=day)

#     if "print" in sys.argv:
#         print(solve2(samp))
#     elif "submit" in sys.argv:
#         submit(solve2(real), year=year, day=day)
#     else:
#         solve2(samp)
