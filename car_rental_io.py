import json
from car_rental import Car, Truck, Van, Reservation, Rent


def read_from_json(file_handle):
    """
    function used to read from database
    returns a list
    """
    cars = []
    data = json.load(file_handle)
    for item in data:
        seats = item['Number of seats']
        name = item['Name']
        fuel_consumption = item['Type of fuel and fuel Consumption per 100km']
        type = item['Type']
        brand = item['Brand']
        drive_type = item['Drive Type']
        additional = item['Additional']
        reservation = item['Reservation']
        last_reserved = item['Last reserved']
        rent = item['Rent']

        if reservation is not None:
            reservation_date = item['Reservation']['Reservation date']
            due_reservation_date = item['Reservation']['Due Reservation Date']
            who_reserved = item['Reservation']['Who reserved']
            reservation = Reservation(reservation_date, due_reservation_date, who_reserved)
        else:
            reservation = None

        if rent is not None:
            rent_date = item['Rent']['Rent date']
            return_date = item['Rent']['Return date']
            who_rented = item['Rent']['Who rented']
            overdue = item['Rent']['Is overdue']
            rent = Rent(rent_date, return_date, who_rented, overdue)
        else:
            rent = None

        if type == "Truck":
            load = additional['Load']
            trailer = additional['Has trailer']
            volume = additional['Max cargo volume']
            car = Truck(type, brand, name, seats, fuel_consumption, drive_type, volume, load, trailer, reservation, rent, last_reserved)
        elif type == "Van":
            volume = additional['Max cargo volume']
            car = Van(type, brand, name, seats, fuel_consumption, drive_type, volume, reservation, rent, last_reserved)
        else:
            car = Car(type, brand, name, seats, fuel_consumption, drive_type, reservation, rent, last_reserved)
        cars.append(car)
    return cars


def write_to_json(cars, file_handle):
    """
    function used to write items into database
    returns a list of dictionaries
    """
    data = cars_as_dict(cars)
    json.dump(data, file_handle, indent=4)
    return data


def cars_as_dict(cars):
    """
    function that represents a list of objects as a list of dicts.
    """
    data = []
    for car in cars:
        type = car.type
        brand = car.brand
        name = car.name
        seats = car.seats
        fuel_consumption = car.fuel_consumption
        drive_type = car.drive_type
        reservation = car.reservation
        rent = car.rent
        last_reserved = car.last_reserved()
        if reservation is not None:
            reservation_date = reservation.reservation_date
            due_reservation_date = reservation.due_reservation_date
            who_reserved = reservation.who_reserved
            reservation = {
                'Reservation date': reservation_date,
                'Due Reservation Date': due_reservation_date,
                'Who reserved': who_reserved
            }
        additional = None
        if rent is not None:
            rent_date = rent.rent_date
            return_date = rent.return_date
            who_rented = rent.who_rented
            overdue = rent.overdue
            rent = {
                'Rent date': rent_date,
                'Return date': return_date,
                'Who rented': who_rented,
                'Is overdue': overdue
            }
        if type == "Truck":
            load = car.load
            trailer = car.trailer
            volume = car.volume
            additional = {
                'Load': load,
                'Has trailer': trailer,
                'Max cargo volume': volume
            }

        if type == "Van":
            volume = car.volume
            additional = {
                'Max cargo volume': volume
            }

        car_data = {
            'Type': type,
            'Brand': brand,
            'Name': name,
            'Number of seats': seats,
            'Type of fuel and fuel Consumption per 100km': fuel_consumption,
            'Drive Type': drive_type,
            'Additional': additional,
            'Reservation': reservation,
            'Last reserved': last_reserved,
            'Rent': rent
        }

        data.append(car_data)
    return data
