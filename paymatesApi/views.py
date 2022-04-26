from urllib.parse import parse_qs, urlparse
from django.shortcuts import render
import requests
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import status
from .utils import requestNeeds
from .serializers import ChargeBodySerializer
from .types import ChargeBody
from .errors import RequestError


class Checker(APIView):
    """
    Checker class makes a get request which returns a welcome test to show you
    that you have succefuly installed the app to your project.
    """

    def get(self, requests):
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
                          request.data['redirect_url'],# the redirect_url is the webhook url
                          request.data['description']
                          )
        serializer = ChargeBodySerializer(data.chargeBodyObject())
        jsonBody = json.dumps(serializer.data)

        sender = requests.post(
            url=f"{requestInfo['url']}", data=jsonBody, headers=dict(requestInfo['headers']))

        data = sender.json()
        if data['status'] != "success":
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data)


class ViewTransaction(APIView):
    """
    This class is responsible for view sepcific 
    """

    def get(self, request, customerName: str):
        requestInfo = requestNeeds(
            "https://api.flutterwave.com/v3/transactions", customerName)

        responseData = requests.get(
            url=requestInfo['url'], params=dict(requestInfo['params']), headers=dict(requestInfo['headers']))

        try:
            if not responseData.ok:
                raise RequestError
        except RequestError:
            return Response({"error": "error happened from flutterwave"})

        response = Response()
        response.data = responseData.json()
        return response


class Verification(APIView):
    """
    Verification class acts as a webhook which recieves response of a transaction made.
    It verifies if the transaction is done successfuly or not.
    It returns a dictionary of data and verification status where data is a dictionary 
    of data returned and verification status is a bolean 
    """

    def get(self, request):
        verificationStatus = False
        url = request.build_absolute_uri()
        parsed_url = urlparse(url)
        captured_value = parse_qs(parsed_url.query)['resp'][0]
        data = json.loads(captured_value)
        if data["status"] == "success":
            if data["data"]["status"] == "successful":
                verificationStatus = True
            return Response({"verificationStatus": verificationStatus, "data": data}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
