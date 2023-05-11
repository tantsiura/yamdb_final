from django.db import models

class Category(models.Model):
    """Модель категории."""

    name = models.CharField(
        max_length=20, 
        verbose_name="Наименование категории"
    )
    slug = models.SlugField(
        unique=True, 
        db_index=True, 
        verbose_name="Слаг категории"
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Genre(models.Model):
    """Модель жанра."""

    name = models.CharField(
        max_length=20, 
        verbose_name="Наименование жанра"
    )
    slug = models.SlugField(
        unique=True, 
        db_index=True, 
        blank=True, 
        verbose_name="Слаг жанра"
    )

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

    def __str__(self):
        return self.name


class Title(models.Model):
    """Модель произведения."""

    name = models.CharField(
        max_length=20, 
        verbose_name="Наименование произведения"
    )
    year = models.PositiveIntegerField(
        db_index=True,)
    description = models.TextField(
        blank=True, 
        verbose_name="Описание произведения"
    )
    genre = models.ManyToManyField(
        Genre,
        related_name="titles",
        related_query_name="query_titles",
        verbose_name="Жанр",
        blank=True,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="titles",
        verbose_name="Категория",
    )

    class Meta:
        verbose_name = "Произведение"
        verbose_name_plural = "Произведения"

    def __str__(self):
        return self.name