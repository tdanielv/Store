from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Book, BookInstance, Author, Genre, Language

def index(request):
    # Первая часть функции отображения получает количество записей при помощи вызова функции objects.all()
    # у атрибута objects, доступного для всех классов моделей.
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count() # Метод 'all()' применён по умолчанию.
    num_genre = Genre.objects.count()
    num_authors_den = Author.objects.filter(first_name='Дэн').count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genre': num_genre,
        'num_author_den': num_authors_den
    }
    # render() - функцию, которая генерирует HTML-файлы при помощи шаблонов страниц
    # и соответствующих данных.
    return render(request,'index.html', context)

# Поскольку обобщённый класс уже реализует большую часть того, что нам нужно,
# и следуя лучшим практикам Django, мы сможем создать более эффективный список
# при помощи меньшего количества кода, меньшего количества повторений и гораздо лучшей поддержкой
class BookListView(generic.ListView):
    #  Обобщённое отображение выполнит запрос к базе данных, получит все записи заданной модели (Book),
    #  затем отрендерит (отрисует) соответствующий шаблон
    model = Book
    context_object_name = 'my_book_list' # ваше собственное имя переменной контекста в шаблоне
    # queryset = Book.objects.filter(title__icontains='а')[:5]# Получение 5 книг, содержащих слово 'a' в заголовке
    template_name = 'book_list.html'  # Определение имени вашего шаблона и его расположения

    # мы можем переопределить метод получения списка всех записей get_queryset().
    # Данный подход является более гибким, чем использование атрибута queryset,
    # как мы сделали в предыдущем фрагменте кода (хотя, в данном случае и нет никакой разницы):

    # def get_queryset(self):
    #     return Book.objects.filter(title__icontains='а')[:5]# Получение 5 книг, содержащих слово 'a' в заголовке

    # В первую очередь - получить существующий контекст из нашего суперкласса.
    # Затем добавить в контекст новую информацию.
    # Затем вернуть новый (обновлённый) контекст.
    def get_context_data(self, *, object_list=None, **kwargs):
        # В первую очередь получаем базовую реализацию контекста
        context = super(BookListView, self).get_context_data(**kwargs)
        print(context)
        context['some_data'] = 'This si adding data'
        return context

# class BookDetailView(generic.ListView):
#     model = Book
#     queryset = Book.objects.filter(title__icontains='а')[:5]
#     template_name = 'book_detail.html'
#     context_object_name = 'book'
#
#     def get_queryset(self):
#         print(self.id)
#         return Book.objects.all()

def detail(request, id):
    book = get_object_or_404(Book, pk=id)
    return render(request, 'book_detail.html', {'book':book})


