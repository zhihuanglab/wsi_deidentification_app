import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from main_window import MainWindow

def main():
    app = QApplication(sys.argv)
    
    # Set the application icon
    app.setWindowIcon(QIcon("resources/icon.ico"))
    
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
