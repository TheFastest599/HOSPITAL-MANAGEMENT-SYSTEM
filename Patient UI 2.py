from tkinter import *
import tkinter
import tkinter.font
from PIL import ImageTk, Image  # install pil
import csv
import math
from tkinter import filedialog, messagebox
from tkinter import ttk
from fpdf import FPDF  # install fpdf
import random
import pandas as pc  # import pandas library
from tabulate import tabulate  # import tabulate module from tabulate library
import pyttsx3  # install pyttsx3
import datetime
import threading
import webbrowser
import os


def Clinics_Near_me():
    webbrowser.open(
        'https://www.google.co.in/maps/@26.1843445,91.7636191,14z?hl=en-GB')


def btn_clicked(a):  # Stores various info
    d = {"Centre of Excellence": "Centre of Excellence.txt", "Emergency Contact": "Emergency Contact.txt",
         "Health Tips": "Health Tips.txt", "Specialists": "Specialists.txt", "About Us": "About Us.txt",
         "Contact Us": "Contact Us.txt", "Privacy Policy": "Privacy Policy.txt"}
    x = open(os.getcwd()+r"/Button_display/"+d[a], "r")
    display = x.read()
    root = Tk()
    root.geometry("1000x450")
    root.title(a)
    scrollbarY = Scrollbar(root, orient=VERTICAL)
    scrollbarY.pack(side=RIGHT, fill=Y)
    f = ('Times', 14)
    textbox = Text(root, height=1000, width=450,
                   font=f, bg="#98CBDD", state=NORMAL)
    textbox.pack()
    textbox.insert(END, display)
    textbox.pack()

    textbox.pack()
    textbox.config(yscrollcommand=scrollbarY.set)
    scrollbarY.config(command=textbox.yview)


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
volume = engine.getProperty('volume')
engine.setProperty('volume', 0.7)
engine.runAndWait()
engine.setProperty('rate', 200)


def Patient_ID_Generator():
    Alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    A1 = random.randint(0, 25)
    A2 = random.randint(0, 25)
    N = random.randint(1000, 9999)
    PID = Alphabets[A1] + Alphabets[A2] + str(N)
    return PID


def Table(x):
    head = ["BED_ID", "BED_TYPE", "BED_STATUS", "PATIENT_ID"]
    print(tabulate(x, headers=head, tablefmt='github'))


def Filtering(x):
    DATA_forFiltering = pc.read_csv("HOSPITAL BED INFO.csv")
    DATA_forFiltering.columns = [column.replace(
        " ", "_") for column in DATA_forFiltering.columns]
    DATA_forFiltering.query(x, inplace=True)
    List = list(DATA_forFiltering["BED_ID"])
    Number_of_rows = len(DATA_forFiltering["BED_ID"].axes[0])
    return List, Number_of_rows


def UpdatingRow(x, z1, z2):
    DATA_All.loc[x, "BED_STATUS"] = (z1)
    DATA_All.loc[x, "PATIENT_ID"] = (z2)
    # Change file name accordingly
    DATA_All.to_csv("HOSPITAL BED INFO.csv", index=False)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!Wellcome to Health Wings Hospital !")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!Wellcome to Health Wings Hospital !")
    else:
        speak("Good Evening!Wellcome to Health Wings Hospital !")


def count_bed(x):
    if x == 0:
        y = "Sorry no beds are available!!"
        return y
    else:
        y = x
        return y


# -----------------------------------------------------------
DATA_All = pc.read_csv("HOSPITAL BED INFO.csv")
PINFO = pc.read_csv("PATIENT_INFO.csv")

# Opening databases
# -------------------------------------------------

window = Tk()
window.geometry("1360x690+0+0")
window.title("HOSPITAL MANAGEMENT SYSTEM : PATIENT SIDE")
window.iconbitmap("HOSPITAL.ico")
t1 = threading.Thread(target=wishMe(), args=10)
t1.start()  # Voice used--------------------------------------------
window.configure(bg="#ffffff")
canvas = Canvas(window, bg="#ffffff", height=690, width=1360,
                bd=0, highlightthickness=0, relief="ridge")
canvas.place(x=0, y=0)
background_img = PhotoImage(file="background.png")
background = canvas.create_image(680.0, 345.0, image=background_img)

