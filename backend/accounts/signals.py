from django_rest_passwordreset.signals import reset_password_token_created
from django.dispatch import receiver
from accounts.tasks import  pword_reset_email
from django.urls import reverse



@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    firstname = reset_password_token.user.get_full_name()
    email = reset_password_token.user.email
    reset_password_url = "{}?token={}".format(
            instance.request.build_absolute_uri(reverse('password_reset:reset-password-confirm')),
            reset_password_token.key)
    print('password rest token create!')

    # send email with celery
    pword_reset_email.delay(firstname, email, reset_password_url)
