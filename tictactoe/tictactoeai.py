import math

human_score = 0
ai_score = 0
draws = 0

board = [" " for _ in range(9)]

def print_board():

    print()

    for i in range(9):

        print(board[i], end="")

        if (i + 1) % 3 == 0:
            print()

            if i < 6:
                print("---------")

        else:
            print(" | ", end="")

    print()

def check_winner(player):

    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]

    for condition in win_conditions:

        if all(board[i] == player for i in condition):
            return True

    return False

def is_draw():
    return " " not in board

def minimax(is_maximizing):

    if check_winner("O"):
        return 1

    if check_winner("X"):
        return -1

    if is_draw():
        return 0

    if is_maximizing:

        best_score = -math.inf

        for i in range(9):

            if board[i] == " ":

                board[i] = "O"

                score = minimax(False)

                board[i] = " "

                best_score = max(score, best_score)

        return best_score

    else:

        best_score = math.inf

        for i in range(9):

            if board[i] == " ":

                board[i] = "X"

                score = minimax(True)

                board[i] = " "

                best_score = min(score, best_score)

        return best_score

def ai_move():

    best_score = -math.inf
    best_move = -1

    for i in range(9):

        if board[i] == " ":

            board[i] = "O"

            score = minimax(False)

            board[i] = " "

            if score > best_score:
                best_score = score
                best_move = i

    board[best_move] = "O"

def human_move():

    while True:

        try:

            position = int(input("Enter position (1-9): ")) - 1

            if position in range(9) and board[position] == " ":
                board[position] = "X"
                break

            else:
                print("Invalid or occupied position!")

        except:
            print("Please enter a valid number!")

def play_game():

    global human_score, ai_score, draws, board

    board = [" " for _ in range(9)]

    print("\n===== TIC-TAC-TOE AI =====")
    print("You = X | AI = O")

    print_board()

    while True:

        human_move()
        print_board()

        if check_winner("X"):
            print("You Win!")
            human_score += 1
            break

        if is_draw():
            print("Match Draw!")
            draws += 1
            break

        print("AI is thinking...")

        ai_move()
        print_board()

        if check_winner("O"):
            print("AI Wins!")
            ai_score += 1
            break

        if is_draw():
            print("Match Draw!")
            draws += 1
            break

    print(f"\nScoreboard -> You: {human_score} | AI: {ai_score} | Draws: {draws}")

while True:

    play_game()

    again = input("\nPlay again? (y/n): ").lower()

    if again != "y":
        print("Thanks for playing!")
        break
