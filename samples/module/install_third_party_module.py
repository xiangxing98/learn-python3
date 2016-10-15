#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
* @Author: Stone_Hou
* Created Date: 2016-10-15 17:48:47
* Version History: 1.0
* runfile('E:/Github/learn-python3/samples/basic/the_dict.py', wdir='E:/Github/learn-python3/samples/basic')
"""
# @author: Administrator

#install_third_party_module.
#pip install Pillow

#有了Pillow，处理图片易如反掌。随便找个图片生成缩略图：
from PIL import Image
im = Image.open("D:/用户目录/我的图片/Saved Pictures/test.png")
print(im.format, im.size, im.mode)
#PNG (2484, 1656) RGB
im.thumbnail((12000, 10000))
im.save('thumb.jpg', 'JPEG')

#import mymodule