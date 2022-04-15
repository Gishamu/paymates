import uuid
from paymets.settings import PAYMET_API_KEY


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
    paymet token with is used for authorization when
    making requests
    """
    token = str(PAYMET_API_KEY)
    return token
