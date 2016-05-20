#!/usr/local/bin/env python3
#-*- coding utf-8 -*-

from PIL import Image
im = Image.open("../assets/profile.jpg")
print("profile size: ",im.size)
im.thumbnail((150,150))
im.save("../assets/thumb_profile.jpg","JPEG")

im = Image.open("../assets/thumb_profile.jpg")
print("profile size: ",im.size)