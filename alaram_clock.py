# importing all the necessary libraries to form the alaram clock

from tkinter import *
import datetime
import time
import winsound


# create a while loop
def alaram(set_alaram_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H : %M : %S")
        date = current_time.strftime("%d/%m/%y")
        print("The Set Date is :", date)
        print("Current Time", now)
        print("Alaram Time", set_alaram_timer)
        print('--------------')
        if now == set_alaram_timer:
            print("Time to Wake up")
        print('--------------')

        winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
        print('--------------')

        break
        print('--------------')
        


def actual_time():
    set_alaram_timer = f"{hour.get()} : {min.get()} : {sec.get()}"
    alaram(set_alaram_timer)


clock = Tk()

clock.title("DataFlair Alaram Clock")
clock.geometry("400x200")
time_format = Label (clock, text="enter time in 24 hrs format!", fg="red", bg="black", font="Arial").place(x=60, y=120)
addTime = Label(clock, text="when to wake up", fg="blue", relief="solid", font=("Helevetica", 7, "bold")).place(x=0, y=29)


#variables we require to set the alaram(initialization):
hour = StringVar()
min = StringVar()
sec = StringVar()

#time required to set the alaram clock
hourTime = Entry(clock, textvariable=hour, bg="#fdaa97", width=7).place(x=130, y=30)
minTime = Entry(clock, textvariable=min, bg="#aa97fd", width=7).place(x=190, y=30)
secTime = Entry(clock, textvariable=sec, bg="#97fdaa", width=7).place(x=250, y=30)

#To take the time input by user:
submit = Button(clock, text="set Alaram", fg="red", width=10, command=actual_time).place(x=110, y=70)





clock.mainloop()

