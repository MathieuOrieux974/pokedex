

from django.urls import path

from api import views

urlpatterns = [
    path('',views.main,name='main')
]
