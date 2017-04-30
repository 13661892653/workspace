# -*- coding: utf-8 -*-
import os
from io import StringIO
from PIL import Image, ImageFilter, ImageDraw, ImageFont, ImageEnhance, ImageFilter
import pygame
pygame.init()
text = u"这是一段测试文本，test 123。"
im = Image.new("RGB", (1024, 755), (255, 255, 255))
font = pygame.font.SysFont("arial", 12)
# dr.text((10, 5), text, font=font, fill="#000000")
rtext = font.render(text, True, (0, 0, 0), (255, 255, 255))
# pygame.image.save(rtext, "t.gif")
sio = StringIO()
pygame.image.save(rtext, sio)
sio.seek(0)

line = Image.open(sio)
im.paste(line, (10, 5))

im.show()
im.save("t.png")