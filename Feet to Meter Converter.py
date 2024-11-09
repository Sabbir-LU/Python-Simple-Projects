# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 21:58:15 2024

@author: ahmed
"""

from tkinter import Tk, Button, Label, DoubleVar, Entry, Frame, CENTER, StringVar
import tkinter.font as tkFont

def convert_feet_to_meters():
    feet = ft_value.get()
    meters = round(feet * 0.3048, 4)
    mt_value.set(f"{meters} meters")

window = Tk()
window.title("Feet to Meter Conversion Application")
window.configure(background="#2E8B57")
window.geometry("400x400")
window.resizable(width=False, height=False)


title_font = tkFont.Font(family="Helvetica", size=18, weight="bold")
label_font = tkFont.Font(family="Arial", size=12)
button_font = tkFont.Font(family="Arial", size=12, weight="bold")

title = Label(window, text="Feet to Meter Conversion", bg="#2E8B57", fg="white", font=title_font)
title.pack(pady=20)


frame = Frame(window, bg="#2E8B57")
frame.pack(pady=10)

ft_lb1 = Label(frame, text='Feet:', bg="#2E8B57", fg='white', font=label_font, anchor=CENTER, width=10)
ft_lb1.grid(column=0, row=0, padx=20, pady=10)

ft_value = DoubleVar()
ft_entry = Entry(frame, textvariable=ft_value, width=14, font=label_font, justify=CENTER)
ft_entry.grid(column=1, row=0, padx=20, pady=10)


mt_lb1 = Label(frame, text='Converted:', bg="#2E8B57", fg='white', font=label_font, anchor=CENTER, width=10)
mt_lb1.grid(column=0, row=1, padx=20, pady=10)

mt_value = StringVar()
mt_output = Label(frame, textvariable=mt_value, bg="white", fg="#333333", font=label_font, width=14, relief="sunken")
mt_output.grid(column=1, row=1, padx=20, pady=10)


convert_btn = Button(window, text='Convert', font=button_font, bg="#4682B4", fg="white", 
                     width=15, command=convert_feet_to_meters, bd=3, relief="raised", activebackground="#5F9EA0")
convert_btn.pack(pady=30)

window.mainloop()