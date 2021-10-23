from django.db.models.signals import post_delete, post_save
from authetifications.models import User
from users.models import Profile


def createProfile(sender, instance, created, **kwargs):
  if created:
    user = instance
    profile = Profile.objects.create(
      user = user,
      email = user.email,
      username = user.username,
    )

def deleteUser(sender, instance, **kwargs):
    try:
        user = instance.user
        user.delete()
    except:
        pass

post_save.connect(createProfile, sender=User)
post_delete.connect(deleteUser, sender=Profile)