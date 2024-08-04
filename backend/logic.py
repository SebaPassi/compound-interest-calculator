# This code is responsible of the logic necessary for the calculator

# IMPORTS
from PyQt6.QtCore import QObject, pyqtSignal

# CODE
class CalculatorLogic(QObject):

    # Signals
    signal_inputs_validity = pyqtSignal(bool)
    signal_result = pyqtSignal(float, float)

    # Methods
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        pass

    def check_inputs(self, initial_deposit, contributions, rate, length, compound_frequency) -> None:
        self.condition = True
        if initial_deposit == "" or contributions == "" or rate == "" or length == "":
            self.condition = False

        if self.condition == True:
            self.obtain_verified_inputs(float(initial_deposit), float(contributions), float(rate), \
                                        float(length), compound_frequency)
        else:
            self.signal_inputs_validity.emit(self.condition)

    def obtain_verified_inputs(self, initial_deposit, contributions, rate, length, compound_frequency) -> None:
        if compound_frequency == "Annually":
            compound_frequency = 1
        else:
            compound_frequency = 12

        rate_as_decimal = rate / 100

        initial_deposit_amount = initial_deposit * (1 + rate_as_decimal / compound_frequency) ** (compound_frequency * length)
        contributions_amount = contributions * (((1 + rate_as_decimal / compound_frequency) ** (compound_frequency * length) - 1) / (rate_as_decimal / compound_frequency))
        result = initial_deposit_amount + contributions_amount
        self.submit_result(length, result)

    def submit_result(self, length, result) -> None:
        self.signal_result.emit(length, result)