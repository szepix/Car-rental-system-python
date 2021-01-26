# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'car_rental.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1203, 874)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pages = QStackedWidget(self.centralwidget)
        self.pages.setObjectName(u"pages")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pages.sizePolicy().hasHeightForWidth())
        self.pages.setSizePolicy(sizePolicy)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout = QGridLayout(self.page)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.searchButton = QPushButton(self.page)
        self.searchButton.setObjectName(u"searchButton")

        self.verticalLayout_8.addWidget(self.searchButton)

        self.typeSearch = QLineEdit(self.page)
        self.typeSearch.setObjectName(u"typeSearch")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.typeSearch.sizePolicy().hasHeightForWidth())
        self.typeSearch.setSizePolicy(sizePolicy1)

        self.verticalLayout_8.addWidget(self.typeSearch)

        self.brandSearch = QLineEdit(self.page)
        self.brandSearch.setObjectName(u"brandSearch")
        sizePolicy1.setHeightForWidth(self.brandSearch.sizePolicy().hasHeightForWidth())
        self.brandSearch.setSizePolicy(sizePolicy1)

        self.verticalLayout_8.addWidget(self.brandSearch)

        self.nameSearch = QLineEdit(self.page)
        self.nameSearch.setObjectName(u"nameSearch")
        sizePolicy1.setHeightForWidth(self.nameSearch.sizePolicy().hasHeightForWidth())
        self.nameSearch.setSizePolicy(sizePolicy1)

        self.verticalLayout_8.addWidget(self.nameSearch)

        self.seatsSearch = QLineEdit(self.page)
        self.seatsSearch.setObjectName(u"seatsSearch")
        sizePolicy1.setHeightForWidth(self.seatsSearch.sizePolicy().hasHeightForWidth())
        self.seatsSearch.setSizePolicy(sizePolicy1)

        self.verticalLayout_8.addWidget(self.seatsSearch)

        self.fuelSearch = QLineEdit(self.page)
        self.fuelSearch.setObjectName(u"fuelSearch")
        sizePolicy1.setHeightForWidth(self.fuelSearch.sizePolicy().hasHeightForWidth())
        self.fuelSearch.setSizePolicy(sizePolicy1)

        self.verticalLayout_8.addWidget(self.fuelSearch)

        self.driveSearch = QLineEdit(self.page)
        self.driveSearch.setObjectName(u"driveSearch")
        sizePolicy1.setHeightForWidth(self.driveSearch.sizePolicy().hasHeightForWidth())
        self.driveSearch.setSizePolicy(sizePolicy1)

        self.verticalLayout_8.addWidget(self.driveSearch)

        self.volumeSearch = QLineEdit(self.page)
        self.volumeSearch.setObjectName(u"volumeSearch")
        sizePolicy1.setHeightForWidth(self.volumeSearch.sizePolicy().hasHeightForWidth())
        self.volumeSearch.setSizePolicy(sizePolicy1)

        self.verticalLayout_8.addWidget(self.volumeSearch)

        self.trailerSearch = QLineEdit(self.page)
        self.trailerSearch.setObjectName(u"trailerSearch")
        sizePolicy1.setHeightForWidth(self.trailerSearch.sizePolicy().hasHeightForWidth())
        self.trailerSearch.setSizePolicy(sizePolicy1)

        self.verticalLayout_8.addWidget(self.trailerSearch)

        self.loadSearch = QLineEdit(self.page)
        self.loadSearch.setObjectName(u"loadSearch")
        sizePolicy1.setHeightForWidth(self.loadSearch.sizePolicy().hasHeightForWidth())
        self.loadSearch.setSizePolicy(sizePolicy1)

        self.verticalLayout_8.addWidget(self.loadSearch)

        self.availabilitySearch = QLineEdit(self.page)
        self.availabilitySearch.setObjectName(u"availabilitySearch")
        sizePolicy1.setHeightForWidth(self.availabilitySearch.sizePolicy().hasHeightForWidth())
        self.availabilitySearch.setSizePolicy(sizePolicy1)

        self.verticalLayout_8.addWidget(self.availabilitySearch)


        self.gridLayout.addLayout(self.verticalLayout_8, 1, 0, 1, 1)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.ShowCarList = QPushButton(self.page)
        self.ShowCarList.setObjectName(u"ShowCarList")

        self.verticalLayout_9.addWidget(self.ShowCarList)

        self.overdueCars = QPushButton(self.page)
        self.overdueCars.setObjectName(u"overdueCars")

        self.verticalLayout_9.addWidget(self.overdueCars)

        self.reservedCars = QPushButton(self.page)
        self.reservedCars.setObjectName(u"reservedCars")

        self.verticalLayout_9.addWidget(self.reservedCars)

        self.modifyDatabase = QPushButton(self.page)
        self.modifyDatabase.setObjectName(u"modifyDatabase")

        self.verticalLayout_9.addWidget(self.modifyDatabase)

        self.availableRent = QPushButton(self.page)
        self.availableRent.setObjectName(u"availableRent")

        self.verticalLayout_9.addWidget(self.availableRent)


        self.gridLayout.addLayout(self.verticalLayout_9, 0, 0, 1, 1)

        self.pages.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.horizontalLayout_4 = QHBoxLayout(self.page_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.carList = QListWidget(self.page_2)
        self.carList.setObjectName(u"carList")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.carList.sizePolicy().hasHeightForWidth())
        self.carList.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.carList)

        self.carInfo_background = QStackedWidget(self.page_2)
        self.carInfo_background.setObjectName(u"carInfo_background")
        sizePolicy.setHeightForWidth(self.carInfo_background.sizePolicy().hasHeightForWidth())
        self.carInfo_background.setSizePolicy(sizePolicy)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_4 = QVBoxLayout(self.page_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.backButton = QPushButton(self.page_3)
        self.backButton.setObjectName(u"backButton")
        self.backButton.setEnabled(True)

        self.verticalLayout_4.addWidget(self.backButton)

        self.label = QLabel(self.page_3)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label)

        self.CarInfo = QLabel(self.page_3)
        self.CarInfo.setObjectName(u"CarInfo")

        self.verticalLayout_4.addWidget(self.CarInfo)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.RemoveReservation = QPushButton(self.page_3)
        self.RemoveReservation.setObjectName(u"RemoveReservation")
        self.RemoveReservation.setEnabled(False)

        self.verticalLayout_3.addWidget(self.RemoveReservation)

        self.RemoveRent = QPushButton(self.page_3)
        self.RemoveRent.setObjectName(u"RemoveRent")
        self.RemoveRent.setEnabled(False)

        self.verticalLayout_3.addWidget(self.RemoveRent)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.name_details = QLineEdit(self.page_3)
        self.name_details.setObjectName(u"name_details")
        self.name_details.setEnabled(False)

        self.verticalLayout_2.addWidget(self.name_details)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.date_begin = QLineEdit(self.page_3)
        self.date_begin.setObjectName(u"date_begin")
        self.date_begin.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.date_begin)

        self.date_end = QLineEdit(self.page_3)
        self.date_end.setObjectName(u"date_end")
        self.date_end.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.date_end)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.reserve_button = QPushButton(self.page_3)
        self.reserve_button.setObjectName(u"reserve_button")
        self.reserve_button.setEnabled(False)

        self.verticalLayout.addWidget(self.reserve_button)

        self.rent_button = QPushButton(self.page_3)
        self.rent_button.setObjectName(u"rent_button")
        self.rent_button.setEnabled(False)

        self.verticalLayout.addWidget(self.rent_button)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.carInfo_background.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_5 = QVBoxLayout(self.page_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.backButton_2 = QPushButton(self.page_4)
        self.backButton_2.setObjectName(u"backButton_2")
        self.backButton_2.setEnabled(True)

        self.verticalLayout_5.addWidget(self.backButton_2)

        self.verticalSpacer = QSpacerItem(20, 440, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.carInfo_background.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.verticalLayout_7 = QVBoxLayout(self.page_5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.backButton_3 = QPushButton(self.page_5)
        self.backButton_3.setObjectName(u"backButton_3")

        self.verticalLayout_7.addWidget(self.backButton_3)

        self.label_4 = QLabel(self.page_5)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_7.addWidget(self.label_4)

        self.typeDatabase = QLineEdit(self.page_5)
        self.typeDatabase.setObjectName(u"typeDatabase")

        self.verticalLayout_7.addWidget(self.typeDatabase)

        self.label_3 = QLabel(self.page_5)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_7.addWidget(self.label_3)

        self.brandDatabase = QLineEdit(self.page_5)
        self.brandDatabase.setObjectName(u"brandDatabase")

        self.verticalLayout_7.addWidget(self.brandDatabase)

        self.label_2 = QLabel(self.page_5)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_7.addWidget(self.label_2)

        self.nameDatabase = QLineEdit(self.page_5)
        self.nameDatabase.setObjectName(u"nameDatabase")

        self.verticalLayout_7.addWidget(self.nameDatabase)

        self.label_7 = QLabel(self.page_5)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_7.addWidget(self.label_7)

        self.seatsDatabase = QLineEdit(self.page_5)
        self.seatsDatabase.setObjectName(u"seatsDatabase")

        self.verticalLayout_7.addWidget(self.seatsDatabase)

        self.label_6 = QLabel(self.page_5)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_7.addWidget(self.label_6)

        self.fuelDatabase = QLineEdit(self.page_5)
        self.fuelDatabase.setObjectName(u"fuelDatabase")

        self.verticalLayout_7.addWidget(self.fuelDatabase)

        self.label_5 = QLabel(self.page_5)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_7.addWidget(self.label_5)

        self.driveDatabase = QLineEdit(self.page_5)
        self.driveDatabase.setObjectName(u"driveDatabase")

        self.verticalLayout_7.addWidget(self.driveDatabase)

        self.label_8 = QLabel(self.page_5)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_7.addWidget(self.label_8)

        self.volumeDatabase = QLineEdit(self.page_5)
        self.volumeDatabase.setObjectName(u"volumeDatabase")

        self.verticalLayout_7.addWidget(self.volumeDatabase)

        self.label_9 = QLabel(self.page_5)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_7.addWidget(self.label_9)

        self.trailerDatabase = QLineEdit(self.page_5)
        self.trailerDatabase.setObjectName(u"trailerDatabase")

        self.verticalLayout_7.addWidget(self.trailerDatabase)

        self.label_10 = QLabel(self.page_5)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_7.addWidget(self.label_10)

        self.loadDatabase = QLineEdit(self.page_5)
        self.loadDatabase.setObjectName(u"loadDatabase")

        self.verticalLayout_7.addWidget(self.loadDatabase)

        self.editDatabase = QPushButton(self.page_5)
        self.editDatabase.setObjectName(u"editDatabase")

        self.verticalLayout_7.addWidget(self.editDatabase)

        self.addDatabase = QPushButton(self.page_5)
        self.addDatabase.setObjectName(u"addDatabase")

        self.verticalLayout_7.addWidget(self.addDatabase)

        self.removeDatabase = QPushButton(self.page_5)
        self.removeDatabase.setObjectName(u"removeDatabase")

        self.verticalLayout_7.addWidget(self.removeDatabase)

        self.carInfo_background.addWidget(self.page_5)

        self.horizontalLayout.addWidget(self.carInfo_background)


        self.horizontalLayout_4.addLayout(self.horizontalLayout)

        self.pages.addWidget(self.page_2)

        self.horizontalLayout_2.addWidget(self.pages)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1203, 20))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.pages.setCurrentIndex(1)
        self.carInfo_background.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.searchButton.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.typeSearch.setInputMask("")
        self.typeSearch.setText("")
        self.typeSearch.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type", None))
        self.brandSearch.setText("")
        self.brandSearch.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Brand", None))
        self.nameSearch.setText("")
        self.nameSearch.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.seatsSearch.setText("")
        self.seatsSearch.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Number of seats", None))
        self.fuelSearch.setText("")
        self.fuelSearch.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Fuel type and Consumption", None))
        self.driveSearch.setText("")
        self.driveSearch.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Drive Type", None))
        self.volumeSearch.setText("")
        self.volumeSearch.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Max Cargo volume", None))
        self.trailerSearch.setText("")
        self.trailerSearch.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Trailer", None))
        self.loadSearch.setText("")
        self.loadSearch.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.availabilitySearch.setText("")
        self.availabilitySearch.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Availability", None))
        self.ShowCarList.setText(QCoreApplication.translate("MainWindow", u"Show car list", None))
        self.overdueCars.setText(QCoreApplication.translate("MainWindow", u"Show overdue cars", None))
        self.reservedCars.setText(QCoreApplication.translate("MainWindow", u"Show reserved cars", None))
        self.modifyDatabase.setText(QCoreApplication.translate("MainWindow", u"Modify Database", None))
        self.availableRent.setText(QCoreApplication.translate("MainWindow", u"Show available to rent", None))
        self.backButton.setText(QCoreApplication.translate("MainWindow", u"Go back", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Car Info:", None))
        self.CarInfo.setText("")
        self.RemoveReservation.setText(QCoreApplication.translate("MainWindow", u"Remove Reservation", None))
        self.RemoveRent.setText(QCoreApplication.translate("MainWindow", u"Remove Rent", None))
        self.name_details.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Name and Surname", None))
        self.date_begin.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Beginning date", None))
        self.date_end.setText("")
        self.date_end.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ending date", None))
        self.reserve_button.setText(QCoreApplication.translate("MainWindow", u"Reserve", None))
        self.rent_button.setText(QCoreApplication.translate("MainWindow", u"Rent", None))
        self.backButton_2.setText(QCoreApplication.translate("MainWindow", u"Go back", None))
        self.backButton_3.setText(QCoreApplication.translate("MainWindow", u"Go back", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Type", None))
        self.typeDatabase.setInputMask("")
        self.typeDatabase.setText("")
        self.typeDatabase.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Brand", None))
        self.brandDatabase.setText("")
        self.brandDatabase.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Brand", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.nameDatabase.setText("")
        self.nameDatabase.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Number of seats", None))
        self.seatsDatabase.setText("")
        self.seatsDatabase.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Number of seats", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Type of fuel and consumption", None))
        self.fuelDatabase.setText("")
        self.fuelDatabase.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type of fuel and consumption", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Drive Type", None))
        self.driveDatabase.setText("")
        self.driveDatabase.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Drive Type", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Max cargo volume", None))
        self.volumeDatabase.setText("")
        self.volumeDatabase.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Max cargo volume", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Trailer", None))
        self.trailerDatabase.setText("")
        self.trailerDatabase.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Trailer", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.loadDatabase.setText("")
        self.loadDatabase.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.editDatabase.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.addDatabase.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.removeDatabase.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
    # retranslateUi

