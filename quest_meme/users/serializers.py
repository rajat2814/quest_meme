from rest_framework import serializers
from django.contrib.auth.models import User

from .models import CookieInformation


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email',)

class CookieSerializer(serializers.ModelSerializer):

    user = UserSerializer()

    class Meta:
        model = CookieInformation
        fields = ('user', 'consent',)