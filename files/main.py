from PySide2 import QtWidgets, QtCore, QtGui
from ui_files.history import Ui_MainWindow
import files
import webbrowser
import help
import os
import sys

def show_profile_of_developer():
    if help.StatusMessageBox.status:
        pass
    else:
        webbrowser.open("https://t.me/joludyaster")


# def get_instruction():
#     webbrowser.open("https://telegra.ph/%D0%86NSTRUKC%D0%86YA-Z-KORISTUVANNYA-PROGRAMI-04-30")


class History(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(History, self).__init__(parent)
        self.clickPosition = None
        self.window = None
        self.history = Ui_MainWindow()
        self.history.setupUi(self)
        
        def drag_window(e):
            if not self.isMaximized():
                try:
                    if e.buttons() == QtCore.Qt.LeftButton and self.clickPosition:
                        self.move(self.pos() + e.globalPos() - self.clickPosition)
                except AttributeError:
                    pass

                self.clickPosition = e.globalPos()
                e.accept()

        self.history.header_frame.mouseMoveEvent = drag_window

        # font = QtGui.QFontDatabase.addApplicationFont(":/fonts/Montserrat-Medium.ttf")
        # if font == -1:
        #     print('Шрифт Montserrat-Medium не установлен')
        #
        # else:
        #
        #     fontName = QtGui.QFontDatabase.applicationFontFamilies(font)[0]
        #     self.f = QtGui.QFont(fontName, 20)
        #     self.f.setBold(True)
        #
        #     self.history.title.setText("I LOVE BIG\nNIGGERS")
        #     self.history.title.setFont(self.f)
        #     self.history.title.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        #
        #     self.history.select_theme.setText("I LOVE YOU")
        #     self.history.select_theme.setFont(self.f)



            # help.Settings.settings_label(
            #
            #     self,
            #     widgets=[self.history.title],
            #     text={self.history.title: {"text": "ПОМІЧНИК З\nІСТОРІЇ УКРАЇНИ"}},
            #     alignment={self.history.title: {"alignment": QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter}},
            #     font={self.history.title: {"font": self.f}},
            #     bold={self.history.title: {"bold": True}}
            #
            #
            # )

        self.settings_programm()
        self.clicks()

    def clicks(self):
        self.history.info_about_program.clicked.connect(self.instruction)
        self.history.comunication_with_developer.clicked.connect(show_profile_of_developer)
        self.history.select_theme.clicked.connect(self.select_theme)

        self.history.close_window.clicked.connect(lambda: self.close())
        self.history.minimize_window.clicked.connect(lambda: self.showMinimized())

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

    def select_theme(self):
        self.close()
        self.window = files.Themes()
        self.window.show()

    def instruction(self):

        help.message_box(
            icon="Information",
            stylesheet="""QMessageBox {
            min-width: 100px;
            min-height: 300px;
            }""",
            text="""ІНСТРУКЦІЯ ПО ВИКОРИСТАННЮ!
            
1. НАТИСНІТЬ НА КНОПКУ "ВИБРАТИ ТЕМУ".

2. ВИБЕРІТЬ ПОТРІБНУ ДЛЯ ВАС ТЕМУ.
    P.S: ТЕМИ РОЗДІЛЕНІ ПО РОЗДІЛАХ.

3. ПІСЛЯ ВИБОРУ ТЕМИ НА ЕКРАНІ З'ЯВИТЬСЯ
    ПИТАННЯ ТА ВАРІАНТИ ВІДПОВІДЕЙ НА КНОПКАХ.
   
    ПІСЛЯ ВИБОРУ ВАРІАНТА, ПРОГРАММА ПОКАЖЕ
    ЧИ ПРАВИЛЬНО ВИ ВІДПОВІЛИ НА ЗАПИТАННЯ

4. ПІСЛЯ ЗАКІНЧЕННЯ ТЕСТУ ВИ ЗМОЖЕТЕ
    ПОБАЧИТИ КІЛЬКІСТЬ ПРАВИЛЬНИХ ТА 
    НЕПРАВИЛЬНИХ ВІДПОВІДЕЙ, А ТАКОЖ 
    ВАШІ ВИБОРИ ВАРІНТУ ВІДПОВІДЕЙ.
   
    НАТИСНІСТЬ КНОПКУ "В МЕНЮ" ЩОБ
    ПОВЕРНУТИСЯ В МЕНЮ ТА ЩЕ РАЗ 
    ВИБРАТИ ТЕМУ ТА ПРОЙТИ ТЕСТ.


ГАРНОГО ВИКОРИСТАННЯ ПРОГРАММИ ТА
УДАЧІ ПРИ ПІДГОТОВЦІ ДО ЗНО!
"""
        )
