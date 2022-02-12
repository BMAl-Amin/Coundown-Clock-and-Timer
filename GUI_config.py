import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import time

root = tk.Tk()
root.title('Countdown Timer')

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root_width = 350
root_height = 130
screen_x_pos = screen_width // 2 - root_width // 2
screen_y_pos = screen_height // 2 - root_height // 2

root.geometry(f'{root_width}x{root_height}+{screen_x_pos}+{screen_y_pos}')
root.resizable(False, False)

f = ("Arial", 24)
watch_frame = ttk.Frame(root)
watch_frame.pack(
    fill='x'
)

hours = tk.StringVar()
minutes = tk.StringVar()
seconds = tk.StringVar()

hours.set("00")
minutes.set("00")
seconds.set("00")

hours_entry = ttk.Entry(
    watch_frame, textvariable=hours, width=4, font=f, justify='center'
)
hours_entry.focus()
hours_entry.pack(
    ipadx=10,
    ipady=10,
    padx=8,
    pady=8,
    fill='both',
    side='left'
)

minutes_entry = ttk.Entry(
    watch_frame, textvariable=minutes, width=4, font=f, justify='center'
)
minutes_entry.pack(
    ipadx=10,
    ipady=10,
    padx=10,
    pady=8,
    fill='both',
    side='left'
)

seconds_entry = ttk.Entry(
    watch_frame, textvariable=seconds, width=4, font=f, justify='center'
)
seconds_entry.pack(
    ipadx=10,
    ipady=10,
    padx=8,
    pady=8,
    fill='both',
    side='left'
)


def countdown_time():
    try:
        userinput = int(hours_entry.get()) * 3600 + int(minutes_entry.get()) * 60 + int(seconds_entry.get())
    except:
        messagebox.showwarning('', 'Invalid Input!')

    while userinput > -1:
        mins, secs = divmod(userinput, 60)

        hour = 0
        if mins > 60:
            hour, mins = divmod(mins, 60)

        hours.set("{0:2d}".format(hour))
        minutes.set("{0:2d}".format(mins))
        seconds.set("{0:2d}".format(secs))

        root.update()
        time.sleep(1)

        if userinput == 0:
            messagebox.showinfo("", "Time's Up")

        userinput -= 1


start_btn = ttk.Button(
    root, text='Begin', width=5,
    command=lambda: countdown_time()
)
start_btn.place(x=120, y=120)
start_btn.pack(
    ipadx=8,
    ipady=5,
    pady=5
)

root.mainloop()
