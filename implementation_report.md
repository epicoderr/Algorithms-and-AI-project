**The general structure of the program**:
- board.py contains the game logic for 2048 and is thus responsible for initializing the grid, tracking the current score and other related functions.  During gameplay, the move_tiles() function is used in order to make all player moves possible. The board state is tracked during each move to make sure that only legal moves are possible.

- expectiminimax.py includes the expectiminimax search algorithm which tries to find the optimal move alongside the heuristic. This is similar to regular minimax besides that MIN is replaced by CHANCE, which finds the expected value based on where the next value will appear and if it is a 2 or 4.

- heuristic.py contains the heuristic evaluation function that is the base for the expectiminimax search. This heuristic uses three variables: the amount of empty cells, a positional weighted score using a weight matrix and smoothness, which prioritizes tiles that are close in value.

- main.py has a text based display where the user can play the game themselves as well as let the AI agent play it. The maximum depth can be changed in order to observe varying results.

**Possible shortcomings and suggestions for improvement**:
- The heuristic could certainly still be improved, as while it is pretty effective right now, I did not perform rigorous testing or anything to make sure it was perfect. One idea could be adding monoticity as a variable, which would reward rows with increasing numbers in one direction.

- In depths larger than 4, the program slows down noticeably, thus limiting its capability. Using something like a cashe to improve performance is something to consider in the future.

- Currently the presentation is just text based, and while it is probably enough for the purposes of this project one may prefer to use something like pygame to make it nicer looking.

**Achieved time and space complexities**:
- Expectiminimax has the same time complecity as minimax: O(b^m) where b is the branching factor and m is the maximum depth

**Use of large language models (ChatGPT, etc.)**:
Used the LLM Gemini for assistance at various points. Code that was directly copied should be marked.

**List of the sources**:
"AI Plays 2048" by Yun Nie (yunn), Wenqi Hou (wenqihou), Yicheng An (yicheng)