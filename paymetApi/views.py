from django.shortcuts import render

import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed


class Checker(APIView):
    def get(self, requests):
        return Response("When you see this message that means that you have installed me successfuly")
