
import builder
import utils
import dsl
import lambdas
import patch

from dsl import With

#patches
import python_builder
from python_builder import PythonBuilder

P = PythonBuilder(utils.identity)

# shortcuts
Then0 = P.Then0
Then = P.Then
Then1 = P.Then1
Then2 = P.Then2
Then3 = P.Then3
Then4 = P.Then4
Then5 = P.Then5
ThenAt = P.ThenAt
Read = P.Read
Write = P.Write
Val = P.Val
Pipe = P.Pipe
NPipe = P.NPipe
Make = P.Make
NMake = P.NMake
Run = P.Run
NRun = P.NRun
Obj = P.Obj
Rec = P.Rec
Context = P.Context

M = Make
"""
Abreviation for `P.Make` or `phi.Make`.
"""
NM = NMake
"""
Abreviation for `P.NMake` or `phi.Make`.
"""

########################
# Documentation
########################
import os

#set documentation

def _to_pdoc_markdown(doc):
    indent = False
    lines = []

    for line in doc.split('\n'):
        if "```" in line:
            indent = not indent
            line = line.replace("```python", '')
            line = line.replace("```", '')

        if indent:
            line = "    " + line

        lines.append(line)

    return '\n'.join(lines)

def _read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

_raw_docs = _read("README-template.md")
__version__ = _read("version.txt")
__doc__ = _to_pdoc_markdown(_raw_docs.format(__version__))
