from django.shortcuts import render
from .forms import NotificationForm
from django.core.mail import send_mail
from django.conf import settings
def index(request):
    form = NotificationForm(request.POST or None)
    context = {
        'form': form,
    }
    if form.is_valid():
        form.save()
        email = form.cleaned_data.get('email')
        number = form.cleaned_data.get('number')
        name = form.cleaned_data.get('name')
        surname = form.cleaned_data.get('surname')

        subject = 'Zgłoszenie klienta przez stronę'
        message = "Imię: {}, nazwisko: {}, email: {}, numer telefonu: {}".format(name, surname, email, number)

        send_mail(subject,
                  message,
                  settings.EMAIL_HOST_USER,
                  [settings.EMAIL_HOST_USER],
                  fail_silently=True)

    return render(request, 'main/home.html', context)
