from django.urls import path

from .views import Checker

urlpatterns =[
  path('',Checker.as_view())
]