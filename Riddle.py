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
        self.text_font = tkFont.Font(family="Courier New", size=15, weight="bold")
        self.heading_font = tkFont.Font(family="Verdana", size=40, weight="bold")
        self.button_font = tkFont.Font(family="Playbill",size=15,weight="bold")
        self.BackgroundImage(self.root)
        self.first_page()
        self.root.mainloop()

    def first_page(self):
        self.CreateMainFrame("First")
        self.content_frame = Frame(self.main_frame,height=100,width=800,bg="#1a0d00")
        self.content_frame.place(x=200,y=450)
        self.play_comp_button = Button(self.content_frame, text="Play with computer", activebackground="saddle brown", bd=3,bg="black", fg="white",
                                       command=self.play_comp, font=self.button_font, justify=CENTER, height=2,width=15)
        self.play_comp_button.place(x=20,y=10)
        self.play_friend_button = Button(self.content_frame, text="Play with a friend", activebackground="saddle brown", bd=3,bg="black", fg="white",
                                         command=self.play_friend, font=self.button_font,justify=CENTER, height=2, width=15)
        self.play_friend_button.place(x=285,y=10)
        self.about_button = Button(self.content_frame, text="About", activebackground="saddle brown", bd=3,bg="black", fg="white",
                                   command=self.about, font=self.button_font,justify=CENTER, height=2, width=15)
        self.about_button.place(x=550,y=10)

    def play_comp(self):
        self.main_frame.destroy()
        self.CreateMainFrame()
        self.heading_frame= Frame(self.main_frame,height=100,width=1100,bg="#1a0d00")
        self.heading_frame.place(x=20,y=20)
        self.heading = Message(self.heading_frame,font=self.heading_font,bg="#1a0d00",fg="White",width=1100,justify=CENTER,text="Let us start with your details")
        self.heading.place(x=10,y=10)
        self.content_frame = Frame(self.main_frame, height=150, width=700, bg="#1a0d00")
        self.content_frame.place(x=300, y=300)
        self.name_label = Label(self.content_frame, bg="#1a0d00", font=self.text_font, text="Name", height=1, width=9,fg="White")
        self.name_label.place(x=10,y=10)
        self.name_entry = Entry(self.content_frame, width=70,bd=3)
        self.name_entry.place(x=100,y=10)
        self.age_label = Label(self.content_frame, bg="#1a0d00", font=self.text_font, text="Age", height=1, width=9,fg="White")
        self.age_label.place(x=10,y=50)
        self.age_entry = Entry(self.content_frame, width=70,bd=3)
        self.age_entry.place(x=100,y=50)
        self.ButtonFrame = Frame(self.main_frame, height=50, width=600,bg="#1a0d00")
        self.ButtonFrame.place(x=350, y=600)
        self.continue_button = Button(self.ButtonFrame, text="Continue", activebackground="saddle brown", bd=3,bg="black", fg="white",
                                      command=self.PlayPage, font=self.button_font, justify=CENTER, height=1,width=15)
        self.continue_button.place(x=0,y=0)
        self.back_button = Button(self.ButtonFrame,text="Back",activebackground="saddle brown",bd=3,bg="black",fg="white",
                                  command=self.first_page,font=self.button_font,justify=CENTER,height=1,width=15)
        self.back_button.place(x=285,y=0)

    def PlayPage(self):
        self.age=self.age_entry.get()
        self.name=self.name_entry.get()
        self.name=self.name.replace(" ", "")
        if self.age.isdigit() and self.name.isalpha():
            self.main_frame.destroy()
        else:
            self.name_entry.delete(0,len(self.name)+2)
            self.age_entry.delete(0, len(self.age))
            self.alert = "Please enter valid details"
            self.alert_info =Label(self.content_frame,bg="#1a0d00", font=self.text_font, text=self.alert, height=1, width=50,fg="White")
            self.alert_info.place(x=80,y=100)

    def CreateMainFrame(self,page="Any"):
        self.main_frame = Frame(self.root, height=800, width=1200)
        self.main_frame.place(x=0, y=0)
        self.BackgroundImage(self.main_frame,page)

    def BackgroundImage(self,root,page="Any"):
        if page=="First":
            self.background_image = ImageTk.PhotoImage(file="images/riddle_front.jpg")
        else:
            self.background_image = ImageTk.PhotoImage(file="images/riddle_simple.jpg")
        self.background_label = Label(root, image=self.background_image)
        self.background_label.grid(row=0, column=0)

    def play_friend(self):
        pass
    def about(self):
        pass

if __name__ == '__main__':
    Riddle_Game()