img_view = Image.open(r"Health Wings.png")
img_view.thumbnail((1290, 420))
img_view1 = Image.open(r"Health Wings(5).png")
img_view1.thumbnail((1290, 420))
img_view2 = Image.open(r"Health Wings(2).png")
img_view2.thumbnail((1290, 420))
img_view3 = Image.open(r"Health Wings(3).png")
img_view3.thumbnail((1290, 420))
img_view4 = Image.open(r"Health Wings(4).png")
img_view4.thumbnail((1290, 420))
img_view5 = Image.open(r"Health Wings(1).png")
img_view5.thumbnail((1290, 420))

# open images to use with labels
image1 = ImageTk.PhotoImage(img_view)
image2 = ImageTk.PhotoImage(img_view1)
image3 = ImageTk.PhotoImage(img_view2)
image4 = ImageTk.PhotoImage(img_view3)
image5 = ImageTk.PhotoImage(img_view4)
image6 = ImageTk.PhotoImage(img_view5)


frame = Frame(window, width=1292, height=420, bg='white', relief=GROOVE, bd=2)
frame.place(x=53, y=109)

# create list of images
images = [image2, image1, image3, image4, image5]
# configure the image to the Label in frame
i = 0
image_label = Label(frame, image=images[i])
image_label.grid(row=1)

# creating loop af photos to change by itself


def start():
    global i, show
    if i >= (len(images) - 1):
        i = 0
        image_label.config(image=images[i])
    else:
        i = i + 1
        image_label.configure(image=images[i])
    show = image_label.after(3000, start)

# create functions to display
# previous an next images


def previous():
    global i
    i = i - 1
    try:
        image_label.config(image=images[i])
    except:
        i = 0
        previous()


def next():
    global i
    i = i + 1
    try:
        image_label.config(image=images[i])
    except:
        i = -1
        next()


start()


min_w = 50  # Minimum width of the frame
max_w = 200  # Maximum width of the frame
cur_width = min_w  # Increasing width of the frame
expanded = False  # Check if it is completely exanded

image = Image.open("logo 2.png")
image = image.resize((50, 40), Image.Resampling.LANCZOS)
img = ImageTk.PhotoImage(image)
# menu starting-----------------------------------------------------------------------------------------


def expand():
    global cur_width, expanded
    cur_width += 10  # Increase the width by 10
    rep = window.after(5, expand)  # Repeat this func every 5 ms
    frame.config(width=cur_width)  # Change the width to new increase width
    if cur_width >= max_w:  # If width is greater than maximum width
        expanded = True  # Frame is expended
        window.after_cancel(rep)  # Stop repeating the func
        fill()


def contract():
    global cur_width, expanded
    cur_width -= 10  # Reduce the width by 10
    rep = window.after(5, contract)  # Call this func every 5 ms
    frame.config(width=cur_width)  # Change the width to new reduced width
    if cur_width <= min_w:  # If it is back to normal width
        expanded = False  # Frame is not expanded
        window.after_cancel(rep)  # Stop repeating the func
        fill()


def fill():
    if expanded:  # If the frame is exanded
        ring_b.config(text='MENU', image='', font=(0, 15))
        set_b.config(text='Tutorial', image='', font=(0, 21))
        home_b.config(text='Exit', image='', font=(0, 21))
    else:
        # Bring the image back
        ring_b.config(image=ring, font=(0, 21))
        set_b.config(image=tut, font=(0, 21))
        home_b.config(image=tut, font=(0, 21))


# Define the icons to be shown and resize it
ring = ImageTk.PhotoImage(Image.open(
    'menu_img.png').resize((21, 14), Image.Resampling.LANCZOS))
tut = ImageTk.PhotoImage(Image.open(
    'mig.jpeg').resize((21, 19), Image.Resampling.LANCZOS))
# ext = ImageTk.PhotoImage(Image.open('t.png').resize((21,19),Image.Resampling.LANCZOS))

window.update()  # For the width to get updated
frame = Frame(window, bg='#464646', width=50, height=window.winfo_height())
frame.grid(row=0, column=0)


def tutorial():
    win = Toplevel()
    win.title("TUTORIAL")
    win.geometry("1366x700")
    img_view = Image.open(os.getcwd()+r"/Tutorial/TutorialP2.png")
    img_view.thumbnail((1366, 690))
    # open images to use with labels
    image1 = ImageTk.PhotoImage(img_view)
    frame = Frame(win, width=1024, height=720, bg='white', relief=GROOVE, bd=2)
    frame.grid(column=0, row=0)
    # create list of images
    images = [image1]
    # configure the image to the Label in frame
    i = 0
    image_label = Label(frame, image=image1)
    image_label.grid(row=1)
    # previous an next images

    def previous():
        global i
        i = i - 1
        try:
            image_label.config(image=images[i])
        except:
            i = 0
            previous()

    def next():
        global i
        i = i + 1
        try:
            image_label.config(image=images[i])
        except:
            i = -1
            next()


