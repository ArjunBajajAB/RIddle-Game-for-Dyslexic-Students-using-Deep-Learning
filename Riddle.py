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
                                      command=self.PlayPageComp, font=self.button_font, justify=CENTER, height=1,width=15)
        self.continue_button.place(x=0,y=0)
        self.back_button = Button(self.ButtonFrame,text="Back",activebackground="saddle brown",bd=3,bg="black",fg="white",
                                  command=self.first_page,font=self.button_font,justify=CENTER,height=1,width=15)
        self.back_button.place(x=285,y=0)

    def PlayPageComp(self):
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

    def play_friend(self):
        self.main_frame.destroy()
        self.CreateMainFrame()
        self.heading_frame = Frame(self.main_frame, height=100, width=1100, bg="#1a0d00")
        self.heading_frame.place(x=20, y=20)
        self.heading = Message(self.heading_frame, font=self.heading_font, bg="#1a0d00", fg="White", width=1100,
                               justify=CENTER, text="Let us start with your details")
        self.heading.place(x=10, y=10)
        self.content_frame = Frame(self.main_frame, height=250, width=800, bg="#1a0d00")
        self.content_frame.place(x=300, y=300)
        self.nameOne_label = Label(self.content_frame, bg="#1a0d00", font=self.text_font, text="Player 1 Name", height=1, width=15,justify=LEFT,fg="White")
        self.nameOne_label.place(x=10, y=10)
        self.nameOne_entry = Entry(self.content_frame, width=70, bd=3)
        self.nameOne_entry.place(x=200, y=10)
        self.ageOne_label = Label(self.content_frame, bg="#1a0d00", font=self.text_font, text="Player 1 Age", height=1, width=15,justify=LEFT,fg="White")
        self.ageOne_label.place(x=10, y=60)
        self.ageOne_entry = Entry(self.content_frame, width=70, bd=3)
        self.ageOne_entry.place(x=200, y=60)

        self.nameTwo_label = Label(self.content_frame, bg="#1a0d00", font=self.text_font, text="Player 2 Name", height=1,width=15,justify=LEFT,fg="White")
        self.nameTwo_label.place(x=10, y=110)
        self.nameTwo_entry = Entry(self.content_frame, width=70, bd=3)
        self.nameTwo_entry.place(x=200, y=110)
        self.ageTwo_label = Label(self.content_frame, bg="#1a0d00", font=self.text_font, text="Player 2 Age", height=1,width=15,justify=LEFT,fg="White")
        self.ageTwo_label.place(x=10, y=160)
        self.ageTwo_entry = Entry(self.content_frame, width=70, bd=3)
        self.ageTwo_entry.place(x=200, y=160)

        self.ButtonFrame = Frame(self.main_frame, height=50, width=600, bg="#1a0d00")
        self.ButtonFrame.place(x=450, y=630)
        self.continue_button = Button(self.ButtonFrame, text="Continue", activebackground="saddle brown", bd=3,bg="black", fg="white",
                                      command=self.PlayPageFriend, font=self.button_font, justify=CENTER, height=1, width=15)
        self.continue_button.place(x=0, y=0)
        self.back_button = Button(self.ButtonFrame, text="Back", activebackground="saddle brown", bd=3, bg="black",fg="white",
                                  command=self.first_page, font=self.button_font, justify=CENTER, height=1, width=15)
        self.back_button.place(x=285, y=0)

    def PlayPageFriend(self):
        self.ageOne=self.ageOne_entry.get()
        self.nameOne=self.nameOne_entry.get()
        self.nameOne=self.nameOne.replace(" ", "")
        self.ageTwo=self.ageTwo_entry.get()
        self.nameTwo=self.nameTwo_entry.get()
        self.nameTwo=self.nameTwo.replace(" ", "")
        if self.ageOne.isdigit() and self.nameOne.isalpha() and self.nameTwo.isalpha() and self.ageTwo.isdigit():
            self.main_frame.destroy()
        else:
            self.nameOne_entry.delete(0,len(self.nameOne)+2)
            self.ageOne_entry.delete(0, len(self.ageOne))
            self.nameTwo_entry.delete(0,len(self.nameTwo)+2)
            self.ageTwo_entry.delete(0, len(self.ageTwo))
            self.alert = "Please enter valid details"
            self.alert_info =Label(self.content_frame,bg="#1a0d00", font=self.text_font, text=self.alert, height=1, width=50,fg="White")
            self.alert_info.place(x=80,y=200)

    def about(self):
        self.content_frame.destroy()  # Just destroy the content frame as the heading is needed
        self.content_frame = Frame(self.main_frame, height=300, width=700, bg="#1a0d00")
        self.content_frame.place(x=270, y=450)  # Place below heading
        self.about = "Riddle Game \n\n This is a game mainly developed for children suffering from dyslexia or children who are unable to read and write properly. The children can play with computer or other children and should play under someone's supervision \n This application is developed by Arjun Bajaj, a BCA student"
        self.AboutInfo = Message(self.content_frame, bg="#1a0d00", fg="White", font=self.text_font, justify=CENTER,width=600,text=self.about)
        self.AboutInfo.place(x=0, y=0)
        self.BackButton = Button(self.content_frame, text="Back", activebackground="grey", bd=3, bg="White", fg="Black",
                                 command=self.first_page, font=self.button_font, justify=CENTER, height=1, width=5)
        self.BackButton.place(x=400, y=250)

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

if __name__ == '__main__':
    Riddle_Game()