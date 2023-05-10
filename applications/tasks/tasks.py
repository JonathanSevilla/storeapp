from celery import shared_task
from django.core.mail import send_mail
from time import sleep


@shared_task
def sleepy(durations):
    sleep(durations)
    return None


@shared_task
def send_email(subject, message, recipient_list):
    send_mail(subject, message, 'your_email@example.com', recipient_list, fail_silently=False)
