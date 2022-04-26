class CustomeException(Exception):
    """
    This class is the base of custom exception which inherits Exception class
    """
    pass


class RequestError(CustomeException):
    """
    This is a custom exception error which you can raise when there is an error of connetion
    while using the requests library
    """
    pass
