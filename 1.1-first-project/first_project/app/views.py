from django.http import HttpResponse
from django.shortcuts import render, reverse
from os import listdir
from datetime import datetime


def home_view(request):
    template_name = "app/home.html"
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        "Главная страница": reverse("home"),
        "Показать текущее время": reverse("time"),
        "Показать содержимое рабочей директории": reverse("workdir"),
    }

    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {"pages": pages}
    return render(request, template_name, context)


def time_view(request):
    # обратите внимание – здесь HTML шаблона нет,
    # возвращается просто текст
    # Получение текущего времени
    current_time = datetime.now()
    # Форматирование времени
    # current_time = current_time.strftime("%d.%m.%Y %H:%M:%S")
    current_time = current_time.strftime("%H:%M:%S")
    msg = f"Текущее время: {current_time}"
    return HttpResponse(msg)


def workdir_view(request):
    # по аналогии с `time_view`, напишите код,
    # который возвращает список файлов в рабочей
    # директории
    msg = (
        "<h1>Cодержимое рабочей директории:</h1><p>"
        + "</p>\n<p>".join(listdir())
        + "</p>"
    )
    return HttpResponse(msg)
