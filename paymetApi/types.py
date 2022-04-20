from .utils import uuidGenerator

class ChargeBody:
    """
    ChargeBody class takes in arguments of data and creates 
    an object out the passed data. the object created is for 
    the charge end point to be sent.
    """

    def __init__(self, amount: str, currency: str, phone_number: str,
                 email: str, fullName: str, network: str, redirect_url: str,
                 description: str) -> None:
        # Asign to self object
        self.amount = amount
        self.currency = currency
        self.phone_number = phone_number
        self.email = email
        self.tx_ref = uuidGenerator()
        self.fullName = fullName
        self.network = network
        self.redirect_url = redirect_url
        self.description = description

    def chargeBodyObject(self) -> dict:
        return {
            "amount": self.amount,
            "currency": self.currency,
            "phone_number": self.phone_number,
            "email": self.email,
            "tx_ref": self.tx_ref,
            "fullName": self.fullName,
            "network": self.network,
            "redirect_url": self.redirect_url,
            "description": self.description
        }



