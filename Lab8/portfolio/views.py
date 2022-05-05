# Create your views here.
from django.shortcuts import render
import datetime

def home_page_view(request):
    agora = datetime.datetime.now()
    local = 'Lisboa'

    context = {
        'hora': agora.hour,
        'local': local,
    }
    return render(request, 'portfolio/home.html', context)