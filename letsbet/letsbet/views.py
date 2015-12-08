from django.http import HttpResponse
from django.shortcuts import render
from django.core.urlresolvers import reverse
from paypal.standard.forms import PayPalPaymentsForm
from csgorox.settings import PAYPAL_RECEIVER_EMAIL
from django.conf import settings

def index(request):
    return render(request, 'index.html')

def forms(request):
    return render(request, 'forms.html')