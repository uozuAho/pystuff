from pipe import tee
from utils.input import lines
import pyperclip as clipboard

test = """
abc
def
"""

list(lines(test) | tee)  # type: ignore
list(lines(clipboard.paste()) | tee)  # type: ignore
