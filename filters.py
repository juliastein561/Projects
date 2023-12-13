#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project 1: This project changes images to have different filters.
@author: Julia Stein
"""


import math
import random

default_image_name = 'houseScenery.jpg'

def grayscale(red, green, blue):
    avg_value = (red + green + blue)//3
    red = avg_value
    green = avg_value
    blue = avg_value
    return red, green, blue


def posterize(red, green, blue):
    range_num = 255//3
    red = red//range_num
    green = green//range_num
    blue = blue//range_num
    red = red * range_num
    green = green * range_num
    blue = blue * range_num
    return red, green, blue


def lighter(red, green, blue):
    red = int(red + abs(red - 255) * 0.4)
    green = int(green + abs(green - 255) * 0.4)
    blue = int(blue + abs(blue - 255) * 0.4)
    return red, green, blue


def invert(red, green, blue):
    red = abs(red - 250)
    green = abs(green - 250)
    blue = abs(blue - 250)
    return red, green, blue


def tiedye(red, green, blue):
    red = (red % 100) * 2
    green = (green % 100) * 2
    blue = (blue % 100) * 2
    return red, green, blue


''' this code puts rainbow confetti all over'''
'''     the picture and makes it grainy.    '''
def my_filter(red, green, blue, x, y, width, height):
    int_random = random.randint(1,3)
    if int_random == 1:
        red = 255
    elif int_random == 2:
        green = 255
    elif int_random == 3:
        blue = 255
    return red, green, blue

""" Write no new code below here """
""" Here be dragons """
""" Don't Change this code """
if __name__ == '__main__':
    import elon_image
    elon_image.main(default_image_name)
