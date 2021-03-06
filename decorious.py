#!/usr/bin/python3

import PIL.Image, PIL.ImageFilter, PIL.ImageOps


class IImage:
  def get_img_obj(self):
    raise NotImplementedError("cannot call method of IImage.get_img_obj on the interface")
  def get_parent(self):
    raise NotImplementedError("cannot call method of IImage.get_parent on the interface")



class BaseImage(IImage):
  def __init__(self, img_obj):
    self.img_obj = img_obj
  def get_parent(self):
    return self
  def get_img_obj(self):
    return self.img_obj


class ImageDecorator(IImage):
  def get_img_obj(self):
    raise NotImplementedError("cannot call method of ImageDecorator.get_img_obj on the base class")
  def get_parent(self):
    return self.img
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

