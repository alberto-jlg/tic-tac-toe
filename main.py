BOARD = [[0,0,0],[0,0,0],[0,0,0]]
PLAYER = [1]

"""
HELPER: Prints out the board to the screen with the format
X O X
O X O
O X O
"""
def display_board():
    for row in BOARD:
        for square in row:
            if square == 0:
                print("-", end=" ")
            elif square == 1:
                print("X", end=" ")
            else: # square==2
                print("O", end=" ")
        print() # newline


# HELPER
def check_valid_move(square):
    return 0 <= square < 9 and BOARD[square // 3][square % 3] == 0


def get_next_player():
    def helper_get_next_player(player):
        if player[0] == 1:
            player[0] = 2
            return 2
        else:
            player[0] = 1
            return 1

    return helper_get_next_player(PLAYER)

"""
notes on the status
0 : continue playing
1 : victory for player
2 : tie
"""
def check_endgame(player): # naive approach
    # check column win
    for i in range(0, 3):
        if BOARD[0][i] == player and BOARD[1][i] == player and BOARD[2][i] == player:
            return 1

    # check row win
    for i in range(0, 3):
        if BOARD[i][0] == player and BOARD[i][1] == player and BOARD[i][2] == player:
            return 1

    # check diagonals
    if BOARD[0][0] == player and BOARD[1][1] == player and BOARD[2][2] == player:
        return 1

    if BOARD[2][0] == player and BOARD[1][1] == player and BOARD[0][2] == player:
        return 1

    # check if all the board is full
    for i in range(len(BOARD)):
        for j in range(len(BOARD[0])):
            if BOARD[i][j] == 0:  # there are still moves possible
                return 0

    return 2  # code for board full

def end_game():
    def reset_board(board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = 0

    option = input("Do you want to play another game? (y/n): ")
    if option.lower() == "y":
        reset_board(BOARD)
        return play(1)
    else:
        print("Bye!")
        return 0

def make_move(player, square):
    BOARD[square // 3][square % 3] = player  # player is either 1 or 2.

# Requests the user for a next move, validates it, makes the move and checks for win.
def play(pPlayer):
    player = pPlayer
    display_board()
    square = int(input(f"Player {player}, enter your next move: ")) - 1
    if check_valid_move(square):
        make_move(player, square)
        status = check_endgame(player)
        if status == 1:
            display_board()
            print(f"Player {player} has won!")
            return end_game()
        if status == 2:
            display_board()
            print("The game is a tie!")
            return end_game()
    else:
        print("That was not a valid move. Please try again.")
    play(get_next_player())


if __name__ == "__main__":
    play(1)
