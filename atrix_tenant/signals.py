from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile


@receiver(post_save, sender=User)
def new_user(sender, **kwargs):
    """
    Criamos um perfil quando se cria um usuario
    """
    if kwargs.get('created', False):
        tenantprofile = Profile()
        tenantprofile.user = kwargs.get("instance")
        tenantprofile.save()


@receiver(post_delete, sender=Profile)
def delete_userprofile(sender, **kwargs):
    """
    Eliminamos um usuario vinculado a um perfil
    """
    tenantprofile = kwargs.get("instance")
    user = tenantprofile.user
    user.delete()
