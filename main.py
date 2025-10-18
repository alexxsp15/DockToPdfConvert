import sys
import os
from PyQt6.QtCore import Qt, QUrl
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import (
    QMainWindow, QApplication, QPushButton, QLabel, QWidget,
    QFileDialog, QProgressBar, QHBoxLayout, QVBoxLayout,
    QScrollArea, QListWidget, QListWidgetItem, QAbstractItemView
)
from docx2pdf import convert

class MyListWidget(QListWidget):
    def __init__(self):
        super().__init__()

        self.setAcceptDrops(True)
        self.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)

        self.files_urls = []

    def dragEnterEvent(self, e):
        data = e.mimeData()
        if not data.hasUrls():
            e.ignore()
            return

        urls = data.urls()

        for url in urls:
            if url.isLocalFile():
                start_url = url.toLocalFile()
                _, ext = os.path.splitext(start_url)
                if ext.lower() in (".doc", ".docx"):
                    e.acceptProposedAction()
                    return

        e.ignore()

    def dragMoveEvent(self, e):
        data = e.mimeData()
        if data.hasUrls():
            e.acceptProposedAction()
        else:
            e.ignore()

    def dropEvent(self, e):
        data = e.mimeData()
        if not data.hasUrls():
            e.ignore()
            return

        urls = data.urls()
        added_any = False
        for url in urls:
            if url.isLocalFile():
                start_url = url.toLocalFile()
                _, ext = os.path.splitext(start_url)
                if ext.lower() in (".doc", ".docx"):
                    name = url.fileName()
                    self.files_urls.append([start_url, name])
                    icon = QIcon("icons/icons8-docx-64.png")
                    item = QListWidgetItem(icon, name)
                    self.addItem(item)
                    added_any = True

        if added_any:
            e.acceptProposedAction()
            print(self.files_urls)
            print(self.count())
        else:
            e.ignore()


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
        self.inputList = MyListWidget()
        self.inputList.setStyleSheet("""
        QListWidget {
        background-color: #228DA9;
        border: 5px solid #1E7E96;
        border-radius: 6px;
        font-size: 18px;
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
        self.convertButton.clicked.connect(self.convert_pressed)

    # output files list
        self.outputFiles = QListWidget()
        scrollLayout.addWidget(self.outputFiles)
        self.outputFiles.setStyleSheet("""
                QListWidget {
                background-color: #228DA9;
                border: 5px solid #1E7E96;
                border-radius: 6px;
                font-size: 18px;
                padding: 5 px;
                }
                """)
        self.outputFiles.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.outputFiles.hide()

    #clearButton
        self.clearButton = QPushButton("Clear")
        self.clearButton.setFixedSize(110, 60)
        self.clearButton.setStyleSheet("""
                QPushButton {
                font-size: 20px;
                font-weight: bold;
                color: #DAEDD3;
                border: 5px solid #1E7E96;
                border-radius: 4px;
                }
                """)
        scrollLayout.addWidget(self.clearButton, alignment=Qt.AlignmentFlag.AlignCenter)
        self.clearButton.hide()
        self.clearButton.clicked.connect(self.clear_pressed)

        # main Layout
        mainLayout = QVBoxLayout()
        mainWidget = QWidget()
        mainWidget.setStyleSheet("background-color: #1E7E96")
        mainLayout.addWidget(self.mainScroll)
        mainWidget.setLayout(mainLayout)
        self.setCentralWidget(mainWidget)

    def convert_pressed(self):
        folder_path = QFileDialog.getExistingDirectory(
            parent=self,
            caption="Save converted files",
            directory=""
        )
        if folder_path:
            for url, name in self.inputList.files_urls:
                n = name.find(".")
                new_name = name[:n]
                convert(url, os.path.join(folder_path, new_name + ".pdf"))
                icon = QIcon("icons/icons8-pdf-50.png")
                item = QListWidgetItem(icon, new_name + ".pdf")
                self.outputFiles.addItem(item)
        self.outputFiles.show()
        self.clearButton.show()

    def clear_pressed(self):
        self.inputList.files_urls.clear()
        self.inputList.clear()
        self.outputFiles.clear()
        self.outputFiles.hide()
        self.clearButton.hide()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
