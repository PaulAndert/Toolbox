from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from app.models import *


class ApplicationList(ListView):
    model = Application


class ApplicationView(DetailView):
    model = Application


def binaryToDecimal(number):
    return int(number, 2)

def decimalToBinary(number):
    return bin(number)

def octalToDecimal(number):
    return int(number)

def decimalToOctal(decimal_num):
    return oct(decimal_num)

def decimalToHexa(num):
    return hex(num)

def hexaToDecimal(hexa_num):
    return int(hexa_num, 16)

def rgbToCmyk(r, g, b, CMYK_SCALE = 100, RGB_SCALE = 255):
    if (r, g, b) == (0, 0, 0): return 0, 0, 0, CMYK_SCALE
    c = 1 - r / RGB_SCALE
    m = 1 - g / RGB_SCALE
    y = 1 - b / RGB_SCALE
    min_cmy = min(c, m, y)
    c = (c - min_cmy) / (1 - min_cmy)
    m = (m - min_cmy) / (1 - min_cmy)
    y = (y - min_cmy) / (1 - min_cmy)
    k = min_cmy
    return c * CMYK_SCALE, m * CMYK_SCALE, y * CMYK_SCALE, k * CMYK_SCALE

def cmykToRgb(c, m, y, k, cmyk_scale = 100, rgb_scale=255):
    r = rgb_scale * (1.0 - c / float(cmyk_scale)) * (1.0 - k / float(cmyk_scale))
    g = rgb_scale * (1.0 - m / float(cmyk_scale)) * (1.0 - k / float(cmyk_scale))
    b = rgb_scale * (1.0 - y / float(cmyk_scale)) * (1.0 - k / float(cmyk_scale))
    return r, g, b

