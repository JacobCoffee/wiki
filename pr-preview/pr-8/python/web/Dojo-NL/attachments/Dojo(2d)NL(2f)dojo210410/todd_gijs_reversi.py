
directions = [(-1, -1), (-1, 0), (-1, 1),
              (0, -1),           (0, 1),
              (1, -1 ), (1, 0), (1, 1)]

switch = { 'b': 'w', 'w': 'b'}


def legal_moves(board, player):
    stones = find_pieces(board, player)
    moves = []
    for stone in stones:
        moves += (find_valid_paths(board, stone))
    return set(moves)


def find_pieces(board, colour):
    l = []
    for (i, col) in enumerate(board):
        for (j, row) in enumerate(col):
            if row == colour:
                l.append((i,j))
    return set(l)


def check_direction(board, start, direction):
    (row, col) = start
    me = board[row][col]

    if me == ".":
        return

    other = switch[me]
    between = False

    while True: 
        row += direction[0]
        col += direction[1]

        if row < 0 or col < 0 or row > len(board)-1 or col > len(board[0])-1:
            break

        checked = board[row][col]

        if  checked == other:
            between = True
            continue
        elif checked == "." and between:
            return (row, col)
        else:
            return


def find_valid_paths(board, position):
    coords = []
    for direction in directions:
        result = check_direction(board, position, direction)
        if result:
            coords.append(result)
    return set(coords)

