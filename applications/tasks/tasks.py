from celery import shared_task
from django.core.mail import send_mail
from time import sleep
from django.contrib.auth import get_user_model
from storeapp import settings
from applications.store.models import (
    Stores,
    Subscription
)


@shared_task
def sleepy(durations):
    sleep(durations)
    return None


@shared_task(bind=True)
def send_mail_func(self):
    list_email = []
    value = Stores.objects.count()

    for item in range(value):
        item = item + 1
        subscription = Subscription.objects.filter(store=item).values('user__email')

        for sub in subscription:
            list_email.append(sub['user__email'])

    list_email = list(dict.fromkeys(list_email)) 

    mail_subject = "Ofertas y descuentos"
    message = "Esta invitando a visitar nuestras tiendas para disfrutar de descuentos y ofertas que tenemos para usted."
    send_mail(
        subject = mail_subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=list_email,
        fail_silently=True,
    )
        
    return "Correo enviado."