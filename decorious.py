#!/usr/bin/python3

import PIL.Image, PIL.ImageFilter, PIL.ImageOps


class IImage:
  def get_img_obj(self):
    raise NotImplementedError("cannot call method of IImage.getImgArr on the interface")

class BaseImage(IImage):
  def __init__(self, img_obj):
    self.img_obj = img_obj

  def get_img_obj(self):
    return self.img_obj


class ImageDecorator(IImage):
  def get_img_obj(self):
    raise NotImplementedError("cannot call method of ImageDecorator.getImgArr on the base class")
  def __init__(self, img):
    self.img = img


class BlurFilter(ImageDecorator):
  def __init__(self, img, radius):
    ImageDecorator.__init__(self, img)
    self.radius = radius
  def get_img_obj(self):
    imageIternal = self.img.get_img_obj()
    return imageIternal.filter(PIL.ImageFilter.GaussianBlur(self.radius))


class ImageFlipper(ImageDecorator):
  def __init__(self, img):
    ImageDecorator.__init__(self, img)
  def get_img_obj(self):
    imageIternal = self.img.get_img_obj()
    return PIL.ImageOps.flip(imageIternal)



im_raw = PIL.Image.open("lena.gif")
im_raw = im_raw.convert('L')
im_obj = BaseImage(im_raw)
im_obj_flipped = ImageFlipper(im_obj)
im_obj_flipped_blurred = BlurFilter(im_obj_flipped, 5)


im_obj.get_img_obj().show("original")
im_obj_flipped.get_img_obj().show("flipped")
im_obj_flipped_blurred.get_img_obj().show("flipped and blurred")
