from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from app.models import *

alphabet = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', }


class ApplicationList(ListView):
    model = Application


class ApplicationView(DetailView):
    model = Application


def binaryToDecimal(request):
    number = request.POST['bin']
    try:
        return render(request, 'app/binaryToDecimal.html',
                      {'page_title': 'binaryToDecimal', 'op': 0, 'error': "",
                       'result': int(number, 2), 'number': number})

    except:
        return render(request, 'app/binaryToDecimal.html',
                      {'page_title': 'binaryToDecimal', 'op': 1, 'error': "Geben Sie bitte eine Binärzahl ein",
                       'result': "", 'number': number})


def decimalToBinary(request):
    number = request.POST['bin']
    try:
        return render(request, 'app/decimalToBinary.html',
                      {'page_title': 'decimalToBinary', 'op': 0, 'error': "",
                       'result': bin(int(number)), 'number': number})
    except:
        return render(request, 'app/decimalToBinary.html',
                      {'page_title': 'decimalToBinary', 'op': 1, 'error': "Geben Sie bitte eine Dezimalzahl ein",
                       'result': "", 'number': number})


def octalToDecimal(request):
    number = request.POST['oct']
    try:
        return render(request, 'app/octalToDecimal.html',
                      {'page_title': 'octalToDecimal', 'op': 0, 'error': "",
                       'result': int(number, 8), 'number': number})
    except:
        return render(request, 'app/octalToDecimal.html',
                      {'page_title': 'octalToDecimal', 'op': 1, 'error': "Geben Sie bitte eine Dezimalzahl ein",
                       'result': "", 'number': number})


def decimalToOctal(request):
    number = request.POST['bin']
    try:
        result = oct(int(number))
    except:
        error = "Geben Sie bitte eine Dezimalzahl ein"
        result = ""
        return render(request, f'app/decimalToOctal.html',
                      {'page_title': f'decimalToOctal', 'result': result, 'number': number, 'op': 1, 'error': error})
    return render(request, f'app/decimalToOctal.html',
                  {'page_title': f'decimalToOctal', 'result': result, 'number': number, "op": 0})


def decimalToHexa(request):
    number = request.POST['bin']
    try:
        result = hex(int(number))
    except:
        error = "Geben Sie bitte eine Dezimalzahl ein"
        result = ""
        return render(request, f'app/decimalToHexa.html',
                      {'page_title': f'decimalToHexa', 'result': result, 'number': number, 'op': 1, 'error': error})
    return render(request, f'app/decimalToHexa.html',
                  {'page_title': f'decimalToHexa', 'result': result, 'number': number, 'op': 0})


def hexaToDecimal(request):
    number = request.POST['hex']
    try:
        result = int(number, 16)
    except:
        error = "Geben Sie bitte eine Hexadezimalzahl ein"
        result = ""
        return render(request, f'app/hexaToDecimal.html',
                      {'page_title': f'hexaToDecimal', 'result': result, 'number': number, 'op': 1, 'error': error})
    return render(request, f'app/hexaToDecimal.html',
                  {'page_title': f'hexaToDecimal', 'result': result, 'number': number, 'op': 0})


def rgbToCmyk(request, CMYK_SCALE=100, RGB_SCALE=255):
    try:
        r = int(request.POST['r'])
        g = int(request.POST['g'])
        b = int(request.POST['b'])
    except:
        return render(request, 'app/rgbToCmyk.html',
                      {'page_title': f'rgbToCmyk', 'op': 1,
                       'error': "Bitte geben sie 3 nummern zwischen 0 und 255 ein",
                       'c': "", 'm': "", 'y': "", 'k': "", })

    if not (0 <= r <= 255) or not (0 <= g <= 255) or not (0 <= b <= 255):
        return render(request, f'app/rgbToCmyk.html',
                      {'page_title': f'rgbToCmyk', 'op': 1, 'error': "Bitte nur nummern zwischen 0 und 255 nutzen",
                       'c': "", 'm': "", 'y': "", 'k': "", })
    if (r, g, b) == (0, 0, 0):
        return render(request, f'app/rgbToCmyk.html',
                      {'page_title': f'rgbToCmyk', 'op': 0, 'error': "", 'c': 0, 'm': 0, 'y': 0, 'k': CMYK_SCALE, })
    y = 1 - b / RGB_SCALE
    c = 1 - r / RGB_SCALE
    m = 1 - g / RGB_SCALE
    min_cmy = min(c, m, y)
    c = (c - min_cmy) / (1 - min_cmy)
    m = (m - min_cmy) / (1 - min_cmy)
    y = (y - min_cmy) / (1 - min_cmy)
    k = min_cmy
    return render(request, f'app/rgbToCmyk.html',
                  {'page_title': f'rgbToCmyk', 'op': 0, 'error': "", 'c': c * CMYK_SCALE, 'm': m * CMYK_SCALE,
                   'y': y * CMYK_SCALE, 'k': k * CMYK_SCALE, })


