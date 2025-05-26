import os
import tkinter
import pyautogui
from symtable import Class
from tkinter import *
import sys
import random
import pathlib
import shutil
from fileinput import filename
from itertools import count
from types import NoneType
from tkinter import messagebox
#Window
def center_window():
    global screen_w_c
    global screen_h_c
    point_x, point_y = pyautogui.size()
    screen_w_c = int(point_x/2)
    screen_h_c = int(point_y/4)
center_window()

def window():
    main_window = tkinter.Tk()
    main_window.title("Encode Project Managment")
    main_x = 600
    main_y = 200
    main_window.geometry(f"{main_x}x{main_y}+{screen_w_c-main_x}+{screen_h_c+main_y}")

    frame = tkinter.Frame(main_window, relief=GROOVE, borderwidth=3)
    frame.pack(fill=BOTH, expand=1)

    #label_summ = tkinter.Label(text=f"Сотрудников в базе: {len(freezer)}")
    #label_summ.pack(side="bottom")

    label = tkinter.Label(frame, text="Encode Project Managment", bg=None)
    label.pack(side='top')
    ##def business_trip(): #Button for buisness trip confirmation
        




    def b1(): #Кнопка для перехода в меню заказа
        button1 = Button(main_window,
                                           text='Оформление командировок',
                                           width=50,height=5,
                                           bg="white", fg="black")
        button1.pack()
        #button1.bind("<Button-1>", business_trip) unbind
        business_trip()
    b1()

    # buisness_trip_ticket = "Командировка на персонал"
    # main_buttons_list = []
    # main_buttons_list.append(buisness_trip_ticket)# add buttons
    #
    # def btn():
    #     for _ in main_buttons_list:
    #
    #                         button =  Button(main_window,
    #                                    text=_,
    #                                    width=50,height=5,
    #                                    bg="white", fg="black")
    #                         button.pack()
    # btn()


    def quit_window(ev):
        main_window.destroy()

    exit_button =  Button(main_window,
                 text="Выход", width=50,
                 height=5,
                 bg="white", fg="black")
    exit_button.pack(side="top")
    exit_button.bind("<Button-1>", quit_window)

    main_window.mainloop()





window()
