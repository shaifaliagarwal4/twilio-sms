from django.shortcuts import render

# Create your views here.
from django.conf import settings                                                                                                                                                       
from django.http import HttpResponse
from twilio.rest import Client


def broadcast_sms(request):
    message_to_broadcast = ("Hello, shaily happy to see you!!! "
                                                "yet? Grab it here: https://www.twilio.com/quest")
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    for recipient in settings.SMS_BROADCAST_TO_NUMBERS:
        if recipient:
            client.messages.create(to=recipient,
                                   from_=settings.TWILIO_NUMBER,
                                   body=message_to_broadcast)
    return HttpResponse("messages sent!", 200)
