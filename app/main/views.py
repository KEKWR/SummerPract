import re
from django.shortcuts import render

def main(request):
    return render(request,'main/main.html', {'title': 'Советское кино'})

def actor(request):
    return render(request, 'main/actor.html', {'title': 'Актеры'})

def directors(request):
    return  render(request, 'main/directors.html', {'title': 'Режиссеры'})

def movies(request):
    return  render(request, 'main/movies.html', {'title': 'Фильмы'})

def reviews(request):
    return  render(request, 'main/reviews.html', {'title': 'Рецензии'})

def history(request):
    return  render(request, 'main/history.html', {'title': 'Исторяи кино'})

def account(request):
    return  render(request, 'main/account.html', {'title': 'Вход/Регистрация'})