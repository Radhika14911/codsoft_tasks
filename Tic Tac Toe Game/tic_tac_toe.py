board = [" " for _ in range(9)]

print("🎮 TIC TAC TOE AI")

player_name = input("Enter Your Name: ")
computer_name = "Computer"

print(f"\nPlayer : {player_name}")
print(f"Opponent : {computer_name}")
print()

print("Position Guide")
print("1 | 2 | 3")
print("---------")
print("4 | 5 | 6")
print("---------")
print("7 | 8 | 9")
print()


def print_board():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()


def check_winner():

    winning_combinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for combo in winning_combinations:

        if board[combo[0]] == board[combo[1]] == board[combo[2]] != " ":
            return board[combo[0]]

    return None


def minimax(is_maximizing):

    game_winner = check_winner()

    if game_winner == "O":
        return 1

    if game_winner == "X":
        return -1

    if " " not in board:
        return 0

    if is_maximizing:

        best_score = -100

        for i in range(9):

            if board[i] == " ":

                board[i] = "O"

                score = minimax(False)

                board[i] = " "

                best_score = max(score, best_score)

        return best_score

    else:

        best_score = 100

        for i in range(9):

            if board[i] == " ":

                board[i] = "X"

                score = minimax(True)

                board[i] = " "

                best_score = min(score, best_score)

        return best_score


def best_move():

    best_score = -100
    move = 0

    for i in range(9):

        if board[i] == " ":

            board[i] = "O"

            score = minimax(False)

            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    return move


current_player = "X"

for turn in range(9):

    print_board()

    if current_player == "X":

        while True:

            try:

                position = int(input(f"{player_name}, Choose position (1-9): "))
                if position < 1 or position > 9:
                    print("Please enter a number between 1 and 9.")
                    continue

                if board[position - 1] != " ":
                    print("Position already occupied!")
                    continue

                board[position - 1] = "X"
                break

            except ValueError:
                print("Invalid input! Enter a number.")

    else:

        print("🤖 Computer is thinking...")

        position = best_move()

        board[position] = "O"

        print(f"Computer chose position {position + 1}")

    winner = check_winner()

    if winner:

        print_board()

        if winner == "X":
            print(f"🎉 {player_name} Wins!")
        else:
            print(f"🤖 {computer_name} Wins!")

        break

    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

else:

    print_board()

    print("🤝 It's a Draw! Well Played.")