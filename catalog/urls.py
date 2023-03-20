from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path, include
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    # path('', RedirectView.as_view(url='/catalog/', permanent=True)),
# определяем параметр name, который уникально определяет это частное URL-преобразование.
    # Вы можете использовать данное имя для "обратного" ("reverse") преобразования — то есть,
    # для динамического создания URL-адреса, указывающего на ресурс, на которое указывает данное преобразование
    path('', views.index, name='index'),
    # Данный паттерн РВ сопоставления URL-адреса полностью соответствует строке books/
    # (^ является маркером начала строки, а $ - маркер конца строки).
    path('books/', views.BookListView.as_view(), name='books'),
    # Данное РВ сопоставляет любой URL-адрес, который начинается с book/, за которым до конца строки
    # (до маркера конца строки - $) следуют одна, или более цифр. В процессе выполнения данного преобразования,
    # оно "захватывает" цифры и передаёт их в функцию отображения как параметр с именем pk.
    path('book/<int:id>', views.detail, name='book_detail')
    # path('book/<int:id>/', views.BookDetailView.as_view(), name='book_detail'),

]
# специальная функция (RedirectView), которая принимает первым параметром новый относительный URL
# на который следует перенаправлять (/catalog/) когда указанный в функции url() адрес
# соотносится с адресом запроса (корневой URL, в данном случае)


