from random import randrange
from trivia import Game, PlayerOnBoard
import pytest

def test_whole_but_badly():
    not_a_winner = False

    game = Game()

    game.add('Chet')
    game.add('Pat')
    game.add('Sue')

    while True:
        game.roll(randrange(5) + 1)

        if randrange(9) == 7:
            not_a_winner = game.wrong_answer()
        else:
            not_a_winner = game.was_correctly_answered()

        if not not_a_winner: break


def test_win_on_correct_answer():
    game = Game()
    game.add("Chet")

    game.roll(randrange(5) + 1)
    winner = game.was_correctly_answered()

    assert winner


def test_player_on_board():
    game = Game()
    game.add("Chet")

    assert game.calc_player_on_board_position(0) == "Pop"


def test_player_on_board_value():
    assert PlayerOnBoard(0).raw == 0
    assert PlayerOnBoard(0).category == "Pop"


def test_player_on_board_out_of_bounds():
    with pytest.raises(ValueError):
        PlayerOnBoard(13)

    with pytest.raises(ValueError):
        PlayerOnBoard(-1)