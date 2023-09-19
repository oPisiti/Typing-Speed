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

This UI is only updated once the user presses a valid key.

At the end of the game loop, an outro screen is displayed, showing its main stats:
- Correct words
- WPM
- CPM
- Accuracy

## Game loop
