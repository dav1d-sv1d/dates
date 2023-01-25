# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'questions.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import photo_rc

class Ui_MainWindow_3(object):
    def setupUi(self, MainWindow_3):
        if not MainWindow_3.objectName():
            MainWindow_3.setObjectName(u"MainWindow_3")
        MainWindow_3.resize(888, 720)
        MainWindow_3.setMinimumSize(QSize(888, 720))
        MainWindow_3.setMaximumSize(QSize(16777215, 16777215))
        self.centralwidget = QWidget(MainWindow_3)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(49, 52, 67)")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_frame = QFrame(self.centralwidget)
        self.header_frame.setObjectName(u"header_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.header_frame.sizePolicy().hasHeightForWidth())
        self.header_frame.setSizePolicy(sizePolicy)
        self.header_frame.setMinimumSize(QSize(0, 30))
        self.header_frame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.header_frame.setFrameShape(QFrame.NoFrame)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.header_frame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.header_frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(30, 30))
        self.pushButton.setMaximumSize(QSize(30, 30))
        self.pushButton.setStyleSheet(u"border: none;")
        icon = QIcon()
        icon.addFile(u":/hs.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_5.addWidget(self.pushButton, 0, Qt.AlignLeft)

        self.frame_2 = QFrame(self.header_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(90, 30))
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(5, 0, 0, 0)
        self.minimize_window = QPushButton(self.frame_2)
        self.minimize_window.setObjectName(u"minimize_window")
        self.minimize_window.setMinimumSize(QSize(30, 30))
        self.minimize_window.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #ABABAB;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #C5C5C5;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/images/fold_window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_window.setIcon(icon1)
        self.minimize_window.setIconSize(QSize(20, 20))

        self.horizontalLayout_6.addWidget(self.minimize_window, 0, Qt.AlignRight)

        self.restore_window = QPushButton(self.frame_2)
        self.restore_window.setObjectName(u"restore_window")
        self.restore_window.setMinimumSize(QSize(30, 30))
        self.restore_window.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #ABABAB;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #C5C5C5;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/images/expand_on.png", QSize(), QIcon.Normal, QIcon.Off)
        self.restore_window.setIcon(icon2)
        self.restore_window.setIconSize(QSize(15, 15))

        self.horizontalLayout_6.addWidget(self.restore_window, 0, Qt.AlignRight)

        self.close_window = QPushButton(self.frame_2)
        self.close_window.setObjectName(u"close_window")
        self.close_window.setMinimumSize(QSize(30, 30))
        self.close_window.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #ABABAB;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #C5C5C5;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/images/close_window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_window.setIcon(icon3)
        self.close_window.setIconSize(QSize(15, 15))

        self.horizontalLayout_6.addWidget(self.close_window, 0, Qt.AlignRight)


        self.horizontalLayout_5.addWidget(self.frame_2, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.header_frame)

        self.upframe = QFrame(self.centralwidget)
        self.upframe.setObjectName(u"upframe")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.upframe.sizePolicy().hasHeightForWidth())
        self.upframe.setSizePolicy(sizePolicy1)
        self.upframe.setMinimumSize(QSize(870, 0))
        self.upframe.setMaximumSize(QSize(16777215, 60))
        self.upframe.setFrameShape(QFrame.StyledPanel)
        self.upframe.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.upframe)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(20, 0, 20, 0)
        self.frameofscore = QFrame(self.upframe)
        self.frameofscore.setObjectName(u"frameofscore")
        self.frameofscore.setFrameShape(QFrame.StyledPanel)
        self.frameofscore.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frameofscore)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 20, -1, -1)
        self.score = QLabel(self.frameofscore)
        self.score.setObjectName(u"score")
        self.score.setMinimumSize(QSize(101, 31))
        font = QFont()
        font.setFamily(u"Tahoma")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.score.setFont(font)
        self.score.setStyleSheet(u"color: white;\n"
"border: 2px solid #df6277")
        self.score.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.score, 0, Qt.AlignLeft)


        self.horizontalLayout.addWidget(self.frameofscore)

        self.frameofdescription = QFrame(self.upframe)
        self.frameofdescription.setObjectName(u"frameofdescription")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frameofdescription.sizePolicy().hasHeightForWidth())
        self.frameofdescription.setSizePolicy(sizePolicy2)
        self.frameofdescription.setMaximumSize(QSize(16777215, 55))
        self.frameofdescription.setFrameShape(QFrame.StyledPanel)
        self.frameofdescription.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frameofdescription)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(200, -1, -1, -1)
        self.settings_test = QPushButton(self.frameofdescription)
        self.settings_test.setObjectName(u"settings_test")
        self.settings_test.setMinimumSize(QSize(40, 40))
        self.settings_test.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(55, 58, 75);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(47, 50, 65);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/images/settings_test.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settings_test.setIcon(icon4)
        self.settings_test.setIconSize(QSize(40, 40))

        self.horizontalLayout_3.addWidget(self.settings_test)

        self.info = QPushButton(self.frameofdescription)
        self.info.setObjectName(u"info")
        sizePolicy1.setHeightForWidth(self.info.sizePolicy().hasHeightForWidth())
        self.info.setSizePolicy(sizePolicy1)
        self.info.setMinimumSize(QSize(40, 40))
        self.info.setMaximumSize(QSize(40, 16777215))
        self.info.setFont(font)
        self.info.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(55, 58, 75);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(47, 50, 65);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/images/question.png", QSize(), QIcon.Normal, QIcon.Off)
        self.info.setIcon(icon5)
        self.info.setIconSize(QSize(40, 40))

        self.horizontalLayout_3.addWidget(self.info, 0, Qt.AlignRight|Qt.AlignBottom)

        self.end_test = QPushButton(self.frameofdescription)
        self.end_test.setObjectName(u"end_test")
        self.end_test.setMinimumSize(QSize(40, 40))
        self.end_test.setFont(font)
        self.end_test.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(55, 58, 75);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(47, 50, 65);\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/images/leave.png", QSize(), QIcon.Normal, QIcon.Off)
        self.end_test.setIcon(icon6)
        self.end_test.setIconSize(QSize(40, 40))

        self.horizontalLayout_3.addWidget(self.end_test, 0, Qt.AlignRight)


        self.horizontalLayout.addWidget(self.frameofdescription)


        self.verticalLayout.addWidget(self.upframe, 0, Qt.AlignHCenter)

        self.centralframe = QFrame(self.centralwidget)
        self.centralframe.setObjectName(u"centralframe")
        self.centralframe.setFrameShape(QFrame.StyledPanel)
        self.centralframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.centralframe)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 0, -1, 0)
        self.frameofquestion = QFrame(self.centralframe)
        self.frameofquestion.setObjectName(u"frameofquestion")
        sizePolicy1.setHeightForWidth(self.frameofquestion.sizePolicy().hasHeightForWidth())
        self.frameofquestion.setSizePolicy(sizePolicy1)
        self.frameofquestion.setFrameShape(QFrame.StyledPanel)
        self.frameofquestion.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frameofquestion)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.framequestion = QFrame(self.frameofquestion)
        self.framequestion.setObjectName(u"framequestion")
        sizePolicy1.setHeightForWidth(self.framequestion.sizePolicy().hasHeightForWidth())
        self.framequestion.setSizePolicy(sizePolicy1)
        self.framequestion.setMinimumSize(QSize(811, 201))
        self.framequestion.setMaximumSize(QSize(811, 201))
        self.framequestion.setLayoutDirection(Qt.RightToLeft)
        self.framequestion.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.framequestion.setFrameShape(QFrame.NoFrame)
        self.framequestion.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.framequestion)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.question = QLabel(self.framequestion)
        self.question.setObjectName(u"question")
        font1 = QFont()
        font1.setFamily(u"Tahoma")
        font1.setPointSize(20)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setWeight(75)
        font1.setStrikeOut(False)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.question.setFont(font1)
        self.question.setStyleSheet(u"color: black;")
        self.question.setTextFormat(Qt.AutoText)
        self.question.setAlignment(Qt.AlignCenter)
        self.question.setWordWrap(True)

        self.verticalLayout_7.addWidget(self.question)


        self.verticalLayout_6.addWidget(self.framequestion)


        self.verticalLayout_5.addWidget(self.frameofquestion, 0, Qt.AlignHCenter)

        self.second_frame = QFrame(self.centralframe)
        self.second_frame.setObjectName(u"second_frame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.second_frame.sizePolicy().hasHeightForWidth())
        self.second_frame.setSizePolicy(sizePolicy3)
        self.second_frame.setMaximumSize(QSize(16777215, 16777215))
        self.second_frame.setFrameShape(QFrame.StyledPanel)
        self.second_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.second_frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(16, 0, 26, 0)
        self.leftbuttonsframe = QFrame(self.second_frame)
        self.leftbuttonsframe.setObjectName(u"leftbuttonsframe")
        self.leftbuttonsframe.setFrameShape(QFrame.StyledPanel)
        self.leftbuttonsframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.leftbuttonsframe)
        self.verticalLayout_8.setSpacing(15)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.answer_1 = QPushButton(self.leftbuttonsframe)
        self.answer_1.setObjectName(u"answer_1")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.answer_1.sizePolicy().hasHeightForWidth())
        self.answer_1.setSizePolicy(sizePolicy4)
        self.answer_1.setMinimumSize(QSize(401, 161))
        font2 = QFont()
        font2.setFamily(u"Tahoma")
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setWeight(75)
        self.answer_1.setFont(font2)
        self.answer_1.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"border: 2px solid #df6277;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #272739;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #323248;\n"