# Make the buttons with the icons to be shown
home_b = Button(frame, bg='#464646', image=tut, fg="#ffffff",
                relief='flat', command=window.destroy)
set_b = Button(frame, bg='#464646', image=tut, fg="#ffffff",
               relief='flat', command=tutorial)
ring_b = Label(frame, image=ring, bg='#464646', fg="#ffffff", relief='flat')

# Put them on the frame
ring_b.place(x=5, y=12)
set_b.place(x=5, y=55)
home_b.place(x=5, y=105)

# Bind to the frame, if entered or left
frame.bind('<Enter>', lambda e: expand())
frame.bind('<Leave>', lambda e: contract())

# So that it does not depend on the widgets inside the frame
frame.grid_propagate(False)
# menu end-------------------------------------------------------------------------


def update_tabel():
    global GEN_BED_ID, nGEN_BED, PAY_BED_ID, nPAY_BED, CABIN_BED_ID, nCABIN_BED, ICU_BED_ID
    global ICU_BED_ID, nICU_BED, COVID_BED_ID, nCOVID_BED
    GEN_BED_ID, nGEN_BED = Filtering(
        'BED_TYPE == "GENERAL BED" and BED_STATUS == "VACANT"')
    PAY_BED_ID, nPAY_BED = Filtering(
        'BED_TYPE == "PAYING BED" and BED_STATUS == "VACANT"')
    CABIN_BED_ID, nCABIN_BED = Filtering(
        'BED_TYPE == "CABIN BED" and BED_STATUS == "VACANT"')
    ICU_BED_ID, nICU_BED = Filtering(
        'BED_TYPE == "ICU BED" and BED_STATUS == "VACANT"')
    COVID_BED_ID, nCOVID_BED = Filtering(
        'BED_TYPE == "COVID BED" and BED_STATUS == "VACANT"')

    t1 = ["BED TYPE", "NUMBER OF BEDS"]
    t2 = ["General Bed", str(count_bed(nGEN_BED))]
    t3 = ["Paying Bed", str(count_bed(nPAY_BED))]
    t4 = ["CABIN Bed", str(count_bed(nCABIN_BED))]
    t5 = ["ICU Bed", str(count_bed(nICU_BED))]
    t6 = ["COVID Bed", str(count_bed(nCOVID_BED))]
    t = [t1, t2, t3, t4, t5, t6]

    with open("BED.csv", "w", newline='') as cs:
        csv_writer = csv.writer(cs)
        csv_writer.writerows(t)
    t = []


update_tabel()


def update_bed_info(choice, P_ID):
    global bed_Type, row_number, bed_ID
    if choice == "OPD":
        bed_Type = "OPD"
        bed_ID = "NONE"
    elif choice == "GENERAL":
        bed_Type = "GENERAL BED"
        row_number = DATA_All[DATA_All["BED_ID"] == GEN_BED_ID[0]].index[0]
        bed_ID = GEN_BED_ID[0]

    elif choice == "PAYING":
        bed_Type = "PAYING BED"
        row_number = DATA_All[DATA_All["BED_ID"] == PAY_BED_ID[0]].index[0]
        bed_ID = PAY_BED_ID[0]

    elif choice == "CABIN":
        bed_Type = "CABIN BED"
        row_number = DATA_All[DATA_All["BED_ID"] == CABIN_BED_ID[0]].index[0]
        bed_ID = CABIN_BED_ID[0]

    elif choice == "ICU":
        bed_Type = "ICU BED"
        row_number = DATA_All[DATA_All["BED_ID"] == ICU_BED_ID[0]].index[0]
        bed_ID = ICU_BED_ID[0]

    elif choice == "COVID":
        bed_Type = "COVID BED"
        row_number = DATA_All[DATA_All["BED_ID"] == COVID_BED_ID[0]].index[0]
        bed_ID = COVID_BED_ID[0]

    if (bed_Type == "GENERAL BED" or bed_Type == "PAYING BED" or
            bed_Type == "CABIN BED" or bed_Type == "ICU BED" or bed_Type == "COVID BED"):
        UpdatingRow(row_number, "OCCUPIED", P_ID)

    # Updates the HOSPITAL BED INFO-------------------------------------------


