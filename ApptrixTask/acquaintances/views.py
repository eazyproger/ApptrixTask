from rest_framework.generics import CreateAPIView

from .models import CustomUser
from .serializers import CustomUserSerializer


class UserCreateView(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer