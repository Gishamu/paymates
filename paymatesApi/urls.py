from django.urls import path

from .views import Checker, Charge, ViewTransaction, Verification

urlpatterns = [
    path('', Checker.as_view()),
    path('charge', Charge.as_view()),
    path('transaction-history/<str:customerName>', ViewTransaction.as_view()),
    path('verify',Verification.as_view()),
]
