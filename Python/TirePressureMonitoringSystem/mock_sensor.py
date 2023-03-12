class MockSensor:
    def __init__(self, sensor_value: int):
        self.sensor_value = sensor_value

    def pop_next_pressure_psi_value(self):
        return self.sensor_value
