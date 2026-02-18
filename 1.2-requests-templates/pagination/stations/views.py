from django.shortcuts import render, redirect
from django.urls import reverse
import csv
from django.core.paginator import Paginator


def index(request):
    return redirect(reverse("bus_stations"))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    bus_stations = []
    with open("data-398-2018-08-30.csv", encoding="UTF-8") as f:
        reader = csv.DictReader(f.readlines())
        for row in reader:
            bus_stations.append(row)
        paginator = Paginator(bus_stations, 10)
        page_number = request.GET.get("page", "1")
        if page_number.isdigit() and int(page_number):
            page_number = int(page_number)
        else:
            page_number = 1

        page = paginator.get_page(page_number)
    context = {
        "bus_stations": page,
        "page": page,
    }
    return render(request, "stations/index.html", context)
