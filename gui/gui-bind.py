import tkinter as tk
import sys


main = tk.Tk()
button = tk.Button(main, text="Double click to exit")

button.bind('<Button 1>', lambda event: print("Double click to exit"))
button.bind('<Double 1>', lambda event: sys.exit())

button.pack(side="bottom")

main.mainloop()
