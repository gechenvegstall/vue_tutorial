from django.urls import path

from . import views

urlpatterns = [
    path("list/",views.movie_list),
    path("list/<name>",views.movie_list_query)
]
