# Create your views here.
from django.shortcuts import render
import datetime

from portfolio.models import Subject, Teacher

def home_page_view(request):
    agora = datetime.datetime.now()
    local = 'Lisboa'

    context = {
        'hora': agora.hour,
        'local': local,
    }
    return render(request, 'portfolio/home.html', context)

def licenciatura_page_view(request):
    agora = datetime.datetime.now()
    local = 'Lisboa'
    context = {
        'cadeiras':Subject.objects.all().order_by('year','semester')[:3],
    }
    return render(request, 'portfolio/licenciatura.html',context)