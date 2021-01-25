# Skeletal Division
Skeletal Division Satisfiability Solver
This program is a SAT solver of cryptarithmetic skeletal division puzzles. It determines whether or not a given puzzle is 
satisfiable (if a solution exists). If the puzzle is deemed satisfiable, it will produce all possible solutions or
a given number of solutions if limited by the user. 

## Installation
On Eclipse:
  Install [PyDev - Python IDE for Eclipse](https://www.pydev.org/download.html) as a plug-in
  1. Open Eclipse
  2. Manage plug-ins
  3. Search for 'PyDev - Python IDE'
  4. Install
  5. Import z3 library into source code
  ```bash
from z3 import *
```
For further information on alternative z3 installation:
https://github.com/Z3Prover/z3/wiki

## Usage
  ```python
import SkeletalDivision
SkeletalDivision.skeletalDivision('FGHJ / AB == CD.E',
                                  ['KL6', 
                                   'MNP',
                                   'QR',
                                   'ST',
                                   'UV',
                                   '0'],
                                   limit = 3)
pass
```
returns:
```bash
   FGHJ / AB == CD.E
   {'FGHJ': 1365, 'AB': 14, 'CD': 97, 'E': 5, 'KL6': 126, 'MNP': 105, 'QR': 98, 'ST': 70, 'UV': 70, '0': 0}
   *** 1 solutions found in 22.0s ***
```
