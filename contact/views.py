from django.shortcuts import render
from .models import ContactDetails


def send_mail(request):
    contact_details = ContactDetails.objects.last()
    template = 'contact/contact.html'
    context = {
        'contact_details': contact_details
    }
    return render(request, template, context)


def success(request):
    pass
