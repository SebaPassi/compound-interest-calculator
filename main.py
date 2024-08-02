# Main ".py" file which has to be executed in order to use the calculator

# IMPORTS 
import sys
from frontend.main_window import MainWindow
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

    sys.exit(app.exec())