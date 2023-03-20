"""Store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls')),
]

# При создании сайта, был создан файл сопоставления URL (urls.py) в корне проекта.
# Хотя можно использовать его для обработки всех URL адресов, более
# целесообразно подключать отдельные файлы сопоставлений для каждого приложения.

# URL соотношения хранятся в переменной urlpatterns, которая является списком функций path().
# Каждая path() функция или ассоциирует шаблон URL_ с контроллером(views) или же его с другим
# таким списком (во втором случае, первый URL становится "базовым" для других, которые определяются
# в дочернем списке). Список urlpatterns инициализирует список функции, которая, например,
# соотносит _admin/ с модулем admin.site.urls , который содержит собственный файл-соотноситель.


from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# Django не размещает статические файлы(CSS, JavaScript, и изображения) по умолчанию,
# и это крайне полезно на этапе разработки нашего сайта.