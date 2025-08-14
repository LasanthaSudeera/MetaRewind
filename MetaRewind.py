import sys
import pandas as pd
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt
from PyQt6 import uic
from PyQt6.QtGui import QIcon

from lightweight_charts.widgets import QtChart

class MetaRewindApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MetaRewind")
        self.mountTheChartToCanvas()
        
    def mountTheChartToCanvas(self):
        uic.loadUi("ui/main.ui", self)
        
        # Create layout for the chart frame
        chart_layout = QVBoxLayout(self.FrameCanvasView)
        chart_layout.setContentsMargins(0, 0, 0, 0)
        
        # Create chart and set data
        self.chart = QtChart(self.FrameCanvasView)
        
        # Load OHLCV data from CSV
        df = pd.read_csv('ohlcv.csv')
        self.chart.set(df)
        
        # Add chart's webview to the layout
        chart_layout.addWidget(self.chart.get_webview())
        
        # Set icons for toolbar buttons
        self.setToolButtonIcons()
    
    def setToolButtonIcons(self):
        """Set icons for all tool buttons"""
        # Define icon paths
        icon_paths = {
            'btnAutoPlay': 'ui/icons/play_arrow.svg',
            'BtnPause': 'ui/icons/pause.svg',
            'btnFastSpeed': 'ui/icons/fast_forward.svg',
            'btnPrevious': 'ui/icons/skip_previous.svg',
            'btnNext': 'ui/icons/skip_next.svg',
            'btnSlowSpeed': 'ui/icons/fast_rewind.svg'  # Assuming this is for rewind
        }
        
        # Set icons for each button
        for button_name, icon_path in icon_paths.items():
            if hasattr(self, button_name):
                button = getattr(self, button_name)
                button.setIcon(QIcon(icon_path))
                # Make icon larger and more visible
                button.setIconSize(button.size() * 0.4)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    myApp = MetaRewindApp()
    myApp.show()
    
    try:
        sys.exit(app.exec())
    except SystemExit:
        print("Closing Window...")
    
    