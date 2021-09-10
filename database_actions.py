from database import write_to_database
from car_rental_io import cars_as_dict
from datetime import datetime


def remove_from_database(item, list):
    """
    Function used to remove items from database,
    as input takes item and list it's in
    returns a list
    """
    list.remove(item)
    write_to_database(list)
    return list


def add_to_database(item, list):
    """
    Function used to add items to database,
    as input takes item and list it's in
    returns a list
    """
    list.append(item)
    write_to_database(list)
    return list


def overdue_cars(cars):
    """
    Function returns overdue cars with amount of days they're late,
    as input takes a list, using datetime compares today's date and rent end date
    returns a list
    """
    today = datetime.now().date()
    if cars:
        overdue = []
        for car in cars:
            rent_info = car.rent
            if rent_info:
                rent_end_date = datetime.strptime(rent_info.return_date, '%d.%m.%Y').date()
            if rent_info is not None and (rent_end_date < today):
                overdue.append(car)
        return overdue


def search_database(criteria, cars):
    """
    Function used to search items from database,
    as an input takes criteria as dictionary and a list of cars,
    iterates through dictionary and checks if criteria meet
    return a list
    """
    cars_as_list = cars_as_dict(cars)
    if len(criteria) == 0:
        return []

    criteria_meeting = []
    for car_index, car in enumerate(cars_as_list):
        criteria_met = 0
        criteria_size = len(criteria)
        for crit_name in criteria:
            crit = criteria[crit_name]
            car_crit = car[crit_name]
            if isinstance(crit, dict):
                if crit_name == 'Rent':
                    if car_crit is not None and crit['Return date'] is not None:
                        car_date = datetime.strptime(car_crit['Return date'], '%d.%m.%Y').date()
                        crit_date = datetime.strptime(crit['Return date'], '%d.%m.%Y').date()
                    if car_crit is None or crit['Return date'] is None or car_date < crit_date:
                        criteria_met += 1
                    continue
                if crit_name == 'Reservation':
                    if car_crit is not None and crit['Due Reservation Date'] is not None:
                        car_date = datetime.strptime(car_crit['Due Reservation Date'], '%d.%m.%Y').date()
                        crit_date = datetime.strptime(crit['Due Reservation Date'], '%d.%m.%Y').date()
                    if car_crit is None or crit['Due Reservation Date'] is None or car_date < crit_date:
                        criteria_met += 1
                    continue

                criteria_size += len(crit)
                for add in crit:
                    if crit[add] != '':
                        try:
                            if crit[add] == car_crit[add]:
                                criteria_met += 1
                        except Exception:
                            pass
                    else:
                        criteria_met += 1
                criteria_met += 1
            elif crit in [car_crit, '']:
                criteria_met += 1
        if(criteria_met == criteria_size):
            car_class = cars[car_index]
            criteria_meeting.append(car_class)
    return criteria_meeting


def reserved_cars(cars):
    """
    function that lists all reserved cars,
    as input takes a list, returns a list
    """
    list = []
    if cars:
        for car in cars:
            if car.reservation is not None:
                list.append(car)
    return list


def not_reserved_cars(cars):
    """
    function that lists all available to rent cars,
    as input takes a list, returns a list
    """
    list = []
    if cars:
        for car in cars:
            if car.reservation is None and car.rent is None:
                list.append(car)
    return list
