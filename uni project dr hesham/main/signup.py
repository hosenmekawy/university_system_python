from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import font
import csv
import pandas as pd
import numpy as np
import mysql.connector


class sign_up:
    def __init__(self, root):
        # ---------- design of the page --------------------
        self.root = root
        self.root.geometry('1920x1080')
        self.root.title('project university')
        self.root.iconbitmap("logo\Wardiere-removebg-preview.ico")
        self.root.configure(background="#FFCCCC")  # pink
        self.root.resizable(True, True)
        pinky = '#FFCCCC'
        whitey = '#F7F7F2'

        # frame logo
        login_form = Frame(self.root, bg="#F7F7F2")
        login_form.place(x=640, y=0, width=1286, height=1080)

        img = ImageTk.PhotoImage(Image.open("main\logo.png"))
        label = Label(self.root, image=img, bg="#FFCCCC")
        label.image = img
        label.place(x=60, y=10)
# text under the logo
        text_logo = Label(self.root, text='Project University',
                          font=("Gill Sans MT", 22))
        text_logo.config(fg="#13325B", bg="#FFCCCC")
        text_logo.place(x=205, y=420)
# text explain

        Exp_logo = Label(
            self.root, text="Project university is \n a smart university application \n to mange student needs")
        Exp_logo.place(x=205, y=480)
        Exp_logo.config(fg="#13325B", bg=pinky, justify="left")
