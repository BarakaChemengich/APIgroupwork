from django.shortcuts import render, redirect, get_object_or_404
from .models import Payment

def payment_form(request):
    if request.method == 'POST':
        # Get form data
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        amount = request.POST['amount']
        payment_method = request.POST['payment_method']

        # Save to database
        payment = Payment.objects.create(
            name=name,
            email=email,
            phone=phone,
            amount=amount,
            payment_method=payment_method
        )

        # Redirect with payment ID
        return redirect('payment_success', payment_id=payment.id)

    # GET request → show the form
    return render(request, 'payments/payment_form.html')


def payment_success(request, payment_id):
    # Retrieve the payment
    payment = get_object_or_404(Payment, id=payment_id)
    
    return render(request, 'payments/payment_success.html', {
        'payment': payment
    })
