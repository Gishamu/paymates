from django.urls import path

from .views import Checker, Charge

urlpatterns = [
    path('', Checker.as_view()),
    path('charge', Charge.as_view())
]
