from rest_framework import serializers


class ChargeBodySerializer(serializers.Serializer):
    """
    This class serializes the body data that is to be sent in the request 
    for charge end point
    """
    amount = serializers.CharField(max_length="255")
    currency = serializers.CharField(max_length="255")
    phone_number = serializers.CharField(max_length="255")
    email = serializers.CharField(max_length="255")
    tx_ref = serializers.CharField(max_length="255")
    fullName = serializers.CharField(max_length="255")
    network = serializers.CharField(max_length="255")
    redirect_url = serializers.CharField(max_length="255")
    description = serializers.CharField(max_length="255")
