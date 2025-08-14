import sys
import pandas as pd
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt
from PyQt6 import uic

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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    myApp = MetaRewindApp()
    myApp.show()
    
    try:
        sys.exit(app.exec())
    except SystemExit:
        print("Closing Window...")
    
    