from django.shortcuts import render, HttpResponseRedirect
from products.models import Product
from coffeehouse.verify_request import verify_request
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.

@verify_request
def contact(request):
    """
    This function dsiplay the contact page which includes contact details
    """
    products = Product.objects.all()
    product_data = []
    product_url = [{'name':p.name} for p in products]
    cart_data = request.session['cart'] if 'cart' in request.session else {}
    has_item = True if len(cart_data)>0 else False
    request.session['data'] = product_url
    return render(request, 'contacts/contact.html', {'data':product_data,'cart':cart_data,'has_item':has_item})


@verify_request
@login_required
def send_message(request):
    """
    This function includes the code to send user request message to owner emails
    """
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        address = request.POST.get('address')
        message = request.POST.get('message')
        subject = 'User Query'
        email_from = request.user.email
        message = " Address: "+address+ " Message: " + message 

        recipient_list = [settings.EMAIL_HOST_USER]
        send_mail( subject, message, request.user.email, recipient_list )
        messages.info(request, "Message has been delivered successfully")
        return HttpResponseRedirect('/contact')

