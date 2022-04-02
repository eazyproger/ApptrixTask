from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response

from .app_funcrions import send_message
from .models import CustomUser, MatchModel
from .serializers import CustomUserSerializer, MatchSerializer


class UserCreateView(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class UserListView(ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['first_name', 'second_name', 'gender', ]


class CreateMatchView(CreateAPIView):
    queryset = MatchModel.objects.all()
    serializer_class = MatchSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def create(self, request, id, *args, **kwargs):
        first_email = CustomUser.objects.get(id=id).email
        if first_email:
            person_one_name = CustomUser.objects.get(id=id).first_name
            second_email = self.request.user.email
            person_two_name = self.request.user.first_name
            match = [match for match in self.get_queryset()
                     if (match.first_email == first_email and match.second_email == second_email)
                     or (match.first_email == second_email and match.second_email == first_email)]
            if match:
                send_message(first_email, person_two_name)
                send_message(second_email, person_one_name)
                return Response('Match! Message sent.')
            else:
                match = MatchModel(first_email=first_email, second_email=second_email)
                match.save()
                return Response('New match created.')
        else:
            return Response('err')
