from car_rental import Car, Truck, Van, Reservation, Rent, InvalidDateRange, InvalidDate
from car_rental_io import write_to_json, cars_as_dict
from database import read_from_database
from database_actions import overdue_cars, search_database, reserved_cars, not_reserved_cars
from datetime import datetime, timedelta
from io import StringIO
import pytest


def test_car():
    car = Car("Sportback", "BMW", "X1", "5", "Diesel, 7", "AWD")
    assert car.type == 'Sportback'
    assert car.brand == "BMW"
    assert car.name == 'X1'
    assert car.seats == "5"
    assert car.fuel_consumption == "Diesel, 7"
    assert car.drive_type == "AWD"
    assert car.reservation is None
    assert car.rent is None


def test_car_add_reservation():
    car = Car("Sportback", "BMW", "X1", "5", "Diesel, 7", "AWD")
    reservation = Reservation("02.01.2021", "09.01.2021", "Thomas")
    car.add_reservation(reservation)
    assert car.reservation == reservation
    assert car.last_reserved() == f'{datetime.now():%d.%m.%Y}'


def test_car_add_reservation_twice():
    car = Car("Sportback", "BMW", "X1", "5", "Diesel, 7", "AWD")
    reservation = Reservation("02.01.2021", "09.01.2021", "Thomas")
    car.add_reservation(reservation)
    assert car.reservation == reservation
    assert car.last_reserved() == f'{datetime.now():%d.%m.%Y}'
    assert car.add_reservation(reservation) == "Cannot reserve today"


def test_car_add_reservation_expired():
    car = Car("Sportback", "BMW", "X1", "5", "Diesel, 7", "AWD")
    reservation = Reservation("02.01.2021", "06.01.2021", "Thomas")
    car.add_reservation(reservation)
    assert car.reservation.check_expiration() == "EXPIRED"


def test_reservation_invalid_range():
    with pytest.raises(InvalidDateRange):
        Reservation("10.01.2021", "06.01.2021", "Thomas")


def test_reservation_invalid_date():
    with pytest.raises(InvalidDate):
        Reservation("02-01-2021", "06.01.2021", "Thomas")


def test_reservation_invalid_str():
    with pytest.raises(InvalidDate):
        Reservation("ddd", "06.01.2021", "Thomas")


def test_reservation_int():
    with pytest.raises(InvalidDate):
        Reservation(123, "06.01.2021", "Thomas")


def test_rent():
    today = f'{datetime.now():%d.%m.%Y}'
    rent = Rent("02.01.2021", today, "Thomas")
    assert rent.rent_date == "02.01.2021"
    assert rent.return_date == today
    assert rent.who_rented == "Thomas"
    assert rent.overdue == "NO"


def test_rent_overdue():
    rent = Rent("02.01.2021", "06.01.2021", "Thomas")
    assert rent.rent_date == "02.01.2021"
    assert rent.return_date == "06.01.2021"
    assert rent.who_rented == "Thomas"
    assert rent.overdue == "OVERDUE"


def test_rent_invalid_range():
    with pytest.raises(InvalidDateRange):
        Rent("10.01.2021", "06.01.2021", "Thomas")


def test_rent_invalid_date():
    with pytest.raises(InvalidDate):
        Rent("10-01.2021", "06.01.2021", "Thomas")


def test_rent_invalid_str():
    with pytest.raises(InvalidDate):
        Rent('ddd', "06.01.2021", "Thomas")


def test_rent_int():
    with pytest.raises(InvalidDate):
        Rent(123, "06.01.2021", "Thomas")


def test_van():
    car = Van("Van", "Volvo", "Splinter", "2", "Diesel, 14", "FWD", "1500L")
    assert car.type == 'Van'
    assert car.brand == "Volvo"
    assert car.name == 'Splinter'
    assert car.seats == "2"
    assert car.fuel_consumption == "Diesel, 14"
    assert car.drive_type == "FWD"
    assert car.volume == "1500L"
    assert car.reservation is None
    assert car.rent is None


def test_truck():
    car = Truck("Van", "Volvo", "Splinter", "2", "Diesel, 14", "FWD", "1500L", "2000Kg", True)
    assert car.type == 'Van'
    assert car.brand == "Volvo"
    assert car.name == 'Splinter'
    assert car.seats == "2"
    assert car.fuel_consumption == "Diesel, 14"
    assert car.drive_type == "FWD"
    assert car.volume == "1500L"
    assert car.load == '2000Kg'
    assert car.trailer is True
    assert car.reservation is None
    assert car.rent is None


def test_reserved_cars():
    car = Car("Sportback", "BMW", "X1", "5", "Diesel, 7", "AWD")
    reservation = Reservation("02.01.2021", "27.02.2021", "Thomas")
    car.add_reservation(reservation)
    car2 = Van("Van", "Volvo", "Splinter", "2", "Diesel, 14", "FWD", "1500L")
    cars = [car, car2]
    reserved = reserved_cars(cars)
    assert reserved == [car]


def test_reserved_cars_empty():
    cars = []
    reserved = reserved_cars(cars)
    assert reserved == []


def test_not_reserved_cars():
    car = Car("Sportback", "BMW", "X1", "5", "Diesel, 7", "AWD")
    reservation = Reservation("02.01.2021", "27.02.2021", "Thomas")
    car.add_reservation(reservation)
    car2 = Van("Van", "Volvo", "Splinter", "2", "Diesel, 14", "FWD", "1500L")
    cars = [car, car2]
    not_reserved = not_reserved_cars(cars)
    assert not_reserved == [car2]


