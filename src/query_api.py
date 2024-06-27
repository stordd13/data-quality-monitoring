import sys
import os
from datetime import date, datetime
import requests


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

        save_data(year, month, day, hour, response.json())

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while querying the API: {e}")

def save_data(year, month, day, hour, visit_count):

    try:
        folder_path = "data/raw/"
        if os.path.exists(folder_path):
            print("ok")
        else:
            os.mkdir(folder_path)

        file_path = os.path.join(folder_path, f"{year}-{month}-{day}-{hour}.csv")
        df = pd.DataFrame(
            values=[datetime(year, month, day), hour, visit_count, None],
            columns=['date', 'hour', 'visit_count','id_capteur']
            )
        df.to_csv(file_path, index=False)
    except Exception as e:
        raise e


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py YYYY-MM-DD-HH")
    else:
        date_parts = validate_and_print_date(sys.argv[1])
        if date_parts:
            #year, month, day, hour = date_parts
            query_api(*date_parts) 