def data_update(x):
    if do_the_thing == "YES":
        P_ID = Patient_ID_Generator()
        reffered_by = x[8]
        Name_of_patient = x[0]
        age = x[3]
        gender = x[4]
        contact_number = x[6]
        address = x[5]
        ID_type = x[2]
        ID_number = ("'" + x[7])

        now = datetime.datetime.now()  # Time And Date
        Time = now.strftime("%H:%M:%S")
        Date = now.strftime("%d-%m-%Y")

        # Gets the type of bed , gives the bed ID and the row of HOSPITAL BED INFO.csv to be updated
        choice = x[1]

        update_bed_info(choice, P_ID)
        global q
        q = []
        q.append([P_ID, bed_ID, bed_Type, reffered_by, Name_of_patient.upper(), age, gender.upper(), contact_number,
                  address.replace(",", "|"), ID_type, ID_number, Time, Date])  # Stores the input data in a list.
        with open("PATIENT_INFO.csv", "a+", newline='') as ds:
            csv_writer = csv.writer(ds)
            # Stoes the newly entered data in the CSV file.
            csv_writer.writerows(q)
        ds.close()

        # Updates the Patient part.----------------------------------------------------


def bill_prescription(h):
    if prep:
        f = ('Times', 14)
        bill_widow = Toplevel()
        bill_widow.title("sub Panel")
        bill_widow.minsize(800, 500)
        Grid.rowconfigure(bill_widow, 0, weight=1)
        Grid.columnconfigure(bill_widow, 0, weight=1)
        name_hospital = Label(bill_widow, text="HEALTH-WINGS HOSPITAL", bg="#581845", fg="#d1cddb",
                              font="Copperplate 23 italic",
                              relief=RIDGE, anchor=W, image=img, compound=LEFT, padx=30)
        name_hospital.grid(row=0, column=0, columnspan=2,
                           ipady=8, sticky="new")
        line = h[0]
        a = line[8]
        b = a.replace("|", ",")
        line[8] = b

        def get_pdf():
            # save FPDF() class into a
            # variable pdf
            pdf = FPDF()

            # Add a page
            pdf.add_page()

            # set style and size of fontin the pdf
            pdf.set_font("Arial", size=15)
            line1 = ["Patient ID:", line[0],
                     "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tGender:", line[6]]
            line2 = ["Name:", line[4], "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tAge:",
                     line[5]]
            line3 = ["Contact No.:", line[7],
                     "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tDate:", line[12]]
            line4 = ["Address:", line[8],
                     "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tTime:", line[11]]
            line5 = ["Patient Bed type:", line[2],
                     "\t\t\t\t\t\t\t\t\t\t\t\t\t\tReffered By:", line[3]]

            line1_1, line1_2, line1_3, line1_4 = line1[0], line1[1], line1[2], line1[3]
            line2_1, line2_2, line2_3, line2_4 = line2[0], line2[1], line2[2], line2[3]
            line3_1, line3_2, line3_3, line3_4 = line3[0], line3[1], line3[2], line3[3]
            line4_1, line4_2, line4_3, line4_4 = line4[0], line4[1], line4[2], line4[3]
            line5_1, line5_2, line5_3, line5_4 = line5[0], line5[1], line5[2], line5[3]

            line1_add = line1_1 + line1_2 + line1_3 + line1_4
            line2_add = line2_1 + line2_2 + line2_3 + line2_4
            line3_add = line3_1 + line3_2 + line3_3 + line3_4
            line4_add = line4_1 + line4_2 + line4_3 + line4_4
            line5_add = line5_1 + line5_2 + line5_3 + line5_4

            # create a cell
            pdf.cell(200, 10, txt="HEALTH-WINGS HOSPITAL", ln=1, align="C")
            pdf.cell(200, 10, txt="Maya Ville,House No.97,Borthakur Mill Road,Ulubari,guwahati-781007,Assam", ln=2,
                     align="C")
            pdf.cell(200, 10, txt="Phone:+91 (0361) 2456510", ln=3, align="C")
            pdf.cell(
                200, 10, txt="Email:assam.healthwingshospital@gmail.com", ln=4, align="C")
            pdf.cell(100, 10, txt="", ln=5)
            pdf.cell(100, 10, txt="", ln=6)
            pdf.cell(100, 10, txt=line1_add, ln=7)
            pdf.cell(100, 10, txt=line2_add, ln=8)
            pdf.cell(100, 10, txt=line3_add, ln=9)
            pdf.cell(100, 10, txt=line4_add, ln=10)
            pdf.cell(100, 10, txt=line5_add, ln=11)

            # save the pdf with name .pdf
            output_path = filedialog.askdirectory()
            pdf.output(output_path + "/" + save_as_name.get()+'.pdf')

        def save_as():
            save = Toplevel()
            save.geometry("600x150+470+250")
            save.title("save as")
            Label(save, text="Save as:", font="Comic").grid(
                row=0, column=0, padx=(30, 0), pady=(30, 20))
            Entry(save, width=70, textvariable=save_as_name).grid(row=0, column=1, padx=(30, 50),
                                                                  pady=(30, 20))
            Button(save, text="Save", font="Comic", command=lambda: [get_pdf(), save.destroy()]).grid(row=1, column=1,
                                                                                                      ipadx=10,
                                                                                                      padx=(
                                                                                                          30, 50),
                                                                                                      pady=(
                                                                                                          0, 20),
                                                                                                      sticky=E)

        Label(bill_widow, text="BILL RECIEPT", font=f).grid(
            row=5, column=0, ipady=8, pady=(30, 6))
        Button(bill_widow, width=12, image=pdf_img_button, font=f, relief=RAISED, command=save_as) \
            .grid(row=5, column=1, ipadx=30, padx=(0, 50), sticky=W)

        save_as_name = StringVar()

        bil_address = Label(bill_widow, text="Maya Ville,Borthakur Mill Road,Ulubari,guwahati-781007,Assam",
                            font="Calibri 15")
        bil_address.grid(row=2, padx=50, columnspan=2, sticky="new")
        bil_address = Label(
            bill_widow, text="Phone:+91 (0361) 2456510", font="Calibri 15")
        bil_address.grid(row=3, padx=50, columnspan=2, sticky="new")
        bil_address = Label(
            bill_widow, text="Email:assam.healthwingshospital@gmail.com", font="Calibri 15")
        bil_address.grid(row=4, padx=50, columnspan=2, sticky="new")
        bill_frame = Frame(bill_widow, bd=2, bg='#CCCCCC',
                           relief=SOLID, padx=10)
        bill_frame.grid(row=6, padx=50, columnspan=2,
                        sticky="new", pady=(0, 100))

        Label(bill_frame, text="Patient ID:", bg='#CCCCCC', font=f).grid(
            row=0, column=0, sticky=W, pady=10, padx=(100, 0))
        Label(bill_frame, text="Name:", bg='#CCCCCC', font=f).grid(
            row=1, column=0, sticky=W, pady=10, padx=(100, 0))
        Label(bill_frame, text="Contact No.:", bg='#CCCCCC', font=f).grid(
            row=2, column=0, sticky=W, pady=10, padx=(100, 0))
        Label(bill_frame, text="Address:", bg='#CCCCCC', font=f).grid(
            row=3, column=0, sticky=W, pady=10, padx=(100, 0))
        Label(bill_frame, text="Patient Bed type:", bg='#CCCCCC', font=f).grid(row=4, column=0, sticky=W, pady=10,
                                                                               padx=(100, 0))
        Label(bill_frame, text="Gender:", bg='#CCCCCC', font=f).grid(
            row=0, column=3, sticky=W, pady=10, padx=(300, 0))
        Label(bill_frame, text="Age:", bg='#CCCCCC', font=f).grid(
            row=1, column=3, sticky=W, pady=10, padx=(300, 0))
        Label(bill_frame, text="Date:", bg='#CCCCCC', font=f).grid(
            row=2, column=3, sticky=W, pady=10, padx=(300, 0))
        Label(bill_frame, text="Time:", bg='#CCCCCC', font=f).grid(
            row=3, column=3, sticky=W, pady=10, padx=(300, 0))
        Label(bill_frame, text="Reffered By:", bg='#CCCCCC', font=f).grid(
            row=4, column=3, sticky=W, pady=10, padx=(300, 0))

        Label(bill_frame, text=line[0], bg='#CCCCCC', font=f).grid(
            row=0, column=1, sticky=W, padx=(50, 60))
        Label(bill_frame, text=line[4], bg='#CCCCCC', font=f).grid(
            row=1, column=1, sticky=W, padx=(50, 60))
        Label(bill_frame, text=line[7], bg='#CCCCCC', font=f).grid(
            row=2, column=1, sticky=W, padx=(50, 60))
        Label(bill_frame, text=line[8], bg='#CCCCCC', font=f).grid(
            row=3, column=1, sticky=W, padx=(50, 60))
        Label(bill_frame, text=line[2], bg='#CCCCCC', font=f).grid(
            row=4, column=1, sticky=W, padx=(50, 60))
        Label(bill_frame, text=line[6], bg='#CCCCCC', font=f).grid(
            row=0, column=4, sticky=W, padx=(50, 60))
        Label(bill_frame, text=line[5], bg='#CCCCCC', font=f).grid(
            row=1, column=4, sticky=W, padx=(50, 60))
        Label(bill_frame, text=line[12], bg='#CCCCCC', font=f).grid(
            row=2, column=4, sticky=W, padx=(50, 60))
        Label(bill_frame, text=line[11], bg='#CCCCCC', font=f).grid(
            row=3, column=4, sticky=W, padx=(50, 60))
        Label(bill_frame, text=line[3], bg='#CCCCCC', font=f).grid(
            row=4, column=4, sticky=W, padx=(50, 60))
    else:
        pop = Toplevel()
        pop.geometry("320x170+500+250")
        pop.overrideredirect(True)
        pop.title("pop up")
        notification = Frame(pop, bd=2, relief="raised", padx=10, bg="#FF6B00")
        notification.grid(row=0, padx=0)
        Label(notification, text="No Patient with Patient ID:\n"+TIG, font="Comic", bg="#FF6B00")\
            .grid(row=0, column=0, pady=(30, 10), padx=(35, 0))
        Button(notification, text="OK", font="Comic", command=lambda: [pop.destroy()])\
            .grid(row=1, column=1, sticky="es", pady=40, ipadx=18)


