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
        self.size = (400, 700)
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
        self.rate = QLabel('Estimated rate of return: ', self)
        self.rate.setStyleSheet("font-weight: bold; font-family: Times;")
        self.rate_insert = QLineEdit('', self)
        hbox_3.addWidget(self.rate)
        hbox_3.addWidget(self.rate_insert)
        vbox.addLayout(hbox_3)

        # Calculate botton
        

        self.setLayout(vbox)
        self.show()