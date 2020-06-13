import requests
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import *
from .models import *

class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()

    @action(detail=False, methods=['GET'])
    def user_details(self, request, *args, **kwargs):

        user_serializer = self.get_serializer(request.user, many=False)


        try:
            cookie_info = CookieInformation.objects.get(user=request.user)
            consent = cookie_info.consent
        except CookieInformation.DoesNotExist:
            consent = None


        return Response({'user_data': user_serializer.data, 'cookie_consent': consent})

    @action(detail=False, methods=['POST'])
    def logout(self, request, *args, **kwargs):

        return Response({
            'success': True
        })


class CookieViewSet(viewsets.ModelViewSet):

    serializer_class = CookieSerializer
    queryset = CookieInformation.objects.all()


    @action(detail=False, methods=['POST'])
    def consent(self, request, *args, **kwargs):

        data = request.data

        consent = data.get('consent', False)

        consent = True if consent == 'Y' else False

        try:

            cookie = CookieInformation.objects.get(user=request.user)
            cookie.consent = consent
            cookie.save()

        except CookieInformation.DoesNotExist:

            cookie_dict = {
                'user': request.user,
                'created_by': request.user,
                'modified_by': request.user,
                'consent': consent
            }

            CookieInformation.objects.create(**cookie_dict)

        return Response({
            'success': True,
            'data': data
        })


class MemeViewSet(viewsets.ViewSet):

    @action(detail=False, methods=['GET'])
    def get_memes(self, request, *args, **kwargs):

        try:
            r = requests.get('https://api.imgflip.com/get_memes')
            data = r.json()['data']['memes']
            return Response(data)
        except Excpection as e:
            return Response({
                    'success': False
                })
