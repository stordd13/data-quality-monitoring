from datetime import date, timedelta
import sys
import numpy as np

class Sensor:
    def __init__(self, 
    avg_visit : int,
    std_visit : int) -> None:
        self.avg_visit = avg_visit
        self.std_visit = std_visit

    def simulate_sensor_count(self, business_date: date) -> int:

        np.random.seed(seed=date.toordinal())

        weekday = business_datete.weekday()
        hour = business_date.hour()

        visit = np.random.normal(self.avg_visit, self.std_visit)

        if weekday == 6:
            visit = -1
        else:
            if 8 <= hour <= 19:
                visit *= np.random(1,2)*visit

        return np.floor(visit)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        year, month, day, hour = [int(v) for v in sys.argv[1].split("-")]
    else:
        year, month, day = 2023, 10, 25
    queried_date = date(year, month, day, hour)
    sensor = Sensor(50,3)
    print(sensor.simulate_sensor_count())