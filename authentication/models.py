from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db.models import CASCADE


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile',on_delete=CASCADE)
    calle = models.CharField(max_length=255,null=True)
    num_ext = models.PositiveIntegerField(null=True)
    num_int = models.PositiveIntegerField(null=True)
    phone_num = models.PositiveIntegerField(null=True)


    def __str__(self):
        return  self.user.username

    class Meta:
        verbose_name = 'Perfil de Usuario'
        verbose_name_plural = 'Perfiles de Usuario'

