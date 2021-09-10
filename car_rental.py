from datetime import datetime


class InvalidDateRange(Exception):
    """
    Class InvalidDateRange.
    Error message if date range is invalid
    """
    def __init__(self):
        super().__init__("You've entered invalid date range")


class InvalidDate(Exception):
    """
    Class InvalidDate.
    Error message if date is invalid
    """
    def __init__(self):
        super().__init__("You've entered invalid date")


class Car:
    """
    Class Car. Contains attributes:
    :param type: type of car
    :type type: str

    :param brand: car brand
    :type brand: str

    :param name: car name
    :type name: str

    :param seats: number of seats
    :type seats: int

    :param fuel_consumption: fuel consumption per 100km
    :type fuel_consumption: int

    :param drive_type: car's drive type (AWD, FWD, RWD)
    :type drive_type: str

    :param reservation: information about reservation
    :type reservation: class

    :param rent: information about rent
    :type rent: class
    """
    def __init__(self, type, brand, name, seats, fuel_consumption, drive_type, reservation=None, rent=None, last_reserved=None):
        self.seats = seats
        self.fuel_consumption = fuel_consumption
        self.type = type
        self.brand = brand
        self.name = name
        self.rent = rent
        self.drive_type = drive_type
        self.reservation = reservation
        self._last_reserved = last_reserved

    def add_reservation(self, reservation):
        """
        function that adds reservation,
        using datetime check if item was reserved today
        """
        self.today = f'{datetime.now():%d.%m.%Y}'
        if(self._last_reserved is None or self._last_reserved < self.today):
            self.reservation = reservation
            self._last_reserved = self.today
        else:
            return "Cannot reserve today"

    def last_reserved(self):
        return self._last_reserved

    def __str__(self):
        return f'{self.type}, {self.brand} {self.name}'


class Van(Car):
    """
    Class Van. Contains attributes:
    :param type: type of car (Truck, Van)
    :type type: str

    :param brand: car brand
    :type brand: str

    :param name: car name
    :type name: str

    :param seats: number of seats
    :type seats: int

    :param fuel_consumption: fuel consumption per 100km
    :type fuel_consumption: int

    :param drive_type: car's drive type (AWD, FWD, RWD)
    :type drive_type: str

    :param volume: Trunk volume
    :type name: int

    :param reservation: information about reservation
    :type reservation: class

    :param rent: information about rent
    :type rent: class
    """
    def __init__(self, type, brand, name, seats, fuel_consumption, drive_type, volume, reservation=None, rent=None, last_reserved=None):
        super().__init__(type, brand, name, seats, fuel_consumption, drive_type, reservation, rent, last_reserved)
        self.volume = volume


class Truck(Van):
    """
    Class Van. Contains attributes:
    :param type: type of car (Truck, Van)
    :type type: str

    :param brand: car brand
    :type brand: str

    :param name: car name
    :type name: str

    :param seats: number of seats
    :type seats: int

    :param fuel_consumption: fuel consumption per 100km
    :type fuel_consumption: int

    :param drive_type: car's drive type (AWD, FWD, RWD)
    :type drive_type: str

    :param volume: Trunk volume
    :type name: int

    :param load: Truck's maximum load
    :type load: int

    :param trailer: info if truck has trailer with it, name if defined
    :type trailer: str

    :param reservation: information about reservation
    :type reservation: class

    :param rent: information about rent
    :type rent: class
    """
    def __init__(self, type, brand, name, seats, fuel_consumption, drive_type, volume, load, trailer=None, reservation=None, rent=None, last_reserved=None):
        super().__init__(type, brand, name, seats, fuel_consumption, drive_type, volume, reservation, rent, last_reserved)
        self.load = load
        self.trailer = trailer


class Reservation:
    """
    :param reservation_date: informs when car has been reserved
    :type reservation_date: str

    :param due_reservation_date: end date of car reservation
    :type due_reservation_date: str
    """
    def __init__(self, reservation_date, due_reservation_date, who_reserved):
        self.today = f'{datetime.now():%d.%m.%Y}'
        self.who_reserved = who_reserved
        self.reservation_date = None
        self.due_reservation_date = None
        if None not in [reservation_date, due_reservation_date]:
            try:
                self.reservation_date = datetime.strptime(reservation_date.replace(" ", ""), '%d.%m.%Y').date()
                self.due_reservation_date = datetime.strptime(due_reservation_date.replace(" ", ""), '%d.%m.%Y').date()
                if (self.reservation_date < self.due_reservation_date):
                    self.reservation_date = f'{reservation_date}'
                    self.due_reservation_date = f'{due_reservation_date}'
                else:
                    raise InvalidDateRange
            except (ValueError, AttributeError):
                raise InvalidDate

    def check_expiration(self):
        if(self.due_reservation_date < self.today):
            return "EXPIRED"


class Rent:
    """
    :param rent_date: informs when car has been rented
    :type rent_date: str

    :param return_date: end date of car rent
    :type return_date: str
    """
    def __init__(self, rent_date, return_date, who_rented, overdue=""):
        self.rent_date = rent_date
        self.return_date = return_date
        self.who_rented = who_rented
        try:
            self.rent_date = datetime.strptime(rent_date.replace(" ", ""), '%d.%m.%Y').date()
            self.return_date = datetime.strptime(return_date.replace(" ", ""), '%d.%m.%Y').date()
            if (self.rent_date < self.return_date):
                self.rent_date = f'{rent_date}'
                self.return_date = f'{return_date}'
            else:
                raise InvalidDateRange
        except (ValueError, AttributeError):
            raise InvalidDate
        if self.return_date is None:
            self.overdue = None
        elif (self.return_date < f'{datetime.now():%d.%m.%Y}'):
            self.overdue = "OVERDUE"
        else:
            self.overdue = "NO"
