from django.urls import path

from .views import ItemView, BuyItemView, SuccessView, CancelView, IndexView


urlpatterns = [
    path("item/<pk>/", ItemView.as_view(), name="item"),
    path("buy/<pk>/", BuyItemView.as_view(), name="buy"),
    path("success/", SuccessView.as_view(), name="success"),
    path("cancel/", CancelView.as_view(), name="cancel"),
]
