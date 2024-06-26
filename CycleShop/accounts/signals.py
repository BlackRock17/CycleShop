from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from CycleShop.accounts.models import Profile

UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def created_profile(sender, instance, created, **kwargs):

    if not created:
        return

    Profile.objects.create(user=instance)
