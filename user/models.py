from django.db import models

# Create your models here.
import uuid

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from utils.mixins import TimeStampMixin
class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    preferred_name = models.CharField(max_length=250)


class Profile(TimeStampMixin):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_profile")