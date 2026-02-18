from datetime import date
from django.http import Http404
from django.shortcuts import redirect, render, HttpResponse, get_list_or_404
from django.urls import reverse
from books.models import Book


def index(request):
    return redirect(reverse("books"))


def _make_rows(books):
    row = []
    rows = []
    for book in books:
        print(book)
        row.append(book)
        if len(row) == 2:
            rows.append(row)
            row = []
    if row:
        rows.append(row)
    print(rows)
    return rows


def books_view(request):
    books = Book.objects.all()
    template = "books/books_list.html"
    rows = _make_rows(books)
    context = {"rows": rows}
    return render(request, template, context)


def books_by_date(request, year, month, day):
    # Формируем текущую дату
    try:
        current_date = date(year, month, day)
    except:
        raise Http404

    books = get_list_or_404(Book.objects.filter(pub_date=current_date))
    # Находим предыдущую дату (меньше current_date), для которой есть книги
    prev_date = (
        Book.objects.filter(pub_date__lt=current_date)
        .order_by("-pub_date")
        .values_list("pub_date", flat=True)
        .first()
    )

    # Находим следующую дату (больше current_date), для которой есть книги
    next_date = (
        Book.objects.filter(pub_date__gt=current_date)
        .order_by("pub_date")
        .values_list("pub_date", flat=True)
        .first()
    )
    template = "books/books_by_date.html"
    rows = _make_rows(books)
    context = {"rows": rows, "prev_date": prev_date, "next_date": next_date}
    return render(request, template, context)
