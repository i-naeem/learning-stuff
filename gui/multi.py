from tkinter import Tk
from tkinter import Frame
from tkinter import Label
from tkinter import Button

app = Tk()
app.title = "Adding Multiple Widget"
app.geometry('200x200')


container = Frame(app, bg="#FF5555")

label = Label(container, text="We are in the container")


greet = "Hello, Friend!"
greeting_btn = Button(container, text="Greet me", command=lambda: print(greet))
quit_btn = Button(container, text="Quit", command=app.quit)

label.pack(side="top", fill="both",)
greeting_btn.pack(side="left")
quit_btn.pack(side="right")


container.pack(fill="both", expand=True)
app.mainloop()
