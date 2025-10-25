Unit testing coverage report:
Name                       Stmts   Miss Branch BrPart  Cover
------------------------------------------------------------
src\ai\__init__.py             0      0      0      0   100%
src\ai\expectiminimax.py      34      0     14      0   100%
src\ai\heuristic.py           25      0     16      0   100%
src\game\__init__.py           0      0      0      0   100%
src\game\board.py             88     11     42      1    86%
src\tests\2048_test.py       187      0      4      0   100%
src\tests\__init__.py          0      0      0      0   100%
------------------------------------------------------------
TOTAL                        334     11     76      1    96%

What was tested and how:
- Tested initial board by counting all the non-zero tiles on the board and then looks at if its exactly 2

- Tested updating a score by setting a score then updating it and seeing if it lines up

- Tested clockwise rotation by first checking a single rotation and then four rotations, checking that the direction lines up each time

- Tested the recognition of having valid moves by having a new board with clear valid moves and a full board with none

- Tested merging tiles with a base case, a base case with a rotation and a case where the order of merging was tested. It is important to note that currently up and down seem to be mixed up due to a bug, so that one failed

- Tested moving tiles with no merge but still a change by setting up a starting board where that was possible

- Tested a case where a move should be invalid due to no changes occuring by having a board where moving left changed nothing and thus no new random tiles should be created

- Tested that tiles cannot be added to a full board by setting up a full board, attempting to add a tile and confirming whether changes occured
 
- Tested if the heuristic is able to calculate the correct weighted score by giving it a test case, calculating it and then comparing it to what the heuristic says

- Tested if expectiminimax is applying the heuristic correctly by having a simple case where they are the same, and checking if that is the case

- Tested if expectiminimax is able to recognize that there are no more valid moves as MAX player by checking that the value is -infinity

- Tested if expectiminimax is able to recognize that there are no more valid moves as CHANCE player by checking that the value is the heuristic value

- Tested if the chance player calculation is correct by simulating a scenario where I can easily calculate and compare if that is the case

- Tested if an invalid direction can be done by giving an invalin input and checking what happened

- Tested that new_game functions properly by setting a score and grid and then seeing if they get reset

- Tested that get_empty and add_tile function properly by setting up and empty board and adding a tile then seeing whether it appeared respectively