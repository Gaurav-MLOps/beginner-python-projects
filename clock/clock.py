import tkinter as tk
import time

root = tk.Tk()
root.title("Digital Clock")

label = tk.Label(root, font=('Arial', 48), bg='black', fg='lime')
label.pack(anchor='center')

def update_time():
    current_time = time.strftime('%H:%M:%S')
    label.config(text=current_time)
    root.after(1000, update_time)

update_time()
root.mainloop()