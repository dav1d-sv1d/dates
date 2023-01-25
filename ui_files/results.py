# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'results.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import photo_rc

class Ui_MainWindow_4(object):
    def setupUi(self, MainWindow_4):
        if not MainWindow_4.objectName():
            MainWindow_4.setObjectName(u"MainWindow_4")
        MainWindow_4.resize(917, 720)
        MainWindow_4.setMinimumSize(QSize(917, 720))
        MainWindow_4.setMaximumSize(QSize(917, 720))
        self.centralwidget = QWidget(MainWindow_4)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget {\n"
"background-color: rgb(49, 52, 67)\n"
"}\n"
"\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(45, 45, 68);\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"\n"
"/*  HANDLE BAR VERTICAL */\n"
"QScrollBar::handle:vertical {	\n"
"	background-color: rgb(80, 80, 122);\n"
"	min-height: 30px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:vertical:hover{	\n"
"	background-color: rgb(255, 0, 127);\n"
"}\n"
"QScrollBar::handle:vertical:pressed {	\n"
"	background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"	background-color: rgb(59, 59, 90);\n"
"	height: 15px;\n"
"	border-top-left-radius: 7px;\n"
"	border-top-right-radius: 7px;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {	\n"
"	background-color: rgb(255, 0, 127);\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {	\n"
"	background-color: rgb(185, 0, "
                        "92);\n"
"}\n"
"\n"
"/* BTN BOTTOM - SCROLLBAR */\n"
"QScrollBar::add-line:vertical {\n"
"	border: none;\n"
"	background-color: rgb(59, 59, 90);\n"
"	height: 15px;\n"
"	border-bottom-left-radius: 7px;\n"
"	border-bottom-right-radius: 7px;\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:hover {	\n"
"	background-color: rgb(255, 0, 127);\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {	\n"
"	background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"/* RESET ARROW */\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"	background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"	background: none;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, -1)
        self.header_frame = QFrame(self.centralwidget)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setMinimumSize(QSize(0, 30))
        self.header_frame.setMaximumSize(QSize(16777215, 30))
        self.header_frame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.header_frame.setFrameShape(QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.close_window = QPushButton(self.header_frame)
        self.close_window.setObjectName(u"close_window")
        self.close_window.setGeometry(QRect(890, 0, 30, 30))
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
        icon1 = QIcon()
        icon1.addFile(u":/images/close_window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_window.setIcon(icon1)
        self.close_window.setIconSize(QSize(15, 15))
        self.minimize_window = QPushButton(self.header_frame)
        self.minimize_window.setObjectName(u"minimize_window")
        self.minimize_window.setGeometry(QRect(860, 0, 30, 30))
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
        icon2 = QIcon()
        icon2.addFile(u":/images/fold_window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_window.setIcon(icon2)
        self.minimize_window.setIconSize(QSize(20, 20))
        self.icon = QPushButton(self.header_frame)
        self.icon.setObjectName(u"icon")
        self.icon.setGeometry(QRect(0, 0, 30, 30))
        self.icon.setMinimumSize(QSize(30, 30))
        self.icon.setStyleSheet(u"border: none;")
        icon3 = QIcon()
        icon3.addFile(u":/hs.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.icon.setIcon(icon3)
        self.icon.setIconSize(QSize(20, 20))

        self.verticalLayout.addWidget(self.header_frame)

        self.results = QFrame(self.centralwidget)
        self.results.setObjectName(u"results")
        self.results.setMinimumSize(QSize(0, 170))
        self.results.setMaximumSize(QSize(16777215, 170))
        self.results.setFrameShape(QFrame.StyledPanel)
        self.results.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.results)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(18, -1, 18, -1)
        self.leftframe = QFrame(self.results)
        self.leftframe.setObjectName(u"leftframe")
        self.leftframe.setFrameShape(QFrame.StyledPanel)
        self.leftframe.setFrameShadow(QFrame.Raised)
        self.iconuncorrect = QPushButton(self.leftframe)
        self.iconuncorrect.setObjectName(u"iconuncorrect")
        self.iconuncorrect.setEnabled(True)
        self.iconuncorrect.setGeometry(QRect(10, 30, 81, 61))
        font = QFont()
        font.setFamily(u"Tahoma")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.iconuncorrect.setFont(font)
        self.iconuncorrect.setStyleSheet(u"border:none")
        icon4 = QIcon()
        icon4.addFile(u":/images/uncorrect.png", QSize(), QIcon.Normal, QIcon.Off)
        self.iconuncorrect.setIcon(icon4)
        self.iconuncorrect.setIconSize(QSize(70, 70))
        self.iconcorrect = QPushButton(self.leftframe)
        self.iconcorrect.setObjectName(u"iconcorrect")
        self.iconcorrect.setEnabled(True)
        self.iconcorrect.setGeometry(QRect(10, 90, 81, 61))
        self.iconcorrect.setFont(font)
        self.iconcorrect.setStyleSheet(u"border:none")
        icon5 = QIcon()
        icon5.addFile(u":/images/correct.png", QSize(), QIcon.Normal, QIcon.Off)
        self.iconcorrect.setIcon(icon5)
        self.iconcorrect.setIconSize(QSize(70, 70))
        self.correctanswers = QLabel(self.leftframe)
        self.correctanswers.setObjectName(u"correctanswers")
        self.correctanswers.setGeometry(QRect(92, 40, 91, 41))
        self.correctanswers.setFont(font)
        self.correctanswers.setStyleSheet(u"color: white; border: 2px solid #df6277")
        self.correctanswers.setAlignment(Qt.AlignCenter)
        self.uncorrectanswers = QLabel(self.leftframe)
        self.uncorrectanswers.setObjectName(u"uncorrectanswers")
        self.uncorrectanswers.setGeometry(QRect(92, 100, 91, 41))
        self.uncorrectanswers.setFont(font)
        self.uncorrectanswers.setStyleSheet(u"color: white; border: 2px solid #df6277")
        self.uncorrectanswers.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.leftframe)

        self.rightframe = QFrame(self.results)
        self.rightframe.setObjectName(u"rightframe")
        self.rightframe.setStyleSheet(u"QToolTip {\n"
"\n"
"color: black;\n"
"background: white;\n"
"\n"
"}")
        self.rightframe.setFrameShape(QFrame.StyledPanel)
        self.rightframe.setFrameShadow(QFrame.Raised)
        self.inforesults = QPushButton(self.rightframe)
        self.inforesults.setObjectName(u"inforesults")
        self.inforesults.setGeometry(QRect(330, 10, 40, 40))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inforesults.sizePolicy().hasHeightForWidth())
        self.inforesults.setSizePolicy(sizePolicy)
        self.inforesults.setMinimumSize(QSize(40, 40))
        self.inforesults.setMaximumSize(QSize(40, 40))
        font1 = QFont()
        font1.setFamily(u"Tahoma")
        font1.setPointSize(16)
        font1.setBold(True)
        font1.setWeight(75)
        self.inforesults.setFont(font1)
        self.inforesults.setStyleSheet(u"QPushButton {\n"
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
        icon6.addFile(u":/images/question.png", QSize(), QIcon.Normal, QIcon.Off)
        self.inforesults.setIcon(icon6)
        self.inforesults.setIconSize(QSize(40, 40))
        self.back = QPushButton(self.rightframe)
        self.back.setObjectName(u"back")
        self.back.setGeometry(QRect(380, 10, 40, 40))
        self.back.setMinimumSize(QSize(0, 0))
        self.back.setMaximumSize(QSize(1541841, 16777215))
        self.back.setFont(font1)
        self.back.setStyleSheet(u"QPushButton {\n"
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
        icon7.addFile(u":/images/leave.png", QSize(), QIcon.Normal, QIcon.Off)
        self.back.setIcon(icon7)
        self.back.setIconSize(QSize(40, 40))

        self.horizontalLayout.addWidget(self.rightframe)


        self.verticalLayout.addWidget(self.results)

        self.frameforline = QFrame(self.centralwidget)
        self.frameforline.setObjectName(u"frameforline")
        sizePolicy.setHeightForWidth(self.frameforline.sizePolicy().hasHeightForWidth())
        self.frameforline.setSizePolicy(sizePolicy)
        self.frameforline.setMinimumSize(QSize(850, 10))
        self.frameforline.setMaximumSize(QSize(16777215, 16777215))
        self.frameforline.setFrameShape(QFrame.StyledPanel)
        self.frameforline.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frameforline)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.line = QFrame(self.frameforline)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_4.addWidget(self.line)


        self.verticalLayout.addWidget(self.frameforline, 0, Qt.AlignHCenter)

        self.answersquestions = QFrame(self.centralwidget)
        self.answersquestions.setObjectName(u"answersquestions")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.answersquestions.sizePolicy().hasHeightForWidth())
        self.answersquestions.setSizePolicy(sizePolicy1)
        self.answersquestions.setMinimumSize(QSize(0, 0))
        self.answersquestions.setMaximumSize(QSize(16777215, 16777215))
        self.answersquestions.setFrameShape(QFrame.StyledPanel)
        self.answersquestions.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.answersquestions)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(18, -1, 18, -1)
        self.scrollArea = QScrollArea(self.answersquestions)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy2)
        self.scrollArea.setStyleSheet(u" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(45, 45, 68);\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"\n"
"/*  HANDLE BAR VERTICAL */\n"
"QScrollBar::handle:vertical {	\n"
"	background-color: rgb(80, 80, 122);\n"
"	min-height: 30px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:vertical:hover{	\n"
"	background-color: rgb(255, 0, 127);\n"
"}\n"
"QScrollBar::handle:vertical:pressed {	\n"
"	background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"	background-color: rgb(59, 59, 90);\n"
"	height: 15px;\n"
"	border-top-left-radius: 7px;\n"
"	border-top-right-radius: 7px;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {	\n"
"	background-color: rgb(255, 0, 127);\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {	\n"
"	background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"/* BTN BOTTOM - SCROLLBAR */\n"
"QScrollBar"
                        "::add-line:vertical {\n"
"	border: none;\n"
"	background-color: rgb(59, 59, 90);\n"
"	height: 15px;\n"
"	border-bottom-left-radius: 7px;\n"
"	border-bottom-right-radius: 7px;\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:hover {	\n"
"	background-color: rgb(255, 0, 127);\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {	\n"
"	background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"/* RESET ARROW */\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"	background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"	background: none;\n"
"}")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 865, 1018))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widgets = QFrame(self.scrollAreaWidgetContents)
        self.widgets.setObjectName(u"widgets")
        sizePolicy1.setHeightForWidth(self.widgets.sizePolicy().hasHeightForWidth())
        self.widgets.setSizePolicy(sizePolicy1)
        self.widgets.setMinimumSize(QSize(0, 1000))
        self.widgets.setFrameShape(QFrame.StyledPanel)
        self.widgets.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.widgets)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_3.addWidget(self.scrollArea)


        self.verticalLayout.addWidget(self.answersquestions)

        MainWindow_4.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow_4)

        QMetaObject.connectSlotsByName(MainWindow_4)
    # setupUi

    def retranslateUi(self, MainWindow_4):
        MainWindow_4.setWindowTitle(QCoreApplication.translate("MainWindow_4", u"MainWindow", None))
        self.close_window.setText("")
        self.minimize_window.setText("")
        self.icon.setText("")
#if QT_CONFIG(tooltip)
        self.iconuncorrect.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.iconuncorrect.setText("")
#if QT_CONFIG(tooltip)
        self.iconcorrect.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.iconcorrect.setText("")
        self.correctanswers.setText("")
        self.uncorrectanswers.setText("")
#if QT_CONFIG(tooltip)
        self.inforesults.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.inforesults.setText("")
#if QT_CONFIG(tooltip)
        self.back.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.back.setText("")
    # retranslateUi

