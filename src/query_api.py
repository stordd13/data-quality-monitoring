import sys
import os
from datetime import date, datetime
import requests
import csv


#if __name__ == "_main__":

def validate_and_print_date(date_str):
    try : 

        year, month, day, hour = [int(v) for v in date_str.split("-")]
        date = datetime(year, month, day, hour)
        print("The provided date is:", date)

        return year, month, day, hour
    
    except ValueError:
        print("Error: The date format should be 'YYYY-MM-DD-HH'.")
        return None
    except IndexError:
        print("Error: Please provide all components of the date in the format 'YYYY-MM-DD-HH'.")
        return None  
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


def query_api(year,month,day,hour):
    url = "http://127.0.0.1:8000/visit_count/"
    params = {
        "year": year,
        "month": month,
        "day": day,
        "hour": hour
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status() # Raise an HTTPError for bad responses (4xx and 5xx)
        print("API response:", response.json())
        visitors = response.json()

        sensor_id = "sensor_8"
        store_id = "store_8"

        save_data(year, month, day, hour, visitors, sensor_id, store_id)
        add_unreliable_data(year, month, day, hour, visitors)

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while querying the API: {e}")

def add_unreliable_data(year, month, day, hour, visitors):

    sensor_id = None  # unreliable sensor_id
    store_id = "store_1"
    save_data(year, month, day, hour, visitors, sensor_id, store_id)

def save_data(year, month, day, hour, visitors, sensor_id, store_id):

    try:
        folder_path = "data/raw"
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        file_path = os.path.join(folder_path, f"{year}-{month}.csv")

        file_exists = os.path.isfile(file_path)

        with open(file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(["date", "heure", "nombre_de_visiteurs","id_capteur", "id_magasin"])

            date_str = f"{year}-{month}-{day}"
            hour_str = f"{hour}"
            writer.writerow([date_str,hour_str, visitors, sensor_id, store_id])
     
    except Exception as e:
        raise e


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py YYYY-MM-DD-HH")
    else:
        date_parts = validate_and_print_date(sys.argv[1])
        if date_parts:
            year, month, day, hour = date_parts
            query_api(year, month, day, hour) 
