from django.urls import path

from .views import Checker, Charge, ViewTransaction

urlpatterns = [
    path('', Checker.as_view()),
    path('charge', Charge.as_view()),
    path('transaction-history/<str:customerName>', ViewTransaction.as_view())
]
