from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import AppointmentForm
from .models import Appointment
from twilio.rest import Client
import os

def index(request):
    return render(request, 'main/glav.html')

def omni(request):
    return render(request, 'main/omni.html')

def contact(request):
    return render(request, 'main/contact.html')

def ysligu(request):
    return render(request, 'main/ysligu.html')

def search(request):
    query = request.GET.get('q')
    results = Appointment.objects.filter(fullName__icontains=query)
    return render(request, 'search_results.html', {'results': results, 'query': query})

def privacy_policy(request):
    return render(request, 'main/privacy_policy.html')

def appointment_form(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment-success')
    else:
        form = AppointmentForm()
    return render(request, 'appointment_form.html', {'form': form})

def appointment_success(request):
    return render(request, 'appointment_success.html')

def approve_appointment(request, appointment_id):
    appointment = Appointment.objects.get(id=appointment_id)
    appointment.approved = True
    appointment.save()

    # Функция для отправки SMS
    #def send_sms(appointment):
        #account_sid = os.getenv('TWILIO_ACCOUNT_SID')
       # auth_token = os.getenv('TWILIO_AUTH_TOKEN')
        #twilio_number = os.getenv('TWILIO_PHONE_NUMBER')

       # client = Client(account_sid, auth_token)

       # message = f"Ваша запись на {appointment.appointmentDate} в {appointment.appointmentTime} на услугу {appointment.service} одобрена."

       # message = client.messages.create(
         #   body=message,
         #   from_=twilio_number,
         #   to=appointment.phoneNumber
       # )

       # print("SMS отправлено успешно.")

    # Вызов функции для отправки SMS
   # send_sms(appointment)

    #return redirect('admin_panel')

#def admin_panel(request):
    #appointments = Appointment.objects.all()
   # return render(request, 'admin_panel.html', {'appointments': appointments})

def submit_appointment(request):
    return HttpResponse("Форма записи на прием отправлена.")
