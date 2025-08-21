"""
URL configuration for datebase_demo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path,include

from book import views
from article import urls
from orm_demo import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('book_add',views.add_book),
    path('read_book',views.read_book),
    path('put_book',views.update_book),
    path('del_book',views.del_book),
    path('article/',include('article.urls')),
    path('orm/',include('orm_demo.urls'))

]
