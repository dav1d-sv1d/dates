from PySide2 import QtWidgets, QtCore, QtGui
from ui_files.results import Ui_MainWindow_4
import files
import help
import sys
import os


def show_theme():
    help.message_box(

        icon="Information",
        stylesheet="""QMessageBox {
        min-width: 100px;
        min-height: 300px;
        }""",
        text=f"РЕЗУЛЬТАТИ С ТЕМИ: {help.Helper.name_theme}"

    )


class Results(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.window = None
        self.results = Ui_MainWindow_4()
        self.results.setupUi(self)

        def drag_window(e):
            if not self.isMaximized():
                try:
                    if e.buttons() == QtCore.Qt.LeftButton and self.clickPosition:
                        self.move(self.pos() + e.globalPos() - self.clickPosition)
                except AttributeError:
                    pass

                self.clickPosition = e.globalPos()
                e.accept()

        self.results.header_frame.mouseMoveEvent = drag_window

        self.settings_programm()
        self.clicks()

    def settings_programm(self):
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.setWindowTitle("Помічник з Історії України (дати)")
        if hasattr(sys, "_MEIPASS"):
            icondir = os.path.join(sys._MEIPASS, 'hs.ico')
        else:
            icondir = 'hs.ico'
        self.setWindowIcon(QtGui.QIcon(icondir))

    def clicks(self):
        self.results.back.clicked.connect(self.back)
        self.results.inforesults.clicked.connect(show_theme)

        self.results.close_window.clicked.connect(lambda: self.close())
        self.results.minimize_window.clicked.connect(lambda: self.showMinimized())

    def back(self):
        help.reset_all()

        self.close()
        self.window = files.History()
        self.window.show()