pdf_img = Image.open(r"Mur PDF.png")
pdf_img.thumbnail((75, 75))
pdf_img_button = ImageTk.PhotoImage(pdf_img)

lay = []


joy = []


def display_table():
    top = Toplevel()
    joy.append(top)
    top.configure(bg='#0B5A81')
    top.geometry('500x300+470+250')
    top.minsize(500, 300)
    top.maxsize(500, 300)
    top.overrideredirect(True)
    Grid.rowconfigure(top, 0, weight=1)
    Grid.columnconfigure(top, 0, weight=1)
    Grid.rowconfigure(top, 1, weight=1)
    Grid.columnconfigure(top, 1, weight=1)
    Grid.rowconfigure(top, 2, weight=1)
    Grid.columnconfigure(top, 2, weight=1)
    Grid.rowconfigure(top, 3, weight=1)
    Grid.columnconfigure(top, 3, weight=1)
    Grid.rowconfigure(top, 4, weight=1)
    Grid.columnconfigure(top, 4, weight=1)
    Grid.rowconfigure(top, 5, weight=1)
    Grid.columnconfigure(top, 5, weight=1)
    top.title("bed information")
    msg = Label(top, text="Displying Bed Info:")
    msg.grid(row=1, column=0, columnspan=5, pady=(10, 0))
    with open("BED.csv", newline="") as file:
        reader = csv.reader(file)
        # r and c tell us where to grid the labels
        r = 1
        for col in reader:
            c = 1
            for row in col:
                # i've added some styling
                label = tkinter.Label(
                    top, width=10, height=2, text=row, relief=tkinter.RIDGE)
                label.grid(row=r + 1, column=c + 1, sticky=EW)
                c += 1
            r += 1

    def exit_btn():
        top.destroy()
        top.update()
    btn = Button(top, text='EXIT', command=exit_btn)
    btn.grid(row=8, column=1, columnspan=4, pady=20, ipadx=20, ipady=5)


