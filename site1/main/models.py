# models.py

from django.db import models
from twilio.rest import Client

class Appointment(models.Model):
    fullName = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=15)
    appointmentDate = models.DateField()
    appointmentTime = models.TimeField()
    service = models.CharField(max_length=100)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.fullName

    def send_sms(self):
        # Здесь вы можете добавить вашу логику для отправки SMS
        # Например, использовать Twilio для отправки SMS
        # Пример отправки SMS с использованием Twilio:
        account_sid = 'AC3d57c8c7d66679836b032d15da52172e'
        auth_token = '1d9028c1a49f5398ec400056c065ce28'
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body=f"Ваша запись на {self.appointmentDate} в {self.appointmentTime} на услугу {self.service} одобрена.",
            from_='YOUR_TWILIO_NUMBER',
            to=self.phoneNumber
        )

