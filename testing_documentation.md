The testing document must include the following:

Unit testing coverage report:
Name                       Stmts   Miss Branch BrPart  Cover
------------------------------------------------------------
src\ai\__init__.py             0      0      0      0   100%
src\ai\expectiminimax.py      35     20     14      2    43%
src\ai\heuristic.py           26      2     16      2    90%
src\game\__init__.py           0      0      0      0   100%
src\game\board.py             88     12     42      3    84%
src\tests\2048_test.py       111      3      4      0    97%
src\tests\__init__.py          0      0      0      0   100%
------------------------------------------------------------
TOTAL                        260     37     76      7    83%


What was tested and how:
- Tested initial board by counting all the non-zero tiles on the board and then looks at if its exactly 2

- Tested updating a score by setting a score then updating it and seeing if it lines up

- Tested clockwise rotation by first checking a single rotation and then four rotations

- Tested the recognition of having valid moves by having a new board with clear valid moves and a full board with none

- Tested merging tiles with a base case, a base case with a rotation and a case where the order of merging was tested. It is important to note that currently up and down seem to be mixed up due to a bug, so that one failed.

- Tested a case where a move should be invalid due to no changes occuring by having a board where moving left changed nothing and thus no new random tiles should be created
 
- Tested if the heuristic is able to calculate the correct weighted score by giving it a test case, calculating it and then comparing it to what the heuristic says

- Tested if expectiminimax is applying the heuristic correctly by having a simple case where they are the same

- Tested if expectiminimax is able to recognize that there are no more valid moves by checking that the value is -infinity