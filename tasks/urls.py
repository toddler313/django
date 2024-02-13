from django.urls import path
from . import views

app_name = "tasks"
urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.index, name='index'),
    path('add', views.addTask, name='add')
]