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
- skim for important detail
- if it's looking easy, submit answer ASAP (`make s`). If you get it wrong, you
  have a minute to debug before you can resubmit
    - 4 wrong submissions = 5 minute wait
- be able to instantly go to REPL and back
    - if using vs code: debug + debug console is best:
        - place a breakpoint at the last print statement of tmp.py
        - debug file (use keyboard shortcut)
        - examine with debugger and console
        - IMPORTANT: use a separate terminal for submitting while also
          debugging. The vs code debugger may kill other vs code terminals if
          you're not careful
    - you can also debug tests with vs code. If you're at the point of writing
      tests, you probably need to slow down and think :)
