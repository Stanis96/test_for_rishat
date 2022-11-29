import stripe

from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView, View

from rishat_app.settings import STRIPE_PUBLIC_KEY, STRIPE_SECRET_KEY
from .models import Item


stripe.api_key = STRIPE_SECRET_KEY
DOMAIN = "http://127.0.0.1:8000"


class ItemView(TemplateView):
    template_name = "payment_service/item.html"

    def get_context_data(self, **kwargs):
        context = super(ItemView, self).get_context_data(**kwargs)
        item = get_object_or_404(Item, pk=kwargs.get("pk"))
        context.update({"item": item, "stripe_public_key": STRIPE_PUBLIC_KEY})
        return context


class BuyItemView(View):
    def get(self, request, **kwargs):
        item = get_object_or_404(Item, pk=kwargs.get("pk"))
        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[
                {
                    "price_data": {
                        "currency": "usd",
                        "product_data": {
                            "name": item.name,
                        },
                        "unit_amount": item.price,
                    },
                    "quantity": 1,
                }
            ],
            metadata={"product_id": item.id},
            mode="payment",
            success_url=DOMAIN + "/success/",
            cancel_url=DOMAIN + "/cancel/",
        )
        return JsonResponse({"id": session.id})


class SuccessView(TemplateView):
    template_name = "payment_service/success.html"


class CancelView(TemplateView):
    template_name = "payment_service/cancel.html"
