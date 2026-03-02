from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name="Название")
    text = models.TextField(verbose_name="Текст")
    published_at = models.DateTimeField(verbose_name="Дата публикации")
    image = models.ImageField(
        null=True,
        blank=True,
        verbose_name="Изображение",
    )

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(50)
    articles = models.ManyToManyField(Article, related_name="tags", through="Scope")

    class Meta:
        verbose_name = "Тема"
        verbose_name_plural = "Темы"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Scope(models.Model):
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name="scopes"
    )
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name="scopes")
    is_main = models.BooleanField()

    class Meta:
        verbose_name = "Тема новости"
        verbose_name_plural = "Темы новостей"
        ordering = ["-is_main", "tag__name"]

    def __str__(self):
        return f"[{self.tag.name}]: {self.article.title}"
