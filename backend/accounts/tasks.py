
from celery.decorators import task
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.urls import reverse


@task(name="send reset email")
def pword_reset_email(firstname, email, reset_password_url):
    """
    Handles password reset tokens
    When a token is created, an e-mail needs to be sent to the user
    :param firstname: users firstname
    :param email: users email
    :param rst_password_url: Token Model Object
    :param args:
    :param kwargs:
    :return:
    """

    print('hey working!')
    
    # send an e-mail to the user

    
    send_mail(
        'Password Reset for Your Account',
        f'Hello {firstname}, click on the link below to change your password. Link -> {reset_password_url}',
        'from@example.com',
        ['to@example.com'],
        # fail_silently=False,
    )


