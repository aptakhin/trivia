from random import randrange
from trivia import Game


def test_win_on_correct_answer():
    game = Game()
    game.add('Chet')

    game.roll(randrange(5) + 1)
    winner = game.was_correctly_answered()

    assert winner