import cv2
import os

from PIL import Image, ImageFilter
image=Image.open('myphoto.jpg')
print(image.mode,image.format)

#旋轉
Rotate_img=image.rotate(330)
Rotate_img.save('RT.jpg')
display(Rotate_img)

#模糊化
Blur_img=image.filter(ImageFilter.GaussianBlur(radius=5))
Blur_img.save('BU.jpg')

#銳化
Sarp_img=image.filter(ImageFilter.UnsharpMask(radius=5))
Sarp_img.save('SP.jpg')

#拉伸
W_img=image.resize((int(image.size[0]), int(image.size[1]*0.65)))
W_img.save('W.jpg')

H_img=image.resize((int(image.size[0]*0.65), int(image.size[1])))
H_img.save('H.jpg')

