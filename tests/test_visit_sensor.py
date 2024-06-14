import unittest
from datetime import date

from src.sensor import Sensor

class TestSensor(unittest.TestCase):
    
    def test_sunday_closed(self):
        for test_hour in range(1, 20):
            with self.subTest(i=test_hour):
                sensor = Sensor(550, 80)
                sensor_count = sensor.simulate_sensor_count(date(2023, 9, 17, test_hour))
                self.assertEqual(sensor_count,-1)

    def test_hour_open(self):
        for test_hour in range(8,20):
            with self.subTest(i=test_hour):
                sensor = Sensor(550, 80)
                sensor_count = sensor.simulate_sensor_count(date(2023, 9, 15, test_hour))
                self.assertFalse(sensor_count==-1)

    
    def test_at_night(self):
        for test_hour in range(1,24):
            if test_hour >=20 or test_hour<8:
                with self.subTest(i=test_hour):
                    sensor = Sensor(550, 80)
                    sensor_count = sensor.simulate_sensor_count(date(2023, 9, 15, test_hour))
                    self.assertFalse(sensor_count==-1)
    
    #def test_with_break(self):

    #def test_with_malf(self):


if __name__ == "__main__":
    unittest.main()