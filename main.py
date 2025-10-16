import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QMainWindow, QApplication, QPushButton, QLabel, QWidget,
    QFileDialog, QProgressBar, QHBoxLayout, QVBoxLayout,
    QScrollArea, QListWidget, QListWidgetItem
)

class MyListWidget(QListWidget):
    def __init__(self):
        super().__init__()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setFixedSize(850, 600)

    # top label
        topLabel = QLabel("Welcome to convertor!")
        topLabel.setStyleSheet("""
        QLabel {
        color: #DAEDD3;
        font-size: 35px;
        font-weight: bold; 
        }""")
        topLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

    # scroll
        self.mainScroll = QScrollArea()
        self.mainScroll.setWidgetResizable(True)
        scrollWidget = QWidget()
        scrollWidget.setStyleSheet("background-color: #228DA9")
        scrollLayout = QVBoxLayout(scrollWidget)
        scrollWidget.setLayout(scrollLayout)
        self.mainScroll.setWidget(scrollWidget)

    # input files list
        self.inputList = QListWidget()
        item = QListWidgetItem("lol")
        self.inputList.addItem(item)
        self.inputList.setStyleSheet("""
        QListWidget {
        background-color: #228DA9;
        border: 5px solid #1E7E96;
        border-radius: 6px;
        font-size: 20px;
        padding: 5 px;
        }
        """)
        scrollLayout.addWidget(topLabel)
        scrollLayout.addWidget(self.inputList)

    # convert button
        self.convertButton = QPushButton("Convert")
        self.convertButton.setFixedSize(110, 60)
        self.convertButton.setStyleSheet("""
        QPushButton {
        font-size: 20px;
        font-weight: bold;
        color: #DAEDD3;
        border: 5px solid #1E7E96;
        border-radius: 4px;
        }
        """)
        scrollLayout.addWidget(self.convertButton, alignment=Qt.AlignmentFlag.AlignCenter)

    # output files list
        self.outputFiles = QListWidget()
        scrollLayout.addWidget(self.outputFiles)
        self.outputFiles.hide()

    # main Layout
        mainLayout = QVBoxLayout()
        mainWidget = QWidget()
        mainWidget.setStyleSheet("background-color: #1E7E96")
        mainLayout.addWidget(self.mainScroll)
        mainWidget.setLayout(mainLayout)
        self.setCentralWidget(mainWidget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
