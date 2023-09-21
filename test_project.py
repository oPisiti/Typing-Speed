import pytest
from typing_speed import *


def test_read_words():
    with pytest.raises(FileNotFoundError):
        read_words_from_file("words.py")
    
    assert type(read_words_from_file("words.txt")) == tuple

def test_count_words():
    assert count_words(read_words_from_file("words.txt")) == 1001

def test_get_words():
    game_object = TypingSpeed()

    chosen_words = set(get_chosen_words(game_object))
    
    assert chosen_words.issubset(set(read_words_from_file("words.txt")))