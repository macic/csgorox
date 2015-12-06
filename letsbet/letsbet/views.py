from django.http import HttpResponse
from django.shortcuts import render
from django.core.urlresolvers import reverse
from paypal.standard.forms import PayPalPaymentsForm
from csgorox.settings import PAYPAL_RECEIVER_EMAIL

def index(request):
    return HttpResponse("Hello, world. You're at the csgorox.com index.")



def view_that_asks_for_money(request):

    # What you want the button to do.
    paypal_dict = {
        "business": PAYPAL_RECEIVER_EMAIL,
        "amount": "1.00",
        "item_name": "name of the item",
        "invoice": "unique-invoice-id",
        "notify_url": "https://www.example.com" + reverse('paypal-ipn'),
        "return_url": "https://www.example.com/your-return-location/",
        "cancel_return": "https://www.example.com/your-cancel-location/",
        "custom": "Upgrade all users!",  # Custom command to correlate to some function later (optional)
    }

    # Create the instance.
    form = PayPalPaymentsForm(button_type=PayPalPaymentsForm.DONATE, initial=paypal_dict)
    context = {"form": form}
    return render(request, "payment.html", context)