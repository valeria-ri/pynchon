from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator
from django.db import models
from django.template.defaultfilters import truncatechars
from ckeditor.fields import RichTextField

from core.models import BaseModel, BaseNameModel

User = get_user_model()


class Book(BaseNameModel):
    """ Модель книг. """

    description = models.TextField(
        verbose_name='Описание книги'
    )

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        db_table = 'books'

    def __str__(self) -> str:
        return self.name


class Chapter(BaseModel):
    """ Модель глав у книг. """

    number = models.CharField(
        verbose_name='Номер главы',
        max_length=8
    )
    book = models.ForeignKey(
        Book,
        verbose_name='Книга',
        related_name='chapters',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    description = RichTextField(
        verbose_name='Описание главы',
        blank=True,
        null=True
    )
    book_part = models.PositiveIntegerField(
        verbose_name='Часть книги',
        blank=True, null=True,
        validators=[
            MaxValueValidator(10000)
        ],
    )
    summary = RichTextField(
        verbose_name='Краткое содержание главы',
        blank=True,
        null=True
    )
    interpretation = RichTextField(
        verbose_name='Интерпретация',
        blank=True,
        null=True
    )
    image = models.ImageField(
        verbose_name='Картинка',
        blank=True,
        null=True,
        upload_to='chapters/'
    )
    pages = models.CharField(
        'Номер страниц',
        max_length=50,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Глава'
        verbose_name_plural = 'Главы'
        db_table = 'chapters'

    def __str__(self) -> str:
        return str(self.number)


class ChapterLink(BaseModel):
    """ Модель ссылок для глав книг. """

    link = models.URLField(
        verbose_name='Ссылка к главе',
        blank=True,
        null=True,
    )
    chapter = models.ForeignKey(
        Chapter,
        verbose_name='Глава',
        related_name='chapters',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Ссылка к главе'
        verbose_name_plural = 'Ссылки к главе'
        db_table = 'chapter_links'

    def __str__(self):
        return self.link


class Comment(BaseNameModel):
    """ Модель комментариев. """

    comment_text = RichTextField(
        'Текст примечания'
    )
    image = models.ImageField(
        verbose_name='Картинка',
        blank=True,
        null=True,
        upload_to='comments/'
    )
    book = models.ForeignKey(
        Book, verbose_name='Книга',
        related_name='comments',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    chapter = models.ForeignKey(
        Chapter,
        verbose_name='Номер главы',
        related_name='comments',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    page_number_by_2012 = models.PositiveIntegerField(
        verbose_name='Нумерация глав в старом издании'
    )
    page_number_by_2021 = models.PositiveIntegerField(
        verbose_name='Нумерация глав в новом издании'
    )
    sort = models.PositiveBigIntegerField(
        verbose_name='Сортировка',
        null=True,
        blank=True
    )
    author = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.CASCADE,
        related_name='comments'
    )

    class Meta:
        ordering = ('page_number_by_2012', 'sort')
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        db_table = 'comments'

    @property
    def short_text(self):
        return truncatechars(self.comment_text, 100)

    def __str__(self) -> str:
        return self.name


class CommentLink(BaseModel):
    """ Модель ссылок для комментариев. """

    link = models.URLField(
        verbose_name='Ссылка к комментарию',
        blank=True,
        null=True,
    )
    comment = models.ForeignKey(
        Comment,
        verbose_name='Комментарий',
        related_name='comments',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Ссылка к примечанию'
        verbose_name_plural = 'Ссылки к примечанию'
        db_table = 'comment_links'

    def __str__(self) -> str:
        return self.link


class TableChronology(BaseModel):
    """ Модель таблицы для определения хронологии. """

    date = models.CharField(
        max_length=50,
        verbose_name='Дата',
        blank=True,
        null=True
    )
    description = models.TextField(
        verbose_name='Событие',
        blank=True,
        null=True
    )
    sort = models.CharField(
        max_length=10,
        verbose_name='Сортировка'
    )

    class Meta:
        verbose_name = 'Строка таблицы хронологии'
        verbose_name_plural = 'Строки таблицы хронологии'
        db_table = 'chronologies'
        ordering = ('sort',)

    def __str__(self) -> str:
        return self.description


class Article(BaseNameModel):
    """ Модель статей. """
    text = RichTextField(
        'Текст статьи'
    )
    author = models.ForeignKey(
        User,
        verbose_name='Автор статьи',
        related_name='articles',
        on_delete=models.CASCADE
    )
    image = models.ImageField(
        'Картинка',
        blank=True,
        null=True,
        upload_to='articles/'
    )
    chapter = models.IntegerField(
        'Номер раздела'
    )
    create_at = models.DateTimeField(
        'Дата создания',
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        db_table = 'articles'

    def __str__(self):
        return self.text
