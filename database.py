from car_rental_io import write_to_json, read_from_json
from os.path import getsize


def read_from_database():
    try:
        if (getsize('database.json') == 0):
            return
    except Exception:
        open('database.json', 'w')
        return
    else:
        with open('database.json', 'r') as file_handle:
            cars = read_from_json(file_handle)
    return cars


def write_to_database(cars):
    with open('database.json', 'w') as file_handle:
        data = write_to_json(cars, file_handle)
    return data
