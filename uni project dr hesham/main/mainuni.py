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


class student_main():
    def __init__(self, root):
        self.root = root
        self.root.geometry('1920x1080')
        self.root.title('project university')
        self.root.iconbitmap("logo\Wardiere-removebg-preview.ico")
        self.root.configure(background='white')
        self.root.resizable(True, True)

        # ------------- variables --------------------------------

        # -----------------  frame left --------------------------------

        left_frame = Frame(self.root, bg=whitey, )
        left_frame.place(x=1, y=1, width=350, height=1080)
        # ---------------------frame A------------
        left_frame_A = Frame(left_frame, bg='white',
                             width=350, height=200).place(x=1, y=1)
        # ----------- logo pic --------------------------------
        logo_pic_main = Image.open("main\logo.png")
        resized = logo_pic_main.resize((300, 195))
        logo_pic_mainB = ImageTk.PhotoImage(resized)
        logo_pic_main_A = Label(left_frame_A, image=logo_pic_mainB, bg='white')
        logo_pic_main_A.image = logo_pic_mainB
        logo_pic_main_A.place(x=15, y=1)
        # ----------- end of logo pic --------------------------------

        left_frame_B = Frame(left_frame, bg='white',
                             width=350, height=300).place(x=1, y=206)
        left_frame_c = Frame(left_frame, bg='white',
                             width=350, height=267).place(x=1, y=512)
        # ------------------line cut straight -----------
        line_frame_between = Frame(
            self.root, bg=whitey, width=6, height=1080).place(x=348, y=1)

        top_frame = Frame(self.root, bg='#13325B')
        top_frame.place(x=355, y=1, width=1536, height=200)

        main_logo_text = Button(top_frame, text='PROJECT', font=(
            'Leelawadee', 40), bd=0, bg='#13325B', fg='#9F7944', command=self.main_page).place(x=475, y=40)
        under_main = Label(top_frame, text='university for science', font=(
            'Leelawadee', 10), fg='white', bg='#13325B').place(x=515, y=130)
        # ----------- illustrations --------
        # -------------------Assignments --------------------------------

        Assmnt = Image.open('illustrations\kassignments.png').resize((38, 38))
        Assmnt_resized = ImageTk.PhotoImage(Assmnt)
        Assignment = Label(self.root, image=Assmnt_resized, bg='white')
        Assignment.image = Assmnt_resized
        Assignment.place(x=80, y=417)

        # ---------------------Materials-----------------------------------

        Assmnt = Image.open('illustrations\material.png').resize((38, 38))
        Assmnt_resized = ImageTk.PhotoImage(Assmnt)
        Assignment = Label(self.root, image=Assmnt_resized, bg='white')
        Assignment.image = Assmnt_resized
        Assignment.place(x=80, y=357)

        # ---------------------Quizzes--------------------------------------

        Assmnt = Image.open('illustrations\#919191.png').resize((38, 38))
        Assmnt_resized = ImageTk.PhotoImage(Assmnt)
        Assignment = Label(self.root, image=Assmnt_resized, bg='white')
        Assignment.image = Assmnt_resized
        Assignment.place(x=80, y=297)

        # ---------------------student--------------------------------

        Assmnt = Image.open('illustrations\student.png').resize((38, 38))
        Assmnt_resized = ImageTk.PhotoImage(Assmnt)
        Assignment = Label(self.root, image=Assmnt_resized, bg='white')
        Assignment.image = Assmnt_resized
        Assignment.place(x=80, y=237)

        # ---------------------Fancial--------------------------------

        Assmnt = Image.open('illustrations\money.png').resize((38, 38))
        Assmnt_resized = ImageTk.PhotoImage(Assmnt)
        Assignment = Label(self.root, image=Assmnt_resized, bg='white')
        Assignment.image = Assmnt_resized
        Assignment.place(x=80, y=527)

        # ---------------------Parking-----------------------------------

        Assmnt = Image.open('illustrations\parking.png').resize((38, 38))
        Assmnt_resized = ImageTk.PhotoImage(Assmnt)
        Assignment = Label(self.root, image=Assmnt_resized, bg='white')
        Assignment.image = Assmnt_resized
        Assignment.place(x=80, y=587)

        # -------------------------Market-----------------------------------

        Assmnt = Image.open('illustrations\market.png').resize((38, 38))
        Assmnt_resized = ImageTk.PhotoImage(Assmnt)
        Assignment = Label(self.root, image=Assmnt_resized, bg='white')
        Assignment.image = Assmnt_resized
        Assignment.place(x=80, y=647)

        #  -------------------------survey-----------------------------------

        Assmnt = Image.open('illustrations\survey.png').resize((38, 38))
        Assmnt_resized = ImageTk.PhotoImage(Assmnt)
        Assignment = Label(self.root, image=Assmnt_resized, bg='white')
        Assignment.image = Assmnt_resized
        Assignment.place(x=80, y=707)

        # --------------------end of illustrations -------------------------------


