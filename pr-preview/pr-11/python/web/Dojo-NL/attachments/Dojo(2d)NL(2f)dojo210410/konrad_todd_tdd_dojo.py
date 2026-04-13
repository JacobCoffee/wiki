from nose.tools import assert_equals

def legal_moves(board, player):
    """
    Given a board encoded as a list of strings and a player char
    returns pairs identifying positions of legal moves for given player
    and given situation on the board.
    """
    all_directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),           (0, 1),
                      (1, -1),  (1, 0),  (1, 1)]
    moves = []
    for pos in find_pieces(board, player):
        for direction in all_directions:
            new_move = check_direction(board, pos, direction)
            if new_move is not None:
                moves.append(new_move)
    return moves

def find_pieces(board, player):
    """ find all coords for the player piece. """
    coords = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == player:
                coords.append((i, j))
    return coords

def check_direction(board, start, direction):
    enemy = {"b": "w", "w": "b"}
    row, col = start
    delta_r, delta_c = direction
    found_enemy = False
    player = board[start[0]][start[1]]
    while True:
        row, col = row + delta_r, col + delta_c
        if row >= len(board) or col >= len(board[0]):
            return None
        if board[row][col] == enemy[player]:
            found_enemy = True
        if board[row][col] == '.' and found_enemy:
            return (row, col)
        if board[row][col] == '.' and not found_enemy:
            return None
        if board[row][col] == player:
            return None

TEST_BOARD = ["....",
              ".bw.",
              ".wb.",
              "...."]

def test_simple():
    assert_equals(legal_moves(TEST_BOARD, 'w'), [(1, 0), (3, 2), (0, 1), (2, 3)])

def test_find_pieces():
    assert_equals(find_pieces(TEST_BOARD, 'b'), [(1, 1), (2, 2)],
        find_pieces(TEST_BOARD, 'b'))

def test_check_direction():
    assert_equals(check_direction(TEST_BOARD, (1, 1), (0, 1)), (1, 3))
    assert_equals(check_direction(TEST_BOARD, (1, 1), (-1, 0)), None)
    assert_equals(check_direction(TEST_BOARD, (1, 1), (0, 0)), None)

TEST_BOARD2 = ['bww']

def test_check_border():
    assert_equals(check_direction(TEST_BOARD2, (0,0), (0, 1)), None)
