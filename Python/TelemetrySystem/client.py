import random
from abc import ABC, abstractmethod


class AbstractClient(ABC):
    @property
    @abstractmethod
    def online_status(self):
        pass

    @property
    @abstractmethod
    def diagnostic_message(self):
        pass

    @abstractmethod
    def connect(self, telemetry_server_connection_string: str):
        pass

    @abstractmethod
    def disconnect(self):
        pass

    @abstractmethod
    def send(self, telemetry_message: str):
        pass


class TelemetryClient(AbstractClient):
    # The communication with the server is simulated in this implementation.
    # Because the focus of the exercise is on the other class.
    _MESSAGE = """\
LAST TX rate................ 100 MBPS\r\n
HIGHEST TX rate............. 100 MBPS\r\n
LAST RX rate................ 100 MBPS\r\n
HIGHEST RX rate............. 100 MBPS\r\n
BIT RATE.................... 100000000\r\n
WORD LEN.................... 16\r\n
WORD/FRAME.................. 511\r\n
BITS/FRAME.................. 8192\r\n
MODULATION TYPE............. PCM/FM\r\n
TX Digital Los.............. 0.75\r\n
RX Digital Los.............. 0.10\r\n
BEP Test.................... -5\r\n
Local Rtrn Count............ 00\r\n
Remote Rtrn Count........... 00"""
    _DIAGNOSTIC_MESSAGE = "AT#UD"

    def __init__(self, retries: int = 3):
        self.retries = retries
        self._online_status = False

    @property
    def online_status(self):
        return self._online_status

    @property
    def diagnostic_message(self):
        return self._DIAGNOSTIC_MESSAGE

    def connect(self, telemetry_server_connection_string):
        if telemetry_server_connection_string is None or telemetry_server_connection_string == "":
            raise Exception()

        retry_left = self.retries
        while not self.online_status and retry_left > 0:
            # Fake the connection with 20% chances of success
            success = random.randint(1, 10) <= 2
            self._online_status = success
            retry_left -= 1

        if not self.online_status:
            raise Exception("Unable to connect.")

    def disconnect(self):
        self._online_status = False

    def send(self, telemetry_message):
        if telemetry_message is None or telemetry_message == "":
            raise Exception()

        # The simulation of Send() actually just remember if the last message sent was a diagnostic message.
        # This information will be used to simulate the Receive(). Indeed there is no real server listening.
        if telemetry_message == self.diagnostic_message:
            # Simulate the reception of the diagnostic message
            message = self._MESSAGE
        else:
            #  Simulate the reception of a response message returning a random message.
            message = ""
            message_length = random.randint(0, 50) + 60
            while message_length >= 0:
                message += chr((random.randint(0, 40) + 86))
                message_length -= 1

        return message
