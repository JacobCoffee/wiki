from nose.tools import assert_equals


def legal_moves(board, player):
    """
    Given a board encoded as a list of strings and a player char
    returns pairs identifying positions of legal moves for given player
    and given situation on the board.
    """
    result = []
    b = board2dict(board)
    pieces = find_color(b, player)
    for piece in pieces:
        for neighbour in  find_different_neighbours(b, piece):
            vd = valid_direction(b, piece, neighbour)
            if not vd: continue
            result.append(vd)
    return sorted(set(result))

TEST_BOARD = ["....",
              ".bw.",
              ".wb.",
              "...."]

CASE1 = [     "....",
              ".w..",
              "bww.",
              "wb.."]

CASE2 = [     ".wb",
              "w..",
              "b.."]

CASE3 = [     ".wb.",
              ".bw."]

CASE4 = [     ".bbb",
              ".bwb",
              ".bbb"]

def valid_direction(board, piece, neighbour):
    r1, c1 = piece
    r2, c2 = neighbour
    
    diff1, diff2 = r2-r1, c2-c1    
    r, c = r2, c2    
    color = board[piece]
    
    while True:
        r += diff1
        c += diff2        
        target = r,c
        
        try:
            if board[target] == '.':
                return target
            if board[target] == color:
                return
        except KeyError:
            return
        
        

def find_color(board, find_color):
    results = []
    for piece, color in board.items():
        if color == find_color:
            results.append(piece)
    results.sort()
    return results

def board2dict(board):
    d = {}
    for r, row in enumerate(board):
        for c, col in enumerate(row):
            d[(r,c)] = col
    return d

def find_different_neighbours(board,  piece):
    results = []
    
    d = board
    color = negate_color(d[piece])
    
    r, c = piece
    
    for y in (r-1, r, r+1):
        for x in (c-1, c, c+1):
            if (r,c) == (y, x): continue
            
            try:
                if d[y, x] == color:
                    results.append((y, x))
            except KeyError:
                continue
                
    return results

def negate_color(color):
    if color == 'w':
        return 'b'
    return 'w'

def test_simple():
    assert_equals(legal_moves(TEST_BOARD, "w"), [(0, 1), (1, 0), (2, 3), (3, 2)])

def test_find_color():
    assert_equals(find_color(board2dict(TEST_BOARD), 'w'), [(1,2), (2,1)])
    assert_equals(find_color(board2dict(TEST_BOARD), 'b'), [(1,1), (2,2)])

def test_find_different_neighbours():
    assert_equals(find_different_neighbours(board2dict(TEST_BOARD), (1, 1)), [(1,2), (2,1)])

def test_negate_color():
    assert_equals(negate_color('w'), 'b')
    assert_equals(negate_color('b'), 'w')
    
def test_board2dict():
    test_board = [".b", 
                  "w."]
    expected_dict = {
        (0,0): '.',
        (0,1): 'b',
        (1,0): 'w',
        (1,1): '.'
    }
    assert_equals(board2dict(test_board), expected_dict)
    
def test_valid_direction():
    test_board1 = ["..bbw"]
    assert_equals(valid_direction(board2dict(test_board1), (0,4), (0,3)), (0,1))
    
    test_board1 = ["..bbbbw"]
    assert_equals(valid_direction(board2dict(test_board1), (0,6), (0,5)), (0,1))
    
    test_board1 = ["..bw"]
    assert_equals(valid_direction(board2dict(test_board1), (0,3), (0,2)), (0,1))
    
    assert_equals(valid_direction(board2dict(TEST_BOARD), (2,2), (2,1)), (2,0))
    
    assert_equals(valid_direction(board2dict(TEST_BOARD), (1,1), (1,2)), (1,3))
    
    assert_equals(valid_direction(board2dict(TEST_BOARD), (1,1), (2,1)), (3,1))
    
    assert_equals(valid_direction(board2dict(TEST_BOARD), (2,2), (1,2)), (0,2))
    
def test_case1():
    assert_equals(legal_moves(CASE1, "b"), [(0,1),(0,2),(1,3),(2,3)])
    
def test_case2():
    assert_equals(legal_moves(CASE2, "b"), [(0,0)])
    
def test_case3():
    assert_equals(legal_moves(CASE3, "b"), [(0,0), (1,3)])
    
def test_case4():
    assert_equals(legal_moves(CASE4, "b"), [])