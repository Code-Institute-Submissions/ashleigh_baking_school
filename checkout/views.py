from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'

    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51GqFouGGfwZ2oiZgdCM3aLmpaPtvWKpci7fyOStICBvZKx1bTtlduXmAxtGhRYs1EJLt3sTTdBmeJh3iDRBkkZvd00azX7pGoI',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)