def test_not_reserved_cars_empty():
    cars = []
    not_reserved = not_reserved_cars(cars)
    assert not_reserved == []


def test_search_database():
    car = Car("Sportback", "BMW", "X1", "5", "Diesel, 7", "AWD")
    cars = [car]
    crit = {
        "Type": "Sportback",
        "Brand": "BMW"
    }
    search = search_database(crit, cars)
    assert car in search


def test_search_empty():
    cars = []
    crit = {}
    search = search_database(crit, cars)
    assert search == []


def test_search_availability():
    car = Car("Sportback", "BMW", "X1", "5", "Diesel, 7", "AWD")
    today = datetime.today()
    tommorow = today + timedelta(days=2)
    today = f'{datetime.now():%d.%m.%Y}'
    tommorow = f'{tommorow:%d.%m.%Y}'
    rent = Rent("9.01.2021", today, "Thomas")
    crit = {
        "Rent":
        {
            "Return date": tommorow
        }
    }
    car.rent = rent
    search = search_database(crit, [car])
    assert car in search


def test_search_multiple():
    car = Car("Sportback", "BMW", "X1", "5", "Diesel, 7", "AWD")
    car2 = Van("Van", "Volvo", "Splinter", "2", "Diesel, 14", "FWD", "1500L")
    today = datetime.today()
    tommorow = today + timedelta(days=2)
    today = f'{datetime.now():%d.%m.%Y}'
    tommorow = f'{tommorow:%d.%m.%Y}'
    reservation = Reservation("9.01.2021", today, "Thomas")
    rent = Rent("9.01.2021", today, "Thomas")
    crit = {
        "Rent":
        {
            "Return date": tommorow
        }
    }
    car.rent = rent
    car2.add_reservation(reservation)
    search = search_database(crit, [car, car2])
    assert search == [car, car2]


def test_search_empty_database():
    cars = []
    crit = {
        "Type": "Sportback",
        "Brand": "BMW"
    }
    search = search_database(crit, cars)
    assert search == []


def test_search_empty_crit():
    car = Car("Sportback", "BMW", "X1", "5", "Diesel, 7", "AWD")
    cars = [car]
    crit = {}
    search = search_database(crit, cars)
    assert search == []


def test_search_van():
    car = Car("Sportback", "BMW", "X1", "5", "Diesel, 7", "AWD")
    car2 = Van("Van", "Volvo", "Splinter", "2", "Diesel, 14", "FWD", "1500L")
    crit = {
        'Additional': {
            "Max cargo volume": "1500L"
        }
    }
    search = search_database(crit, [car, car2])
    assert search == [car2]


def test_search_truck():
    car = Car("Sportback", "BMW", "X1", "5", "Diesel, 7", "AWD")
    car2 = Van("Van", "Volvo", "Splinter", "2", "Diesel, 14", "FWD", "1500L")
    car3 = Truck("Van", "Volvo", "Splinter", "2", "Diesel, 14", "FWD", "1500L", "2000Kg", True)
    crit = {
        'Additional': {
            "Max cargo volume": "1500L"
        }
    }
    search = search_database(crit, [car, car2, car3])
    assert search == [car2, car3]


def test_overdue_cars():
    car = Car("Sportback", "BMW", "X1", "5", "Diesel, 7", "AWD")
    rent = Rent("01.01.2021", "02.01.2021", "Thomas")
    car.rent = rent
    cars = [car]
    overdue = overdue_cars(cars)
    assert overdue == [car]


def test_overdue_cars_empty():
    cars = []
    overdue = overdue_cars(cars)
    assert overdue is None


def test_cars_as_dict():
    car = Car("Sportback", "BMW", "X1", "5", "Diesel, 7", "AWD")
    car2 = Van("Van", "Volvo", "Splinter", "2", "Diesel, 14", "FWD", "1500L")
    result = cars_as_dict([car, car2])
    dict = [
        {
            "Type": "Sportback",
            "Brand": "BMW",
            "Name": "X1",
            "Number of seats": "5",
            "Type of fuel and fuel Consumption per 100km": "Diesel, 7",
            "Drive Type": "AWD",
            "Additional": None,
            "Reservation": None,
            "Last reserved": None,
            "Rent": None
        },
        {
            "Type": "Van",
            "Brand": "Volvo",
            "Name": "Splinter",
            "Number of seats": "2",
            "Type of fuel and fuel Consumption per 100km": "Diesel, 14",
            "Drive Type": "FWD",
            "Additional": {
                "Max cargo volume": "1500L"
            },
            "Reservation": None,
            "Last reserved": None,
            "Rent": None
        }
    ]
    assert result == dict


def test_cars_as_dict_empty():
    result = cars_as_dict([])
    assert result == []


def test_write_to_database():
    file = StringIO()
    car = Car("Sportback", "BMW", "X1", "5", "Diesel, 7", "AWD")
    car2 = Van("Van", "Volvo", "Splinter", "2", "Diesel, 14", "FWD", "1500L")
    cars = [car, car2]
    write_to_json(cars, file)


def test_read_from_database():
    items = read_from_database()
    assert len(items) >= 0
