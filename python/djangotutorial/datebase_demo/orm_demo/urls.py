from django.urls import utils,path

from . import views

urlpatterns=[
    path('select',views.read_user)
]
