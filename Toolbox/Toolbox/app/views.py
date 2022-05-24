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
