from client import AbstractClient


class MockClient(AbstractClient):
    _DIAGNOSTIC_MESSAGE = "AT#UD"
    TEST_DIAGNOSTIC_RESPONSE = "diagnostic_message"
    TEST_OTHER_RESPONSE = "other message"

    def __init__(self, override_online_status: bool = False):
        self.override_online_status = override_online_status
        self._online_status = False
        self._diagnostic_message_just_sent = False

    @property
    def online_status(self):
        if self.override_online_status:
            return False
        return self._online_status

    @property
    def diagnostic_message(self):
        return self._DIAGNOSTIC_MESSAGE

    def connect(self, telemetry_server_connection_string):
        self._online_status = True

    def disconnect(self):
        self._online_status = False

    def send(self, message):
        if message == self.diagnostic_message:
            self._diagnostic_message_just_sent = True
        else:
            self._diagnostic_message_just_sent = False

    def receive(self):
        if self._diagnostic_message_just_sent:
            # Simulate the reception of the diagnostic message
            message = self.TEST_DIAGNOSTIC_RESPONSE
            self._diagnostic_message_just_sent = False
        else:
            #  Simulate the reception of a response message returning a random message.
            message = self.TEST_OTHER_RESPONSE

        return message
