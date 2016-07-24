#!/usr/bin/python3


class IImage:
  pass;

class BaseImage(IImage):
  pass;

class Filter(IImage):
  def __init__(self, img):
    self.img = img


class BlurFilter(Filter):
  def __init__(self, img, radius):
    Filter.__init__(self, img)
    self.radius = radius