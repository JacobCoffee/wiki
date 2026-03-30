
import reversi

from nose.tools import assert_equals

TEST_BOARD = ["....",
              ".bw.",
              ".wb.",
              "...."]

TEST_BOARD2 = ['....',
               '.w..',
               'bww.',
               'wb..']


def test_simple():
    assert_equals(reversi.legal_moves(TEST_BOARD, "w"), set([(0, 1), (1, 0), (2, 3), (3, 2)]))
    assert_equals(reversi.legal_moves(TEST_BOARD2, "w"), set([(1, 0), (3, 2)]))

def test_find_pieces():
    assert_equals(reversi.find_pieces(TEST_BOARD, 'b'), set([(1, 1), (2, 2)]))
    assert_equals(reversi.find_pieces(TEST_BOARD, 'w'), set([(2, 1), (1, 2)]))
    assert_equals(reversi.find_pieces(TEST_BOARD2, 'b'), set([(2, 0), (3, 1)]))

def test_check_direction():
    assert_equals(reversi.check_direction(TEST_BOARD, (1, 1), (0, 1)), (1, 3))
    assert_equals(reversi.check_direction(TEST_BOARD, (2, 2), (-1, -1)), None)
    assert_equals(reversi.check_direction(TEST_BOARD, (2, 1), (1, 0)), None)
    assert_equals(reversi.check_direction(TEST_BOARD, (2, 1), (-1, 0)), (0, 1))
    assert_equals(reversi.check_direction(TEST_BOARD2, (2, 0), (0, 1)), (2, 3))
    assert_equals(reversi.check_direction(TEST_BOARD2, (2, 0), (0, -1)), None)

def test_find_valid_paths():
    assert_equals(reversi.find_valid_paths(TEST_BOARD, (1, 1), ), set([(1, 3), (3, 1)]))
    assert_equals(reversi.find_valid_paths(TEST_BOARD, (1, 2)), set([(1, 0), (3, 2)]))
    assert_equals(reversi.find_valid_paths(TEST_BOARD, (2, 1)), set([(2, 3), (0, 1)]))
    assert_equals(reversi.find_valid_paths(TEST_BOARD, (2, 2)), set([(2, 0), (0, 2)]))
    assert_equals(reversi.find_valid_paths(TEST_BOARD2, (2, 0)), set([(2, 3), (0, 2)]))
    assert_equals(reversi.find_valid_paths(TEST_BOARD2, (2, 1)), set([]))

if __name__ == '__main__':
    import nose
    nose.run()
