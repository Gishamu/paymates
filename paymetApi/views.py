from django.shortcuts import render
import requests
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .utils import requestNeeds
from .serializers import ChargeBodySerializer
from .types import ChargeBody


class Checker(APIView):
    def get(self, requests):
        """
        Checker class makes a get request which returns a welcome test to show you
        that you have succefuly installed the app to your project.

        """
        return Response("When you see this message that means that you have installed me successfuly")


class Charge(APIView):
    """
    Charge is a class that sends a post request to flutterwave
    API to charge money from users using mobile money uganda
    """

    def post(self, request):
        requestInfo = requestNeeds(
            "https://api.flutterwave.com/v3/charges?type=mobile_money_uganda")

        data = ChargeBody(request.data['amount'],
                          request.data['currency'],
                          request.data['phoneNumber'],
                          request.data['email'],
                          request.data['fullName'],
                          request.data['network'],
                          request.data['redirect_url'],
                          request.data['description']
                          )
        serializer = ChargeBodySerializer(data.chargeBodyObject())
        jsonBody = json.dumps(serializer.data)

        sender = requests.post(
            url=f"{requestInfo['url']}", data=jsonBody, headers=dict(requestInfo['headers']))
        response = Response()
        response.data = sender.json()
        return response


class ViewTransaction(APIView):
    """
    This class is responsible for view sepcific 
    """

    def get(self, request, customerName: str):
        requestInfo = requestNeeds(
            "https://api.flutterwave.com/v3/transactions", customerName)

        responseData = requests.get(
            url=requestInfo['url'], params=dict(requestInfo['params']), headers=dict(requestInfo['headers']))
        response = Response()
        response.data = responseData.json()
        return response
