from client import AbstractClient


class TelemetryDiagnostics:
    DIAGNOSTIC_CHANNEL_CONNECTION_STRING = "*111#"

    def __init__(self, client: AbstractClient, retries: int = 3):
        self.retries = retries
        self._telemetry_client = client
        self.diagnostic_info = ""

    def check_transmission(self, client_message: str):
        self.diagnostic_info = ""
        self._telemetry_client.disconnect()

        retry_left = self.retries
        while not self._telemetry_client.online_status and retry_left > 0:
            self._telemetry_client.connect(self.DIAGNOSTIC_CHANNEL_CONNECTION_STRING)
            retry_left -= 1

        if not self._telemetry_client.online_status:
            raise Exception("Unable to connect.")

        self._telemetry_client.send(client_message)
        self.diagnostic_info = self._telemetry_client.receive()
