# Riddle Game for Dyslexic students using Handwritten Digit Recognition
# First Edition

## Overview

The program opens a game window with all the instructions mentioned. The user plays against the computer called Arjun Bot and can manually select the number of rounds of the game. In each round Arjun Bot asks the player a small riddle and the player can also listen to the question if he/she finds it difficult to read. The player has to draw the answer in the given box, with each digit in separate box. The correct answer is shown to the user after submission and he/she can read/listen the answer. The final score and winner is displayed then.

## Open Source Model
Python libraries used
1. Opencv
2. Keras
3. Tkinter
4. Numpy
5. Pyscreenshot
6. Tensorflow 
7. PIL
8. Pandas
9. playsound

## Design

The game is written in a python file called "Riddle.py"

1. The first page gives the user option to play or know about the developer.
2. If user presses play button, the program asks for the user's details and evalutes the answer, if successful takes the user to the play page else asks them to correct it.
3. Then the user is asked one question in every round and the number of rounds is selected by the user.
4. The user can both read and listen the questions.
5. Also the user is provided a canvas divided into boxes so that he/she can draw each digit of the answer in individual box.
6. Then the user is shown the answer which he/she can read and listen.
7. Then the score is evaluted and the name of the winner is displayed.

## Important Files

1. Riddle.py - This is the front end file, the main project file.
2. DigitRecognition.h5 - This is the backend deep learning model for handwritten digit recognition.

## Report

The first edition is doing good when the user draws the digit neatly and within the given box. The accuracy of prediction is 98.8% .

## Need Update

The project is the second edition. I will keep update.
