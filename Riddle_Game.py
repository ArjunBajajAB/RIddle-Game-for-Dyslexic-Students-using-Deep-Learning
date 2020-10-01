from tkinter import *
from PIL import ImageTk, Image



class Riddle_Game(object):

    def __init__(self):
        self.root = Tk() #Create a root widget
        self.root.geometry("1200x800") #Define the size of the window or app
        self.root.title("Riddle Game") #Set the title of the window
        self.starter()
        self.root.mainloop()

    def starter(self):
        self.background_header()



    def background_header(self):
        self.header_image = ImageTk.PhotoImage(file="images/Header.png")
        self.header_label = Label(self.root, image=self.header_image)
        self.header_label.place(x=0, y=0)

    def background_solo(self):
        self.background_image = ImageTk.PhotoImage(file="images/riddle.jpg")
        self.background_label = Label(self.root, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

if __name__ == '__main__':
    Riddle_Game()