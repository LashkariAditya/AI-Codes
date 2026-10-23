# ============================================================
# ONE PLAYER TIC-TAC-TOE USING HEURISTIC FUNCTION
# X = HUMAN
# O = COMPUTER
# ============================================================

board = [" "] * 9

WINNING_POSITIONS = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6)
]


# ------------------------------------------------------------
# DISPLAY BOARD
# ------------------------------------------------------------

def display_board():
    print("\n")
    for i in range(0, 9, 3):
        print(f"  {board[i]}  |  {board[i+1]}  |  {board[i+2]}")

        if i < 6:
            print("-----|-----|-----")
    print()


# ------------------------------------------------------------
# CHECK WINNER
# ------------------------------------------------------------

def check_winner(player):
    return any(
        board[a] == board[b] == board[c] == player
        for a, b, c in WINNING_POSITIONS
    )


# ------------------------------------------------------------
# HEURISTIC FUNCTION
# ------------------------------------------------------------

def heuristic(player):
    opponent = "X" if player == "O" else "O"
    score = 0

    for a, b, c in WINNING_POSITIONS:
        line = (board[a], board[b], board[c])

        player_count = line.count(player)
        opponent_count = line.count(opponent)
        empty_count = line.count(" ")

        # Player has already won
        if player_count == 3:
            score += 100

        # Player can win in next move
        elif player_count == 2 and empty_count == 1:
            score += 10

        # Player has one symbol in the line
        elif player_count == 1 and empty_count == 2:
            score += 1

        # Opponent can win in next move
        if opponent_count == 2 and empty_count == 1:
            score -= 10

    # Center
    if board[4] == player:
        score += 3

    # Corners
    for corner in (0, 2, 6, 8):
        if board[corner] == player:
            score += 1

    return score


# ------------------------------------------------------------
# DISPLAY HEURISTIC
# ------------------------------------------------------------

def display_heuristic():
    x_score = heuristic("X")
    o_score = heuristic("O")

    print("--------------------------------")
    print("        HEURISTIC VALUES")
    print("--------------------------------")
    print("Player X Score:", x_score)
    print("Computer O Score:", o_score)

    if x_score > o_score:
        print("Board Advantage: Player X")
    elif o_score > x_score:
        print("Board Advantage: Computer O")
    else:
        print("Board Evaluation: Balanced")

    print("--------------------------------")


# ------------------------------------------------------------
# CHECK DRAW
# ------------------------------------------------------------

def is_draw():
    return " " not in board


# ------------------------------------------------------------
# PLAYER MOVE
# ------------------------------------------------------------

def get_player_move():
    while True:
        try:
            position = int(input("Player X, enter position (1-9): "))

            if not 1 <= position <= 9:
                print("Enter a number between 1 and 9.")
                continue

            index = position - 1

            if board[index] != " ":
                print("That position is already occupied.")
                continue

            board[index] = "X"
            return

        except ValueError:
            print("Please enter a valid number.")


# ------------------------------------------------------------
# COMPUTER MOVE
# ------------------------------------------------------------

def computer_move():
    print("\nComputer is thinking...")

    best_score = float("-inf")
    best_move = None

    for i in range(9):
        if board[i] == " ":

            # Try move
            board[i] = "O"

            # Evaluate move
            score = heuristic("O")

            # Undo move
            board[i] = " "

            if score > best_score:
                best_score = score
                best_move = i

    board[best_move] = "O"

    print("Computer selected position:", best_move + 1)
    print("Computer Heuristic Score:", best_score)


# ------------------------------------------------------------
# MAIN GAME
# ------------------------------------------------------------

def play_game():

    print("=" * 50)
    print("       ONE PLAYER TIC-TAC-TOE")
    print("       USING HEURISTIC FUNCTION")
    print("=" * 50)

    print("\nYou are Player X")
    print("Computer is Player O")

    print("\nBoard Positions:")
    print("""
      1  |  2  |  3
    -----|-----|-----
      4  |  5  |  6
    -----|-----|-----
      7  |  8  |  9
    """)

    current_player = "X"

    while True:

        display_board()

        # Make move
        if current_player == "X":
            get_player_move()
        else:
            computer_move()

        display_board()
        display_heuristic()

        # Check winner
        if check_winner(current_player):

            print("=" * 50)

            if current_player == "X":
                print("           PLAYER X WINS!")
            else:
                print("          COMPUTER WINS!")

            print("=" * 50)

            break

        # Check draw
        if is_draw():
            print("=" * 50)
            print("              GAME DRAW")
            print("=" * 50)
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"


# ------------------------------------------------------------
# START GAME
# ------------------------------------------------------------

play_game()