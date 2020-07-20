import tkinter as Filetracker
from tkinter import filedialog,Text,Tk

import os

root = Filetracker.Tk(screenName='Akram_maher')

root.title("FILE TRACKER/USER EXPLORER")

apps =[]


def openApp():
    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/", title="Select File(s)",
                                      filetypes=(("executables", "*.exe"), ("All Files", "*.*")))
    apps.append(filename)
    print(filename)

    for app in apps:
        label = Filetracker.Label(frame, text=app, bg="red")
        label.pack()

    #def runApp():
    for app in apps:
        os.startfile(app)

canvas = Filetracker.Canvas(root, height=500, width=500, background="aquamarine")
canvas.pack()

frame = Filetracker.Frame(root, bg="orange")
frame.place(relheight=0.5, relwidth=0.5, relx=0.2, rely=0.2)

open = Filetracker.Button(root, width=10, text="App Open", command=openApp)
open.pack()

#run = Filetracker.Button(root, width=10, text="App Run", command=runApp)
#run.pack()



for app in apps:
    l = Filetracker.Button(frame, text=apps.seek, width=10, command=openApp)
    l.pack()


root.mainloop(n=0)