joy = []


def createform():
    top = Toplevel()
    joy.append(top)
    top.title("form")
    top.minsize(620, 690)
    top.maxsize(620, 690)
    msg = Message(top, text="Records and Paperwork",
                  font="Comic 12", width=200)
    msg.grid()
    top.config(bg='#0B5A81')
    f = ('Times', 14)
    var = StringVar()
    var.set('male')

    countries = []
    variable = StringVar()
    world = open("BED_TYPE.txt", 'r')
    for country in world:
        country = country.rstrip('\n')
        countries.append(country)
    variable.set(countries[4])

    idtype = []
    id = StringVar()
    wo = open("ID.txt", 'r')
    for i in wo:
        i = i.rstrip('\n')
        idtype.append(i)
    id.set(idtype[1])

    right_frame = Frame(top, bd=2, bg='#CCCCCC', relief=SOLID, padx=10)
    right_frame.grid(padx=50)

    name_form = Label(right_frame, text="HEALTH-WINGS HOSPITAL ", bg="skyblue", fg="blue", font="Copperplate 23 italic",
                      borderwidth=5, relief=SUNKEN, anchor=N, padx=30)
    name_form.grid(row=0, column=0, sticky=W, pady=15, columnspan=2)
    Label(right_frame, text="Enter Name of patient", bg='#CCCCCC',
          font=f).grid(row=1, column=0, sticky=W, pady=10)
    Label(right_frame, text="Enter Age", bg='#CCCCCC',
          font=f).grid(row=2, column=0, sticky=W, pady=10)
    Label(right_frame, text="Select Gender", bg='#CCCCCC',
          font=f).grid(row=3, column=0, sticky=W, pady=10)
    Label(right_frame, text="Enter Address", bg='#CCCCCC',
          font=f).grid(row=4, column=0, sticky=W, pady=10)
    Label(right_frame, text="Contact Number", bg='#CCCCCC',
          font=f).grid(row=5, column=0, sticky=W, pady=10)
    Label(right_frame, text="Select ID", bg='#CCCCCC',
          font=f).grid(row=7, column=0, sticky=W, pady=10)
    Label(right_frame, text="Enter ID number.", bg='#CCCCCC',
          font=f).grid(row=8, column=0, sticky=W, pady=10)
    Label(right_frame, text="Select Bed Type", bg='#CCCCCC',
          font=f).grid(row=6, column=0, sticky=W, pady=10)
    Label(right_frame, text="Reffered by", bg='#CCCCCC',
          font=f).grid(row=9, column=0, sticky=W, pady=10)
    gender_frame = LabelFrame(right_frame, bg='#CCCCCC', padx=10, pady=10, )

    def getvals():
        global do_the_thing
        do_the_thing = "YES"
        global x
        x = [namevalue.get(), variable.get(), id.get(), agevalue.get(), var.get(), addressvalue.get(),
             contactvalue.get(), id_info_value.get(), refferedvalue.get()]
        data_update(x)

    namevalue = StringVar()
    agevalue = StringVar()
    addressvalue = StringVar()
    contactvalue = StringVar()
    id_info_value = StringVar()
    refferedvalue = StringVar()

    register_name = Entry(right_frame, font=f, textvariable=namevalue)
    register_age = Entry(right_frame, font=f, textvariable=agevalue)
    reffered_by = Entry(right_frame, font=f, textvariable=refferedvalue)
    register_IDinfo = Entry(right_frame, font=f, textvariable=id_info_value)

    male_rb = Radiobutton(gender_frame, text='Male', bg='#CCCCCC',
                          variable=var, value='male', font=('Times', 10))
    female_rb = Radiobutton(gender_frame, text='Female', bg='#CCCCCC', variable=var, value='female',
                            font=('Times', 10))
    others_rb = Radiobutton(gender_frame, text='Others', bg='#CCCCCC',
                            variable=var, value='others', font=('Times', 10))

    register_bedtype = OptionMenu(right_frame, variable, *countries)
    register_id = OptionMenu(right_frame, id, *idtype)

    register_bedtype.config(width=15, font=('Times', 12))
    enter_contact = Entry(right_frame, font=f, textvariable=contactvalue)
    enter_address = Entry(right_frame, font=f, textvariable=addressvalue)

    def perp_prep():
        global prep
        prep = True

    def exit_btn():
        top.destroy()
        top.update()

    register_btn = Button(right_frame, width=15, text='Submit', font=f, relief=RAISED, cursor='hand2',
                          command=lambda: [getvals(), exit_btn(), perp_prep(), bill_prescription(q)])
    register_name.grid(row=1, column=1, pady=10, padx=20)
    register_age.grid(row=2, column=1, pady=10, padx=20)
    enter_address.grid(row=4, column=1, pady=10, padx=20)
    enter_contact.grid(row=5, column=1, pady=10, padx=20)
    register_bedtype.grid(row=6, column=1, pady=10, padx=20)
    register_id.grid(row=7, column=1, pady=10, padx=20)
    register_IDinfo.grid(row=8, column=1, pady=10, padx=20)
    reffered_by.grid(row=9, column=1, pady=10, padx=20)
    register_btn.grid(row=10, column=1, pady=10, padx=20)
    gender_frame.grid(row=3, column=1, pady=10, padx=20)
    male_rb.pack(expand=True, side=LEFT)
    female_rb.pack(expand=True, side=LEFT)
    others_rb.pack(expand=True, side=LEFT)


