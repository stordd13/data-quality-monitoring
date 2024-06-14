from datetime import datetime
from src.sensor import Sensor
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import logging



app = FastAPI()

@app.get("/visit_count/")
def visit(year: int, month: int, day: int, hour: int)-> int:
    
    sensor = Sensor(250,50)
    business_date = datetime(year, month, day, hour)

    return sensor.get_visit_count(business_date)



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)