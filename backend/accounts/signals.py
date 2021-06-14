from django_rest_passwordreset.signals import reset_password_token_created
from django.dispatch import receiver


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    print('password rest token create!')