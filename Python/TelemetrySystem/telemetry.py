from client import AbstractClient


class TelemetryDiagnostics:
    DIAGNOSTIC_CHANNEL_CONNECTION_STRING = "*111#"

    def __init__(self, client: AbstractClient):
        self._telemetry_client = client
        self.diagnostic_info = ""

    def check_transmission(self, client_message: str):
        self.diagnostic_info = ""
        self._telemetry_client.disconnect()

        self._telemetry_client.connect(self.DIAGNOSTIC_CHANNEL_CONNECTION_STRING)

        self.diagnostic_info = self._telemetry_client.send(client_message)
