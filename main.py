from game.board import Board
from ai.expectiminimax import expectiminimax
import time

def main():
    # Initializes the game, so creates 16 empty cells then generates 2 randomly
    game_board = Board()
    game_board.add_random_tile()
    game_board.add_random_tile()

    MAX_DEPTH = 3  

    print("Welcome to 2048!")
    game_board.display()

    while True:
        # Player chooses what action to take, so either a direction, a new game or exit
        print("\nCommands:")
        print("1: Move left")
        print("2: Move right")
        print("3: Move up")
        print("4: Move down")
        print("5: AI move")
        print("6: AI plays to end")
        print("7: New game")
        print("8: Exit")

        choice = input("Enter your choice: ").strip()

        # The directions just display the board after the choice, and the AI ones have a little text explaining what move was chosen
        if choice == "1":
            game_board.move_tiles("LEFT")
            game_board.display()
        elif choice == "2":
            game_board.move_tiles("RIGHT")
            game_board.display()
        elif choice == "3":
            game_board.move_tiles("UP")
            game_board.display()
        elif choice == "4":
            game_board.move_tiles("DOWN")
            game_board.display()
        elif choice == "5":
            value, best_move = expectiminimax(game_board, MAX_DEPTH, True)
            print(f"AI chose move: {best_move} (Evaluation: {value:.2f})")
            if best_move:
                game_board.move_tiles(best_move)
            game_board.display()
        elif choice == "6":
            print("AI will play this out")
            while game_board.has_valid_moves():
                value, best_move = expectiminimax(game_board, MAX_DEPTH, True)
                if best_move:
                    game_board.move_tiles(best_move)
                game_board.display()
                time.sleep(0.1)
            print("\nAI has finished the game.")
            continue
        elif choice == "7":
            game_board.new_game()
            game_board.add_random_tile()
            game_board.add_random_tile()
        elif choice == "8":
            print("Exiting game....")
            break
        else:
            print("Invalid command. Please try again.")
            continue


if __name__ == "__main__":
    main()