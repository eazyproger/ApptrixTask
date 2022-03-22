from rest_framework import serializers

from .models import CustomUser
from .app_funcrions import add_photo_watermark


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'first_name', 'second_name', 'avatar', 'gender']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            second_name=validated_data['second_name'],
            avatar=add_photo_watermark(validated_data['avatar'], validated_data['email']),
            gender=validated_data['gender'],
        )
        user.set_password(validated_data['password'])
        user.save()

        return user
