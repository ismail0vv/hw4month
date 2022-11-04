from django.shortcuts import render, Http404, redirect
from datetime import datetime
from .models import Film, Director
from .forms import FilmForm, DirectorForm, UserCreateForm, UserLoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate


# Create your views here.
def search_view(request):
    search_word = request.GET.get('search_word', '')
    print(search_word)
    context = {
        'directors': Director.objects.filter(),
        'films': Film.objects.filter(title__icontains=search_word).order_by('duration', 'title'),
        'search_word': search_word,
        'results': Film.objects.filter(title__icontains=search_word).count()
    }
    return render(request, 'search.html', context)


def logout_view(request):
    logout(request)
    return redirect('/')


def login_view(request):
    context = {
        'directors': Director.objects.all(),
        'form': UserLoginForm()
    }
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if not user:
                return redirect('/login/')
            else:
                login(request, user)
                return redirect('/')
    return render(request, 'login.html', context)


def register_view(request):
    context = {
        'directors': Director.objects.all(),
        'form': UserCreateForm()
    }
    if request.method == "POST":
        form = UserCreateForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            User.objects.create_user(username=username, password=password)
            return redirect('/login/')
        context['form'] = form
    return render(request, 'register.html', context)


def create_director_view(request):
    context = {
        'directors': Director.objects.all(),
        'form': DirectorForm()
    }
    if request.method == 'POST':
        form = DirectorForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/films/')
    return render(request, 'create_director.html', context)


def create_film_view(request):
    context = {
        'directors': Director.objects.all(),
        'form': FilmForm()
    }
    if request.method == 'POST':
        form = FilmForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/films/')
    return render(request, 'create_film.html', context)


def index_view(request):
    context = {
        'directors': Director.objects.all(),
    }
    return render(request, 'index.html', context)


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


PAGE_SIZE = 3


def films_view(request):
    page = int(request.GET.get('page', 1))
    all_films = Film.objects.all()
    page_films = all_films[PAGE_SIZE * (page - 1): PAGE_SIZE * page]
    pages_amount = (all_films.count() + PAGE_SIZE - 1) // PAGE_SIZE
    context = {
        'film_list': page_films,
        'directors': Director.objects.all(),
        'buttons': [i for i in range(1, pages_amount + 1)],
        'page': page,
        'pages_amount': pages_amount,
        'prev_page': page-1,
        'next_page': page+1,
    }

    return render(request, 'films.html', context=context)


def films_detail_view(request, id):
    context = {
        'film_detail': Film.objects.get(id=id),
        'directors': Director.objects.all(),
    }
    return render(request, 'film_detail.html', context=context)


def director_films_view(request, director_id):
    try:
        director = Director.objects.get(id=director_id)
    except Director.DoesNotExist:
        raise Http404
    context = {
        'director': director,
        'directors': Director.objects.all()
    }

    return render(request, 'director_products.html', context=context)
