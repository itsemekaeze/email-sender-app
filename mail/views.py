from django.shortcuts import render
from django.core.mail import EmailMessage, get_connection
from django.conf import settings
from django.contrib import messages

# Create your views here.


def send_email(request):
    try:
        if request.method == "POST":
            with get_connection(
                    host=settings.EMAIL_HOST,
                    port=settings.EMAIL_PORT,
                    username=settings.EMAIL_HOST_USER,
                    password=settings.EMAIL_HOST_PASSWORD,
                    use_tls=settings.EMAIL_USE_TLS
            ) as connection:
                subject = request.POST.get("subject")
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [request.POST.get("email"), ]
                message = request.POST.get("message")

                if EmailMessage(subject, message, email_from, recipient_list, connection=connection).send():
                    messages.info(request, 'Message was sent Successfully')
                else:
                    messages.error(request, 'Message was not sent ?')
    except:
        messages.error(request, 'Something went wrong')

    return render(request, 'home.html')