def my_patient_id():
    global show_presentation
    show_presentation = "YES"
    global TIG
    TIG = get_ID.get()
    prescription()


def prescription():
    # Part to check previous Prescription/Bill by previous Patient ID.-------------
    PINFO23 = pc.read_csv("PATIENT_INFO.csv")
    global PINFO_list
    global prep
    if show_presentation == "YES":
        try:
            PINFO23.columns = [column.replace(
                " ", "_") for column in PINFO23.columns]
            PINFO23.query('PATIENT_ID == @TIG', inplace=True)
            PINFO_list = PINFO23.values.tolist()
            dh = PINFO_list[0][8]
            adds = dh.replace("|", ",")
            age = str(math.floor(PINFO_list[0][5]))
            address = str(math.floor(PINFO_list[0][7]))
            PINFO_list[0][5] = age
            PINFO_list[0][8] = adds
            PINFO_list[0][7] = address
            prep = True
        except:
            pass
            prep = False


def searched_id():
    top = Toplevel()
    top.title("form")
    top.minsize(620, 690)
    msg = Label(top, text="Info NOT yet Available \n to be updated very soon...", font="Comic 12", bg='#0B5A81',
                width=100)
    msg.grid()
    top.config(bg='#0B5A81')

    def exit_btn():
        top.destroy()
        top.update()

    btn = Button(top, text='EXIT', command=exit_btn)
    btn.grid(ipadx=50)


