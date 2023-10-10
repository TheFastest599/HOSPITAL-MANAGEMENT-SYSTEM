from tkinter import *
from unittest import result
from PIL import ImageTk, Image
from functools import partial
import csv
# import pyperclip as pc #pip install pyperclip




def Login():
    window = Tk()

    window.geometry("509x416+400+100")
    window.configure(bg = "#ffffff")
    window.title("LOGIN")
    canvas = Canvas(window,bg = "#ffffff",height = 416,width = 509,bd = 0,highlightthickness = 0,relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"background_2.png")
    background = canvas.create_image(254.5, 208.0,image=background_img)

    entry0_img = PhotoImage(file = f"img_textBox0.png")
    entry0_bg = canvas.create_image(365.0, 173.5,image = entry0_img)

    namevalue = StringVar()
    passvalue = StringVar()

    def Submit():     #Function for login.The person Logged in as is stored in variable "usser_pass".
        
        credentials = {}

        
        with open('USERNAMES.csv','r+') as cs:
            csv_reader=csv.reader(cs)
            for line in csv_reader:
                credentials[line[0]]=line[1]
        global run_staff_side
        global usser_pass

        run_staff_side=False

        x=namevalue.get()
        y=passvalue.get()
        
        if x in credentials.keys():
            
            if (y == credentials[x]):
                window.destroy()
                usser_pass=(x)
                run_staff_side=True
            else:
                error=Label(text="Invalid password!!",fg="red",font="Copperplate 10 bold")
                error.place(x = 280, y = 283)

        else:
            error=Label(text="User not found!!",fg="red",font="Copperplate 10 bold")
            error.place(x = 280, y = 283)
        
    entry0 = Entry(bd = 0,bg = "#c4c4c4",highlightthickness = 0,font="rose",textvariable=namevalue)
    entry0.place(x = 283, y = 162, width = 163, height = 24)

    entry1_img = PhotoImage(file = f"img_textBox1.png")
    entry1_bg = canvas.create_image(365.0, 252.5,image = entry1_img)

    entry1 = Entry(bd = 0,bg = "#c4c4c4",highlightthickness = 0,font="rose",textvariable=passvalue, show='*')
    entry1.place(x = 283, y = 241,width = 163,height = 24)

    img0 = PhotoImage(file = f"img0.png")
    b0 = Button(image = img0,borderwidth = 0,highlightthickness = 0,command = partial(Submit),relief = "flat")
    b0.place(x = 304, y = 322,width = 115,height = 28)

    

    window.resizable(False, False)
    window.mainloop()
    return usser_pass,run_staff_side

#print("Logged in as:",result)
