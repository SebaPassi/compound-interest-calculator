# Main ".py" file which has to be executed in order to use the calculator

# IMPORTS 
import sys
from frontend.main_window import MainWindow
from backend.logic import CalculatorLogic
from PyQt6.QtWidgets import QApplication

# CODE

if __name__ == '__main__':
    def hook(type, value, traceback) -> None:
        print(type)
        print(traceback)
    sys.__excepthook__ = hook

    app = QApplication([])

    # Initialize classes
    main_window = MainWindow()
    calculator_logic = CalculatorLogic()

    # Signals
    main_window.signal_obtain_result.connect(calculator_logic.check_inputs)
    calculator_logic.signal_inputs_validity.connect(main_window.error_in_inputs)
    calculator_logic.signal_result.connect(main_window.show_result)

    # Execution
    sys.exit(app.exec())