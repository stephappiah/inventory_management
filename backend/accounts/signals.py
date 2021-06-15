from django_rest_passwordreset.signals import reset_password_token_created
from django.dispatch import receiver
from .tasks import pword_reset_email


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    print('password rest token create!')

    # send email with celery
    pword_reset_email(
        sender_cls=sender, 
        view_instance=instance, 
        rst_pword_token=reset_password_token
        )