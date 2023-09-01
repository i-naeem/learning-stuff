from tkinter import Tk
from tkinter import Frame
from tkinter import Label
from tkinter import Button
from tkinter.constants import LEFT, RIGHT, BOTH, TOP

app = Tk()
app.title = "Adding Multiple Widget"
app.geometry('200x200')


container = Frame(app, bg="#FF5555")

label = Label(container, text="We are in the container")


greet = "Hello, Friend!"
greeting_btn = Button(container, text="Greet me", command=lambda: print(greet))
quit_btn = Button(container, text="Quit", command=app.quit)

label.pack(side=TOP, fill=BOTH)
greeting_btn.pack(side=LEFT)
quit_btn.pack(side=RIGHT)


container.pack(fill=BOTH, expand=True)
app.mainloop()