# Buttons in ------------------frame B---------------------

        self.A = Button(left_frame_B, text='STUDENT', bd=0, font=('Dubai Light', 15),
                        bg='white', width=11, fg='#919191', command=self.student).place(x=130, y=230)
        b = Button(left_frame_B, text='QUIZZES', bd=0, font=('Dubai Light', 15),
                   bg='white', width=11, fg='#919191', command=self.quiz).place(x=130, y=290)
        c = Button(left_frame_B, text='MATERIALS', bd=0, font=('Dubai Light', 15),
                   bg='white', width=11, fg='#919191', command=self.materials).place(x=130, y=350)
        d = Button(left_frame_B, text='ASSIGNMENTS', bd=0, font=('Dubai Light', 15),
                   bg='white', width=13, fg='#919191', command=self.Assignments).place(x=130, y=410)

#  Buttons in ----------------frame c ---------------------
        E = Button(left_frame_c, text='FINANCIAL', bd=0, font=(
            'Dubai Light', 15), bg='white', width=11, fg='#919191').place(x=130, y=520)
        F = Button(left_frame_c, text='PARKING', bd=0, font=(
            'Dubai Light', 15), bg='white', width=11, fg='#919191').place(x=130, y=580)
        G = Button(left_frame_c, text='MARKET', bd=0, font=(
            'Dubai Light', 15), bg='white', width=11, fg='#919191').place(x=130, y=640)
        H = Button(left_frame_c, text='SURVEY', bd=0, font=(
            'Dubai Light', 15), bg='white', width=11, fg='#919191').place(x=130, y=700)


