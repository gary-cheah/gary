import os
from tkinter import filedialog, Text
import tkinter as tk
tk.mainloop

root = tk.Tk()

# bg 是背景的颜色，或者可以放colour code
canvas = tk.Canvas(root, height=700, width=700, bg="#A32CC4")
canvas.pack()

frame = tk.Frame(root, bg="#710193")
# relwidth和relheights是宽度和高度的设定，relx和rely是左右2 边的空隙的大小
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

# fg是按键按下去的颜色，bg在按键这里是按键的颜色·
openfile = tk.Button(root, text="Open App", padx=10,
                     pady=8, fg="#710193", bg="#A32CC4")

openfile.pack()

runapps = tk.Button(root, text="Run Apps", padx=10,
                    pady=8, fg="#710193", bg="#A32CC4")

runapps.pack()
root.mainloop()
