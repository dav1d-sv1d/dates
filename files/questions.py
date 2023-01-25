from PySide2 import QtWidgets, QtGui, QtCore
from ui_files.questions import Ui_MainWindow_3
from ui_files.settings_question import Ui_MainWindow_5
import files
import help
import random
import os
import sys


def show_theme():
    help.message_box(

        icon="Information",
        stylesheet="""QMessageBox {
        min-width: 50px;
        min-height: 50px;
        }""",
        text=f"ТЕМА: {help.Helper.name_theme}"

    )






class Questions(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.clickPosition = None
        self.index = 0
        self.current = 0
        self.w = 720
        self.window = None
        self.questions = Ui_MainWindow_3()
        self.questions.setupUi(self)

        def drag_window(e):
            if not self.isMaximized():
                try:
                    if e.buttons() == QtCore.Qt.LeftButton and self.clickPosition:
                        self.move(self.pos() + e.globalPos() - self.clickPosition)
                except AttributeError:
                    pass

                self.clickPosition = e.globalPos()
                e.accept()

        self.questions.header_frame.mouseMoveEvent = drag_window

        self.settings_programm()
        self.logic()
        self.clicks()

    def settings_programm(self):

        help.Helper.len_questions = len(list(help.ThemesAndQuestions.themes[help.Helper.name_theme].keys()))

        self.setWindowTitle("Помічник з Історії України (дати)")
        if hasattr(sys, "_MEIPASS"):
            icondir = os.path.join(sys._MEIPASS, 'hs.ico')
        else:
            icondir = 'hs.ico'

        self.setWindowIcon(QtGui.QIcon(icondir))
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        QtWidgets.QSizeGrip(self.questions.size_grid)

    def logic(self):

        for button in [

            self.questions.answer_1,
            self.questions.answer_2,
            self.questions.answer_3,
            self.questions.answer_4

        ]:
            button.setEnabled(True)
            button.setStyleSheet(

                """QPushButton { 
                color: white;
                border: 2px solid #df6277;
                }

                QPushButton:hover { 
                background-color: #272739;
                }

                QPushButton:pressed {
                background-color: #323248;
                }"""

            )

        if not help.ThemesAndQuestions.themes[help.Helper.name_theme]:
            self.close()
            self.window = files.Results()
            self.window.results.correctanswers.setText(
                f"{help.CorrectAndUncorrectAnswers.correct}/{help.Helper.len_questions}")
            self.window.results.uncorrectanswers.setText(
                f"{help.CorrectAndUncorrectAnswers.uncorrect}/{help.Helper.len_questions}")
            self.window.results.inforesults.setToolTip(
                f"Результати тестування з теми:\n\n{help.Helper.name_theme}"
            )

            score = [20, 20]
            minimumHeight = 0
            question = [20, 64]

            butns = {

                "button 1": [20, 281],
                "button 2": [20, 450],
                "button 3": [430, 280],
                "button 4": [430, 449]

            }

            for i in list(help.Results.data):

                s = QtWidgets.QLabel(self.window.results.widgets)
                s.setGeometry(score[0], score[1], 101, 31)
                s.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                font_s = QtGui.QFont("Tahoma", 16)
                font_s.setBold(True)
                s.setFont(font_s)
                score[1] += 730

                s.setStyleSheet(
                    """color: white;
                    border: 2px solid #df6277;"""
                )

                s.setText(i)

                q = QtWidgets.QLabel(self.window.results.widgets)
                q.setGeometry(question[0], question[1], 811, 201)
                q.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                q.setWordWrap(True)
                font_q = QtGui.QFont("Tahoma", 20)
                font_q.setBold(True)
                q.setFont(font_q)
                question[1] += 730

                q.setStyleSheet(
                    "background-color: rgb(255, 255, 255);"
                )

                q.setText(help.Results.data[i]["question"])

                for j in range(1, 5):
                    button = QtWidgets.QPushButton(self.window.results.widgets)
                    button.setGeometry(butns[f"button {j}"][0], butns[f"button {j}"][1], 401, 161)
                    button.setStyleSheet(help.Results.data[i]["buttons"][f"button {j}"]["stylesheet"])
                    font_b = QtGui.QFont("Tahoma", 14)
                    font_b.setBold(True)
                    button.setFont(font_b)
                    button.setText(help.Results.data[i]["buttons"][f"button {j}"]["text"])
                    button.setEnabled(False)
                    butns[f"button {j}"][1] += 730

                    if button.pos().y() > self.window.results.widgets.minimumHeight():
                        minimumHeight += 590
                        self.window.results.widgets.setMinimumHeight(minimumHeight)

            minimumHeight += 200
            self.window.results.widgets.setMinimumHeight(minimumHeight)

            self.window.show()

        else:

            items = random.choice(list(help.ThemesAndQuestions.themes[help.Helper.name_theme].items()))

            if items[1]["index"] == "dates":

                random.SystemRandom().shuffle(items[1]["answers"])
                help.Helper.question_and_correct_answer = {}
                help.Helper.question_and_correct_answer.update({items[0]: items[1]["correct_answer"]})

                self.questions.question.setText(items[0])

                help.CorrectAndUncorrectAnswers.number_of_question += 1
                self.questions.score.setText(
                    f"{help.CorrectAndUncorrectAnswers.number_of_question}/{help.Helper.len_questions}")

                buttons = dict(zip(

                    [

                        self.questions.answer_1,
                        self.questions.answer_2,
                        self.questions.answer_3,
                        self.questions.answer_4

                    ],

                    items[1]["answers"]

                ))

                for button in buttons:
                    button.setText(buttons[button])

                help.StylesheetsAnswers.stylesheets.update(
                    {
                        self.questions.answer_1: self.questions.answer_1.styleSheet(),
                        self.questions.answer_2: self.questions.answer_2.styleSheet(),
                        self.questions.answer_3: self.questions.answer_3.styleSheet(),
                        self.questions.answer_4: self.questions.answer_4.styleSheet()
                    }
                )

                if help.Settings_Q.status:

                    self.questions.close_answers.setIcon(QtGui.QIcon(":/images/hide.png"))

                    for button in [self.questions.answer_4,
                                   self.questions.answer_3,
                                   self.questions.answer_2,
                                   self.questions.answer_1]:
                        button.setStyleSheet(

                            """QPushButton {
                            color: rgb(49, 52, 67);
                            border: none;
                            }"""

                        )
                        button.setEnabled(False)

                    self.index = 1

            elif items[1]["index"] == "words":

                self.questions.question.setText(items[0])

                answers = items[1]["answers"]
                random_answers = []
                while len(random_answers) != 3:

                    answers_r = help.RandomAnswers.random_answers_words
                    random_answer = random.SystemRandom().choice(answers_r)
                    if random_answer == items[1]["correct_answer"]:
                        continue
                    else:
                        if random_answer in random_answers:
                            continue
                        else:
                            random_answers.append(random_answer)

                for i in random_answers:
                    answers.append(i)

                random.SystemRandom().shuffle(answers)
                help.Helper.question_and_correct_answer = {}
                help.Helper.question_and_correct_answer.update({items[0]: items[1]["correct_answer"]})

                help.CorrectAndUncorrectAnswers.number_of_question += 1
                self.questions.score.setText(
                    f"{help.CorrectAndUncorrectAnswers.number_of_question}/{help.Helper.len_questions}")

                buttons = dict(zip(

                    [

                        self.questions.answer_1,
                        self.questions.answer_2,
                        self.questions.answer_3,
                        self.questions.answer_4

                    ],

                    answers

                ))

                for button in buttons:
                    button.setText(buttons[button])

                help.StylesheetsAnswers.stylesheets.update(
                    {
                        self.questions.answer_1: self.questions.answer_1.styleSheet(),
                        self.questions.answer_2: self.questions.answer_2.styleSheet(),
                        self.questions.answer_3: self.questions.answer_3.styleSheet(),
                        self.questions.answer_4: self.questions.answer_4.styleSheet()
                    }
                )

                if help.Settings_Q.status:

                    self.questions.close_answers.setIcon(QtGui.QIcon(":/images/hide.png"))

                    for button in [self.questions.answer_4,
                                   self.questions.answer_3,
                                   self.questions.answer_2,
                                   self.questions.answer_1]:
                        button.setStyleSheet(

                            """QPushButton {
                            color: rgb(49, 52, 67);
                            border: none;
                            }"""

                        )
                        button.setEnabled(False)

                    self.index = 1

    def mouseMoveEvent(self, event):
        self.clickPosition = event.globalPos()

    def mouseReleaseEvent(self, event):
        try:
            del self.clickPosition
        except AttributeError:
            pass

    def clicks(self):

        for button in [

            self.questions.answer_1,
            self.questions.answer_2,
            self.questions.answer_3,
            self.questions.answer_4

        ]:
            button.clicked.connect(self.logic_buttons)

        self.questions.end_test.clicked.connect(self.leave_of_the_test)
        self.questions.next.clicked.connect(self.check_answer)
        self.questions.info.clicked.connect(show_theme)
        self.questions.close_answers.clicked.connect(self.settings_answers)
        self.questions.settings_test.clicked.connect(self.settings_test)

        self.questions.close_window.clicked.connect(lambda: self.close())
        self.questions.minimize_window.clicked.connect(lambda: self.showMinimized())
        self.questions.restore_window.clicked.connect(lambda: self.restore_or_maximize_window())

    def restore_or_maximize_window(self):
        if self.isMaximized():
            self.showNormal()
            self.questions.restore_window.setIcon(QtGui.QIcon(":/images/expand_on.png"))
        else:
            self.showMaximized()
            self.questions.restore_window.setIcon(QtGui.QIcon(":/images/expand_off.png"))

    def logic_buttons(self):

        text, text_question = self.sender(), self.questions.question.text()

        if text.text() == help.Helper.question_and_correct_answer[text_question]:

            help.StatusAnswer.status = True

            buttons = {}

            for button in [

                self.questions.answer_1,
                self.questions.answer_2,
                self.questions.answer_3,
                self.questions.answer_4

            ]:
                if button.objectName() == text.objectName():
                    buttons.update(
                        {
                            f"button {button.objectName()[-1]}": {
                                "text": button.text(),
                                "stylesheet": """QPushButton {
                                              background-color: #2caa3f; 
                                              color: white;
                                              border: 2px solid #df6277;
                                              }"""
                            }
                        }
                    )
                else:
                    buttons.update(
                        {
                            f"button {button.objectName()[-1]}": {
                                "text": button.text(),
                                "stylesheet": button.styleSheet()
                            }
                        }
                    )

            help.Results.data.update(
                {
                    self.questions.score.text(): {
                        "question": text_question,
                        "buttons": buttons
                    }
                }
            )

            text.setStyleSheet(

                """QPushButton {
                background-color: #2caa3f; 
                color: white;
                border: 2px solid #df6277;
                }"""

            )

            help.CorrectAndUncorrectAnswers.correct += 1

            for button in [

                self.questions.answer_1,
                self.questions.answer_2,
                self.questions.answer_3,
                self.questions.answer_4

            ]:
                button.setEnabled(False)

            help.StylesheetsAnswers.stylesheets.update(
                {
                    self.questions.answer_1: self.questions.answer_1.styleSheet(),
                    self.questions.answer_2: self.questions.answer_2.styleSheet(),
                    self.questions.answer_3: self.questions.answer_3.styleSheet(),
                    self.questions.answer_4: self.questions.answer_4.styleSheet()
                }
            )

            if len(help.ThemesAndQuestions.themes[help.Helper.name_theme]) == 1:
                self.questions.next.setIcon(QtGui.QIcon(":/images/complete.png"))

        else:

            help.StatusAnswer.status = True
            help.CorrectAndUncorrectAnswers.uncorrect += 1

            buttons = {}

            for button in [

                self.questions.answer_1,
                self.questions.answer_2,
                self.questions.answer_3,
                self.questions.answer_4

            ]:
                if button.objectName() == text.objectName():
                    buttons.update(
                        {
                            f"button {button.objectName()[-1]}": {
                                "text": button.text(),
                                "stylesheet": """QPushButton {
                                              background-color: #d53f3f; 
                                              color: white;
                                              border: 2px solid #df6277
                                              }"""
                            }
                        }
                    )
                elif button.text() == help.Helper.question_and_correct_answer[text_question]:
                    buttons.update(
                        {
                            f"button {button.objectName()[-1]}": {
                                "text": button.text(),
                                "stylesheet": """QPushButton {
                                              background-color: #2caa3f; 
                                              color: white;
                                              border: 2px solid #df6277;
                                              }"""
                            }
                        }
                    )

                else:
                    buttons.update(
                        {
                            f"button {button.objectName()[-1]}": {
                                "text": button.text(),
                                "stylesheet": button.styleSheet()
                            }
                        }
                    )

            help.Results.data.update(
                {
                    self.questions.score.text(): {
                        "question": text_question,
                        "buttons": buttons
                    }
                }
            )

            text.setStyleSheet(

                """QPushButton {
                background-color: #d53f3f; 
                color: white;
                border: 2px solid #df6277
                }"""

            )

            for button in [

                self.questions.answer_1,
                self.questions.answer_2,
                self.questions.answer_3,
                self.questions.answer_4

            ]:
                if button.text() == help.Helper.question_and_correct_answer[text_question]:
                    button.setStyleSheet(

                        """QPushButton {
                        background-color: #2caa3f; 
                        color: white;
                        border: 2px solid #df6277;
                        }"""

                    )

            for button in [

                self.questions.answer_1,
                self.questions.answer_2,
                self.questions.answer_3,
                self.questions.answer_4

            ]:
                button.setEnabled(False)

            help.StylesheetsAnswers.stylesheets.update(
                {
                    self.questions.answer_1: self.questions.answer_1.styleSheet(),
                    self.questions.answer_2: self.questions.answer_2.styleSheet(),
                    self.questions.answer_3: self.questions.answer_3.styleSheet(),
                    self.questions.answer_4: self.questions.answer_4.styleSheet()
                }
            )

            if len(help.ThemesAndQuestions.themes[help.Helper.name_theme]) == 1:
                self.questions.next.setIcon(QtGui.QIcon(":/images/complete.png"))

        help.ThemesAndQuestions.themes[help.Helper.name_theme].pop(
            list(help.Helper.question_and_correct_answer.keys())[0])

    def check_answer(self):
        if self.index == 0:
            if help.StatusAnswer.status:
                help.StatusAnswer.status = False
                self.logic()
            else:
                pass
        else:
            pass

    def settings_answers(self):

        if self.index == 0:
            self.questions.close_answers.setIcon(QtGui.QIcon(":/images/hide.png"))

            for button in [self.questions.answer_4,
                           self.questions.answer_3,
                           self.questions.answer_2,
                           self.questions.answer_1]:
                button.setStyleSheet(

                    """QPushButton {
                    color: rgb(49, 52, 67);
                    border: none;
                    }"""

                )
                button.setEnabled(False)

            self.index = 1

        else:
            self.questions.close_answers.setIcon(QtGui.QIcon(":/images/show.png"))

            for button in help.StylesheetsAnswers.stylesheets:

                button.setStyleSheet(
                    help.StylesheetsAnswers.stylesheets[button]
                )
                if help.StatusAnswer.status:
                    button.setEnabled(False)
                else:
                    button.setEnabled(True)

            self.index = 0

    def settings_test(self):
        self.window = SettingsQuestion(self)
        self.window.setWindowFlags(self.window.windowFlags() | QtCore.Qt.Window)
        self.window.setWindowModality(QtCore.Qt.ApplicationModal)
        self.window.show()

    def leave_of_the_test(self):
        help.reset_all()
        self.close()
        self.window = files.History()
        self.window.show()


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
    def __init__(self, parent=None):
        super().__init__(parent)
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
        # self.setWindowModality(QtCore.Qt.ApplicationModal)
        # self.setWindowFlags(QtCore.Qt.SplashScreen | QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint)
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

    # def mousePressEvent(self, event):
    #     self.dragPos = self.pos()
    #     self.mouse_original_pos = self.mapToGlobal(event.pos())
    #
    # def mouseMoveEvent(self, event):
    #     if event.buttons() == QtCore.Qt.MouseButton.LeftButton:
    #         MainWindow_last_pos = self.dragPos + self.mapToGlobal(event.pos()) - self.mouse_original_pos
    #         self.move(MainWindow_last_pos)
    #         event.accept()

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