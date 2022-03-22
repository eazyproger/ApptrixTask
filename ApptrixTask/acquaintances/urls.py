from django.urls import path, include

urlpatterns = [
    path('api/', include('acquaintances.api_urls')),
]