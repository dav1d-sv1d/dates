import files
from PySide2 import QtWidgets, QtGui, QtCore
from ui_files.settings_question import Ui_MainWindow_5
from ui_files.questions import Ui_MainWindow_3
import help
import sys
import os

def info():

    help.message_box(
        icon="Information",
        stylesheet="""QMessageBox {
                min-width: 100px;
                min-height: 300px;
                }""",
        text="""ІНСТРУКЦІЯ!

ПРИХОВАТИ ВІДПОВІДІ — це приховати
відповіді на момент проходження тесту,
та праці програми, щоб краще 
запам'ятовувати дати.

ON — приховати відповіді на момент праці
програми і виконання тесту.

OFF — не приховувати відповідей на момент
праці програми і виконання тесту.

P.S.: після виходу з програми
налаштування НЕ ЗБЕРІГАЮТЬСЯ!"""
    )



class SettingsQuestion(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.mouse_original_pos = None
        self.dragPos = None
        self.window = None

        self.settings_question = Ui_MainWindow_5()
        self.settings_question.setupUi(self)

        self.settings_programm()
        self.clicks()

    def settings_programm(self):
        if help.Settings_Q.status:
            self.settings_question.switch_2.setIcon(QtGui.QIcon(":/images/switch_on.png"))
        else:
            self.settings_question.switch_2.setIcon(QtGui.QIcon(":/images/switch_off.png"))

        self.setWindowTitle("Помічник з Історії України (дати)")
        if hasattr(sys, "_MEIPASS"):
            icondir = os.path.join(sys._MEIPASS, 'hs.ico')
        else:
            icondir = 'hs.ico'

        self.setWindowIcon(QtGui.QIcon(icondir))
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    def clicks(self):
        self.settings_question.switch_2.clicked.connect(self.switch)
        self.settings_question.info_about_switch.clicked.connect(info)
        self.settings_question.accept.clicked.connect(self.accept_settings_for_test)

        # self.settings_question.close_window.clicked.connect(self.close_window)
        # self.settings_question.minimize_window.clicked.connect(lambda: self.showMinimized())
        #
        # self.settings_question.header_frame.mouseMoveEvent = self.mouseMoveEvent
        # self.settings_question.header_frame.mousePressEvent = self.mousePressEvent

    def mousePressEvent(self, event):
        self.dragPos = self.pos()
        self.mouse_original_pos = self.mapToGlobal(event.pos())

    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.MouseButton.LeftButton:
            MainWindow_last_pos = self.dragPos + self.mapToGlobal(event.pos()) - self.mouse_original_pos
            self.move(MainWindow_last_pos)
            event.accept()

    def switch(self):
        if not help.Settings_Q.status:
            self.settings_question.switch_2.setIcon(QtGui.QIcon(":/images/switch_on.png"))
            help.Settings_Q.status = True
        else:
            self.settings_question.switch_2.setIcon(QtGui.QIcon(":/images/switch_off.png"))
            help.Settings_Q.status = False

    def close_window(self):
        self.close()

    def accept_settings_for_test(self):
        self.close()
