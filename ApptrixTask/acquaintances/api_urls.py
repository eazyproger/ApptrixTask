from django.urls import path, include

from .views import UserCreateView, CreateMatchView

urlpatterns = [
    path('clients/create/', UserCreateView.as_view()),
    path('clients/<int:id>/match/', CreateMatchView.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]