# ------------------------ main page-----------------------

        main_page = Frame(self.root, width=1536, height=880,
                          bg='black',).place(x=355, y=202)
        photo_img_main = Image.open(
            'photos\parker-gibbons-kfwPJieZVwI-unsplash.jpg').resize((1300, 700))
        photo_img_main_resized = ImageTk.PhotoImage(photo_img_main)
        photo_img_mainA = Label(
            main_page, image=photo_img_main_resized, bg='white')
        photo_img_mainA.image = photo_img_main_resized
        photo_img_mainA.place(x=355, y=202)

        # -------------- connect to database --------------

        self.connection = mysql.connector.connect(

            host='localhost',
            user='root',
            port='3306',
            password='',
            database='py_dp_st',


        )

        self.c = self.connection.cursor()

        # -----------------------------------------------------

    def main_page(self):
        main_page = Frame(self.root, width=1536, height=880,
                          bg='black',).place(x=355, y=202)
        photo_img_main = Image.open(
            'photos\parker-gibbons-kfwPJieZVwI-unsplash.jpg').resize((1300, 700))
        photo_img_main_resized = ImageTk.PhotoImage(photo_img_main)
        photo_img_mainA = Label(
            main_page, image=photo_img_main_resized, bg='white')
        photo_img_mainA.image = photo_img_main_resized
        photo_img_mainA.place(x=355, y=202)

    def get_last_student_user_info(self):
        # Get a new cursor object
        self.c = self.connection.cursor()

        # Execute SELECT query to retrieve last row from table
        self.c.execute(
            "SELECT * FROM copy_single_student_user ORDER BY Time DESC LIMIT 1")

        # Fetch the result set
        result = self.c.fetchone()

        # Convert the result into a list and store it in student_user_info
        self.student_user_info = list(result)

        return self.student_user_info

    def student(self):

        student_user_info = self.get_last_student_user_info()
        nme = student_user_info[1]
        lvl = student_user_info[5]
        ids = student_user_info[0]
        print(nme, lvl, ids)

        main_pages = Frame(self.root, width=1536, height=880,
                           bg=whitey,).place(x=355, y=202)
        # --------------------student info -----------------------------------
        student_info_frame = Frame(
            main_pages, width=1130, height=250, bg='white').place(x=365, y=212)
        info_label_frame = Frame(
            student_info_frame, width=850, height=230, bg=whitey).place(x=617, y=222)
        Name_label = Label(info_label_frame, text='NAME : ' + nme, font=(' Microsoft Sans Serif', 30),
                           bg=whitey).place(x=630, y=230)

        level_label = Label(info_label_frame, text='LEVEL : ' + lvl, font=(' Microsoft Sans Serif', 30),
                            bg=whitey).place(x=630, y=280)

        id_label = Label(info_label_frame, text='ID : ' + ids, font=(' Microsoft Sans Serif', 30),
                         bg=whitey).place(x=630, y=330)

        status_label = Label(info_label_frame, text='STATUS : ' + 'passed', font=(' Microsoft Sans Serif', 30),
                             bg=whitey).place(x=630, y=380)
        student_image = Frame(main_pages, width=200,
                              height=200, bg=whitey).place(x=375, y=222)
        # aaaa

        photo_img_main = Image.open(
            'main\logo.png').resize((200, 200))
        photo_img_main_resized = ImageTk.PhotoImage(photo_img_main)
        photo_img_mainA = Label(
            main_pages, image=photo_img_main_resized, bg='white')
        photo_img_mainA.image = photo_img_main_resized
        photo_img_mainA.place(x=375, y=222)

        # eeee
        Label(main_pages, text='2023', bg='white').place(x=460, y=430)
        # table of timetable
        Table_frame = Frame(main_pages, width=560, height=300,
                            bg='white').place(x=365, y=472)

        Table_text = Label(Table_frame, text='your classes table', bg='white', font=(
            'Microsoft Sans Serif', 20)).place(x=515, y=482)

        # aa

        photo_img_main = Image.open(
            'photos\images.png').resize((180, 180))
        photo_img_main_resized = ImageTk.PhotoImage(photo_img_main)
        photo_img_mainA = Label(
            main_pages, image=photo_img_main_resized, bg='white')
        photo_img_mainA.image = photo_img_main_resized
        photo_img_mainA.place(x=375, y=522)

        photo_img_main = Image.open(
            'photos\images.png').resize((329, 180))
        photo_img_main_resized = ImageTk.PhotoImage(photo_img_main)
        photo_img_mainA = Label(
            main_pages, image=photo_img_main_resized, bg='white')
        photo_img_mainA.image = photo_img_main_resized
        photo_img_mainA.place(x=590, y=522)

        # ee
        btn_table_download = Button(Table_frame, text='DOWNLOAD', bg='#13325B', fg='#9F7944', font=(
            'Microsoft Sans Serif', 20)).place(x=375, y=700)
        btn_table_show = Button(Table_frame, text='SHOW TABLE', bg='#13325B', fg='White', font=(
            'Microsoft Sans Serif', 20), width=20).place(x=590, y=700)

        # end of time table

        GPA_frame = Frame(main_pages, width=560, height=300,
                          bg='white').place(x=935, y=472)

        photo_img_main = Image.open(
            'photos\images (1).png').resize((560, 300))
        photo_img_main_resized = ImageTk.PhotoImage(photo_img_main)
        photo_img_mainA = Label(
            main_pages, image=photo_img_main_resized, bg='white')
        photo_img_mainA.image = photo_img_main_resized
        photo_img_mainA.place(x=935, y=472)

    def quiz(self):
        main_pages = Frame(self.root, width=1536, height=880,
                           bg='pink',).place(x=355, y=202)

    def money(self):
        main_pages = Frame(self.root, width=1536, height=880,
                           bg='red',).place(x=355, y=202)

    def Assignments(self):
        main_pages = Frame(self.root, width=1536, height=880,
                           bg='red',).place(x=355, y=202)

    def materials(self):
        main_pages = Frame(self.root, width=1536, height=880,
                           bg='grey',).place(x=355, y=202)

    def survey(self):
        main_pages = Frame(self.root, width=1536, height=880,
                           bg='grey',).place(x=355, y=202)

    def parking(self):
        main_pages = Frame(self.root, width=1536, height=880,
                           bg='white',).place(x=355, y=202)

    def market(self):
        main_pages = Frame(self.root, width=1536, height=880,
                           bg='white',).place(x=355, y=202)


whitey = '#F7F7F2'
root = Tk()
# create an instance of student_main with the root window as argument
page = 0
oop = student_main(root)
root.mainloop()
