import unittest

from tire_pressure_monitoring import Alarm
from sensor import Sensor
from mock_sensor import MockSensor


class AlarmTest(unittest.TestCase):

    def test_alarm_is_off_by_default(self):
        sensor = Sensor()
        alarm = Alarm(sensor)
        assert not alarm.is_alarm_on

    def test_alarm_is_lower(self):
        sensor = MockSensor(10)
        alarm = Alarm(sensor)
        alarm.check()
        assert alarm.is_alarm_on

    def test_alarm_is_higher(self):
        sensor = MockSensor(30)
        alarm = Alarm(sensor)
        alarm.check()
        assert alarm.is_alarm_on
