from django.contrib import admin

from .models import Author, BookInstance, Language, Book, Genre

class BookInLine(admin.TabularInline):
    model = Book
    extra = 0
# Для изменения отображения модели в пользовательском интерфейсе
# админ-панели, необходимо определить класс ModelAdmin
# (он описывает расположение элементов интерфейса,
# где Model - наименование модели) и зарегистрировать
# его для использования с этой моделью.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):

    # Чтобы различить их или просто отобразить более интересную информацию о каждом авторе,
    # можно использовать list_display
    list_display = ('first_name', 'last_name', 'date_of_birth', 'date_of_death')

    # Атрибут полей перечисляет только те поля, которые должны
    # отображаться в форме, по порядку. Поля отображаются по
    # вертикали по умолчанию, но будут отображаться горизонтально,
    # если вы дополнительно группируете их в кортеже
    # (как показано в полях «date» ниже).
    fields = ('first_name', 'last_name', ('date_of_birth', 'date_of_death'))
    inlines = [BookInLine]
# admin.site.register(Author, AuthorAdmin)


admin.site.register(Language)

# В этот раз для создания и регистрации новых моделей используем декоратор @register
# (он делает то же самое, что и метод admin.site.register()):
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'id', 'due_back')
    list_filter = ('status', 'due_back')

    # Мы можем добавить строки в разные секции, добавив текст жирным шрифтом в
    # нашу маодель в админпанели.Каждая секция имеет свой заголовок (или None,
    # если заголовок не нужен) и ассоциированный кортеж полей в словаре
    fieldsets = (
         (None, {
             'fields': ('book', 'language', 'id')
         }),
         ('Доступность', {
             'fields': ('status', 'due_back')
         }),
    )
# admin.site.register(BookInstance)
# возможность добавлять связанные записи одновременно.
class BookInstanceInLine(admin.TabularInline):
    # объявили наш встроенный класс tablular, который
    # просто добавляет все поля из встроенной модели.
    model = BookInstance
    # Чтобы  НЕ иметь лишних экземпляров книг по умолчанию и
    # просто добавить их с помощью ссылки Add another Book instance
    extra = 0

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Вместо этого мы определим функцию display_genre в models.py
    # для получения строкового представления информации
    list_display = ('title', 'author', 'language', 'display_genre')
    # возможность добавлять связанные записи одновременно.
    inlines = [BookInstanceInLine]
# admin.site.register(Book)


# Это самый простой способ регистрации модели или моделей.
admin.site.register(Genre)
