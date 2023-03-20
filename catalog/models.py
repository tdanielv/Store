import uuid

from django.db import models

# мы создали жанр как модель, а не как свободный текст или список
# выбора, чтобы возможные значения могли управляться
# через базу данных, а не были закодированными.
from django.urls import reverse


class Genre(models.Model):
    name = models.CharField(max_length=100, help_text='Genre name')
    # Вы можете объявить метаданные на уровне модели для своей модели, объявив класс Meta
    class Meta:
        # подробное имя для класса в единственной и множественной форме
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(verbose_name='birth')
    date_of_death = models.DateField(verbose_name='death', null=True, blank=True)

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def get_absolute_url(self):
        return reverse('author_detail', kwargs={'author_id': str(self.id)})

    def __str__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)

# Модель книги представляет всю информацию о доступной книге
# в общем смысле, но не конкретный физический «экземпляр»
# или «копию» для временного использования
class Book(models.Model):
    title = models.CharField(max_length=100, help_text='Book title')
    # Foreign Key used because book can only have one author,
    # but authors can have multiple books
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField( help_text='Book description')
    isbn = models.CharField('ISBN',max_length=100, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    # ManyToManyField used because genre can contain many books. Books can cover many genres.
    genre = models.ManyToManyField('Genre', help_text='Select a genre')
    language = models.ForeignKey('Language', on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def get_absolute_url(self):
        return reverse('book_detail', kwargs={'book_id': self.id})

    def __str__(self):
        return self.title

    def display_genre(self):
        # создаётся строка из первых трёх значений поля genre (если они существуют)
        # и short_description, которое может быть использовано в админ-панели как название.
        return ', '.join([genre.name for genre in self.genre.all()[:3]])
    display_genre.short_description='Genre'

class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular book across whole library')
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    due_back = models.DateField(verbose_name='date', null=True, blank=True, help_text='Когда будет возвращена если взята наруки')
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)
    LOAN_STATUS = (
        ('m', 'На тех обслуживании'),
        ('o', 'На руках'),
        ('a', 'Доступна'),
        ('r', 'Зарезервирована'),
    )
    status = models.CharField(choices=LOAN_STATUS, max_length=1, blank=True, default='m', help_text='Book availability')

    def __str__(self):
        return '{0} : {1} : {2}'.format(self.book.title, self.id, self.status)

    class Meta:
        ordering = ['due_back']
        verbose_name = 'Экземпляр книги'
        verbose_name_plural = 'Экземпляры книг'


class Language(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Язык'
        verbose_name_plural = 'Языки'

