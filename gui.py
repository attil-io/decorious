#!/usr/bin/python3


import tkinter
import PIL
from PIL import ImageTk, Image
import decorious

root=tkinter.Tk()
image_raw = Image.open("lena.gif").convert('L')
canvas=tkinter.Canvas(root, height=200, width=200)

image_obj = decorious.BaseImage(image_raw)

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
    global image_obj
    image_obj = decorious.BlurFilter(image_obj, 5)
    show_image(image_obj.get_img_obj())

def rotate_callback():
    global image_obj
    image_obj = decorious.ImageFlipper(image_obj)
    show_image(image_obj.get_img_obj())


blur_button = tkinter.Button(root, text="Blur", command=blur_callback)
blur_button.pack()

rotate_button = tkinter.Button(root, text="Rotate", command=rotate_callback)
rotate_button.pack()


show_image(image_obj.get_img_obj())

root.mainloop()
