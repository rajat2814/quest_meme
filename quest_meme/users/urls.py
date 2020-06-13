from django.conf.urls import url

from .views import CustomObtainAuthToken

urlpatterns = [
    url(r'^login/', CustomObtainAuthToken.as_view()),
]