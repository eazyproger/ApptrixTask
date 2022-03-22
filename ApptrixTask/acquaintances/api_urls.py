from django.urls import path

from .views import UserCreateView

urlpatterns = [
    path('clients/create/', UserCreateView.as_view()),
]