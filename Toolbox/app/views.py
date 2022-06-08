from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView
from app.models import *

alphabet = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e',
            6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j',
            11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o',
            16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't',
            21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y',
            26: 'z', }


class ApplicationList(ListView):
    model = Application


class ApplicationView(DetailView):
    model = Application


def manage_functions(request, pk=None):
    if pk:
        function = Application.objects.get(pk=pk)
    val = function.template_text.replace('{{ opci }}', '0').replace('{{ error }}', '')
    for i in range(1, function.output_anzahl + 1):
        val = val.replace('{{ ' + alphabet[i] + ' }}', '')
    return render(request, f'app/template.html',
                  {'page_title': f'{function.name}',
                   'id': f'{pk}',
                   'op': 0,
                   'templatecode': val,
                   'description': function.description,
                   })


def select_function(request, pk=None):
    function = Application.objects.get(pk=pk)
    try:
        values = ""
        for i in range(1, function.input_anzahl + 1):
            values += alphabet[i] + " = '" + (request.POST[alphabet[i]]) + "'\n"

        values += 'error = False \n'

        loc = {}

        exec(values + function.function, globals(), loc)

        if loc['error']:
            raise ValueError()

        val = function.template_text.replace('{{ opci }}', '0')

        for i in range(1, function.output_anzahl + 1):
            val = val.replace('{{ ' + alphabet[i] + ' }}', str(loc[alphabet[i]]))

        return render(request, f'app/template.html',
                      {'page_title': f'{function.name}',
                       'id': f'{pk}',
                       'templatecode': val,
                       'description': function.description, })
    except:
        val = function.template_text.replace('{{ opci }}', '1').replace('{{ error }}', function.error_message)
        for i in range(1, function.output_anzahl + 1):
            val = val.replace('{{ ' + alphabet[i] + ' }}', '')
        return render(request, f'app/template.html',
                      {'page_title': f'{function.name}',
                       'id': f'{pk}',
                       'templatecode': val,
                       'description': function.description,
                       })


def create_template(request):
    return render(request, f'app/create.html', {})


input_variable = 0
output_variable = 0
app_name = ''
code = ''
error = ''
desc = ''


def next_app(request):
    template_text = ''
    global app_name
    global input_variable
    global output_variable
    global code
    global error
    global desc
    app_name = request.POST['appname']
    input_variable = int(request.POST['input'])
    output_variable = int(request.POST['output'])
    code = request.POST['code']
    error = request.POST['error']
    desc = request.POST['description']

    in_str = '''<p>Geben sie {{ num }}. input Variable: <input type="text" name="{{ name }}in">,
             und den type: <select class="btn btn-outline-primary" name="type" id="type">
             <option value="number" selected>Number</option>
             <option value="text">Text</option>
             <option value="email">Email</option>
             <option value="date">Date</option>
             <option value="time">Time</option>
             </select></p>'''
    out_str = '<p>Geben sie num. output Variable: <input type="text" name="{{ name }}out"></p>'

    for x in range(1, input_variable + 1):
        template_text += in_str.replace('{{ num }}', str(x)).replace('{{ name }}', alphabet[x])
    template_text += '<br>'
    for y in range(1, output_variable + 1):
        template_text += out_str.replace('num', str(y)).replace('{{ name }}', alphabet[y])

    return render(request, f'app/inout.html', {'templatetext': template_text})


def app_create(request):
    template_text = ''
    global input_variable
    global output_variable
    global app_name
    global code
    global error
    global desc

    in_str = '<p>Geben Sie {{ name }} ein: <input type="{{ type }}" name="{{ alpha }}"></p>'
    out_str = '<p>{{ name }} : {{ alpha }} </p>'

    for x in range(1, input_variable + 1):
        template_text += in_str.replace('{{ name }}', request.POST[alphabet[x] + 'in']) \
            .replace('{{ type }}', request.POST['type']) \
            .replace('{{ alpha }}', alphabet[x])
    template_text += '<input type="submit" class="btn btn-outline-primary"><p style="opacity:{{ opci }}">' \
                     'Error : {{ error }}</p>'
    for x in range(1, output_variable + 1):
        template_text += out_str.replace('{{ name }}', request.POST[alphabet[x] + 'out']) \
                            .replace('{{ alpha }}', '{{ ' + alphabet[x] + ' }}') + '\n'

    a = Application(name=app_name, input_anzahl=input_variable, output_anzahl=output_variable,
                    template_text=template_text, error_message=error, description=desc, function=code)
    a.save()
    return HttpResponseRedirect(reverse_lazy('app_list'))
