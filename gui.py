#!/usr/bin/python3


import tkinter
import PIL
from PIL import ImageTk, Image

root=tkinter.Tk()
image = Image.open("lena.gif")
canvas=tkinter.Canvas(root, height=200, width=200)
basewidth = 150
wpercent = (basewidth / float(image.size[0]))
hsize = int((float(image.size[1]) * float(wpercent)))
image = image.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
item4 = canvas.create_image(100, 80, image=photo)

canvas.pack(side = tkinter.TOP, expand=True, fill=tkinter.BOTH)


def blur_callback():
    print("blurring")

def rotate_callback():
    print("rotating")


blur_button = tkinter.Button(root, text="Blur", command=blur_callback)
blur_button.pack()

rotate_button = tkinter.Button(root, text="Rotate", command=rotate_callback)
rotate_button.pack()


root.mainloop()