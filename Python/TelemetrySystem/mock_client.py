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
        return self._online_status

    @property
    def diagnostic_message(self):
        return self._DIAGNOSTIC_MESSAGE

    def connect(self, telemetry_server_connection_string):
        if self.override_online_status:
            raise Exception("Unable to connect.")
        self._online_status = True

    def disconnect(self):
        self._online_status = False

    def send(self, telemetry_message):
        if telemetry_message == self.diagnostic_message:
            # Simulate the reception of the diagnostic message
            message = self.TEST_DIAGNOSTIC_RESPONSE
            self._diagnostic_message_just_sent = False
        else:
            message = self.TEST_OTHER_RESPONSE

        return message
