import unittest

from telemetry import TelemetryDiagnostics
from mock_client import MockClient


class TelemetryDiagnosticControlsTest(unittest.TestCase):
    def test_check_transmission_diagnostic_message(self):
        client = MockClient()
        diagnostics = TelemetryDiagnostics(client)
        diagnostics.check_transmission(client.diagnostic_message)
        self.assertEqual(client.TEST_DIAGNOSTIC_RESPONSE, diagnostics.diagnostic_info)

    def test_check_transmission_other_message(self):
        client = MockClient()
        diagnostics = TelemetryDiagnostics(client)
        diagnostics.check_transmission('test')
        self.assertEqual(client.TEST_OTHER_RESPONSE, diagnostics.diagnostic_info)

    def test_check_transmission_offline(self):
        client = MockClient(override_online_status=True)
        diagnostics = TelemetryDiagnostics(client)
        with self.assertRaises(Exception) as context:
            diagnostics.check_transmission('test')

        self.assertEqual("Unable to connect.", str(context.exception))


if __name__ == "__main__":
    unittest.main()
