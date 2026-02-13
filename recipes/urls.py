from django.urls import path
from recipes.views import view

urlpatterns = [
    path('',view)
]