def cmykToRgb(request, cmyk_scale=100, rgb_scale=255):
    try:
        c = float(request.POST['c'])
        m = float(request.POST['m'])
        y = float(request.POST['y'])
        k = float(request.POST['k'])

    except:
        return render(request, 'app/cmykToRgb.html',
                      {'page_title': f'cmykToRgb', 'op': 1,
                       'error': "Bitte geben sie 4 nummern zwischen 0 und 100 ein",
                       'r': "", 'g': "", 'b': "", })
    if not (0 <= c <= 100) or not (0 <= m <= 100) or not (0 <= y <= 100) or not (0.0 <= k <= 1.0):
        return render(request, f'app/cmykToRgb.html',
                      {'page_title': f'cmykToRgb', 'op': 1,
                       'error': "Bitte nur nummern zwischen 0 und 100 nutzen bzw. bei kontrolle nur von 0 bis 1",
                       'r': "", 'g': "", 'b': "", })

    r = rgb_scale * (1.0 - c / float(cmyk_scale)) * (1.0 - k / float(cmyk_scale))
    g = rgb_scale * (1.0 - m / float(cmyk_scale)) * (1.0 - k / float(cmyk_scale))
    b = rgb_scale * (1.0 - y / float(cmyk_scale)) * (1.0 - k / float(cmyk_scale))
    return render(request, f'app/cmykToRgb.html',
                  {'page_title': f'cmykToRgb', 'op': 0, 'error': "",
                   'r': r, 'g': g, 'b': b, })


def manage_functions(request, pk=None):
    if pk:
        function = Application.objects.get(pk=pk)
    val = function.templatetext.replace('{{ opci }}', '0').replace('{{ error }}', '')
    for i in range(1, function.outputanzahl + 1):
        val = val.replace('{{ ' + alphabet[i] + ' }}', '')
    return render(request, f'app/template.html',
                  {'page_title': f'{function.name}',
                   'id': f'{pk}',
                   'op': 0,
                   'templatecode': val,
                   })


def select_function(request, pk=None):
    function = Application.objects.get(pk=pk)
    try:
        values = ""
        for i in range(1, function.inputanzahl + 1):
            values += alphabet[i] + " = '" + (request.POST[alphabet[i]]) + "'\n"

        loc = {}

        print(values + function.functionname)

        exec(values + function.functionname, globals(), loc)

        if loc['error']:
            raise ValueError()

        val = function.templatetext.replace('{{ opci }}', '0', 1)

        for i in range(1, function.outputanzahl + 1):
            val = val.replace('{{ ' + alphabet[i] + ' }}', str(loc[alphabet[i]]))

        return render(request, f'app/template.html',
                      {'page_title': f'{function.name}', 'id': f'{pk}', 'templatecode': val, })
    except:
        val = function.templatetext.replace('{{ opci }}', '1').replace('{{ error }}', function.errormessage)
        for i in range(1, function.outputanzahl + 1):
            val = val.replace('{{ ' + alphabet[i] + ' }}', '')
        return render(request, f'app/template.html',
                      {'page_title': f'{function.name}',
                       'id': f'{pk}',
                       'templatecode': val
                       })