# the version number
        version = Label(self.root, text="Version 1.0")
        version.config(bg=pinky)
        version.place(relx=0.05, rely=0.9, anchor='s')

        self.page = Frame(self.root, width=1286, height=1080, bg=whitey)
        self.page.place(x=640, y=0)
        # -------------- variables --------------------------------
        self.fc = StringVar()
        self.level = StringVar()
        self.pass2 = StringVar()
        self.pass1 = StringVar()
        self.no = StringVar()
        self.email = StringVar()
        self.id = StringVar()
        self.name = StringVar()
        # create an account badge
        acc_badge = Label(self.page, text="have an account ?")
        acc_badge.config(bg=whitey, fg='grey')
        acc_badge.place(x=630, y=25)

        btn_sign_in_bk = Button(
            self.page, text='SIGN IN', command=self.sign_in)
        btn_sign_in_bk.config(bg=whitey, bd=1, width=18)
        btn_sign_in_bk.place(x=740, y=25)
        # text sign up
        login_text = Label(self.page, text=' Sign Up into Project University ', font=(
            'Gill Sans MT', 22, "bold"), bg=whitey)
        login_text.place(x=80, y=200)
        highlight_txt = Label(self.page, text='Enter your details below . ', font=(
            'small fonts', 10), bg=whitey, fg='grey')
        highlight_txt.place(x=90, y=250)
        # -----------------------------NAME-----------------
        user_name = Entry(self.page, width=25, fg='black', bg=whitey,
                          border=0, cursor='hand2', font=('Microsoft YaHei UI Light', 11), textvariable=self.name)
        user_name.place(x=90, y=300)
        user_name.insert(0, 'Name')
        Frame(self.page, width=295, height=2, bg='black',).place(x=90, y=322)

        # --------------ID----------------------
        user_id = Entry(self.page, width=25, fg='black', bg=whitey,
                        border=0, cursor='hand2', font=('Microsoft YaHei UI Light', 11), textvariable=self.id)
        user_id.place(x=90, y=350)
        user_id.insert(0, 'ID')
        Frame(self.page, width=295, height=2, bg='black',).place(x=90, y=377)

        # -----------------Email ----------------

        user_email = Entry(self.page, width=25, fg='black', bg=whitey,
                           border=0, cursor='hand2', font=('Microsoft YaHei UI Light', 11), textvariable=self.email)
        user_email.place(x=90, y=400)
        user_email.insert(0, 'Email Address')
        Frame(self.page, width=295, height=2, bg='black',).place(x=90, y=422)

        # ---------------------phone------------------------

        user_no = Entry(self.page, width=25, fg='black', bg=whitey,
                        border=0, cursor='hand2', font=('Microsoft YaHei UI Light', 11), textvariable=self.no)
        user_no.place(x=90, y=450)
        user_no.insert(0, 'phone number')
        Frame(self.page, width=295, height=2, bg='black',).place(x=90, y=477)

        # --------------------PASSWORD-----------------------

        user_pass1 = Entry(self.page, width=25, fg='black', bg=whitey,
                           border=0, cursor='hand2', font=('Microsoft YaHei UI Light', 11), textvariable=self.pass1)
        user_pass1.place(x=90, y=500)
        user_pass1.insert(0, 'Password')
        Frame(self.page, width=295, height=2, bg='black',).place(x=90, y=522)

        # --------------------confirm pass ---------------------

        user_pass2 = Entry(self.page, width=25, fg='black', bg=whitey,
                           border=0, cursor='hand2', font=('Microsoft YaHei UI Light', 11), textvariable=self.pass2)
        user_pass2.place(x=90, y=550)
        user_pass2.insert(0, 'confirm password ')
        Frame(self.page, width=295, height=2, bg='black',).place(x=90, y=577)

        # -------------------- LEVEL --------------------

        user_level = Entry(self.page, width=25, fg='black', bg=whitey,
                           border=0, cursor='hand2', font=('Microsoft YaHei UI Light', 11), textvariable=self.level)
        user_level.place(x=90, y=600)
        user_level.insert(0, 'LEVEL')
        Frame(self.page, width=295, height=2, bg='black',).place(x=90, y=622)

        # -------------------- Faculty --------------------------------

        user_fc = Entry(self.page, width=25, fg='black', bg=whitey,
                        border=0, cursor='hand2', font=('Microsoft YaHei UI Light', 11), textvariable=self.fc)
        user_fc.place(x=90, y=650)
        user_fc.insert(0, 'Faculty')
        Frame(self.page, width=295, height=2, bg='black',).place(x=90, y=677)

        # --------------- btn sign-up --------------------

        btn_sign_up = Button(self.page, width=20, pady=7,
                             text=' sign up ', bg='black', fg=whitey, border=0, command=self.register)
        btn_sign_up.place(x=90, y=720)

        Label(self.page, text="Copyright \xa9 2023 - Mekawy. INC",
              bg=whitey).place(x=695, y=735)

        self.connection = mysql.connector.connect(

            host='localhost',
            user='root',
            port='3306',
            password='',
            database='py_dp_st'

        )

        self.c = self.connection.cursor()
    # def connect_mysqlDB(self):
    #     self.connection = mysql.connector.connect(

    #         host = 'localhost',
    #         user = 'root',
    #         port = '3306',
    #         password = '',
    #         database = 'py_dp_st'

    #                                         )

    #     self.c = self.connection.cursor()

    def sign_in(self):
        root.destroy()
        import main

    def no_exisist(self, phone):
        phone = self.no.get().strip()

        vals = (phone, )
        select_query = "SELECT * FROM `studeny_info` WHERE `PHONE` =%s"
        self.c.execute(select_query, vals)
        user = self.c.fetchone()
        if user is not None:
            return True
        else:
            return False

    def register(self):

        # self.id = self.id.get()
        id = self.id.get().strip()  # .strip() mean : remove space from text
        Name = self.name.get().strip()
        phone = self.no.get().strip()
        Email = self.email.get().strip()
        Pass1 = self.pass1.get().strip()
        pass2 = self.pass2.get().strip()
        Level = self.level.get().strip()
        Faculty = self.fc.get().strip()

        if len(id) > 0 and len(Name) > 0 and len(phone) > 0 and len(Email) > 0 and len(Pass1) > 0 and len(Level) > 0 and len(Faculty) > 0:
            if self.no_exisist(phone) == False:
                if Pass1 == pass2:
                    vals = (id, Name, phone, Email, Pass1, Level, Faculty)
                    insert_query = "INSERT INTO `studeny_info`(`id`,`NAME`, `PHONE`, `EMAIL`, `PASSWORD`, `LEVEL`, `FACULTY`) VALUES (%s,%s,%s,%s,%s,%s,%s)"
                    self.c.execute(insert_query, vals)
                    self.connection.commit()
                    messagebox.showinfo(
                        'register', 'your account has been registered successfully ' + ' mr/ms : ' + Name)
                    root.destroy()
                    import main
                else:
                    messagebox.showerror(
                        'password', 'your password is not same')
            else:
                messagebox.showwarning(
                    'phone', 'phone number already exist try another')
        else:
            messagebox.showerror(
                'register', 'your account has not been registered  ')


pinky = '#FFCCCC'
whitey = '#F7F7F2'
root = Tk()
oop = sign_up(root)
root.mainloop()
