#!/usr/bin/python3

import PIL.Image, PIL.ImageFilter


class IImage:
  def getImgObj(self):
    raise NotImplementedError("cannot call method of IImage.getImgArr on the interface")

class BaseImage(IImage):
  def __init__(self, imgObj):
    self.imgObj = imgObj

  def getImgObj(self):
    return self.imgObj


class Filter(IImage):
  def getImgObj(self):
    raise NotImplementedError("cannot call method of Filter.getImgArr on the base class")
  def __init__(self, img):
    self.img = img


class BlurFilter(Filter):
  def __init__(self, img, radius):
    Filter.__init__(self, img)
    self.radius = radius
  def getImgObj(self):
    imageIternal = self.img.getImgObj()
    return imageIternal.filter(PIL.ImageFilter.GaussianBlur(self.radius))
    