#Import Libraries required
from PIL import ImageTk, Image
from tkinter import *
from tkinter import font as tkFont
import pandas as pd
import numpy as np
import pyscreenshot as ImageGrab
import cv2
import tensorflow as tf
from playsound import playsound
physical_devices = tf.config.experimental.list_physical_devices("GPU")
tf.config.experimental.set_memory_growth(physical_devices[0], True)


class Riddle_Game(object):

    def __init__(self):
        self.root = Tk()  # Create a root widget
        self.root.geometry("1200x800")  # Define the size of the window or app
        self.root.title("Riddle Game")  # Set the title of the window
        self.root.resizable(0, 0) #Disable resizing of window
        self.text_font = tkFont.Font(family="Courier New", size=15, weight="bold")
        self.heading_font = tkFont.Font(family="Verdana", size=40, weight="bold")
        self.heading_font_small = tkFont.Font(family="Courier New", size=25, weight="bold")
        self.QuesFont = tkFont.Font(family="Courier New", size=20, weight="bold")
        self.button_font = tkFont.Font(family="Playbill", size=15, weight="bold")
        self.BackgroundImage(self.root)        #set the background image for default/first page
        self.first_page()
        self.root.mainloop()

    def first_page(self):
        self.CreateMainFrame("First")
        self.content_frame = Frame(self.main_frame, height=100, width=550, bg="#1a0d00")
        self.content_frame.place(x=350, y=450)
        self.play_comp_button = Button(self.content_frame, text="Play", activebackground="saddle brown",
                                       bd=3, bg="black", fg="white",                                           #The play button
                                       command=self.play_comp, font=self.button_font, justify=CENTER, height=2,
                                       width=15)
        self.play_comp_button.place(x=20, y=10)
        self.about_button = Button(self.content_frame, text="About", activebackground="saddle brown", bd=3, bg="black",
                                   fg="white",                                                                       #The about button
                                   command=self.about, font=self.button_font, justify=CENTER, height=2, width=15)
        self.about_button.place(x=280, y=10)

    def play_comp(self):
        self.main_frame.destroy()
        self.CreateMainFrame()
        self.heading_frame = Frame(self.main_frame, height=100, width=950, bg="#1a0d00")
        self.heading_frame.place(x=150, y=20)
        self.heading = Message(self.heading_frame, font=self.heading_font, bg="#1a0d00", fg="White", width=950,
                               justify=CENTER, text="Let us start with your details")
        self.heading.place(x=0, y=10)
        self.content_frame = Frame(self.main_frame, height=200, width=700, bg="#1a0d00")
        self.content_frame.place(x=300, y=300)
        self.name_label = Label(self.content_frame, bg="#1a0d00", font=self.text_font, text="Name", height=1, width=9,
                                fg="White")
        self.name_label.place(x=10, y=10)
        self.name_entry = Entry(self.content_frame, width=70, bd=3)
        self.name_entry.place(x=120, y=10)
        self.age_label = Label(self.content_frame, bg="#1a0d00", font=self.text_font, text="Age", height=1, width=9,
                               fg="White")
        self.age_label.place(x=10, y=50)
        self.age_entry = Entry(self.content_frame, width=70, bd=3)
        self.age_entry.place(x=120, y=50)
        self.rounds = Label(self.content_frame, bg="#1a0d00", font=self.text_font, text="Rounds", height=1, width=9,
                               fg="White")
        self.rounds.place(x=10,y=90)
        self.default = StringVar(self.content_frame)
        self.default.set("3")
        self.RoundSelect = OptionMenu(self.content_frame,self.default,"1","2","3","4","5","6","7")
        self.RoundSelect.config(bg="#1a0d00",fg="white",activebackground="saddle brown",font=self.text_font)
        self.RoundSelect.place(x=120,y=90)

        self.ButtonFrame = Frame(self.main_frame, height=50, width=600, bg="#1a0d00")
        self.ButtonFrame.place(x=350, y=650)
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
        self.age = self.age_entry.get()      #Get the age user enter
        self.name = self.name_entry.get()    #Get the name the user enters
        self.nameFormat = self.name.replace(" ", "")    #Remove spaces between the first and last name
        self.Rounds = self.default.get()   #Get the number of rounds the user enters
        if self.age.isdigit() and self.nameFormat.isalpha():   #Validate if the name is alphabets and age is digits
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
            self.rule = "1. The game comprises of " + str(self.Rounds) + " rounds with each round having one point.\n2. In each round I will ask you a question and give you time to think and then you have to draw the answer in the given white region of the canvas,then press 'Answer' button.\n3. If you answer correctly you will gain one point else I will gain one point. \n4. After " + str(self.Rounds) + " rounds let's see who wins. \n Let's Go \n\n HINT: All answers comprise of only digits"
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
            self.alert = "Please enter valid details"   #If the name and age are not valid
            self.alert_info = Label(self.content_frame, bg="#1a0d00", font=self.text_font, text=self.alert, height=1,
                                    width=50, fg="White")
            self.alert_info.place(x=80, y=150)

    def PlaySolo(self):
        self.CompScore = []    #Initialise empty list for evaluation computer's score
        self.PlayerScore = []  #Initialise empty list for evaluation of player's score
        self.AskedQues = []    #Add asked question in this list so that repition does not occur
        self.RiddleData = pd.read_csv("Riddle_Data.csv")  #Read from the riddles data
        pd.set_option('display.max_colwidth', None)
        self.CreateQues()

    def CreateQues(self):
        self.main_frame.destroy()
        self.CreateMainFrame()
        self.QuesFrame = Frame(self.main_frame, width=1050, height=250, bg="#1a0d00")
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
                                   width=1000,
                                   text=self.RiddleData["Questions"][self.QuesNo].to_string()[3:])
        self.QuesDisplay.place(x=0, y=0)
        self.CountBox = int(self.RiddleData["DigitsCount"][self.QuesNo])
        self.DrawCanv()
        self.setup()
        self.ButtonFrame = Frame(self.main_frame, width=770, height=50, bg="#1a0d00")
        self.ButtonFrame.place(x=300, y=720)
        self.ListenButton = Button(self.ButtonFrame, text="Listen Ques", font=self.button_font,
                                   activebackground="saddle brown",
                                   bd=3, bg="black", fg="white", justify=CENTER, height=1, width=15,
                                   command=lambda: self.PlayAudio("sounds/Ques{}.mp3".format(str(int(self.QuesNo)))))
        self.ListenButton.place(x=0, y=5)
        self.AnswerButton = Button(self.ButtonFrame, text="Answer", font=self.button_font,
                                   activebackground="saddle brown",
                                   bd=3, bg="black", fg="white", justify=CENTER, height=1, width=15,
                                   command=lambda: self.answer(self.CountBox))
        self.AnswerButton.place(x=250, y=5)
        self.ExitButton = Button(self.ButtonFrame, text="Quit Game", font=self.button_font,
                                 activebackground="saddle brown",
                                 bd=3, bg="black", fg="white", justify=CENTER, command=self.first_page, height=1,
                                 width=15)
        self.ExitButton.place(x=500, y=5)


    def DrawCanv(self):
        self.DrawCanvas = Canvas(self.main_frame, bg="black", height=400, width=1000)
        self.DrawCanvas.place(x=30, y=300)
        self.CountBox = self.RiddleData["DigitsCount"][self.QuesNo]
        for i in range(int(self.CountBox)):
            self.DrawCanvas.create_rectangle(20 + i * 280 + i * 10, 50, 300 + i * 280 + i * 10, 330, outline="white")
        self.DrawCanvas.create_text(700, 380, text="Try to draw each digit in separate box", fill="white",
                                    font=self.text_font)

    def PlayAudio(self,txt):  #Function to play audio in the background
        playsound(txt)

    def setup(self):
        self.old_x = None  # Initialize x coordinate
        self.old_y = None  # Initialize y coordinate
        self.line_width = 35
        self.color = "White"  # Set color
        self.DrawCanvas.bind("<Button-1>",self.addpoint)  # when user presses the left button of the mouse, function addpoint is invoked
        self.DrawCanvas.bind('<B1-Motion>',self.draw)  # invokes draw function when user drags the mouse while the left mouse button is pressed
        # The above two are events that are mapped to some function

    def addpoint(self, event):  # function to be mapped with the event
        for i in range(int(self.CountBox)):
            if (event.x>=20 + i * 280 + i * 10 and event.x<300 + i * 280 + i * 10): #user cannot draw oustide boxes
                self.old_x = event.x
            if (event.y>=50 and event.y<330): #user cannot draw outside boxes
                self.old_y = event.y

    def draw(self, event):  # the draw or paint function
        self.line_width = 35  # select the line width for drawing
        for i in range(int(self.CountBox)):
            if (event.x >= 20 + i * 280 + i * 10 and event.x <= 300 + i * 280 + i * 10) and (event.y>=50 and event.y<=330):
                self.draw_color = self.color
            else:
                self.draw_color = "Black"
            if self.old_x and self.old_y and self.draw_color=="White":  # if the old-x old-y are true and not NONE i.e. the user has pressed on the canvas
                self.DrawCanvas.create_line((self.old_x, self.old_y, event.x, event.y), width=self.line_width,
                                   fill=self.draw_color, capstyle=ROUND, smooth=True,
                                   splinesteps=0)  # draw line from old_x, old_y points to the points where the user left the dragging
                self.old_x = event.x  # to replace the old coordinates with the coordinates where the user left the mouse dragging
                self.old_y = event.y  # to replace the old coordinates with the coordinates where the user left the mouse dragging

    def answer(self, CountBox):
        self.PredictAnswer =[]
        for i in range(int(CountBox)):  #to capture the digits drawn by users
            x1 = self.root.winfo_rootx() + 20 + i * 280 + i * 10 + self.DrawCanvas.winfo_x()
            y1 = self.root.winfo_rooty() + 50 + self.DrawCanvas.winfo_y()
            x2 = self.root.winfo_rootx() + 300 + i * 280 + i * 10 + self.DrawCanvas.winfo_x()
            y2 = self.root.winfo_rooty() + 330 + self.DrawCanvas.winfo_y()
            im = ImageGrab.grab((x1, y1, x2, y2))
            imgpath = "images/Captured{}.png".format(i)
            im.save(imgpath)
        self.model = tf.keras.models.load_model('DigitRecognition.h5')  # Load our trained model
        for i in range(int(self.CountBox)):
            self.Predict = self.predict(i)
            self.PredictAnswer.append(self.Predict)

        self.main_frame.destroy()
        self.CreateMainFrame()
        self.HeadingFrame = Frame(self.main_frame, height=100, width=300, bg="#1a0d00")
        self.HeadingFrame.place(x=400, y=50)
        self.HeadingMess = Message(self.HeadingFrame, width=300, text="Answers", font=self.heading_font, bg="#1a0d00",
                                   fg="White", justify=CENTER)
        self.HeadingMess.place(x=0, y=0)
        self.ContentFrame = Frame(self.main_frame, width=770, height=300, bg="#1a0d00")
        self.ContentFrame.place(x=200, y=200)
        self.CorrectAns = int(self.RiddleData["Answers"][self.QuesNo].to_string()[3:])

        self.predans =""
        for i in self.PredictAnswer:
            self.predans+=str(i)
        self.predans = int(self.predans)
        if self.CorrectAns == self.predans:  #Evaluate score
            self.PlayerScore.append(1)
        else:
            self.CompScore.append(1)

        self.ans = "Your answer was :"+str(self.predans)+"\nThe correct answer is :\t" + self.RiddleData["Answers"][self.QuesNo].to_string()[3:] + "\nHINT: " + self.RiddleData["Hints"][self.QuesNo].to_string()[3:] + "\nYour total score is: "+str(len(self.PlayerScore)) + "\nArjun Bot's score is :" + str(len(self.CompScore))
        self.Ans = Message(self.ContentFrame, width=700, bg="#1a0d00", text=self.ans, fg="White", justify=CENTER,
                           font=self.text_font)
        self.Ans.place(x=10,y=10)

        self.ButtonFrame = Frame(self.main_frame,width=770,height=50,bg="#1a0d00")
        self.ButtonFrame.place(x=200,y=550)
        if len(self.AskedQues)<int(self.Rounds):  #if all rounds are not completed
            self.NextButton = Button(self.ButtonFrame, text="Next Round", font=self.button_font,
                                     activebackground="saddle brown",
                                     bd=3, bg="black", fg="white", justify=CENTER, command=self.CreateQues, height=1,
                                     width=15)
            self.NextButton.place(x=10, y=5)
        else:  #if all rounds are completed
            self.NextButton = Button(self.ButtonFrame, text="Next", font=self.button_font,
                                     activebackground="saddle brown",
                                     bd=3, bg="black", fg="white", justify=CENTER, command=self.Final, height=1,
                                     width=15)
            self.NextButton.place(x=10, y=5)

        self.ListenButton = Button(self.ButtonFrame,text="Listen Answer",font=self.button_font,activebackground="saddle brown",
                                   bd=3, bg="black", fg="white", justify=CENTER, height=1, width=15,
                                   command=lambda:self.PlayAudio("sounds/Ans{}.mp3".format(str(int(self.QuesNo)))))
        self.ListenButton.place(x=260,y=5)
        self.ExitButton = Button(self.ButtonFrame, text="Quit Game", font=self.button_font,
                                 activebackground="saddle brown",
                                 bd=3, bg="black", fg="white", justify=CENTER, command=self.first_page, height=1,
                                 width=15)
        self.ExitButton.place(x=510, y=5)


    def predict(self, i):
        image = cv2.imread('images/Captured{}.png'.format(i))  # read the saved input on canvas which is stores as image
        grey = cv2.cvtColor(image.copy(), cv2.COLOR_BGR2GRAY)  # convert to grayscale
        contours, _ = cv2.findContours(grey.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
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
                self.digit = grey[y:height, x:width]
            elif (h > w):
                m = abs(mean - w)
                height = int(y + h - m)
                width = int(x + w + m)
                self.digit = grey[y:height, x:width]
            elif (h == w):
                self.digit = grey[y:y + h, x:x + w]

            # ResiImport the libraries to create a GUI Applicationzing that digit to (18, 18)
            resized_digit = cv2.resize(self.digit, (18, 18))

            # Padding the digit with 5 pixels of black color (zeros) in each side to finally produce the image of (28, 28)
            self.padded_digit = np.pad(resized_digit, ((5, 5), (5, 5)), "constant", constant_values=0)

        prediction = self.model.predict(self.padded_digit.reshape((1, 28, 28, 1)))  # Predict the digit using our model after reshaping the digit to the dimensions the model is trained on
        ans = np.argmax(prediction)  # convert the predicted array to a readable format
        return ans

    def Final(self):
        self.main_frame.destroy()
        self.CreateMainFrame()
        self.HeadingFrame = Frame(self.main_frame,width=400,bg="#1a0d00",height=100)
        self.HeadingFrame.place(x=350,y=50)
        self.HeadingMess = Message(self.HeadingFrame,bg="#1a0d00",fg="White",font=self.heading_font,justify=CENTER,width=400,
                                   text="Final Result")
        self.HeadingMess.place(x=10,y=10)
        self.content_frame = Frame(self.main_frame,bg="#1a0d00",width=1000,height=300)
        self.content_frame.place(x=100,y=300)
        self.Winner = str(self.name) if len(self.PlayerScore)>len(self.CompScore) else "Arjun Bot"
        self.text = "The winner of this game is "+self.Winner+"\nThe final score is Arjun Bot:"+str(len(self.CompScore))+" and "+str(self.name)+":"+str(len(self.PlayerScore))+"\nThank you for playing the game, We hope you have learnt something.\n\n Hope to see you again!"
        self.Mess = Message(self.content_frame,bg="#1a0d00",fg="White",font=self.heading_font_small,justify=CENTER,width=950,
                            text=self.text)
        self.Mess.place(x=0,y=0)
        self.ButtonFrame = Frame(self.main_frame, width=570, height=50, bg="#1a0d00")
        self.ButtonFrame.place(x=400, y=650)
        self.PlayAgain = Button(self.ButtonFrame, text="Play Again", font=self.button_font,
                                     activebackground="saddle brown",
                                     bd=3, bg="black", fg="white", justify=CENTER, command=self.PlaySolo, height=1,
                                     width=15)
        self.PlayAgain.place(x=10,y=5)
        self.ExitButton = Button(self.ButtonFrame, text="Quit Game", font=self.button_font,
                                 activebackground="saddle brown",
                                 bd=3, bg="black", fg="white", justify=CENTER, command=exit, height=1,
                                 width=15)
        self.ExitButton.place(x=280, y=5)



    def about(self):  #Function that tells about the developer
        self.content_frame.destroy()  # Just destroy the content frame as the heading is needed
        self.content_frame = Frame(self.main_frame, height=300, width=700, bg="#1a0d00")
        self.content_frame.place(x=270, y=450)  # Place below heading
        self.about = "Riddle Game \n\n This is a game mainly developed for children suffering from dyslexia or children who are unable to read and write properly. The children can play with the computer and should play under someone's supervision and should practice drawing answers in the entire box. \n This application is developed by Arjun Bajaj, arjunbajaj2000@gmail.com"
        self.AboutInfo = Message(self.content_frame, bg="#1a0d00", fg="White", font=self.text_font, justify=CENTER,
                                 width=600, text=self.about)
        self.AboutInfo.place(x=0, y=0)
        self.BackButton = Button(self.content_frame, text="Back", activebackground="grey", bd=3, bg="White", fg="Black",
                                 command=self.first_page, font=self.button_font, justify=CENTER, height=1, width=5)
        self.BackButton.place(x=400, y=250)

    def CreateMainFrame(self, page="Any"):     #Function to create the main frame on each page
        self.main_frame = Frame(self.root, height=800, width=1200)
        self.main_frame.place(x=0, y=0)
        self.BackgroundImage(self.main_frame, page)

    def BackgroundImage(self, root, page="Any"):  #Function to set the background image on each page
        if page == "First":
            self.background_image = ImageTk.PhotoImage(file="images/riddle_front.jpg")
        else:
            self.background_image = ImageTk.PhotoImage(file="images/riddle_simple.jpg")
        self.background_label = Label(root, image=self.background_image)
        self.background_label.grid(row=0, column=0)


if __name__ == '__main__':
    Riddle_Game()
# Before executing code, Python interpreter reads source file and define few special variables/global variables.
# If the python interpreter is running that module (the source file) as the main program, it sets the special
# __name__ variable to have a value “__main__”. If this file is being imported from another module,
# __name__ will be set to the module’s name. Module’s name is available as value to __name__ global variable.
# Here our class Riddle_Game script is being used as a module so its __name__ is __main__
