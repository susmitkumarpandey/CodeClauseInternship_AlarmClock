from tkinter import *
from tkinter import messagebox
import time
import winsound


def alarm():
    Alarm_time = alarm_time.get()
    check_alarm(Alarm_time)


def check_alarm(alarm_time):
    while True:
        current_time = time.strftime("%H:%M")
        if current_time == alarm_time:
            winsound.Beep(1000, 5000)
            messagebox.showinfo("Alarm", "Hope You Are FULLy AWAKE!!")
            break
        time.sleep(1)
        screen.update()


screen = Tk()
screen.title("ALARMY")
screen.config(pady=30,)

canvas = Canvas(height=300, width=400)
logo = PhotoImage(
    file="clock.png")
canvas.create_image(200, 150, image=logo)
clock = canvas.create_text(200, 150, text=time.strftime(
    "%H:%M:%S"), font=('Dottles 20 bold'))
canvas.grid(row=0, column=1)

alarm_time = Entry(width=10)
alarm_time.grid(row=1, column=1)

set_alarm = Button(text="Set Alarm", width=8, command=alarm)
set_alarm.grid(row=2, column=1)


def update_clock():
    canvas.itemconfig(clock, text=time.strftime("%H:%M:%S"))
    screen.after(1000, update_clock)
    screen.update()


screen.after(1000, update_clock)

screen.mainloop()
