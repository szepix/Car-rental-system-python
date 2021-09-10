from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QStackedWidget, QListWidgetItem, QDialog
from car_rental_io import cars_as_dict
from car_rental import Car, Truck, Van, Reservation, Rent, InvalidDateRange, InvalidDate
from database_actions import overdue_cars, search_database, remove_from_database, add_to_database, reserved_cars, not_reserved_cars
from database import write_to_database, read_from_database
from ui_car_rental import Ui_MainWindow
from dialog import Ui_Dialog
import sys


class Dialog(QDialog):
    def __init__(self, error, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.error = error
        self.ui.setupUi(self)
        if self.error == "reserve":
            self.ui.Error.setText("Cannot reserve today")
        if self.error == "date":
            self.ui.Error.setText("Invalid date format. Valid date format is day.month.year")
        if self.error == 'daterange':
            self.ui.Error.setText("Invalid date range")


class CarRentalWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.clicked = None
        self.cars = read_from_database() or []
        if self.cars:
            self.cars_dict = cars_as_dict(self.cars)
        self.ui.pages.setCurrentIndex(0)
        self.ui.ShowCarList.clicked.connect(lambda: self._setup_car_list(self.cars, 1))
        self.ui.overdueCars.clicked.connect(lambda: self._setup_car_list(self.cars, 'overdue'))
        self.ui.backButton.clicked.connect(lambda: self.go_back())
        self.ui.backButton_2.clicked.connect(lambda: self. go_back())
        self.ui.backButton_3.clicked.connect(lambda: self. go_back())
        self.ui.modifyDatabase.clicked.connect(lambda: self._setup_car_list(self.cars, 'modify'))
        self.ui.searchButton.clicked.connect(lambda: self.search_cars(self.cars))
        self.ui.typeDatabase.textEdited.connect(lambda: self.set_variables())
        self.ui.reservedCars.clicked.connect(lambda: self._setup_car_list(self.cars, 'reserved'))
        self.ui.carList.itemClicked.connect(self.get_item)
        self.ui.reserve_button.setText("Reserve")
        self.ui.RemoveReservation.clicked.connect(lambda: self._remove_reservation_rent(self.clicked, 'reservation'))
        self.ui.RemoveRent.clicked.connect(lambda: self._remove_reservation_rent(self.clicked, 'rent'))
        self.ui.reserve_button.clicked.connect(lambda: self._reserve_rent(self.clicked, 'reservation'))
        self.ui.rent_button.clicked.connect(lambda: self._reserve_rent(self.clicked, 'rent'))
        self.ui.removeDatabase.clicked.connect(lambda: self.remove_from_database(self.clicked))
        self.ui.addDatabase.clicked.connect(lambda: self.edit_add_to_database(self.clicked, "add"))
        self.ui.editDatabase.clicked.connect(lambda: self.edit_add_to_database(self.clicked, "edit"))
        self.ui.availableRent.clicked.connect(lambda: self._setup_car_list(self.cars, 'availableRent'))

    def check_reservations(self):
        """
        reloads items in the list to check if some of them expired,
        removes expired reservations
        """
        cars = []
        for car in self.cars:
            if car.reservation and car.reservation.check_expiration() == "EXPIRED":
                car.reservation = None
            cars.append(car)
        self.cars_dict = write_to_database(cars)
        self.cars = read_from_database()
        return self.cars

    def set_variables(self):
        """
        depending on text written in database editor sets line editors enabled/disabled
        """
        type = self.ui.typeDatabase.text().replace(" ", "")
        if type == "Van":
            self.ui.volumeDatabase.setEnabled(True)
            self.ui.trailerDatabase.setEnabled(False)
            self.ui.loadDatabase.setEnabled(False)
        elif type == "Truck":
            self.ui.volumeDatabase.setEnabled(True)
            self.ui.trailerDatabase.setEnabled(True)
            self.ui.loadDatabase.setEnabled(True)
        else:
            self.ui.volumeDatabase.setEnabled(False)
            self.ui.trailerDatabase.setEnabled(False)
            self.ui.loadDatabase.setEnabled(False)

    def search_cars(self, cars):
        """
        function that supports graphical representation of searching the database
        uses lineEditors
        """
        name = self.ui.nameSearch.text()
        type = self.ui.typeSearch.text()
        brand = self.ui.brandSearch.text()
        seats = self.ui.seatsSearch.text().replace(" ", "")
        fuel_consumption = self.ui.fuelSearch.text()
        drive_type = self.ui.driveDatabase.text()
        volume = self.ui.volumeSearch.text().replace(" ", "")
        trailer = self.ui.trailerSearch.text()
        if trailer == "True":
            trailer = True
        elif trailer == "False":
            trailer = False
        load = (self.ui.loadSearch.text().replace(" ", ""))
        availability = self.ui.availabilitySearch.text()
        if availability == "":
            availability = None
        criteria = {
            "Type": type,
            "Brand": brand,
            "Name": name,
            "Number of seats": seats,
            "Type of fuel and fuel Consumption per 100km": fuel_consumption,
            "Drive Type": drive_type,
            "Additional": {
                "Load": load,
                "Has trailer": trailer,
                "Max cargo volume": volume
            },
            'Reservation': {
                "Due Reservation Date": availability,
            },
            "Rent": {
                "Return date": availability,
            }
        }
        cars = search_database(criteria, self.cars)
        self.ui.pages.setCurrentIndex(1)
        self._setup_car_list(cars, 'search')

    def go_back(self):
        """
        functionality of go back buttons
        """
        self.ui.pages.setCurrentIndex(0)
        self.ui.carList.clear()

    def _setup_car_list(self, cars, info):
        """
        setups car list depending on purpose it's used for
        """
        if info != 'search':
            cars = self.check_reservations()
        if self.cars:
            self.cars_dict = write_to_database(self.cars)
        self.default_text()
        self.action = info
        self.ui.pages.setCurrentIndex(1)
        self.ui.carList.clear()
        if self.action == "overdue":
            cars = overdue_cars(self.cars)
        if self.action == "reserved":
            cars = reserved_cars(self.cars)
        if self.action == 'availableRent':
            cars = not_reserved_cars(self.cars)
        if cars:
            for car in cars:
                item = QListWidgetItem(str(car))
                item.car = car
                item.car_index = self.cars.index(car)
                item.car_dict = self.cars_dict[item.car_index]
                self.ui.carList.addItem(item)
        self.ui.carList.itemClicked.connect(self._setup_car_info)
        if self.action == "modify":
            self.ui.volumeDatabase.setEnabled(False)
            self.ui.trailerDatabase.setEnabled(False)
            self.ui.loadDatabase.setEnabled(False)
            self.ui.carInfo_background.setCurrentIndex(2)
            self.ui.removeDatabase.setEnabled(False)
            self.ui.editDatabase.setEnabled(False)
        else:
            self.ui.carInfo_background.setCurrentIndex(1)

    def get_item(self, item):
        """
        stores clicked item to help with operating on it
        """
        self.clicked = item

    def remove_from_database(self, item):
        """
        graphical representation of removing from database,
        supported by functions from database.py and car_rental_io
        """
        if item:
            car = item.car
            self.cars = remove_from_database(car, self.cars)
        if self.cars:
            self.cars_dict = write_to_database(self.cars)
        self._setup_car_list(self.cars, "modify")
        self.clicked = None

    def edit_add_to_database(self, item, info):
        """
        function that depending on input edits the item or adds new item into database
        converting input into class objects
        """
        name = self.ui.nameDatabase.text()
        type = self.ui.typeDatabase.text()
        brand = self.ui.brandDatabase.text()
        seats = self.ui.seatsDatabase.text().replace(" ", "")
        fuel_consumption = self.ui.fuelDatabase.text()
        drive_type = self.ui.driveDatabase.text()
        reservation = item.car.reservation
        rent = item.car.rent
        if type == "Van":
            volume = self.ui.volumeDatabase.text()
            car = Van(type, brand, name, seats, fuel_consumption, drive_type, volume, reservation, rent)
        elif type == "Truck":
            volume = self.ui.volumeDatabase.text()
            trailer = self.ui.trailerDatabase.text()
            if trailer == "True":
                trailer = True
            elif trailer == "False":
                trailer = False
            load = self.ui.loadDatabase.text()
            car = Truck(type, brand, name, seats, fuel_consumption, drive_type, volume, load, trailer, reservation, rent)
        else:
            car = Car(type, brand, name, seats, fuel_consumption, drive_type, reservation, rent)
        if info == "add":
            self.cars = add_to_database(car, self.cars)
        if info == "edit":
            item.car = car
            self.cars[item.car_index] = car
        self._setup_car_list(self.cars, "modify")

    def default_text(self):
        """
        sets default text to every lineEditor in Database Editor
        """
        self.ui.reserve_button.setText("Reserve")
        self.ui.date_begin.setText('')
        self.ui.date_end.setText('')
        self.ui.name_details.setText('')
        self.ui.nameDatabase.setText('')
        self.ui.typeDatabase.setText('')
        self.ui.brandDatabase.setText('')
        self.ui.seatsDatabase.setText('')
        self.ui.fuelDatabase.setText('')
        self.ui.driveDatabase.setText('')
        self.ui.volumeDatabase.setText('')
        self.ui.trailerDatabase.setText('')
        self.ui.loadDatabase.setText('')

    def _setup_car_info(self, button):
        """
        represents car info as a text visible to a user
        or inputs it in lineEditors if editing database
        """
        self.default_text()
        car_dict = button.car_dict
        if self.action == "modify":
            self.ui.volumeDatabase.setEnabled(False)
            self.ui.trailerDatabase.setEnabled(False)
            self.ui.loadDatabase.setEnabled(False)
            car = button.car
            self.ui.carInfo_background.setCurrentIndex(2)
            name = car.name
            self.ui.nameDatabase.setText(f"{name}")
            type = car.type
            self.ui.typeDatabase.setText(f"{type}")
            brand = car.brand
            self.ui.brandDatabase.setText(f"{brand}")
            seats = car.seats
            self.ui.seatsDatabase.setText(f"{seats}")
            fuel_consumption = car.fuel_consumption
            self.ui.fuelDatabase.setText(f"{fuel_consumption}")
            drive_type = car.drive_type
            self.ui.driveDatabase.setText(f"{drive_type}")
            if type == "Van":
                self.ui.volumeDatabase.setEnabled(True)
                volume = car.volume
                self.ui.volumeDatabase.setText(f"{volume}")
            if type == "Truck":
                self.ui.volumeDatabase.setEnabled(True)
                self.ui.trailerDatabase.setEnabled(True)
                self.ui.loadDatabase.setEnabled(True)
                volume = car.volume
                self.ui.volumeDatabase.setText(f"{volume}")
                trailer = car.trailer
                self.ui.trailerDatabase.setText(f"{trailer}")
                load = car.load
                self.ui.loadDatabase.setText(f"{load}")
            self.ui.editDatabase.setEnabled(True)
            self.ui.removeDatabase.setEnabled(True)
        else:
            self.ui.carInfo_background.setCurrentIndex(0)
            self.set_text(car_dict)

    def _remove_reservation_rent(self, item, name):
        """
        used to remove reservation or rent depending on input
        """
        if name == 'reservation':
            self.cars[item.car_index].reservation = None
        else:
            self.cars[item.car_index].rent = None
        self.cars_dict = write_to_database(self.cars)
        item.car_dict = self.cars_dict[item.car_index]
        item.car = self.cars[item.car_index]
        self._setup_car_info(item)
        if name == 'reservation':
            self.ui.RemoveReservation.setEnabled(False)
        else:
            self.ui.RemoveRent.setEnabled(False)
        if self.action == 'overdue':
            self._setup_car_list(self.cars, self.action)

    def _reserve_rent(self, item, name):
        """
        used to set reservation or rent depending on input
        """
        beginning_date = self.ui.date_begin.text()
        end_date = self.ui.date_end.text()
        person_info = self.ui.name_details.text()
        if name == 'rent':
            try:
                rent = Rent(beginning_date, end_date, person_info)
            except InvalidDateRange:
                dialog = Dialog('daterange', self)
                dialog.exec_()
            except InvalidDate:
                dialog = Dialog('date', self)
                dialog.exec_()
            if beginning_date == '' and end_date == '':
                self.cars[item.car_index].rent = None
            else:
                self.cars[item.car_index].rent = rent
        if name == 'reservation':
            info = ''
            try:
                reservation = Reservation(beginning_date, end_date, person_info)
                info = self.cars[item.car_index].add_reservation(reservation)
            except InvalidDateRange:
                dialog = Dialog('daterange', self)
                dialog.exec_()
            except InvalidDate:
                dialog = Dialog('date', self)
                dialog.exec_()
            if info == "Cannot reserve today":
                self.ui.reserve_button.setText("Cannot reserve today")
                dialog = Dialog('reserve', self)
                dialog.exec_()
                self.ui.reserve_button.setEnabled(False)
                return
        self.cars_dict = write_to_database(self.cars)
        item.car_dict = self.cars_dict[item.car_index]
        item.car = self.cars[item.car_index]
        self._setup_car_info(item)
        if self.action == 'overdue':
            self._setup_car_list(self.cars, self.action)
        self.ui.date_begin.setEnabled(False)
        self.ui.date_end.setEnabled(False)
        self.ui.name_details.setEnabled(False)
        self.ui.reserve_button.setEnabled(False)
        self.ui.rent_button.setEnabled(False)

    def set_text(self, car_dict):
        """
        used in _setup_car_info to represent car info as a text
        """
        text = ''
        for position_name in car_dict:
            position = car_dict[position_name]
            if(position is not None):
                words = ['Rent', 'Additional', 'Reservation']
                if position_name in words:
                    if position_name == 'Reservation':
                        self.ui.RemoveReservation.setEnabled(True)
                        self.ui.reserve_button.setEnabled(False)
                        self.ui.date_begin.setEnabled(False)
                        self.ui.date_end.setEnabled(False)
                        self.ui.name_details.setEnabled(False)
                    if position_name == 'Rent':
                        self.ui.RemoveRent.setEnabled(True)
                        self.ui.rent_button.setEnabled(False)
                        if self.ui.reserve_button.isEnabled is False:
                            self.ui.date_begin.setEnabled(False)
                            self.ui.date_end.setEnabled(False)
                            self.ui.name_details.setEnabled(False)
                    text += f'\n{position_name} info: \n'

                    for crit in position:
                        text += f'{crit}: {position[crit]}\n'
                else:
                    text += f'{position_name}: {position}\n'
            else:
                if position_name == 'Reservation':
                    self.ui.reserve_button.setEnabled(True)
                    self.ui.RemoveReservation.setEnabled(False)
                    self.ui.date_begin.setEnabled(True)
                    self.ui.date_end.setEnabled(True)
                    self.ui.name_details.setEnabled(True)
                if position_name == 'Rent':
                    self.ui.rent_button.setEnabled(True)
                    self.ui.RemoveRent.setEnabled(False)
                    self.ui.date_begin.setEnabled(True)
                    self.ui.date_end.setEnabled(True)
                    self.ui.name_details.setEnabled(True)
        self.ui.CarInfo.setText(text)


def guiMain(args):
    app = QApplication(args)
    window = CarRentalWindow()
    window.show()
    return app.exec_()


if __name__ == "__main__":
    guiMain(sys.argv)
