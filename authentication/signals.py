from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group

from facebook.settings import APPLICANT_GROUP_NAME
from .models import UserProfile


def userprofile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name=APPLICANT_GROUP_NAME)
        instance.groups.add(group)
        UserProfile.objects.create(
            user=instance,

        )


post_save.connect(userprofile, sender=User)
