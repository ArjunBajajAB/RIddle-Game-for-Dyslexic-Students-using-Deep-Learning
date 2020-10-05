from PIL import ImageTk, Image, ImageOps
from tkinter import *
from tkinter import font as tkFont
import cv2

class Riddle_Game(object):

    def __init__(self):
        self.root = Tk() #Create a root widget
        self.root.geometry("1200x800") #Define the size of the window or app
        self.root.title("Riddle Game") #Set the title of the window
        self.root.resizable(0,0)
        self.background_solo(self.root)
        self.main_frame = Frame(self.root, height=750, width=1150)
        self.main_frame.place(x=100,y=25)
        self.heading_font = tkFont.Font(family="Courier", size=50, weight="bold")
        self.button_font = tkFont.Font(family="Arial",size=20,weight="bold")
        self.first_frame()
        self.root.mainloop()

    def background_solo(self,root):
        self.background_image = ImageTk.PhotoImage(file="images/riddle_main.jpg")
        self.background_label = Label(root, image=self.background_image)
        self.background_label.grid(row=0, column=0)

    def first_frame(self):
        self.heading_frame= Frame(self.main_frame, height= 300, width=1000,bg="DodgerBlue4",bd=4)
        self.heading_frame.pack(expand=True,fill=X)
        self.game_heading()
        self.content_frame = Frame(self.main_frame,height=300,width=1000,bg="DodgerBlue4",bd=4)
        self.content_frame.pack(side=BOTTOM,expand=True,fill=BOTH,pady=15)
        self.first_frame_buttons()

    def game_heading(self):
        self.heading_line_1 = Label(self.heading_frame,font=self.heading_font, fg="Black",bg ="White", justify=CENTER, text="THE",height=2, width=7)
        self.heading_line_1.place(x=400,y=0)
        self.heading_line_2 = Label(self.heading_frame, font=self.heading_font, fg="Black",bg ="White", justify=CENTER, text="RIDDLE", height=2, width=7)
        self.heading_line_2.place(x=400,y=100)
        self.heading_line_3 = Label(self.heading_frame, font=self.heading_font, fg="Black",bg ="White", justify=CENTER, text="GAME", height=2, width=7)
        self.heading_line_3.place(x=400,y=200)

    def first_frame_buttons(self):
        self.play_comp_button = Button(self.content_frame, text="Play with computer", activebackground="Yellow", bd=3,bg="black", fg="white",
                                       command=self.play_comp, font=self.button_font, justify=CENTER, height=2,width=20)
        self.play_comp_button.place(x=80,y=80)
        self.play_friend_button = Button(self.content_frame, text="Play with a friend", activebackground="Yellow", bd=3,
                                        bg="black", fg="white", command=self.play_friend, font=self.button_font,
                                        justify=CENTER, height=2, width=20)
        self.play_friend_button.place(x=550,y=80)
        self.about_button = Button(self.content_frame, text="About", activebackground="Yellow", bd=3,
                                        bg="black", fg="white", command=self.about, font=self.button_font,
                                        justify=CENTER, height=2, width=20)
        self.about_button.place(x=300,y=200)

    def play_comp(self):
        pass
    def play_friend(self):
        pass
    def about(self):
        pass

if __name__ == '__main__':
    Riddle_Game()