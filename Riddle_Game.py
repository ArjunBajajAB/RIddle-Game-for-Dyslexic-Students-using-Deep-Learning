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
        self.frame1 = self.alot_frame(height=300,width=1000,side=TOP)
        self.frame2 = self.alot_frame(height=100,width=400,side=LEFT,padx=10,pady=10)
        self.frame3 = self.alot_frame(height=100,width=400,side=RIGHT,padx=10,pady=10)
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
            self.play_comp_button = Button(frame, text="Play with computer", activebackground="Yellow", bd=3,
                                           bg="black", fg="white",
                                           command=self.play_comp, font=self.button_font, justify=CENTER, height=2,
                                           width=20)
            self.play_comp_button.pack(side=LEFT)
        elif name=="play_with_friend":
            self.play_friend_button = Button(frame, text="Play with a friend", activebackground="Yellow", bd=3,
                                             bg="black", fg="white", command=self.play_friend, font=self.button_font,
                                             justify=CENTER, height=2, width=20)
            self.play_friend_button.pack(side=RIGHT)
        elif name=="Continue":
            self.continue_button = Button(frame,text="Continue",activebackground="Yellow", bd=3,bg="black", fg="white",
                                          command=self.comp_ques(self.name,self.age),font=self.button_font,justify=CENTER, height=2, width=20)
            self.continue_button.pack(side=BOTTOM)

    def alot_frame(self,height,width,side,padx=None,pady=None):
        self.frame = Frame(self.root,height=height,width=width,bg="White",padx=padx,pady=pady)
        self.frame.pack(side=side)
        return self.frame

    def play_comp(self):
        self.frame2.destroy()
        self.frame3.destroy()
        self.frame1.destroy()
        self.frame = self.alot_frame(height=100,width=1200,side=TOP)
        self.label = Label(self.frame,bg="White",font=self.heading_font,fg="Black",height=2,width=50,text="Let us start with your details")
        self.label.pack(side=TOP)
        self.frame2 = self.alot_frame(height=800, width=400, side=LEFT)
        self.label_name = Label(self.frame2, bg="White", font=self.button_font, text="Name", height=1, width=9,fg="Black")
        self.label_name.pack(side=LEFT)
        self.frame3 = self.alot_frame(height=100, width=600, side=RIGHT)
        self.input = Entry(self.frame3,width=50)
        self.input.pack(side=RIGHT,ipady=6)
        self.name = self.input.get()
        self.frame4 = Frame(height=800, width=400)
        self.frame4.place(x=0,y=550)
        self.label_name2 = Label(self.frame4, bg="White", font=self.button_font, text="Age", height=1, width=9,fg="Black")
        self.label_name2.pack(side=LEFT)
        self.frame5 = Frame(height=100, width=600)
        self.frame5.place(x=795,y=550)
        self.input2 = Entry(self.frame5, width=50)
        self.input2.pack(side=RIGHT, ipady=6)
        self.age = self.input2.get()
        self.button_frame = Frame(height=100,width=500)
        self.button_frame.pack(side=BOTTOM)
        self.buttons(self.button_frame,name="Continue")

    def play_friend(self):
        pass

    def comp_ques(self,name,age):
        if name and age:
            self.frame.destroy()

if __name__ == '__main__':
    Riddle_Game()