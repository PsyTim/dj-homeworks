import pprint
from django.contrib import admin
from django.forms import BaseInlineFormSet, ValidationError

from .models import Article, Tag, Scope


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        for form in self.forms:
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            form.cleaned_data
            pprint.pprint(form.cleaned_data)
            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке
        # sum(self.forms, lambda x: int(x.is_main))
        if sum([int(form.cleaned_data.get("is_main", 0)) for form in self.forms]) > 1:
            raise ValidationError("Тут всегда ошибка")
        return super().clean()  # вызываем базовый код переопределяемого метода


class ScopeInline(admin.TabularInline):  # admin.StackInlint (внешний вид)
    model = Scope
    extra = 3  # необязательный, 3 - дефолт (число доп строк)
    formset = ScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "published_at"]
    list_filter = ["tags"]

    inlines = [ScopeInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    list_filter = ["articles"]
    pass


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    list_display = ["id", "is_main", "tag", "article"]
    list_filter = ["tag", "article"]
    pass
