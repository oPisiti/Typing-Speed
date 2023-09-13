#!/usr/bin/python3

from collections.abc import Iterable
from enum import Enum
from getch import getch
from time import time, sleep

import os
import random
import re
import sys


class Colors:
    """
    Nice colors :)
    """

    OKGREEN   = '\033[92m'
    WARNING   = '\033[93m'
    FAILRED   = '\033[91m'
    ENDC      = '\033[0m'
    BOLD      = '\033[1m'
    UPONELINE = '\033[F'


class Results(Enum):
    """ Possible values for user input and corresponding color """

    CORRECT       = Colors.OKGREEN
    WRONG         = Colors.FAILRED
    IN_PROGRESS   = Colors.BOLD
    NOT_ATTEMPTED = Colors.ENDC


class TypingSpeed():
    """ Class constants """

    WORDS_FILE_NAME = "words.txt"
    WORDS_COUNT     = 10
    CLEAR_COMMAND   = "cls" if os.name == "nt" else "clear"

    def __init__(self, file_name: str = "words.txt"):

        if file_name != TypingSpeed.WORDS_FILE_NAME: TypingSpeed.WORDS_FILE_NAME = file_name

        # Parsing the words
        try:
            self.words_list = self.read_words_from_file(TypingSpeed.WORDS_FILE_NAME)
        except FileNotFoundError as e:
            sys.exit(f"File '{WORDS_FILE_NAME}' not found") 
    
        # Choosing the words
        self.words = tuple(
                      {"word": random.choice(self.words_list), 
                       "status": Results.NOT_ATTEMPTED}
                      for _ in range(TypingSpeed.WORDS_COUNT)
                     )
        self.letter_count = sum([len(w["word"]) for w in self.words])

        self.require_space_press = False
        
        # Score specific
        self.score           = 0
        self.key_presses     = 0
        self.correct_presses = 0


    def get_and_handle_letter(self) -> None:
        """ Gets one letter at a time """

        new_char = getch()   

        # Requires a space press at the end of each word in order to go to the next
        if self.require_space_press and new_char != " ": return 

        # Space bar is the key for a new word
        if new_char == " ":
            # Setting the word to wrong if it is skipped
            if self.words[self.word_index]["status"] != Results.CORRECT:
                self.words[self.word_index]["status"] = Results.WRONG

            # Generic changes
            self.word_index   += 1
            self.letter_index  = 0
            self.require_space_press = False
            
            return

        # A keypress that is not blank space
        self.key_presses += 1

        # Correct char
        if new_char == self.words[self.word_index]["word"][self.letter_index]:
            self.words[self.word_index]["status"] = Results.IN_PROGRESS        
            self.letter_index += 1

            self.correct_presses += 1

            # Correct word
            if self.letter_index >= len(self.words[self.word_index]["word"]):
                self.words[self.word_index]["status"] = Results.CORRECT
     
                self.score += 1                
                self.require_space_press = True

                # Changing word index to indicate the end of words.
                # A loop would exit here, without the need for a space bar press
                if self.word_index == len(self.words) - 1: 
                    self.word_index += 1

        # Wrong char
        else:
            self.words[self.word_index]["status"] = Results.WRONG
            self.letter_index  = 0


    @staticmethod
    def read_words_from_file(file_name: str) -> tuple:
        """ 
        Returns a tuple containing all the words in a file.
        File must be inside the same directory as this file's.
        Raises FileNotFoundError if file is inaccessible.
        """

        file_path = os.path.join(os.path.dirname(__file__), file_name) 

        with open(file_path) as f:
            raw_data = f.read()

        return tuple(re.findall("\w+", raw_data))


    def render_frame(self) -> None:
        """ Renders a single frame """

        os.system(TypingSpeed.CLEAR_COMMAND)

        # Information
        print(f"Score:    {Colors.BOLD}{self.score}{Colors.ENDC}") 
        if self.key_presses >0:
            print(f"Accuracy: {Colors.BOLD}{100 * self.correct_presses / self.key_presses :.2f}%{Colors.ENDC}")
        else:
            print(f"Accuracy: {Colors.BOLD}0%{Colors.BOLD}")
        print()


        word = self.words[self.word_index]['word']
        
        # Words already attempted
        for i in range(self.word_index): 
            print(self.words[i]["status"].value + self.words[i]["word"] + Colors.ENDC, end=" ")
        
        # Currently attempting word
        letter_status = Results.CORRECT
        for i, letter in enumerate(self.words[self.word_index]["word"]):
            if letter_status == Results.IN_PROGRESS: letter_status = Results.NOT_ATTEMPTED
            if i == self.letter_index: letter_status = Results.IN_PROGRESS
            
            print(letter_status.value + letter + Colors.ENDC, end="")

        print(end=" ")

        # Others
        for i in range(self.word_index + 1, len(self.words)):
            print(self.words[i]["status"].value + self.words[i]["word"] + Colors.ENDC, end=" ")

        print()


    def render_gameover(self, dt: int) -> None:
        """ 
        Gameover splash screen.
        dt is the time it took to complete execution.
        """

        os.system(TypingSpeed.CLEAR_COMMAND)

        print(f'Correct words:    {Colors.BOLD}{self.score}/{len(self.words)}{Colors.ENDC}')
        print(f'Words per minute: {Colors.BOLD}{60 * self.score / dt:.2f}{Colors.ENDC}')
        
        # Getting the count of correct chars
        correct_chars = 0
        for word in self.words:
            if word["status"] == Results.CORRECT:
                correct_chars += len(word["word"])
        print(f'Chars per minute: {Colors.BOLD}{60 * correct_chars / dt:.2f}{Colors.ENDC}')

        print(f'Accuracy:         {Colors.BOLD}{100 * self.correct_presses / self.key_presses :.2f}%{Colors.ENDC}')


    def run(self) -> None:
        """ Main game loop """

        t0 = time()

        # Game Loop
        self.letter_index = 0
        self.word_index   = 0

        # Setting the status for the first word
        self.words[self.word_index]["status"] = Results.IN_PROGRESS
        
        while self.word_index < len(self.words):
            self.render_frame()
            self.get_and_handle_letter()

        t1 = time()
        self.render_gameover(t1 - t0)
        input()



if __name__ == '__main__':
    game = TypingSpeed()
    game.run()