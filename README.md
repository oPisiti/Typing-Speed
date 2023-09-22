# Typing-Speed

#### Video Demo:  <URL HERE>
#### Description:
A command line typing speed test.

![README](https://github.com/oPisiti/Typing-Speed/assets/78967454/c6fa61fd-d9c8-41db-819a-950b3d7a691a)


## Usage
``` python
python3 typing_speed
```

## Available words
Everytime the script is executed, it reads all the words, one per line, contained in "words.txt".

Then, it chooses (at random) 10 of these, which will be the prompts for the game.

This file contains the 1000 most frequent words of the english language.

Feel free to modify and add your own!

This file name can be changed inside the main function.

## UI
The main screen displays the following:
- Score
- Current accuracy
- Words to be typed

This UI is only updated once the player presses a valid key.

At the end of the game loop, an outro screen is displayed, showing its main stats:
- Correct words
- WPM
- CPM
- Accuracy

## Game loop
This script serves a frame only when the player presses a valid (alphanumeric) key. Therefore, it is extremely lightweight.

The currently expected letter is always rendered in bold.

Correctly typed letters are rendered in green.

Unattempted letters are rendered in white.

At the end of each word, the player must press the space bar in order to move to the next. 
All other keys will be disconsidered.
This prevents the player from accidently pressing the wrong key of the next word, given the flow of the game.

When the player misses a letter in the middle of a word, they are moved back to the start of such word.
Therefore, for a word to be accepted, it must be correctly typed from start to finish.

## Design
This core of this script is a class called "TypingSpeed". 

I have a preference for OOP as it provides great encapsulation.
I find it creates a more readable and organized code. 
This is specially in python, which is quite flexible and relies heavily on conventions.
Therefore, it is easy to mistakenly use a wrong and simmilarly named function, which will raise exceptions.

Having said that, I realize bare functions would have been suffice for this project and the use of classes introduced some boilerplate to the code.