"}")

        self.verticalLayout_8.addWidget(self.answer_1)

        self.answer_2 = QPushButton(self.leftbuttonsframe)
        self.answer_2.setObjectName(u"answer_2")
        sizePolicy4.setHeightForWidth(self.answer_2.sizePolicy().hasHeightForWidth())
        self.answer_2.setSizePolicy(sizePolicy4)
        self.answer_2.setMinimumSize(QSize(401, 161))
        self.answer_2.setFont(font2)
        self.answer_2.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"border: 2px solid #df6277;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #272739;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #323248;\n"
"}")

        self.verticalLayout_8.addWidget(self.answer_2)


        self.horizontalLayout_2.addWidget(self.leftbuttonsframe)

        self.rightbuttonsframe = QFrame(self.second_frame)
        self.rightbuttonsframe.setObjectName(u"rightbuttonsframe")
        self.rightbuttonsframe.setFrameShape(QFrame.StyledPanel)
        self.rightbuttonsframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.rightbuttonsframe)
        self.verticalLayout_9.setSpacing(15)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(-1, -1, 0, -1)
        self.answer_3 = QPushButton(self.rightbuttonsframe)
        self.answer_3.setObjectName(u"answer_3")
        sizePolicy4.setHeightForWidth(self.answer_3.sizePolicy().hasHeightForWidth())
        self.answer_3.setSizePolicy(sizePolicy4)
        self.answer_3.setMinimumSize(QSize(401, 161))
        self.answer_3.setFont(font2)
        self.answer_3.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"border: 2px solid #df6277;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #272739;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #323248;\n"
