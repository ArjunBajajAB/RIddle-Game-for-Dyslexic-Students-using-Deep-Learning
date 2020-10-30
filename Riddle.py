from PIL import ImageTk, Image, ImageOps
from tkinter import *
from tkinter import font as tkFont
import pandas as pd
import numpy as np
import pyscreenshot as ImageGrab
import cv2
import tensorflow as tf


class Riddle_Game(object):

    def __init__(self):
        self.root = Tk()  # Create a root widget
        self.root.geometry("1200x800")  # Define the size of the window or app
        self.root.title("Riddle Game")  # Set the title of the window
        self.root.resizable(0, 0)
        self.text_font = tkFont.Font(family="Courier New", size=15, weight="bold")
        self.heading_font = tkFont.Font(family="Verdana", size=40, weight="bold")
        self.heading_font_small = tkFont.Font(family="Courier New", size=25, weight="bold")
        self.QuesFont = tkFont.Font(family="Courier New", size=20, weight="bold")
        self.button_font = tkFont.Font(family="Playbill", size=15, weight="bold")
        self.BackgroundImage(self.root)
        self.first_page()
        self.root.mainloop()

    def first_page(self):
        self.CreateMainFrame("First")
        self.content_frame = Frame(self.main_frame, height=100, width=800, bg="#1a0d00")
        self.content_frame.place(x=200, y=450)
        self.play_comp_button = Button(self.content_frame, text="Play with computer", activebackground="saddle brown",
                                       bd=3, bg="black", fg="white",
                                       command=self.play_comp, font=self.button_font, justify=CENTER, height=2,
                                       width=15)
        self.play_comp_button.place(x=20, y=10)
        self.play_friend_button = Button(self.content_frame, text="Play with a friend", activebackground="saddle brown",
                                         bd=3, bg="black", fg="white",
                                         command=self.play_friend, font=self.button_font, justify=CENTER, height=2,
                                         width=15)
        self.play_friend_button.place(x=285, y=10)
        self.about_button = Button(self.content_frame, text="About", activebackground="saddle brown", bd=3, bg="black",
                                   fg="white",
                                   command=self.about, font=self.button_font, justify=CENTER, height=2, width=15)
        self.about_button.place(x=550, y=10)

    def play_comp(self):
        self.main_frame.destroy()
        self.CreateMainFrame()
        self.heading_frame = Frame(self.main_frame, height=100, width=950, bg="#1a0d00")
        self.heading_frame.place(x=150, y=20)
        self.heading = Message(self.heading_frame, font=self.heading_font, bg="#1a0d00", fg="White", width=950,
                               justify=CENTER, text="Let us start with your details")
        self.heading.place(x=0, y=10)
        self.content_frame = Frame(self.main_frame, height=150, width=700, bg="#1a0d00")
        self.content_frame.place(x=300, y=300)
        self.name_label = Label(self.content_frame, bg="#1a0d00", font=self.text_font, text="Name", height=1, width=9,
                                fg="White")
        self.name_label.place(x=10, y=10)
        self.name_entry = Entry(self.content_frame, width=70, bd=3)
        self.name_entry.place(x=100, y=10)
        self.age_label = Label(self.content_frame, bg="#1a0d00", font=self.text_font, text="Age", height=1, width=9,
                               fg="White")
        self.age_label.place(x=10, y=50)
        self.age_entry = Entry(self.content_frame, width=70, bd=3)
        self.age_entry.place(x=100, y=50)
        self.ButtonFrame = Frame(self.main_frame, height=50, width=600, bg="#1a0d00")
        self.ButtonFrame.place(x=350, y=600)
        self.continue_button = Button(self.ButtonFrame, text="Continue", activebackground="saddle brown", bd=3,
                                      bg="black", fg="white",
                                      command=self.PlayPageComp, font=self.button_font, justify=CENTER, height=1,
                                      width=15)
        self.continue_button.place(x=0, y=0)
        self.back_button = Button(self.ButtonFrame, text="Back", activebackground="saddle brown", bd=3, bg="black",
                                  fg="white",
                                  command=self.first_page, font=self.button_font, justify=CENTER, height=1, width=15)
        self.back_button.place(x=285, y=0)

    def PlayPageComp(self):
        self.age = self.age_entry.get()
        self.name = self.name_entry.get()
        self.nameFormat = self.name.replace(" ", "")
        if self.age.isdigit() and self.nameFormat.isalpha():
            self.main_frame.destroy()
            self.CreateMainFrame()
            self.heading_frame = Frame(self.main_frame, height=100, width=1100, bg="#1a0d00")
            self.heading_frame.place(x=10, y=20)
            self.text = "Hello " + str(self.name) + ", I am Arjun Bot, let us begin the game"
            self.heading = Message(self.heading_frame, font=self.heading_font_small, bg="#1a0d00", fg="White",
                                   width=1050, justify=CENTER, text=self.text)
            self.heading.place(x=0, y=10)
            self.content_frame = Frame(self.main_frame, height=300, width=800, bg="#1a0d00")
            self.content_frame.place(x=200, y=300)
            self.rule = "1. The game comprises of 5 rounds with each round having one point.\n2. In each round Arjun Bot will ask you a question and give you 2 minutes time to think and then you have to draw the answer in the given white region of the canvas and press 'Answer' button.\n3. If you answer correctly you will gain one point else Arjun will gain one point. \n4. After 5 rounds let's see who wins. \n Let's Go \n\n HINT: All answers comprise of only digits"
            self.rules = Message(self.content_frame, font=self.text_font, bg="#1a0d00", fg="white", width=750,
                                 justify=LEFT, text=self.rule)
            self.rules.place(x=0, y=0)
            self.ButtonFrame = Frame(self.main_frame, height=50, width=600, bg="#1a0d00")
            self.ButtonFrame.place(x=250, y=630)
            self.continue_button = Button(self.ButtonFrame, text="Continue", activebackground="saddle brown", bd=3,
                                          bg="black", fg="white",
                                          command=self.PlaySolo, font=self.button_font, justify=CENTER, height=1,
                                          width=15)
            self.continue_button.place(x=0, y=0)
            self.back_button = Button(self.ButtonFrame, text="Back", activebackground="saddle brown", bd=3, bg="black",
                                      fg="white",
                                      command=self.play_comp, font=self.button_font, justify=CENTER, height=1, width=15)
            self.back_button.place(x=285, y=0)

        else:
            self.name_entry.delete(0, len(self.name) + 2)
            self.age_entry.delete(0, len(self.age))
            self.alert = "Please enter valid details"
            self.alert_info = Label(self.content_frame, bg="#1a0d00", font=self.text_font, text=self.alert, height=1,
                                    width=50, fg="White")
            self.alert_info.place(x=80, y=100)

    def PlaySolo(self):
        self.CompScore = []
        self.PlayerScore = []
        self.AskedQues = []
        self.RiddleData = pd.read_csv("Riddle_Data.csv")
        pd.set_option('display.max_colwidth', None)
        self.CreateQues()

    def CreateQues(self):
        self.main_frame.destroy()
        self.CreateMainFrame()
        self.QuesFrame = Frame(self.main_frame, width=1100, height=200, bg="#1a0d00")
        self.QuesFrame.place(x=20, y=10)
        self.loop = 1
        while (self.loop == 1):
            self.QuesNo = np.random.randint(0, 20, 1)
            if self.QuesNo not in self.AskedQues:
                self.AskedQues.append(self.QuesNo)
                self.loop = 0
            else:
                self.loop = 1
        self.QuesDisplay = Message(self.QuesFrame, bg="#1a0d00", fg="White", font=self.QuesFont, justify=CENTER,
                                   width=1050,
                                   text=self.RiddleData["Questions"][self.QuesNo].to_string()[3:])
        self.QuesDisplay.place(x=0, y=0)
        self.DrawCanvas = Canvas(self.main_frame, bg="black", height=400, width=1000)
        self.DrawCanvas.place(x=30, y=250)
        self.CountBox = self.RiddleData["DigitsCount"][self.QuesNo]
        for i in range(int(self.CountBox)):
            self.DrawCanvas.create_rectangle(20 + i * 280 + i * 10, 50, 300 + i * 280 + i * 10, 330, outline="white")
        self.DrawCanvas.create_text(700, 380, text="Try to draw each digit in separate box", fill="white",
                                    font=self.text_font)

        self.ButtonFrame = Frame(self.main_frame, width=500, height=50, bg="#1a0d00")
        self.ButtonFrame.place(x=400, y=720)
        self.ExitButton = Button(self.ButtonFrame, text="Quit Game", font=self.button_font,
                                 activebackground="saddle brown",
                                 bd=3, bg="black", fg="white", justify=CENTER, command=self.first_page, height=1,
                                 width=15)
        self.ExitButton.place(x=250, y=5)
        self.AnswerButton = Button(self.ButtonFrame, text="Answer", font=self.button_font,
                                   activebackground="saddle brown",
                                   bd=3, bg="black", fg="white", justify=CENTER, height=1, width=15,
                                   command=lambda: self.answer(self.CountBox))
        self.AnswerButton.place(x=0, y=5)

    def answer(self, CountBox):
        for i in range(int(CountBox)):
            x1 = self.root.winfo_rootx() + 20 + i * 280 + i * 10 + self.DrawCanvas.winfo_x()
            y1 = self.root.winfo_rooty() + 50 + self.DrawCanvas.winfo_y()
            x2 = self.root.winfo_rootx() + 300 + i * 280 + i * 10 + self.DrawCanvas.winfo_x()
            y2 = self.root.winfo_rooty() + 330 + self.DrawCanvas.winfo_y()
            im = ImageGrab.grab((x1, y1, x2, y2))
            imgpath = "images/Captured{}.png".format(i)
            im.save(imgpath)
        self.PredictAnswer = self.predict(self.CountBox)
        self.main_frame.destroy()
        self.CreateMainFrame()
        self.HeadingFrame = Frame(self.main_frame, height=100, width=500, bg="#1a0d00")
        self.HeadingFrame.place(x=300, y=50)
        self.HeadingMess = Message(self.HeadingFrame, width=500, text="Answers", font=self.heading_font, bg="#1a0d00",
                                   fg="White", justify=CENTER)
        self.HeadingMess.place(x=0, y=0)
        self.ContentFrame = Frame(self.main_frame, width=900, height=300, bg="#1a0d00")
        self.ContentFrame.place(x=50, y=200)
        self.CorrectAns = int(self.RiddleData["Answers"][self.QuesNo].to_string()[3:])
        self.ans = "The correct answer is :\t" + self.RiddleData["Answers"][self.QuesNo].to_string()[3:] + "\nHINT: " + \
                   self.RiddleData["Hints"][self.QuesNo].to_string() + ""
        self.Ans = Message(self.ContentFrame, width=900, bg="#1a0d00", text=self.ans, fg="White", justify=CENTER,
                           font=self.text_font)

    def predict(self, CountBox):
        answ = []
        for i in range(CountBox):
            image = cv2.imread(
                'images/Captured{}.png'.format(i))  # read the saved input on canvas which is stores as image
            grey = cv2.cvtColor(image.copy(), cv2.COLOR_BGR2GRAY)  # convert to grayscale
            ret, thresh = cv2.threshold(grey.copy(), 75, 255,
                                        cv2.THRESH_BINARY_INV)  # threshold the image for contouring
            contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL,
                                                   cv2.CHAIN_APPROX_SIMPLE)  # find contours on threshold image
            preprocessed_digits = []  # empty list to add processed images
            for c in contours:
                x, y, w, h = cv2.boundingRect(c)

                # Creating a rectangle around the digit in the original image (for displaying the digits fetched via contours)
                cv2.rectangle(image, (x, y), (x + w, y + h), color=(0, 255, 0), thickness=2)

                # Cropping out the digit from the image corresponding to the current contours in the for loop
                mean = w + h
                mean = mean / 2
                if (w > h):
                    m = abs(mean - h)
                    height = int(y + h + m)
                    width = int(x + w - m)
                    self.digit = thresh[y:height, x:width]
                elif (h > w):
                    m = abs(mean - w)
                    height = int(y + h - m)
                    width = int(x + w + m)
                    self.digit = thresh[y:height, x:width]
                elif (h == w):
                    self.digit = thresh[y:y + h, x:x + w]

                # ResiImport the libraries to create a GUI Applicationzing that digit to (18, 18)
                resized_digit = cv2.resize(self.digit, (18, 18))

                # Padding the digit with 5 pixels of black color (zeros) in each side to finally produce the image of (28, 28)
                padded_digit = np.pad(resized_digit, ((5, 5), (5, 5)), "constant", constant_values=0)

                # Adding the preprocessed digit to the list of preprocessed digits
                preprocessed_digits.append(padded_digit)

            model = tf.keras.models.load_model('Digit_Recognition_Model_2.model')  # Load our trained model
            for digit in preprocessed_digits:
                prediction = model.predict(digit.reshape(1, 28, 28, 1))  # Predict the digit using our model after reshaping the digit to the dimensions the model is trained on
                ans = np.argmax(prediction)  # convert the predicted array to a readable format
                answ.append(ans)

        return answ

    def play_friend(self):
        self.main_frame.destroy()
        self.CreateMainFrame()
        self.heading_frame = Frame(self.main_frame, height=100, width=950, bg="#1a0d00")
        self.heading_frame.place(x=150, y=20)
        self.heading = Message(self.heading_frame, font=self.heading_font, bg="#1a0d00", fg="White", width=950,
                               justify=CENTER, text="Let us start with your details")
        self.heading.place(x=0, y=10)
        self.content_frame = Frame(self.main_frame, height=250, width=800, bg="#1a0d00")
        self.content_frame.place(x=300, y=300)
        self.nameOne_label = Label(self.content_frame, bg="#1a0d00", font=self.text_font, text="Player 1 Name",
                                   height=1, width=15, justify=LEFT, fg="White")
        self.nameOne_label.place(x=10, y=10)
        self.nameOne_entry = Entry(self.content_frame, width=70, bd=3)
        self.nameOne_entry.place(x=200, y=10)
        self.ageOne_label = Label(self.content_frame, bg="#1a0d00", font=self.text_font, text="Player 1 Age", height=1,
                                  width=15, justify=LEFT, fg="White")
        self.ageOne_label.place(x=10, y=60)
        self.ageOne_entry = Entry(self.content_frame, width=70, bd=3)
        self.ageOne_entry.place(x=200, y=60)

        self.nameTwo_label = Label(self.content_frame, bg="#1a0d00", font=self.text_font, text="Player 2 Name",
                                   height=1, width=15, justify=LEFT, fg="White")
        self.nameTwo_label.place(x=10, y=110)
        self.nameTwo_entry = Entry(self.content_frame, width=70, bd=3)
        self.nameTwo_entry.place(x=200, y=110)
        self.ageTwo_label = Label(self.content_frame, bg="#1a0d00", font=self.text_font, text="Player 2 Age", height=1,
                                  width=15, justify=LEFT, fg="White")
        self.ageTwo_label.place(x=10, y=160)
        self.ageTwo_entry = Entry(self.content_frame, width=70, bd=3)
        self.ageTwo_entry.place(x=200, y=160)

        self.ButtonFrame = Frame(self.main_frame, height=50, width=600, bg="#1a0d00")
        self.ButtonFrame.place(x=450, y=630)
        self.continue_button = Button(self.ButtonFrame, text="Continue", activebackground="saddle brown", bd=3,
                                      bg="black", fg="white",
                                      command=self.PlayPageFriend, font=self.button_font, justify=CENTER, height=1,
                                      width=15)
        self.continue_button.place(x=0, y=0)
        self.back_button = Button(self.ButtonFrame, text="Back", activebackground="saddle brown", bd=3, bg="black",
                                  fg="white",
                                  command=self.first_page, font=self.button_font, justify=CENTER, height=1, width=15)
        self.back_button.place(x=285, y=0)

    def PlayPageFriend(self):
        self.ageOne = self.ageOne_entry.get()
        self.nameOne = self.nameOne_entry.get()
        self.nameOne = self.nameOne.replace(" ", "")
        self.ageTwo = self.ageTwo_entry.get()
        self.nameTwo = self.nameTwo_entry.get()
        self.nameTwo = self.nameTwo.replace(" ", "")
        if self.ageOne.isdigit() and self.nameOne.isalpha() and self.nameTwo.isalpha() and self.ageTwo.isdigit():
            self.main_frame.destroy()
        else:
            self.nameOne_entry.delete(0, len(self.nameOne) + 2)
            self.ageOne_entry.delete(0, len(self.ageOne))
            self.nameTwo_entry.delete(0, len(self.nameTwo) + 2)
            self.ageTwo_entry.delete(0, len(self.ageTwo))
            self.alert = "Please enter valid details"
            self.alert_info = Label(self.content_frame, bg="#1a0d00", font=self.text_font, text=self.alert, height=1,
                                    width=50, fg="White")
            self.alert_info.place(x=80, y=200)

    def about(self):
        self.content_frame.destroy()  # Just destroy the content frame as the heading is needed
        self.content_frame = Frame(self.main_frame, height=300, width=700, bg="#1a0d00")
        self.content_frame.place(x=270, y=450)  # Place below heading
        self.about = "Riddle Game \n\n This is a game mainly developed for children suffering from dyslexia or children who are unable to read and write properly. The children can play with computer or other children and should play under someone's supervision \n This application is developed by Arjun Bajaj, a BCA student"
        self.AboutInfo = Message(self.content_frame, bg="#1a0d00", fg="White", font=self.text_font, justify=CENTER,
                                 width=600, text=self.about)
        self.AboutInfo.place(x=0, y=0)
        self.BackButton = Button(self.content_frame, text="Back", activebackground="grey", bd=3, bg="White", fg="Black",
                                 command=self.first_page, font=self.button_font, justify=CENTER, height=1, width=5)
        self.BackButton.place(x=400, y=250)

    def CreateMainFrame(self, page="Any"):
        self.main_frame = Frame(self.root, height=800, width=1200)
        self.main_frame.place(x=0, y=0)
        self.BackgroundImage(self.main_frame, page)

    def BackgroundImage(self, root, page="Any"):
        if page == "First":
            self.background_image = ImageTk.PhotoImage(file="images/riddle_front.jpg")
        else:
            self.background_image = ImageTk.PhotoImage(file="images/riddle_simple.jpg")
        self.background_label = Label(root, image=self.background_image)
        self.background_label.grid(row=0, column=0)


if __name__ == '__main__':
    Riddle_Game()
