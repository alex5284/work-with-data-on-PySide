import sys
from PySide6.QtWidgets import QApplication, QWidget
from main import Window

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())