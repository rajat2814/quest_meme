from quest_meme.common.models import BaseModel

from django.db import models
from django.contrib.auth.models import User

class CookieInformation(BaseModel):

    user    = models.ForeignKey(User, on_delete=models.CASCADE)
    consent = models.BooleanField(default=False)

    def __str__(self):
        return '{0}'.format(self.user)
