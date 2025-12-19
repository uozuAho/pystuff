# My advent of code solutions

# Quick start
- install uv, make
- clone repo
- run `uv sync`
- save your AOC session cookie to `/home/$USER/.config/aocd/token`
- set the year and day in tmp.py
- check make rules work. See Makefile

# how to go fast
- have ready
    - up to date session token
    - check make rules work. See Makefile. Install required python versions.
    - tmp.py and test_tmp.py open in vs code, have the debugger ready on
      keyboard shortcut
    - pypy (`make pp`). Just in case - set the python version to 3.11 in
      pyproject.toml
- skim for important detail
- if it's looking easy, submit answer ASAP (`make s`). If you get it wrong, you
  have a minute to debug before you can resubmit
    - 4 wrong submissions = 5 minute wait
- be able to instantly go to REPL and back
    - vs code's rich REPL is great: shift+enter to send a chunk of code to the
      REPL
- be able to step-by-step debug: vs code's python debugger is great
- more important in later/difficult puzzles: don't rush. Assert early and often -
  it takes more time to fix bugs the later you find them.
