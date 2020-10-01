from tkinter import *
from PIL import ImageTk, Image
from tkinter import font as tkFont


class Riddle_Game(object):

    def __init__(self):
        self.root = Tk() #Create a root widget
        self.root.geometry("1200x800") #Define the size of the window or app
        self.root.title("Riddle Game") #Set the title of the window
        self.root.resizable(0,0)
        self.button_font = tkFont.Font(family="Arial",size=20,weight="bold")
        self.starter()
        self.root.mainloop()

    def starter(self):
        self.background_header()
        self.play_comp_button = Button(self.root, text="Play with computer",activebackground="Yellow",bd=3,bg="black",fg="white",
                                       command=self.play_comp,font=self.button_font, justify=CENTER, height=2, width=20)
        self.play_comp_button.place(x=300,y=500)
        self.play_friend_button = Button(self.root, text="Play with a friend", activebackground="Yellow", bd=3,
                                       bg="black", fg="white",command=self.play_friend, font=self.button_font, justify=CENTER,height=2, width=20)
        self.play_friend_button.place(x=660, y=500)


    def background_header(self):
        self.header_image = ImageTk.PhotoImage(file="images/Header.png")
        self.header_label = Label(self.root, image=self.header_image)
        self.header_label.place(x=0, y=0)

    def background_solo(self):
        self.background_image = ImageTk.PhotoImage(file="images/riddle.jpg")
        self.background_label = Label(self.root, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

    def play_comp(self):
        pass

    def play_friend(self):
        pass

if __name__ == '__main__':
    Riddle_Game()