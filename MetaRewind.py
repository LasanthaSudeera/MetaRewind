import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import Qt
from PyQt6 import uic

class MetaRewindApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/main.ui", self)
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    myApp = MetaRewindApp()
    myApp.show()
    
    try:
        sys.exit(app.exec())
    except SystemExit:
        print("Closing Window...")
    
    