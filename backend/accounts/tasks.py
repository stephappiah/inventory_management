
from celery import shared_task
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.urls import reverse


# @shared_task
def pword_reset_email(sender_cls, view_instance, rst_pword_token):
    """
    Handles password reset tokens
    When a token is created, an e-mail needs to be sent to the user
    :param sender_cls: View Class that sent the signal
    :param view_instance: View Instance that sent the signal
    :param rst_pword_token: Token Model Object
    :param args:
    :param kwargs:
    :return:
    """
    
    # send an e-mail to the user


    current_user = rst_pword_token.user
    firstname = rst_pword_token.user.get_full_name()
    email = rst_pword_token.user.email
    reset_password_url = "{}?token={}".format(
            view_instance.request.build_absolute_uri(reverse('password_reset:reset-password-confirm')),
            rst_pword_token.key)

    print(current_user)
    print(firstname)
    print(email)
    print(reset_password_url)
    
    # send_mail(
    #     'Password Reset for Your Account',
    #     f'Hello {firstname}, click on the link below to change your password. Link -> {reset_password_url}',
    #     'from@example.com',
    #     ['to@example.com'],
    #     # fail_silently=False,
    # )
