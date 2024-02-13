from django.urls import path

from . import views # from . means from the current directory

urlpatterns = [
    path("", views.index, name="index"),
    path("brian", views.brian, name="brian"),
    path("<str:name>", views.greeting, name="greeting")
]