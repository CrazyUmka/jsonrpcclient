"""exceptions.py"""


class JsonRpcClientError(Exception):
    """Base class for the other exceptions"""
    pass


class InvalidRequest(JsonRpcClientError):
    """The request you're trying to send is not valid json."""

    def __init__(self):
        super().__init__('The request you\'re sending is not valid json')


class ConnectionError(JsonRpcClientError): # pylint: disable=redefined-builtin
    """There was a network issue, invalid HTTP response or timeout."""

    def __init__(self):
        super().__init__('Connection error')


class Non200Response(JsonRpcClientError):
    """The server responded with status code other than 200."""

    def __init__(self, status_code):
        super().__init__('Returned status code '+str(status_code))


class ParseResponseError(JsonRpcClientError):
    """Couldnt parse the json response."""

    def __init__(self):
        super().__init__('The response was not valid json')


class InvalidResponse(JsonRpcClientError):
    """The response didnt validate against the json-rpc response schema."""

    def __init__(self):
        super().__init__('The response was not a valid json-rpc 2.0 response')


class ReceivedNoResponse(JsonRpcClientError):
    """A response was expected, but none was given."""

    def __init__(self):
        super().__init__('No response was received')


class UnwantedResponse(JsonRpcClientError):
    """A response was not requested, but was given anyway."""

    def __init__(self):
        super().__init__('The response was not asked for')


class ReceivedErrorResponse(JsonRpcClientError):
    """The server responded with *error*."""

    def __init__(self, code, message): #pylint:disable=unused-argument
        super().__init__(message)
