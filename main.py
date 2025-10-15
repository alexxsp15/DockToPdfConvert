import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QMainWindow, QApplication, QPushButton, QLabel, QWidget,
    QFileDialog, QProgressBar, QHBoxLayout, QVBoxLayout,
    QScrollArea, QListWidget
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setFixedSize(850, 600)

        # top label
        topLabel = QLabel("Welcome to convertor!")
        topLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # scroll
        self.mainScroll = QScrollArea()
        self.mainScroll.setWidgetResizable(True)
        scrollWidget = QWidget()
        scrollLayout = QVBoxLayout(scrollWidget)
        scrollWidget.setLayout(scrollLayout)
        self.mainScroll.setWidget(scrollWidget)

        # input files list
        self.inputList = QListWidget()
        scrollLayout.addWidget(topLabel)
        scrollLayout.addWidget(self.inputList)

        # convert button
        self.convertButton = QPushButton("Convert")
        scrollLayout.addWidget(self.convertButton)

        # output files list
        self.outputFiles = QListWidget()
        scrollLayout.addWidget(self.outputFiles)
        self.outputFiles.hide()

        # main Layout
        mainLayout = QVBoxLayout()
        mainWidget = QWidget()
        mainLayout.addWidget(self.mainScroll)
        mainWidget.setLayout(mainLayout)
        self.setCentralWidget(mainWidget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
