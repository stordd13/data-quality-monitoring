from datetime import date, timedelta, datetime
import sys
import numpy as np

class Sensor:
    def __init__(self, 
    avg_visit : int,
    std_visit : int,
    perc_break: float = 0.015,
    perc_malfunction: float = 0.035) -> None:

        self.avg_visit = avg_visit
        self.std_visit = std_visit
        self.perc_break = perc_break
        self.perc_malfunction = perc_malfunction

    def simulate_sensor_count(self, business_date: date) -> int:

        seed = business_date.toordinal() * 24 + business_date.hour
        np.random.seed(seed)

        weekday = business_date.weekday()
        hour = business_date.hour

        if weekday == 6: # sunday
            visit = -1

        else:
            if 8 <= hour < 20:
                visit = np.random.normal(self.avg_visit / 11, self.std_visit / 11)
            else: #night hours
                visit = 0

        return int(np.floor(visit))

    def get_visit_count(self, business_date:date) -> int:

        # seed = business_date.toordinal() * 24 + business_date.hour 
        proba = np.random.random()
        print(proba)

        if proba < self.perc_break:
            return 0

        if proba < self.perc_malfunction:
            return np.random.choice([-100, 100])
        
        return self.simulate_sensor_count(business_date)



if __name__ == "__main__":
    if len(sys.argv) > 1:
        year, month, day, hour = [int(v) for v in sys.argv[1].split("-")]
    else:
        year, month, day, hour = 2023, 6, 14, 15
    queried_date = datetime(year, month, day, hour)
    sensor = Sensor(240,50)
    print(sensor.get_visit_count(queried_date))