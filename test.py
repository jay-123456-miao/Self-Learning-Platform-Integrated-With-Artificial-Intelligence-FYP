import tkinter as tk
import time

def countdown(duration):
    mins, secs = divmod(duration, 60)
    timer = '{:02d}:{:02d}'.format(mins, secs)
    countdown_label.config(text=timer)
    if duration > 0:
        countdown_label.after(1000, lambda: countdown(duration - 1))
    else:
        countdown_label.config(text="Time is up!")

root = tk.Tk()
root.title("Countdown Timer")

countdown_label = tk.Label(root, font=("Helvetica", 48))
countdown_label.pack(pady=20)

start_button = tk.Button(root, text="Start Countdown", command=lambda: countdown(20))
start_button.pack(pady=10)

root.mainloop()