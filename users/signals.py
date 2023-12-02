from django.db.models.signals import post_save, post_delete #Signal Db
from django.dispatch import receiver #decorator

from django.contrib.auth.models import User
from .models import Profile

# Signal funtion:
#Creating
@receiver(post_save, sender=User)
def createProfile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(
            user=instance,
            username=instance.username,
            email=instance.email,
            name=instance.first_name,
        )


#Deleting
def deleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()


post_save.connect(createProfile, sender=User)
post_delete.connect(deleteUser, sender=Profile)