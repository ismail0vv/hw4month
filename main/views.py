from django.shortcuts import render
from datetime import datetime
from .models import Film

# Create your views here.
def index_view(request):
    return render(request, 'index.html')


def about_us_view(request):
    return render(request, 'about.html', context={'year': str(datetime.now().year - 2005)})


def date_now_view(request):
    cur_date = datetime.now()
    context = {
        'year': cur_date.year,
        'month': cur_date.month,
        'day': cur_date.day,
        'hour': cur_date.hour,
        'minute': cur_date.minute,
    }

    return render(request, 'date_now.html', context=context)


def films_view(request):
    context = {
        'film_list': Film.objects.all()
    }

    return render(request, 'films.html', context=context)


def films_detail_view(request, id):
    context = {
        'film_detail': Film.objects.get(id=id)
    }
    return render(request, 'film_detail.html', context=context)