img1 = PhotoImage(file=f"img1P.png")
b1 = Button(image=img1, borderwidth=0, highlightthickness=0,
            command=createform, relief="flat")  # bed book
b1.place(x=782, y=536, width=230, height=30)


img2 = PhotoImage(file=f"img2P.png")  # check for beds
b2 = Button(image=img2, borderwidth=0, highlightthickness=0,
            relief="flat", command=display_table)
b2.place(x=326, y=536, width=400, height=30)

img0 = PhotoImage(file=f"img0P.png")
b0 = Button(image=img0, borderwidth=0, highlightthickness=0, command=lambda: [
            my_patient_id(), bill_prescription(PINFO_list)], relief="flat")
b0.place(x=836, y=579, width=176, height=30)
get_ID = Entry(bd=0, bg="#FFFFFF", highlightthickness=0, font="rose")
get_ID.place(x=349, y=579, width=422, height=32)
get_ID.insert(0, "Enter Your Id Here To Get The Bill Report")

img3 = PhotoImage(file=f"img3P.png")
b3 = Button(image=img3, borderwidth=0, highlightthickness=0, command=lambda: [
            btn_clicked("Centre of Excellence")], relief="flat")
b3.place(x=984, y=67, width=225, height=25)

img4 = PhotoImage(file=f"img4P.png")
b4 = Button(image=img4, borderwidth=0, highlightthickness=0,
            command=lambda: [btn_clicked("Health Tips")], relief="flat")
b4.place(x=604, y=67, width=147, height=25)

img5 = PhotoImage(file=f"Button.png")
b5 = Button(image=img5, borderwidth=0, highlightthickness=0,
            command=lambda: [btn_clicked("Specialists")], relief="flat")
b5.place(x=200, y=67, width=126, height=25)

img6 = PhotoImage(file=f"img6P.png")
b6 = Button(image=img6, borderwidth=0, highlightthickness=0,
            command=Clinics_Near_me, relief="flat")
b6.place(x=780, y=67, width=173, height=25)

img7 = PhotoImage(file=f"img7P.png")
b7 = Button(image=img7, borderwidth=0, highlightthickness=0, command=lambda: [
            btn_clicked("Emergency Contact")], relief="flat")
b7.place(x=376, y=67, width=199, height=25)

img8 = PhotoImage(file=f"img8P.png")
b8 = Button(image=img8, borderwidth=0, highlightthickness=0,
            command=lambda: [btn_clicked("Contact Us")], relief="flat")
b8.place(x=335, y=653, width=171, height=30)

img9 = PhotoImage(file=f"img9P.png")
b9 = Button(image=img9, borderwidth=0, highlightthickness=0,
            command=lambda: [btn_clicked("Privacy Policy")], relief="flat")
b9.place(x=563, y=653, width=157, height=30)

img10 = PhotoImage(file=f"img10P.png")
b10 = Button(image=img10, borderwidth=0, highlightthickness=0,
             command=lambda: [btn_clicked("About Us")], relief="flat")
b10.place(x=796, y=653, width=149, height=30)


window.mainloop()
