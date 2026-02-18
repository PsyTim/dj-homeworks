from django.shortcuts import get_object_or_404, render, redirect
from phones.models import Phone


def index(request):
    return redirect("catalog")


def show_catalog(request):
    template = "catalog.html"
    context = {}
    sort_by = request.GET.get("sort", "name")
    if sort_by in ["min_price", "max_price"]:
        order_by = "price"
    else:
        order_by = "name"
    phones = Phone.objects.order_by(order_by).all()
    if sort_by == "max_price":
        phones = phones[::-1]
        pass
    context["phones"] = phones
    context["sort"] = sort_by
    return render(request, template, context)


def show_product(request, slug):
    template = "product.html"
    sort_by = request.GET.get("sort", "name")

    product = get_object_or_404(Phone, slug=slug)
    context = {"phone": product, "sort": sort_by}
    return render(request, template, context)
