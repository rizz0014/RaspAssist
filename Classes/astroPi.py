class Sensor:
    def __init__(self, name, data):
        self.name = name
        self.data = data


class Temperature(Sensor):
    def get_temp(self):
        return self.data


class Pressure(Sensor):
    def get_pressure(self):
        return self.data


class Humidity(Sensor):
    def get_humidity(self):
        return self.data
