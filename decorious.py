#!/usr/bin/python3

import PIL.Image, PIL.ImageFilter, PIL.ImageOps


class IImage:
  def getImgObj(self):
    raise NotImplementedError("cannot call method of IImage.getImgArr on the interface")

class BaseImage(IImage):
  def __init__(self, imgObj):
    self.imgObj = imgObj

  def getImgObj(self):
    return self.imgObj


class ImageDecorator(IImage):
  def getImgObj(self):
    raise NotImplementedError("cannot call method of ImageDecorator.getImgArr on the base class")
  def __init__(self, img):
    self.img = img


class BlurFilter(ImageDecorator):
  def __init__(self, img, radius):
    ImageDecorator.__init__(self, img)
    self.radius = radius
  def getImgObj(self):
    imageIternal = self.img.getImgObj()
    return imageIternal.filter(PIL.ImageFilter.GaussianBlur(self.radius))


class ImageFlipper(ImageDecorator):
  def __init__(self, img):
    ImageDecorator.__init__(self, img)
  def getImgObj(self):
    imageIternal = self.img.getImgObj()
    return PIL.ImageOps.flip(imageIternal)



im_raw = PIL.Image.open("lena.gif")
im_raw = im_raw.convert('L')
im_obj = BaseImage(im_raw)
im_obj_flipped = ImageFlipper(im_obj)
im_obj_flipped_blurred = BlurFilter(im_obj_flipped, 5)


im_obj.getImgObj().show("original")
im_obj_flipped.getImgObj().show("flipped")
im_obj_flipped_blurred.getImgObj().show("flipped and blurred")
