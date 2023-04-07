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
import time
# import sys

# def on_enter(self,event):
#     self.id_var.delete(0,'end')
# def on_leave(self,event):
#     if self.id_var.get() == '' :
#         self.id_var.insert(0,'Your ID')
# sys.setrecursionlimit(10000)


class login:

    # -------------degisn the page ----------
    def __init__(self, root):
        self.root = root
        self.root.geometry('1920x1080')
        self.root.title('project university')
        self.root.iconbitmap("logo\Wardiere-removebg-preview.ico")
        self.root.configure(background="#FFCCCC")  # pink
        self.root.resizable(True, True)
        pinky = '#FFCCCC'
        whitey = '#F7F7F2'

        # ---------------- variabels ---------------------------------

        self.id_var = StringVar()
        self.pass_var = StringVar()

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
# ---------------- began of the page ----------------
        # create an account badge
        acc_badge = Label(login_form, text="Don't have an account ?")
        acc_badge.config(bg=whitey, fg='grey')
        acc_badge.place(x=590, y=25)

        btn_create_acc = Button(
            login_form, text='CREATE ACCOUNT', command=self.sign_up)
        btn_create_acc.config(bg=whitey, bd=1, width=18)
        btn_create_acc.place(x=740, y=25)
#  ----------------------login-----------------------------------
        login_text = Label(login_form, text=' Log Into Project University ', font=(
            'Gill Sans MT', 22, "bold"), bg=whitey)
        login_text.place(x=80, y=200)

        highlight_txt = Label(login_form, text='Enter your login details below . ', font=(
            'small fonts', 10), bg=whitey, fg='grey')
        highlight_txt.place(x=90, y=250)
        # ------------------------------------ username ------------------------------------------
        user = Entry(login_form, width=25, fg='black', bg=whitey,
                     border=0, cursor='hand2', font=('Microsoft YaHei UI Light', 11), textvariable=self.id_var)
        user.place(x=90, y=350)
        user.insert(0, 'YOUR ID')
        # user.bind('<FocusIn>', on_enter)
        # user.bind('<FocusOut>', on_leave)

        Frame(login_form, width=295, height=2, bg='black',).place(x=90, y=377)
        # ----------------------------------------passowrd------------------------------------------
        password = Entry(login_form, width=25, fg='black', bg=whitey,
                         border=0, font=('Microsoft YaHei UI Light', 11), textvariable=self.pass_var, show='*')
        password.place(x=90, y=440)
        password.insert(0, 'Password')

        Frame(login_form, width=295, height=2, bg='black').place(x=90, y=467)

        # ------------------ forget password --------------------------------------
        frgt_psrd = Button(login_form, width=25, text='forget your password ?', border=0, font=(
            'Elephant', 9, 'underline'), fg='black', bg=whitey)
        frgt_psrd.place(x=390, y=450)

        # ------------------------------------- sign in btn --------------------------------
        btn_sign_in = Button(login_form, width=20, pady=7,
                             text=' sign in ', bg='black', fg=whitey, border=0, command=self.sign_in_logic)
        btn_sign_in.place(x=90, y=530)
        # ------------------------------------- copyright ----------------------------------------------------------------

        self.connection = mysql.connector.connect(

            host='localhost',
            user='root',
            port='3306',
            password='',
            database='py_dp_st',


        )

        self.c = self.connection.cursor()

    def sign_in_logic(self):
        usern = self.id_var.get().strip()
        password = self.pass_var.get().strip()

        vals = (usern, password)
        select_query = "SELECT * FROM `studeny_info` WHERE `id` =%s AND `PASSWORD` = + %s"
        self.c.execute(select_query, vals)
        user = self.c.fetchone()

        if user is not None:
            self.login_user(usern, password)
            messagebox.showinfo('project', 'welcome')
            root.destroy()
            import mainuni
        else:
            messagebox.showerror('error', 'Wrong Username or Password')

    def login_user(self, usern, password):
        vals = (usern, password)
        select_query = "SELECT * FROM `studeny_info` WHERE `id` = %s AND `PASSWORD` =  %s"
        self.c.execute(select_query, vals)
        result = self.c.fetchone()
        # insert row into second table
        insert_query = "INSERT INTO `copy_single_student_user` (`id`,`NAME`, `PHONE`, `EMAIL`, `PASSWORD`, `LEVEL`, `FACULTY`,`Time`) VALUES (%s, %s, %s,%s,%s,%s,%s,%s)"
        insert_values = (result[0], result[1], result[2], result[3], result[4],
                         result[5], result[6], time.strftime('%Y-%m-%d %H:%M:%S'))
        self.c.execute(insert_query, insert_values)
        self.connection.commit()

    def sign_up(self):
        root.destroy()
        import signup

    # def login (self):
    #     id = self.id_var.get()
    #     password = self.pass_var.get()
    #     root.destroy()
    #     import mainuni


pinky = '#FFCCCC'
whitey = '#F7F7F2'
root = Tk()
page = 0
oop = login(root)
root.mainloop()
