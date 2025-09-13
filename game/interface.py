from game.board import Board
# Will probably do a text version like this for the interface for now

def game_test():
    # Initializes the game, so creates 16 empty cells then generates 2 randomly
    test = Board()
    test.new_game()
    for _ in range(2):
        test.add_random_tile()

    while True:
        # Player chooses what action to take, so either a direction, a new game or exit
        print("\nCommands:")
        print("1: Move left")
        print("2: Move right")
        print("3: Move up")
        print("4: Move down")
        print("5: New game")
        print("6: Exit")