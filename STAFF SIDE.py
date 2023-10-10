from tkinter import *
import tkinter
import tkinter.ttk as ttk
from PIL import ImageTk, Image  # install pil
import os
import csv
import math
from tkinter import filedialog, messagebox
from fpdf import FPDF  # install fpdf
import random
import pandas as pc  # import pandas library
from tabulate import tabulate  # import tabulate module from tabulate library
import datetime
from LOGIN import Login

v, run_staff_side = Login()
i = 0
if run_staff_side:  # If Login is succesfull,it starts the Staff Side Program

    # -------------------------------------------------
    window = Tk()
    window.geometry("1360x690+0+0")
    window.configure(bg="#ffffff")
    window.title("HOSPITAL MANAGEMENT SYSTEM : STAFF SIDE")
    window.iconbitmap("HOSPITAL.ico")
    window.configure(bg="#ffffff")

    canvas = Canvas(window, bg="#ffffff", height=690, width=1360,
                    bd=0, highlightthickness=0, relief="ridge")
    canvas.place(x=0, y=0)

    image = Image.open("logo 2.png")
    image = image.resize((40, 40), Image.Resampling.LANCZOS)
    img = ImageTk.PhotoImage(image)

    # menu--------------------------------
    min_w = 50  # Minimum width of the frame
    max_w = 200  # Maximum width of the frame
    cur_width = min_w  # Increasing width of the frame
    expanded = False  # Check if it is completely exanded

    # -----------------------------------------------------------
    DATA_All = pc.read_csv("HOSPITAL BED INFO.csv")
    PINFO = pc.read_csv("PATIENT_INFO.csv")
    # Opening databases

    def btn_clicked():
        frame = Frame(window, bg='grey', width=1066, height=529)
        frame.place(x=276, y=151)
        label = Label(frame, text="the stuff is displayed...", fg="black")
        label.grid(row=0, column=0)

        def exit():
            label = Label(frame, text="its done")
            label.grid(row=0, column=0)

        b10 = Button(frame, text="exit", borderwidth=0,
                     highlightthickness=0, command=exit, relief="flat")
        b10.grid(row=0, column=1)

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

    def count_bed(x):
        if x == 0:
            y = "Sorry no beds are available!!"
            return y
        else:
            y = x
            return y

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
    ring = ImageTk.PhotoImage(Image.open('menu_img.png').resize(
        (21, 14), Image.Resampling.LANCZOS))
    tut = ImageTk.PhotoImage(Image.open('mig.jpeg').resize(
        (21, 19), Image.Resampling.LANCZOS))

    window.update()  # For the width to get updated
    frame = Frame(window, bg='#464646', width=50, height=window.winfo_height())
    frame.grid(row=0, column=0)

    def tutorial():  # For Tutorial
        win = Toplevel()
        win.geometry("1366x690")
        win.title("TUTORIAL")
        img_view = Image.open(os.getcwd()+r"/Tutorial/TutorialS1.png")
        img_view.thumbnail((1366, 690))
        img_view1 = Image.open(os.getcwd()+r"/Tutorial/Patient Update23.png")
        img_view1.thumbnail((1366, 690))
        # open images to use with labels
        image1 = ImageTk.PhotoImage(img_view)
        image2 = ImageTk.PhotoImage(img_view1)
        frame = Frame(win, width=1292, height=420,
                      bg='white', relief=GROOVE, bd=2)
        frame.grid(column=0, row=0)

        # create list of images
        images = [image1, image2]
        # configure the image to the Label in frame
        i = 0
        image_label = Label(frame, image=images[i])
        image_label.grid(row=1)

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
        # start()

        btn1 = Button(win, text="<", bg='grey',
                      font='ariel 15 bold', relief=RAISED, command=previous)
        btn1.place(x=50, y=300)
        btn2 = Button(win, text=">", bg='grey',
                      font='ariel 15 bold', relief=RAISED, command=next)
        btn2.place(x=1200, y=300)

    # Make the buttons with the icons to be shown
    home_b = Button(frame, bg='#464646', image=tut, fg="#ffffff",
                    relief='flat', command=window.destroy)
    set_b = Button(frame, bg='#464646', image=tut, fg="#ffffff",
                   relief='flat', command=tutorial)
    ring_b = Label(frame, image=ring, bg='#464646',
                   fg="#ffffff", relief='flat')

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
            row_number = DATA_All[DATA_All["BED_ID"]
                                  == CABIN_BED_ID[0]].index[0]
            bed_ID = CABIN_BED_ID[0]

        elif choice == "ICU":
            bed_Type = "ICU BED"
            row_number = DATA_All[DATA_All["BED_ID"] == ICU_BED_ID[0]].index[0]
            bed_ID = ICU_BED_ID[0]

        elif choice == "COVID":
            bed_Type = "COVID BED"
            row_number = DATA_All[DATA_All["BED_ID"]
                                  == COVID_BED_ID[0]].index[0]
            bed_ID = COVID_BED_ID[0]

        if (bed_Type == "GENERAL BED" or bed_Type == "PAYING BED" or
                bed_Type == "CABIN BED" or bed_Type == "ICU BED" or bed_Type == "COVID BED"):
            UpdatingRow(row_number, "OCCUPIED", P_ID)

    # Updates the HOSPITAL BED INFO-------------------------------------------
    def Relese_Patient(ID):
        DATA_All1 = pc.read_csv("HOSPITAL BED INFO.csv")
        DATA_All1.columns = [column.replace(
            " ", "_") for column in DATA_All1.columns]
        DATA_All1.query('PATIENT_ID == @ID', inplace=True)
        PINFO_list = DATA_All1.values.tolist()
        x = list(DATA_All1["PATIENT_ID"])
        v = DATA_All1[DATA_All1["PATIENT_ID"] == x[0]].index[0]
        UpdatingRow(v, "VACANT", "")

    # Choice- Bed type Choice in uppercase.
    def Change_Bed_of_Patient(ID, choice):
        Relese_Patient(ID)  # Clears the currrent bed type and bed ID.
        update_bed_info(choice, ID)  # Updates bed info

        PU = pc.read_csv("PATIENT_INFO.csv")
        PU.columns = [column.replace(" ", "_") for column in PU.columns]
        PU.query('PATIENT_ID == @ID', inplace=True)
        PINFO_list = PU.values.tolist()
        x = list(PU["PATIENT_ID"])
        v = PU[PU["PATIENT_ID"] == x[0]].index[0]

        PINFO1 = pc.read_csv("PATIENT_INFO.csv")
        PINFO1.loc[v, "BED_ID"] = (bed_ID)
        PINFO1.loc[v, "BED_TYPE"] = (choice + " BED")
        # Updates the Patient Info accordingly.
        PINFO1.to_csv("PATIENT_INFO.csv", index=False)

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
        f = ('Times', 14)
        bill_widow = Toplevel()
        bill_widow.title("sub Panel")
        bill_widow.geometry("1320x530+60+180")
        bill_widow.overrideredirect(True)
        Grid.rowconfigure(bill_widow, 0, weight=1)
        Grid.columnconfigure(bill_widow, 0, weight=1)
        bill_widow.lift()
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
            pdf.output(output_path + "/" + save_as_name.get() + '.pdf')

        def save_as():
            save = Toplevel()
            save.geometry("600x150+470+250")
            save.title("save as")
            Label(save, text="Save as:", font="Comic").grid(
                row=0, column=0, padx=(30, 0), pady=(30, 20))
            Entry(save, width=70, textvariable=save_as_name).grid(row=0, column=1, padx=(30, 50),
                                                                  pady=(30, 20))
            Button(save, text="Save", font="Comic", command=lambda: [get_pdf(), save.destroy()])\
                .grid(row=1, column=1, ipadx=10, padx=(30, 50), pady=(0, 20), sticky=E)

        Label(bill_widow, text="BILL RECIEPT", font=f).grid(
            row=5, column=0, ipady=8, pady=(30, 6))
        Button(bill_widow, width=12, image=pdf_img_button, font=f, relief=RIDGE, command=save_as) \
            .grid(row=0, column=0, ipadx=30, padx=68, sticky=W)
        Button(bill_widow, width=12, image=back, relief=RIDGE, command=bill_widow.destroy) \
            .grid(row=0, column=0, ipadx=25, padx=(0, 50), sticky=W)
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
        bill_frame.grid(row=5, padx=50, columnspan=2,
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
            row=0, column=3, sticky=W, pady=10, padx=(200, 0))
        Label(bill_frame, text="Age:", bg='#CCCCCC', font=f).grid(
            row=1, column=3, sticky=W, pady=10, padx=(200, 0))
        Label(bill_frame, text="Date:", bg='#CCCCCC', font=f).grid(
            row=2, column=3, sticky=W, pady=10, padx=(200, 0))
        Label(bill_frame, text="Time:", bg='#CCCCCC', font=f).grid(
            row=3, column=3, sticky=W, pady=10, padx=(200, 0))
        Label(bill_frame, text="Reffered By:", bg='#CCCCCC', font=f).grid(
            row=4, column=3, sticky=W, pady=10, padx=(200, 0))

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

    pdf_img = Image.open(r"Mur PDF.png")
    pdf_img.thumbnail((30, 30))
    pdf_img_button = ImageTk.PhotoImage(pdf_img)

    exit_img = Image.open(r"back.png")
    exit_img.thumbnail((60, 30))
    back = ImageTk.PhotoImage(exit_img)

    lay = []

    joy = []

    def display_table():
        top = Toplevel()
        joy.append(top)
        top.configure(bg='#0B5A81')
        top.geometry('600x350+450+300')  # ('600x350+470+250')
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
                    label.grid(row=r + 1, column=c + 1, sticky=NSEW)
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
        gender_frame = LabelFrame(
            right_frame, bg='#CCCCCC', padx=10, pady=10, )

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
        register_IDinfo = Entry(right_frame, font=f,
                                textvariable=id_info_value)

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

        def exit_btn():
            top.destroy()
            top.update()

        register_btn = Button(right_frame, width=15, text='Submit', font=f, relief=RAISED, cursor='hand2',
                              command=lambda: [getvals(), exit_btn(), bill_prescription(q)])
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
            except:
                pass

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

    background_img = PhotoImage(file=f"background 2.png")
    background = canvas.create_image(
        680.0, 345.0,
        image=background_img)

    def MANAGE_PATIENT(h):
        try:
            line = h[0]
            a = line[8]
            b = a.replace("|", ",")
            line[8] = b
            f = ('Times', 14)
            bill_widow = Toplevel()
            bill_widow.title("sub Panel")
            bill_widow.geometry("1320x530+60+180")
            bill_widow.overrideredirect(True)
            Grid.rowconfigure(bill_widow, 0, weight=1)
            Grid.columnconfigure(bill_widow, 0, weight=1)
            bill_widow.lift()

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
                pdf.cell(200, 10, txt="Phone:+91 (0361) 2456510",
                         ln=3, align="C")
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
                pdf.output(output_path + "/" + save_as_name.get() + '.pdf')

            def save_as():
                save = Toplevel()
                save.geometry("600x150+470+250")
                save.title("save as")
                Label(save, text="Save as:", font="Comic").grid(
                    row=0, column=0, padx=(30, 0), pady=(30, 20))
                Entry(save, width=70, textvariable=save_as_name).grid(row=0, column=1, padx=(30, 50),
                                                                      pady=(30, 20))
                Button(save, text="Save", font="Comic", command=lambda: [get_pdf(), save.destroy()])\
                    .grid(row=1, column=1, ipadx=10, padx=(30, 50), pady=(0, 20), sticky=E)
        # VR2595
            Label(bill_widow, text="BILL RECIEPT", font=f).grid(
                row=5, column=0, ipady=8, pady=(30, 6))
            Button(bill_widow, width=12, image=pdf_img_button, font=f, relief=RIDGE, command=save_as) \
                .grid(row=0, column=0, ipadx=30, padx=323, sticky=W)
            Button(bill_widow, width=12, image=back, relief=RIDGE, command=bill_widow.destroy) \
                .grid(row=0, column=0, ipadx=25, padx=(0, 50), sticky=W)

            def released():
                pop = Toplevel()
                pop.geometry("250x170+500+250")
                pop.overrideredirect(True)
                pop.title("pop up")
                notification = Frame(
                    pop, bd=2, relief="raised", padx=10, bg="#FF6B00")
                notification.grid(row=0, padx=0)
                Label(notification, text="Patient Released\nSuccesfully", font="Comic", bg="#FF6B00")\
                    .grid(row=0, column=0, pady=(30, 10), padx=(35, 0))
                Button(notification, text="OK", font="Comic", command=lambda: [pop.destroy(), bill_widow.destroy()])\
                    .grid(row=1, column=1, sticky="es", pady=40, ipadx=18)

            def bed_changed():
                pop = Toplevel()
                pop.geometry("250x170+500+250")
                pop.overrideredirect(True)
                pop.title("pop up")
                notification = Frame(
                    pop, bd=2, relief="raised", padx=10, bg="#FF6B00")
                notification.grid(row=0, padx=0)
                Label(notification, text="Bed changed\nSuccesfully", font="Comic", bg="#FF6B00")\
                    .grid(row=0, column=0, pady=(30, 10), padx=(35, 0))
                Button(notification, text="OK", font="Comic", command=lambda: [pop.destroy(), bill_widow.destroy()])\
                    .grid(row=1, column=1, sticky="es", pady=40, ipadx=18)

            def update_bed():
                bed = Toplevel()
                width = 300
                height = 100
                screen_width = bed.winfo_screenwidth()
                screen_height = bed.winfo_screenheight()
                x = (screen_width / 2) - (width / 2)
                y = (screen_height / 2) - (height / 2)
                bed.geometry("%dx%d+%d+%d" % (width, height, x, y))
                bed.resizable(0, 0)
                countries = []
                variable = StringVar()
                world = open("MANAGE BED.txt", 'r')
                for country in world:
                    country = country.rstrip('\n')
                    countries.append(country)
                variable.set(countries[4])
                Label(bed, text="Change the bed type to:", font="Comic").grid(
                    row=0, column=0, padx=(70, 0))
                register_bedtype = OptionMenu(bed, variable, *countries)
                register_bedtype.grid(row=1, column=0, padx=(45, 0))
                Button(bed, text="Update Patient", font="Comic", command=lambda: [Change_Bed_of_Patient(
                    line[0], variable.get()), bed.destroy(), bed_changed()]).grid(row=2, column=0, padx=(45, 0))

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
            bill_frame.grid(row=5, padx=50, columnspan=2,
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
                row=0, column=3, sticky=W, pady=10, padx=(200, 0))
            Label(bill_frame, text="Age:", bg='#CCCCCC', font=f).grid(
                row=1, column=3, sticky=W, pady=10, padx=(200, 0))
            Label(bill_frame, text="Date:", bg='#CCCCCC', font=f).grid(
                row=2, column=3, sticky=W, pady=10, padx=(200, 0))
            Label(bill_frame, text="Time:", bg='#CCCCCC', font=f).grid(
                row=3, column=3, sticky=W, pady=10, padx=(200, 0))
            Label(bill_frame, text="Reffered By:", bg='#CCCCCC', font=f).grid(
                row=4, column=3, sticky=W, pady=10, padx=(200, 0))

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

            # Conditions
            bedcsv = pc.read_csv("HOSPITAL BED INFO.csv")
            x = list((bedcsv["PATIENT_ID"]))
            bedtype = line[2]
            if (line[0] not in x and bedtype == "OPD"):  # For bed type OPD
                emp_ty = Label(bill_widow, text="             ", fg="#FF0000",
                               font="Calibri 15")
                emp_ty.grid(row=6, padx=50, columnspan=2, sticky="new")
            elif (line[0] not in x):  # For already released patients
                has_been_released = Label(bill_widow, text="----------This Patient has already been released----------", fg="#FF0000",
                                          font="Calibri 15")
                has_been_released.grid(
                    row=6, padx=50, columnspan=2, sticky="new")
            else:  # For Patients curently in hospital
                Button(bill_widow, width=12, text="Release Patient", font="Comic", relief=RIDGE, command=lambda: [released(), Relese_Patient(line[0])]) \
                    .grid(row=0, column=0, ipadx=5, ipady=2, padx=68, sticky=W)
                Button(bill_widow, width=12, text="Update Bed", font="Comic", relief=RIDGE, command=lambda: [update_bed()]) \
                    .grid(row=0, column=0, ipadx=5, ipady=2, padx=195, sticky=W)
        except:
            pop = Toplevel()
            pop.geometry("320x170+500+250")
            pop.overrideredirect(True)
            pop.title("pop up")
            notification = Frame(
                pop, bd=2, relief="raised", padx=10, bg="#FF6B00")
            notification.grid(row=0, padx=0)
            Label(notification, text="No Patient with Patient ID:\n"+TIG, font="Comic", bg="#FF6B00")\
                .grid(row=0, column=0, pady=(30, 10), padx=(35, 0))
            Button(notification, text="OK", font="Comic", command=lambda: [pop.destroy()])\
                .grid(row=1, column=1, sticky="es", pady=40, ipadx=18)

    img0 = PhotoImage(file=f"search.png")
    b0 = Button(image=img0, borderwidth=0, highlightthickness=0,
                command=lambda: [my_patient_id(), MANAGE_PATIENT(PINFO_list)], relief="flat")
    b0.place(x=568, y=85, width=94, height=31)

    get_ID = Entry(bd=0, bg="#FFFFFF", highlightthickness=0, font="rose")
    get_ID.place(x=327, y=80, width=236, height=41)
    get_ID.insert(0, "Enter Your Id")

    img1 = PhotoImage(file=f"check beds.png")
    b1 = Button(image=img1, borderwidth=0, highlightthickness=0,
                command=display_table, relief="flat")
    b1.place(x=710, y=84, width=322, height=31)

    img3 = PhotoImage(file=f"bood_bed.png")
    b3 = Button(image=img3, borderwidth=0, highlightthickness=0,
                command=createform, relief="flat", bg="#6F6B6B")
    b3.place(x=1115, y=15, width=65, height=45)

    def bedinfo():
        root = Tk()
        root.title("BED INFO")
        width = 400
        height = 400
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        root.geometry("%dx%d+%d+%d" % (width, height, x, y))
        root.resizable(0, 0)

        TableMargin = Frame(root, width=500)
        TableMargin.pack(side=TOP)
        scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
        scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
        tree = ttk.Treeview(TableMargin, columns=("BED ID", "BED TYPE", "BED STATUS", "PATIENT ID"),
                            height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        scrollbary.config(command=tree.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=tree.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)
        tree.heading('BED ID', text="BED ID", anchor=W)
        tree.heading('BED TYPE', text="BED TYPE", anchor=W)
        tree.heading('BED STATUS', text="BED STATUS", anchor=W)
        tree.heading('PATIENT ID', text="PATIENT ID", anchor=W)
        tree.column('#0', stretch=NO, minwidth=0, width=0)
        tree.column('#1', stretch=NO, minwidth=0, width=100)
        tree.column('#2', stretch=NO, minwidth=0, width=100)
        tree.column('#3', stretch=NO, minwidth=0, width=100)
        tree.column('#4', stretch=NO, minwidth=0, width=100)
        tree.pack()

        x = []
        with open('HOSPITAL BED INFO.csv', 'r') as cs:
            csv_reader = csv.reader(cs)
            for line in csv_reader:
                x.append(line)
        cs.close()
        x.pop(0)
        for i in x[::-1]:
            tree.insert("", 0, values=(i[0], i[1], i[2], i[3]))

    def patient_info():
        root = Tk()
        root.title("PATIENT INFO")
        width = 1000
        height = 400
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        root.geometry("%dx%d+%d+%d" % (width, height, x, y))
        root.resizable(0, 0)

        TableMargin = Frame(root, width=500)
        TableMargin.pack(side=TOP)
        scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
        scrollbary = Scrollbar(TableMargin, orient=VERTICAL)

        # ---------------------------------------------------------------------------------------------------------
        tree = ttk.Treeview(TableMargin,
                            columns=("SL.NO", "PATIENT ID", "BED ID", "BED TYPE", "Reffered by", "NAME OF PATIENT",
                                     "AGE", "GENDER", "CONTACT No", "ADDRESS", "ID TYPE", "ID NUMBER", "TIME", "DATE"),
                            height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        # ---------------------------------------------------------------------------------------------------------
        scrollbary.config(command=tree.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=tree.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)
        tree.heading("SL.NO", text="SL.NO", anchor=W)
        tree.heading("PATIENT ID", text="PATIENT ID", anchor=W)
        tree.heading("BED ID", text="BED ID", anchor=W)
        tree.heading("BED TYPE", text="BED TYPE", anchor=W)
        tree.heading("Reffered by", text="Reffered by", anchor=W)
        tree.heading("NAME OF PATIENT", text="NAME OF PATIENT", anchor=W)
        tree.heading("AGE", text="AGE", anchor=W)
        tree.heading("GENDER", text="GENDER", anchor=W)
        tree.heading("CONTACT No", text="CONTACT No", anchor=W)
        tree.heading("ADDRESS", text="ADDRESS", anchor=W)
        tree.heading("ID TYPE", text="ID TYPE", anchor=W)
        tree.heading("ID NUMBER", text="ID NUMBER", anchor=W)
        tree.heading("TIME", text="TIME", anchor=W)
        tree.heading("DATE", text="DATE", anchor=W)
        tree.column('#0', stretch=NO, minwidth=0, width=0)
        tree.column('#1', stretch=NO, minwidth=0, width=20)
        tree.column('#2', stretch=NO, minwidth=0, width=70)
        tree.column('#3', stretch=NO, minwidth=0, width=50)
        tree.column('#4', stretch=NO, minwidth=0, width=100)
        tree.column('#5', stretch=NO, minwidth=0, width=100)
        tree.column('#6', stretch=NO, minwidth=0, width=180)
        tree.column('#7', stretch=NO, minwidth=0, width=50)
        tree.column('#8', stretch=NO, minwidth=0, width=100)
        tree.column('#9', stretch=NO, minwidth=0, width=100)
        tree.column('#10', stretch=NO, minwidth=0, width=350)
        tree.column('#11', stretch=NO, minwidth=0, width=100)
        tree.column('#12', stretch=NO, minwidth=0, width=120)
        tree.column('#13', stretch=NO, minwidth=0, width=100)
        tree.column('#14', stretch=NO, minwidth=0, width=100)
        tree.pack()

        x = []
        with open('PATIENT_INFO.csv', 'r') as cs:
            csv_reader = csv.reader(cs)
            for line in csv_reader:
                a = line[8]
                b = a.replace("|", ",")
                line[8] = b
                x.append(line)
        x.pop(0)
        a = len(x)
        for i in x[::-1]:
            tree.insert("", 0, values=(
                a, i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12]))
            a = a - 1

    def enq_display():
        display = Toplevel()
        display.geometry("300x70+1010+95")
        display.overrideredirect(True)
        Label(display, text="Want to display:", font="Calibri").grid(
            row=0, column=0, padx=(70, 0))
        Button(display, text="Bed Info", font="Calibri", command=lambda: [
               bedinfo(), display.destroy()]).grid(row=1, column=0, sticky=E, ipadx=20)
        Button(display, text="Patient Info", font="Calibri", command=lambda: [
               patient_info(), display.destroy()]).grid(row=1, column=1, sticky=W, ipadx=10)

    logged_name = v
    loged = Label(text=logged_name, font="rose 11", bg="#c4c4c4")
    loged.place(x=192, y=23, width=120, height=22)

    pdf_img = Image.open(r"patient details.png")
    pdf_img.thumbnail((43, 43))
    img4 = ImageTk.PhotoImage(pdf_img)
    b4 = Button(image=img4, borderwidth=0, highlightthickness=0,
                command=enq_display, relief="flat", bg="#6F6B6B")
    b4.place(x=1231, y=17, width=48, height=43)

    window.mainloop()