"}")

        self.verticalLayout_9.addWidget(self.answer_3)

        self.answer_4 = QPushButton(self.rightbuttonsframe)
        self.answer_4.setObjectName(u"answer_4")
        sizePolicy4.setHeightForWidth(self.answer_4.sizePolicy().hasHeightForWidth())
        self.answer_4.setSizePolicy(sizePolicy4)
        self.answer_4.setMinimumSize(QSize(401, 161))
        self.answer_4.setFont(font2)
        self.answer_4.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"border: 2px solid #df6277;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #272739;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #323248;\n"
"}")

        self.verticalLayout_9.addWidget(self.answer_4)


        self.horizontalLayout_2.addWidget(self.rightbuttonsframe)


        self.verticalLayout_5.addWidget(self.second_frame)


        self.verticalLayout.addWidget(self.centralframe)

        self.downframe = QFrame(self.centralwidget)
        self.downframe.setObjectName(u"downframe")
        sizePolicy1.setHeightForWidth(self.downframe.sizePolicy().hasHeightForWidth())
        self.downframe.setSizePolicy(sizePolicy1)
        self.downframe.setMaximumSize(QSize(16777215, 65))
        self.downframe.setFrameShape(QFrame.StyledPanel)
        self.downframe.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.downframe)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(600, 0, 40, 0)
        self.close_answers = QPushButton(self.downframe)
        self.close_answers.setObjectName(u"close_answers")
        sizePolicy1.setHeightForWidth(self.close_answers.sizePolicy().hasHeightForWidth())
        self.close_answers.setSizePolicy(sizePolicy1)
        self.close_answers.setMinimumSize(QSize(40, 40))
        self.close_answers.setMaximumSize(QSize(16777215, 16777215))
        font3 = QFont()
        font3.setFamily(u"Tahoma")
        font3.setPointSize(16)
        self.close_answers.setFont(font3)
        self.close_answers.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(55, 58, 75);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(47, 50, 65);\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/images/show.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_answers.setIcon(icon7)
        self.close_answers.setIconSize(QSize(40, 40))

        self.horizontalLayout_4.addWidget(self.close_answers)

        self.next = QPushButton(self.downframe)
        self.next.setObjectName(u"next")
        self.next.setMinimumSize(QSize(39, 39))
        font4 = QFont()
        font4.setFamily(u"Tahoma")
        font4.setPointSize(20)
        font4.setBold(True)
        font4.setWeight(75)
        self.next.setFont(font4)
        self.next.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(55, 58, 75);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(47, 50, 65);\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/images/next.png", QSize(), QIcon.Normal, QIcon.Off)
        self.next.setIcon(icon8)
        self.next.setIconSize(QSize(40, 40))

        self.horizontalLayout_4.addWidget(self.next, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.downframe, 0, Qt.AlignRight)

        self.size_grid = QFrame(self.centralwidget)
        self.size_grid.setObjectName(u"size_grid")
        self.size_grid.setMinimumSize(QSize(5, 5))
        self.size_grid.setMaximumSize(QSize(5, 5))
        self.size_grid.setFrameShape(QFrame.StyledPanel)
        self.size_grid.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.size_grid, 0, Qt.AlignRight)

        MainWindow_3.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow_3)

        QMetaObject.connectSlotsByName(MainWindow_3)
    # setupUi

    def retranslateUi(self, MainWindow_3):
        MainWindow_3.setWindowTitle(QCoreApplication.translate("MainWindow_3", u"MainWindow", None))
        self.pushButton.setText("")
        self.minimize_window.setText("")
        self.restore_window.setText("")
        self.close_window.setText("")
        self.score.setText("")
        self.settings_test.setText("")
#if QT_CONFIG(tooltip)
        self.info.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.info.setText("")
#if QT_CONFIG(tooltip)
        self.end_test.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.end_test.setText("")
#if QT_CONFIG(shortcut)
        self.end_test.setShortcut(QCoreApplication.translate("MainWindow_3", u"Esc", None))
#endif // QT_CONFIG(shortcut)
        self.question.setText("")
#if QT_CONFIG(tooltip)
        self.answer_1.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.answer_1.setText("")
#if QT_CONFIG(tooltip)
        self.answer_2.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.answer_2.setText("")
#if QT_CONFIG(tooltip)
        self.answer_3.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.answer_3.setText("")
#if QT_CONFIG(tooltip)
        self.answer_4.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.answer_4.setText("")
        self.close_answers.setText("")
#if QT_CONFIG(tooltip)
        self.next.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.next.setText("")
#if QT_CONFIG(shortcut)
        self.next.setShortcut(QCoreApplication.translate("MainWindow_3", u"Return", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

