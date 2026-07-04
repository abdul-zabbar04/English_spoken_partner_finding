from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.users.models import User
from apps.profiles.models import Profile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Automatically create a profile
    when a new user is created.
    """

    if not created:
        return

    display_name = instance.email.split("@")[0]

    Profile.objects.create(
        user=instance,
        display_name=display_name,
    )