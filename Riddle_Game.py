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
        self.heading_font = tkFont.Font(family="Courier", size=50, weight="bold")
        self.starter()
        self.root.mainloop()

    def starter(self):
        self.first_frame()


    def first_frame(self):
        self.background()
        self.frame1 = Frame(self.root, height=300, width= 1000,bg="White")
        self.frame1.pack(side= TOP)
        self.frame2 =  Frame(self.root, height=100, width=400,bg="White",padx=10,pady=10)
        self.frame2.pack(side=LEFT)
        self.frame3 = Frame(self.root, height=100, width=400, bg="White",padx=10,pady=10)
        self.frame3.pack(side=RIGHT)
        self.game_heading(self.frame1)
        self.buttons(self.frame2,name="play_with_comp")
        self.buttons(self.frame3,name="play_with_friend")



    def game_heading(self,frame):
        self.heading1 = Label(frame,font=self.heading_font,fg="Black",justify=CENTER,text="THE",height=2,width=7)
        self.heading1.pack(side=TOP)
        self.heading2 = Label(frame, font=self.heading_font, fg="Black", justify=CENTER, text="RIDDLE", height=2, width=7)
        self.heading2.pack(side=TOP)
        self.heading3 = Label(frame, font=self.heading_font, fg="Black", justify=CENTER, text="GAME", height=2, width=7)
        self.heading3.pack(side=TOP)


    def background(self):
        self.background_image = ImageTk.PhotoImage(file="images/riddle.jpg")
        self.background_label = Label(self.root, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

    def buttons(self,frame,name="None"):
        if name=="play_with_comp":
            self.play_comp_button = Button(self.frame2, text="Play with computer", activebackground="Yellow", bd=3,
                                           bg="black", fg="white",
                                           command=self.play_comp, font=self.button_font, justify=CENTER, height=2,
                                           width=20)
            self.play_comp_button.pack(side=LEFT)
        if name=="play_with_friend":
            self.play_friend_button = Button(self.frame3, text="Play with a friend", activebackground="Yellow", bd=3,
                                             bg="black", fg="white", command=self.play_friend, font=self.button_font,
                                             justify=CENTER, height=2, width=20)
            self.play_friend_button.pack(side=RIGHT)


    def play_comp(self):
        self.root.delete("all")

    def play_friend(self):
        pass

if __name__ == '__main__':
    Riddle_Game()