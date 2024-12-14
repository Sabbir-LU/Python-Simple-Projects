# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 19:27:57 2024

@author: ahmed
"""

import tkinter as tk
from tkinter import messagebox

def start_timer():
    global paused, remaining_time
    try:
        total_minutes = int(entry.get())
        if total_minutes <= 0:
            raise ValueError
        remaining_time = total_minutes * 60 * 1000
        paused = False
        countdown(remaining_time)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a positive integer.")

def countdown(time_left):
    global paused, remaining_time
    if paused:
        return

    if time_left > 0:
        remaining_time = time_left
        mins, secs = divmod(time_left // 1000, 60)
        millis = (time_left % 1000) // 10
        timer_label.config(text=f"{mins:02}:{secs:02}:{millis:02}")

        root.after(10, countdown, time_left - 10)
    else:
        timer_label.config(text="00:00:00")
        messagebox.showinfo("Time's Up", "The timer has ended!")

def pause_timer():
    global paused
    paused = not paused
    if not paused:
        countdown(remaining_time)

root = tk.Tk()
root.title("Simple Timer")


paused = False
remaining_time = 0


entry_label = tk.Label(root, text="Enter time in minutes:")
entry_label.pack(pady=5)

entry = tk.Entry(root)
entry.pack(pady=5)

start_button = tk.Button(root, text="Start Timer", command=start_timer)
start_button.pack(pady=5)

pause_button = tk.Button(root, text="Pause/Resume Timer", command=pause_timer)
pause_button.pack(pady=5)


timer_label = tk.Label(root, text="00:00:00", font=("Helvetica", 48))
timer_label.pack(pady=20)

root.mainloop()
