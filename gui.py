#!/usr/bin/python3


import tkinter
import PIL
from PIL import ImageTk, Image
import decorious

root=tkinter.Tk()
image_raw = Image.open("lena.gif").convert('L')
canvas=tkinter.Canvas(root, height=200, width=200)

wrapped_image = decorious.BaseImage(image_raw)

def show_image(image):
    canvas.delete("all")
    basewidth = 150
    wpercent = (basewidth / float(image.size[0]))
    hsize = int((float(image.size[1]) * float(wpercent)))
    image = image.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)
    item4 = canvas.create_image(100, 80, image=photo)
    canvas.image = photo
    canvas.pack(side = tkinter.TOP, expand=True, fill=tkinter.BOTH)


def blur_callback():
    global wrapped_image
    wrapped_image = decorious.BlurFilter(wrapped_image, 5)
    show_image(wrapped_image.get_img_obj())

def flip_callback():
    global wrapped_image
    wrapped_image = decorious.ImageFlipper(wrapped_image)
    show_image(wrapped_image.get_img_obj())


def undo_callback():
    global wrapped_image
    wrapped_image = wrapped_image.get_parent()
    show_image(wrapped_image.get_img_obj())


blur_button = tkinter.Button(root, text="Blur", command=blur_callback)
blur_button.pack()

flip_button = tkinter.Button(root, text="Flit", command=flip_callback)
flip_button.pack()


undo_button = tkinter.Button(root, text="Undo", command=undo_callback)
undo_button.pack()


show_image(wrapped_image.get_img_obj())

root.mainloop()
