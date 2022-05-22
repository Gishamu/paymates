import uuid
from django.conf import settings


def uuidGenerator():
    """
    this function is for generating and returning a
    uuid
    """
    txRef = str(uuid.uuid1())
    return txRef


def getToken():
    """
    getToken is the functtion that returns 
    public_key token wich is used for authorization when
    making requests
    """
    token = str(settings.PUBLIC_KEY)
    return token


def requestNeeds(url: str, customerName: str = "") -> dict:
    """
    requestNeeds returns a dictionary of url and headers.
    token value is the API key that set in the settings files of the project.
    searchValue is only passed when you are calling a transaction history for a single 
    person
    """
    token = getToken()
    setUrl = url
    headers = {'Content-type': 'application/json',
               'Authorization': f"Bearer {token}"}
    params = {
        "customer_fullname": customerName
    }

    return {
        'url': setUrl,
        'headers': headers,
        'params': params
    }
