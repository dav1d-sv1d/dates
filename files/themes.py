from PySide2 import QtWidgets, QtCore, QtGui
from ui_files.themes import Ui_MainWindow_2
import files
import help
import os
import sys

class Themes(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.clickPosition = None
        self.window = None
        self.themes = Ui_MainWindow_2()
        self.themes.setupUi(self)
        
        def drag_window(e):
            if not self.isMaximized():
                try:
                    if e.buttons() == QtCore.Qt.LeftButton and self.clickPosition:
                        self.move(self.pos() + e.globalPos() - self.clickPosition)
                except AttributeError:
                    pass

                self.clickPosition = e.globalPos()
                e.accept()

        self.themes.header_frame.mouseMoveEvent = drag_window

        self.settings_programm()
        self.clicks()

    def clicks(self):
        for button in [

            self.themes.theme_1, self.themes.theme_2, self.themes.theme_3, self.themes.theme_4,
            self.themes.theme_5, self.themes.theme_6, self.themes.theme_7, self.themes.theme_8,
            self.themes.theme_9, self.themes.theme_10, self.themes.theme_11, self.themes.theme_12,
            self.themes.theme_13, self.themes.theme_14, self.themes.theme_15, self.themes.theme_16,
            self.themes.theme_17, self.themes.theme_18, self.themes.theme_19, self.themes.theme_20,
            self.themes.theme_21, self.themes.theme_22, self.themes.theme_23, self.themes.theme_24,
            self.themes.theme_25, self.themes.theme_26, self.themes.theme_27, self.themes.theme_28,
            self.themes.theme_29, self.themes.theme_30, self.themes.theme_31

        ]:
            button.clicked.connect(self.open_questions)

        self.themes.back.clicked.connect(self.back)
        self.themes.close_window.clicked.connect(lambda: self.close())
        self.themes.minimize_window.clicked.connect(lambda: self.showMinimized())

    def settings_programm(self):
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.setWindowTitle("Помічник з Історії України (дати)")
        if hasattr(sys, "_MEIPASS"):
            icondir = os.path.join(sys._MEIPASS, 'hs.ico')
        else:
            icondir = 'hs.ico'
        self.setWindowIcon(QtGui.QIcon(icondir))
        
    def mouseMoveEvent(self, event):
        self.clickPosition = event.globalPos()

    def mouseReleaseEvent(self, event):
        try:
            del self.clickPosition
        except AttributeError:
            pass

    def open_questions(self):
        theme = self.sender()
        help.Helper.check, help.Helper.name_theme = True, theme.text().replace("\n", " ")

        self.close()
        self.window = files.Questions()
        self.window.show()
        # self.window = files.Questions()
        # self.window.show()

    def back(self):

        self.close()
        self.window = files.History()
        self.window.show()
