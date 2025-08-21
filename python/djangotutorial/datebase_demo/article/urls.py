from django.urls import utils,path

from . import views

urlpatterns = [
    path('last',views.article_test)

]