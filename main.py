from UI import ui
import sys
from PyQt6.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ui()
    window.show()
    sys.exit(app.exec())