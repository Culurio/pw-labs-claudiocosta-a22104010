# Create your views here.
from django.shortcuts import render
import datetime

from portfolio.models import Cadeira, Teacher

def home_page_view(request):
    agora = datetime.datetime.now()
    local = 'Lisboa'

    context = {
        'hora': agora.hour,
        'local': local,
    }
    return render(request, 'portfolio/home.html', context)

def licenciatura_page_view(request):
    #professor = Teacher("Pedro Alves","https://www.ulusofona.pt/unicos/prof-pedro-alves","https://pt.linkedin.com/in/palves?original_referer=https%3A%2F%2Fwww.google.com%2F")
    #cadeira = Cadeira("AED","1º","5","2º","2021","3","Algoritmos e Estrutura de dados",professor)
    return render(request, 'portfolio/licenciatura.html')