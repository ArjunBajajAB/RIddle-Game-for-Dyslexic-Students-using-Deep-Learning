# Riddle Game for Dyslexic students using Handwritten Digit Recognition
# First Edition

## Overview

The program opens a game window with all the instructions mentioned. The user plays against the computer called Arjun Bot and can manually select the number of rounds of the game. In each round Arjun Bot asks the player a small riddle and the player can also listen to the question if he/she finds it difficult to read. The player has to draw the answer in the given box, with each digit in separate box. The correct answer is shown to the user after submission and he/she can read/listen the answer. The final score and winner is displayed then.

## Important Notice
This project is tested on Ubuntu 20.04 LTS and Ubuntu 18.04 LTS and is working according to the images and videos shown.

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
![Screenshot from 2020-11-18 19-35-55](https://user-images.githubusercontent.com/65706125/99542596-44dde680-29d8-11eb-8cb4-f5e8965e5c23.png)
![Screenshot from 2020-11-18 19-46-02](https://user-images.githubusercontent.com/65706125/99542867-866e9180-29d8-11eb-9b14-0f91ad65be5c.png)
2. If user presses play button, the program asks for the user's details and evalutes the answer, if successful takes the user to the play page else asks them to correct it.
![Screenshot from 2020-11-18 19-36-49](https://user-images.githubusercontent.com/65706125/99542885-8d959f80-29d8-11eb-9271-465bdaf76821.png)
![Screenshot from 2020-11-18 19-37-10](https://user-images.githubusercontent.com/65706125/99542897-925a5380-29d8-11eb-84cc-667f79c7128a.png)
3. Then the user is asked one question in every round and the number of rounds is selected by the user.
![Screenshot from 2020-11-18 19-37-23](https://user-images.githubusercontent.com/65706125/99542906-95554400-29d8-11eb-83ea-0f6fbab91896.png)
4. The user can both read and listen the questions.
![Screenshot from 2020-11-18 19-37-57](https://user-images.githubusercontent.com/65706125/99542923-97b79e00-29d8-11eb-99ff-bebfce02e608.png)
5. Also the user is provided a canvas divided into boxes so that he/she can draw each digit of the answer in individual box.
![Screenshot from 2020-11-18 19-38-21](https://user-images.githubusercontent.com/65706125/99542927-9ab28e80-29d8-11eb-8d6d-3afe7fecf0e2.png)
6. Then the user is shown the answer which he/she can read and listen.
![Screenshot from 2020-11-18 19-38-44](https://user-images.githubusercontent.com/65706125/99542938-9d14e880-29d8-11eb-9c05-997bc90736ae.png)
7. Then the score is evaluted and the name of the winner is displayed.
![Screenshot from 2020-11-18 19-39-00](https://user-images.githubusercontent.com/65706125/99542955-a0a86f80-29d8-11eb-917c-6bbda55b7f8e.png)


## Important Files

1. Riddle.py - This is the front end file, the main project file.
2. DigitRecognition.h5 - This is the backend deep learning model for handwritten digit recognition.

## Report

The first edition is doing good when the user draws the digit neatly and within the given box. The accuracy of prediction is 98.8% .

## Full Working of the game

## Need Update

The project is the second edition. I will keep update.
