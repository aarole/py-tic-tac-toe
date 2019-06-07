import itertools


def print_board(game_map, player=0, row=0, column=0, display=False):
    try:
        if game_map[row][column] != 0:
            print(f"({row}, {column}) is already occupied!")
            return game_map, False
        print('\n')
        column_header = "   " + "  ".join(str(i) for i in range(len(game_map)))
        print(column_header)
        if not display:
            game_map[row][column] = player
        for count, row in enumerate(game_map):
            print(count, row)
        return game_map, True
    except IndexError as e:
        print("Error: Row/Column can only be 0, 1 or 2.", e)
        return game_map, False
    except Exception as e:
        print("Something went wrong!", e)
        return game_map, False


def win(current_game):

    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return False
    # Horizontal
    for row in current_game:
        if all_same(row):
            print(f"Player {row[0]} won horizontally!")
            return True
    # Vertical
    for col in range(len(current_game)):
        check = []
        for row in current_game:
            check.append(row[col])
        if all_same(check):
            print(f"Player {check[0]} won vertically!")
            return True
    # Diagonal
    diag = []
    for ix in range(len(current_game)):
        diag.append(game[ix][ix])
    if all_same(diag):
        print(f"Player {diag[0]} won diagonally(\\)!")
        return True
    rows = range(len(current_game))
    cols = list(reversed(range(len(current_game))))
    check1 = []
    for idx in rows:
        check1.append(game[idx][cols[idx]])
    if all_same(check1):
        print(f"Player {check1[0]} won diagonally(/)!")
        return True
    return False


# TODO: Fix check for draw


def draw(current_game):
    f = False
    def all_not_zero(p):
        flag = False
        for i in p:
            if i != 0:
                flag = True
            else:
                flag = False
                break
        return flag

    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return False
    for row in current_game:
        if not all_same(row) and all_not_zero(row):
            f = True
        else:
            f = False
            break
    return f


play = True
players = [1, 2]
player_choice = itertools.cycle(players)
while play:
    game_size = int(input("What size tic tac toe game would you like to play? "))
    game = [[0 for i in range(game_size)] for i in range(game_size)]
    game_won = False
    game, _ = print_board(game, display=True)
    while not game_won:
        current_player = next(player_choice)
        print(f"Current Player: {current_player}")
        played = False
        while not played:
            column_choice = int(input("What column do you want to play? : "))
            row_choice = int(input("What row do you want to play? : "))
            game, played = print_board(game, current_player, row_choice, column_choice)
        if win(game):
            game_won = True
            again = input("The game is over. Would you like to play again? (y/n) ")
            if again.lower() == "y":
                print("Restarting")
            elif again.lower() == "n":
                print("Have a great day!")
                play = False
            else:
                print("")
        elif draw(game):
            game_won = True
            again = input("The game was a draw. Would you like to play again? (y/n) ")
            if again.lower() == "y":
                print("Restarting")
            elif again.lower() == "n":
                print("Have a great day!")
                play = False
            else:
                print("")
        else:
            game_won = False
