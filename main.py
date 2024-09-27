import sys
from PyQt5.QtWidgets import QApplication
from liteSci_CalLayout import SciCalcLayout #import the layout class

if __name__ == "__main__":  
    app = QApplication(sys.argv)
    try:
        calculator = SciCalcLayout()  # Instance of layout class
        calculator.show()  # Display the calculator
        sys.exit(app.exec_())  # Run the app loop
    except Exception as e:
        print(f"An error occurred: {e}")
