from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from users.models import User

from .constants import MAX_REVIEW_SCORE_VALUE, MIN_REVIEW_SCORE_VALUE


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


class Review(models.Model):
    """Title Review model."""
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reviews'
    )
    title = models.ForeignKey(
        Title, on_delete=models.CASCADE, related_name='reviews'
    )
    text = models.TextField()
    pub_date = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True
    )
    score = models.IntegerField(
        'Оценка',
        validators=[MinValueValidator(MAX_REVIEW_SCORE_VALUE),
                    MaxValueValidator(MIN_REVIEW_SCORE_VALUE)]
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['author', 'title'],
                name='unique_review'
            )
        ]

    def __str__(self):
        """Return review text."""
        return self.text


class Comment(models.Model):
    """Review comment model."""
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments'
    )
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name='comments'
    )
    text = models.TextField()
    pub_date = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True
    )

    def __str__(self):
        """Return review comment text."""
        return self.text
