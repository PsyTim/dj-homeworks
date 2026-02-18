import csv

from django.core.management.base import BaseCommand
from phones.models import Phone
from django.utils.text import slugify


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open("phones.csv", "r") as file:
            phones = list(csv.DictReader(file, delimiter=";"))

        for phone in phones:
            # TODO: Добавьте сохранение модели
            phone["id"] = int(phone["id"])
            print(phone)
            # id = int(phone["id"])
            # name = phones["name"]
            # price = phone["price"]
            # rel = phone["release_date"]
            # lte = phone["lte_exists"]
            # Phone(id, price=price, release_date=rel, lte_exists=lte).save()
            phone["slug"] = slugify(phone["name"])
            Phone(**phone).save()
            pass
