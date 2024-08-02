# This code creates the main window that will appear when executing "main.py"

# IMPORTS
import parameters as p
from PyQt6.QtWidgets import (QHBoxLayout, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, 
                             QGridLayout, QMessageBox)
from PyQt6.QtGui import QPixmap

# CODE

class MainWindow(QWidget):

    # Signals

    # Methods
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initialize_gui()

    def initialize_gui(self):
        
        self.position = (200, 200)
        self.size = (400, 600)
        self.setGeometry(*self.position, *self.size)
        self.setWindowTitle('Compound interest calculator')

        ## DESIGN ##
        vbox = QVBoxLayout()

        # Image
        self.logo = QLabel('', self)
        pixeles_logo = QPixmap(p.RUTA_LOGO)
        pixeles_logo = pixeles_logo.scaled(350, 350)
        self.logo.setPixmap(pixeles_logo)
        vbox.addWidget(self.logo)

        # Problem in data inserted warning
        self.data_warning = QLabel('', self)
        vbox.addWidget(self.data_warning)
        
        # Initial deposit
        hbox_1 = QHBoxLayout()
        self.initial_deposit = QLabel('Initial deposit: ', self)
        self.initial_deposit.setStyleSheet("font-weight: bold; font-family: Times;")
        self.initial_deposit_insert = QLineEdit('', self)
        hbox_1.addWidget(self.initial_deposit)
        hbox_1.addWidget(self.initial_deposit_insert)
        vbox.addLayout(hbox_1)

        # Contributions (monthly)
        hbox_2 = QHBoxLayout()
        self.contributions = QLabel('Monthly contributions: ', self)
        self.contributions.setStyleSheet("font-weight: bold; font-family: Times;")
        self.contributions_insert = QLineEdit('', self)
        hbox_2.addWidget(self.contributions)
        hbox_2.addWidget(self.contributions_insert)
        vbox.addLayout(hbox_2)

        # Estimated rate of return
        hbox_3 = QHBoxLayout()
        self.rate = QLabel('Estimated anual rate of return: ', self)
        self.rate.setStyleSheet("font-weight: bold; font-family: Times;")
        self.rate_insert = QLineEdit('', self)
        hbox_3.addWidget(self.rate)
        hbox_3.addWidget(self.rate_insert)
        vbox.addLayout(hbox_3)

        # Length of time in years
        hbox_4 = QHBoxLayout()
        self.length = QLabel('Length of time in years: ')
        self.length.setStyleSheet("font-weight: bold; font-family: Times;")
        self.length_insert = QLineEdit('', self)
        hbox_4.addWidget(self.length)
        hbox_4.addWidget(self.length_insert)
        vbox.addLayout(hbox_4)

        # Compound frequency
        hbox_5 = QHBoxLayout()
        self.compound_frequency = QLabel('Compound frequency: ', self)
        self.compound_frequency.setStyleSheet("font-weight: bold; font-family: Times;")
        self.compound_frequency_insert = QLineEdit('', self)
        hbox_5.addWidget(self.compound_frequency)
        hbox_5.addWidget(self.compound_frequency_insert)
        vbox.addLayout(hbox_5)

        # Calculate & clear all bottons
        hbox_6 = QHBoxLayout()
        self.calculate = QPushButton('Calculate', self)
        self.calculate.setStyleSheet("""
            QPushButton {
                background-color: #90EE90;
                color: black;
                border: 2px solid #32CD32;
                border-radius: 10px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #77DD77;
            }
            QPushButton:pressed {
                background-color: #5EAD5E;
            }
        """)
        self.calculate.clicked.connect(self.calculate_result)
        self.clear_all_button = QPushButton('Clear', self)
        self.clear_all_button.setStyleSheet("""
            QPushButton {
                background-color: #FF6666;
                color: black;
                border: 2px solid #CC0000;
                border-radius: 10px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #FF9999;
            }
            QPushButton:pressed {
                background-color: #CC0000;
            }
        """)
             
        self.clear_all_button.clicked.connect(self.clear_all)
        hbox_6.addWidget(self.calculate)
        hbox_6.addWidget(self.clear_all_button)
        vbox.addLayout(hbox_6)

        self.setLayout(vbox)
        self.show()

    def calculate_result(self):
        pass

    def clear_all(self):
        self.initial_deposit_insert.clear()
        self.contributions_insert.clear()
        self.rate_insert.clear()
        self.length_insert.clear()
        self.compound_frequency_insert.clear()