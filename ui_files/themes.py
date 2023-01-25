# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'themes.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import photo_rc

class Ui_MainWindow_2(object):
    def setupUi(self, MainWindow_2):
        if not MainWindow_2.objectName():
            MainWindow_2.setObjectName(u"MainWindow_2")
        MainWindow_2.setEnabled(True)
        MainWindow_2.resize(425, 649)
        MainWindow_2.setMinimumSize(QSize(425, 649))
        MainWindow_2.setMaximumSize(QSize(425, 649))
        MainWindow_2.setAutoFillBackground(False)
        MainWindow_2.setStyleSheet(u"background-color: rgb(40, 42, 54);\n"
"\n"
"")
        MainWindow_2.setInputMethodHints(Qt.ImhNone)
        MainWindow_2.setDocumentMode(False)
        MainWindow_2.setDockNestingEnabled(False)
        self.help = QAction(MainWindow_2)
        self.help.setObjectName(u"help")
        icon1 = QIcon()
        icon1.addFile(u":/images/help.png", QSize(), QIcon.Normal, QIcon.Off)
        self.help.setIcon(icon1)
        self.develop = QAction(MainWindow_2)
        self.develop.setObjectName(u"develop")
        icon2 = QIcon()
        icon2.addFile(u":/images/developer.png", QSize(), QIcon.Normal, QIcon.Off)
        self.develop.setIcon(icon2)
        self.centralwidget = QWidget(MainWindow_2)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(0, 0))
        self.centralwidget.setMaximumSize(QSize(16777215, 16777215))
        self.centralwidget.setStyleSheet(u"QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(45, 45, 68);\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"	border-radius: 7px;\n"
" }\n"
"\n"
"/*  HANDLE BAR VERTICAL */\n"
"QScrollBar::handle:vertical {	\n"
"	background-color: rgb(80, 80, 122);\n"
"	min-height: 30px;\n"
"	border-radius: 7px;\n"
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
"	height: 0px;\n"
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
"QScrollBar::"
                        "add-line:vertical {\n"
"	border: none;\n"
"	background-color: rgb(59, 59, 90);\n"
"	height: 0px;\n"
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
"}\n"
"\n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, -1)
        self.header_frame = QFrame(self.centralwidget)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setMinimumSize(QSize(0, 0))
        self.header_frame.setMaximumSize(QSize(16777215, 30))
        self.header_frame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.header_frame.setFrameShape(QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.close_window = QPushButton(self.header_frame)
        self.close_window.setObjectName(u"close_window")
        self.close_window.setGeometry(QRect(396, 0, 30, 30))
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
        self.minimize_window = QPushButton(self.header_frame)
        self.minimize_window.setObjectName(u"minimize_window")
        self.minimize_window.setGeometry(QRect(365, 0, 30, 30))
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
        icon4 = QIcon()
        icon4.addFile(u":/images/fold_window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_window.setIcon(icon4)
        self.minimize_window.setIconSize(QSize(20, 20))
        self.icon = QPushButton(self.header_frame)
        self.icon.setObjectName(u"icon")
        self.icon.setGeometry(QRect(0, 0, 30, 30))
        self.icon.setMinimumSize(QSize(30, 30))
        self.icon.setStyleSheet(u"border: none;")
        icon5 = QIcon()
        icon5.addFile(u":/hs.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.icon.setIcon(icon5)
        self.icon.setIconSize(QSize(20, 20))

        self.verticalLayout.addWidget(self.header_frame)

        self.background_2 = QFrame(self.centralwidget)
        self.background_2.setObjectName(u"background_2")
        self.background_2.setEnabled(True)
        font = QFont()
        font.setKerning(False)
        self.background_2.setFont(font)
        self.background_2.setFrameShape(QFrame.NoFrame)
        self.background_2.setFrameShadow(QFrame.Raised)
        self.scrollArea = QScrollArea(self.background_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setEnabled(True)
        self.scrollArea.setGeometry(QRect(0, 0, 405, 605))
        self.scrollArea.setAutoFillBackground(False)
        self.scrollArea.setStyleSheet(u" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(45, 45, 68);\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"	border-radius: 7px;\n"
" }\n"
"\n"
"/*  HANDLE BAR VERTICAL */\n"
"QScrollBar::handle:vertical {	\n"
"	background-color: rgb(80, 80, 122);\n"
"	min-height: 30px;\n"
"	border-radius: 7px;\n"
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
"	height: 0px;\n"
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
"QScrollBar:"
                        ":add-line:vertical {\n"
"	border: none;\n"
"	background-color: rgb(59, 59, 90);\n"
"	height: 0px;\n"
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
"}\n"
"\n"
"\n"
"")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -3863, 391, 4468))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(20, -1, 0, -1)
        self.background = QFrame(self.scrollAreaWidgetContents)
        self.background.setObjectName(u"background")
        self.background.setEnabled(True)
        self.background.setMinimumSize(QSize(0, 4450))
        self.background.setStyleSheet(u"background-color: rgb(40, 42, 54);")
        self.background.setFrameShape(QFrame.StyledPanel)
        self.background.setFrameShadow(QFrame.Raised)
        self.background_3 = QFrame(self.background)
        self.background_3.setObjectName(u"background_3")
        self.background_3.setGeometry(QRect(0, 110, 361, 72))
        self.background_3.setStyleSheet(u"background-color: #df6277;")
        self.background_3.setFrameShape(QFrame.StyledPanel)
        self.background_3.setFrameShadow(QFrame.Raised)
        self.text_3 = QLabel(self.background_3)
        self.text_3.setObjectName(u"text_3")
        self.text_3.setGeometry(QRect(18, 1, 321, 67))
        font1 = QFont()
        font1.setFamily(u"Tahoma")
        font1.setPointSize(16)
        font1.setBold(True)
        font1.setWeight(75)
        self.text_3.setFont(font1)
        self.text_3.setStyleSheet(u"color: white;")
        self.text_3.setAlignment(Qt.AlignCenter)
        self.theme_1 = QPushButton(self.background)
        self.theme_1.setObjectName(u"theme_1")
        self.theme_1.setGeometry(QRect(0, 200, 361, 71))
        self.theme_1.setFont(font1)
        self.theme_1.setToolTipDuration(-1)
        self.theme_1.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"border: 2px solid #df6277;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #2b2b3e;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #323248;\n"
"}")
        self.theme_3 = QPushButton(self.background)
        self.theme_3.setObjectName(u"theme_3")
        self.theme_3.setGeometry(QRect(0, 380, 361, 71))
        self.theme_3.setFont(font1)
        self.theme_3.setToolTipDuration(-1)
        self.theme_3.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"border: 2px solid #df6277;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #2b2b3e;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #323248;\n"
"}")
        self.theme_4 = QPushButton(self.background)
        self.theme_4.setObjectName(u"theme_4")
        self.theme_4.setGeometry(QRect(0, 470, 361, 131))
        self.theme_4.setFont(font1)
        self.theme_4.setToolTipDuration(-1)
        self.theme_4.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"border: 2px solid #df6277;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #2b2b3e;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #323248;\n"
"}")
        self.theme_2 = QPushButton(self.background)
        self.theme_2.setObjectName(u"theme_2")
        self.theme_2.setGeometry(QRect(0, 290, 361, 71))
        self.theme_2.setFont(font1)
        self.theme_2.setToolTipDuration(-1)
        self.theme_2.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"border: 2px solid #df6277;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #2b2b3e;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #323248;\n"
"}")
        self.background_4 = QFrame(self.background)
        self.background_4.setObjectName(u"background_4")
        self.background_4.setGeometry(QRect(0, 700, 361, 72))
        self.background_4.setStyleSheet(u"background-color: #df6277;")
        self.background_4.setFrameShape(QFrame.StyledPanel)
        self.background_4.setFrameShadow(QFrame.Raised)
        self.text_4 = QLabel(self.background_4)
        self.text_4.setObjectName(u"text_4")
        self.text_4.setGeometry(QRect(20, 1, 321, 67))
        self.text_4.setFont(font1)
        self.text_4.setStyleSheet(u"color: white;")
        self.text_4.setAlignment(Qt.AlignCenter)
        self.line = QFrame(self.background)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 640, 361, 20))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.theme_5 = QPushButton(self.background)
        self.theme_5.setObjectName(u"theme_5")
        self.theme_5.setGeometry(QRect(0, 790, 361, 101))
        self.theme_5.setFont(font1)
        self.theme_5.setToolTipDuration(-1)
        self.theme_5.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"border: 2px solid #df6277;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #2b2b3e;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #323248;\n"
"}")
        self.theme_6 = QPushButton(self.background)
        self.theme_6.setObjectName(u"theme_6")
        self.theme_6.setGeometry(QRect(0, 910, 361, 101))
        self.theme_6.setFont(font1)
        self.theme_6.setToolTipDuration(-1)
        self.theme_6.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"border: 2px solid #df6277;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #2b2b3e;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #323248;\n"
"}")
        self.theme_7 = QPushButton(self.background)
        self.theme_7.setObjectName(u"theme_7")
        self.theme_7.setGeometry(QRect(0, 1030, 361, 101))
        self.theme_7.setFont(font1)
        self.theme_7.setToolTipDuration(-1)
        self.theme_7.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"border: 2px solid #df6277;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #2b2b3e;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #323248;\n"
"}")
        self.theme_8 = QPushButton(self.background)
        self.theme_8.setObjectName(u"theme_8")
        self.theme_8.setGeometry(QRect(0, 1150, 361, 91))
        self.theme_8.setFont(font1)
        self.theme_8.setToolTipDuration(-1)
        self.theme_8.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"border: 2px solid #df6277;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #2b2b3e;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #323248;\n"
"}")
        self.theme_9 = QPushButton(self.background)
        self.theme_9.setObjectName(u"theme_9")
        self.theme_9.setGeometry(QRect(0, 1260, 361, 101))
        self.theme_9.setFont(font1)
        self.theme_9.setToolTipDuration(-1)
        self.theme_9.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"border: 2px solid #df6277;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #2b2b3e;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #323248;\n"
"}")
        self.theme_10 = QPushButton(self.background)
        self.theme_10.setObjectName(u"theme_10")
        self.theme_10.setGeometry(QRect(0, 1380, 361, 81))
        self.theme_10.setFont(font1)
        self.theme_10.setToolTipDuration(-1)
        self.theme_10.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"border: 2px solid #df6277;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #2b2b3e;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #323248;\n"
"}")
        self.background_5 = QFrame(self.background)
        self.background_5.setObjectName(u"background_5")
        self.background_5.setGeometry(QRect(0, 1560, 361, 72))
        self.background_5.setStyleSheet(u"background-color: #df6277;")
        self.background_5.setFrameShape(QFrame.StyledPanel)
        self.background_5.setFrameShadow(QFrame.Raised)
        self.text_5 = QLabel(self.background_5)
        self.text_5.setObjectName(u"text_5")
        self.text_5.setGeometry(QRect(34, 1, 301, 67))
        self.text_5.setFont(font1)
        self.text_5.setStyleSheet(u"color: white;")
        self.text_5.setAlignment(Qt.AlignCenter)
        self.line_2 = QFrame(self.background)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(0, 1500, 361, 20))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.theme_11 = QPushButton(self.background)
        self.theme_11.setObjectName(u"theme_11")
        self.theme_11.setGeometry(QRect(0, 1650, 361, 131))
        self.theme_11.setFont(font1)
        self.theme_11.setToolTipDuration(-1)
        self.theme_11.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"border: 2px solid #df6277;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #2b2b3e;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #323248;\n"
"}")
        self.theme_12 = QPushButton(self.background)
        self.theme_12.setObjectName(u"theme_12")
        self.theme_12.setGeometry(QRect(0, 1800, 361, 131))
        self.theme_12.setFont(font1)
        self.theme_12.setToolTipDuration(-1)
        self.theme_12.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"border: 2px solid #df6277;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #2b2b3e;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #323248;\n"
"}")
        self.theme_13 = QPushButton(self.background)
        self.theme_13.setObjectName(u"theme_13")
        self.theme_13.setGeometry(QRect(0, 1950, 361, 101))
        self.theme_13.setFont(font1)
        self.theme_13.setToolTipDuration(-1)
        self.theme_13.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"border: 2px solid #df6277;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #2b2b3e;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #323248;\n"
"}")
        self.theme_14 = QPushButton(self.background)
        self.theme_14.setObjectName(u"theme_14")
        self.theme_14.setGeometry(QRect(0, 2070, 361, 101))
        self.theme_14.setFont(font1)
        self.theme_14.setToolTipDuration(-1)
        self.theme_14.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"border: 2px solid #df6277;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #2b2b3e;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #323248;\n"
"}")
        self.theme_15 = QPushButton(self.background)
        self.theme_15.setObjectName(u"theme_15")
        self.theme_15.setGeometry(QRect(0, 2190, 361, 101))
        self.theme_15.setFont(font1)
        self.theme_15.setToolTipDuration(-1)
        self.theme_15.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"border: 2px solid #df6277;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #2b2b3e;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #323248;\n"
"}")
        self.theme_16 = QPushButton(self.background)
        self.theme_16.setObjectName(u"theme_16")
        self.theme_16.setGeometry(QRect(0, 2310, 361, 101))
        self.theme_16.setFont(font1)
        self.theme_16.setToolTipDuration(-1)
        self.theme_16.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"border: 2px solid #df6277;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #2b2b3e;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #323248;\n"
"}")
        self.theme_17 = QPushButton(self.background)
        self.theme_17.setObjectName(u"theme_17")
        self.theme_17.setGeometry(QRect(0, 2430, 361, 101))
        self.theme_17.setFont(font1)
        self.theme_17.setToolTipDuration(-1)
        self.theme_17.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"border: 2px solid #df6277;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #2b2b3e;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #323248;\n"
"}")
        self.theme_18 = QPushButton(self.background)
        self.theme_18.setObjectName(u"theme_18")
        self.theme_18.setGeometry(QRect(0, 2550, 361, 101))
        self.theme_18.setFont(font1)
        self.theme_18.setToolTipDuration(-1)
        self.theme_18.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"border: 2px solid #df6277;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #2b2b3e;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #323248;\n"
"}")
        self.background_6 = QFrame(self.background)
        self.background_6.setObjectName(u"background_6")
        self.background_6.setGeometry(QRect(0, 2750, 361, 72))
        self.background_6.setStyleSheet(u"background-color: #df6277;")
        self.background_6.setFrameShape(QFrame.StyledPanel)
        self.background_6.setFrameShadow(QFrame.Raised)
        self.text_7 = QLabel(self.background_6)
        self.text_7.setObjectName(u"text_7")
        self.text_7.setGeometry(QRect(106, 1, 161, 67))
        self.text_7.setFont(font1)
        self.text_7.setStyleSheet(u"color: white;")
        self.text_7.setAlignment(Qt.AlignCenter)
        self.line_3 = QFrame(self.background)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(0, 2690, 361, 20))
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.theme_19 = QPushButton(self.background)
        self.theme_19.setObjectName(u"theme_19")
        self.theme_19.setGeometry(QRect(0, 2840, 361, 71))
        self.theme_19.setFont(font1)
        self.theme_19.setToolTipDuration(-1)
        self.theme_19.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"border: 2px solid #df6277;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #2b2b3e;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #323248;\n"
"}")
        self.theme_20 = QPushButton(self.background)
        self.theme_20.setObjectName(u"theme_20")
        self.theme_20.setGeometry(QRect(0, 2930, 361, 71))
        self.theme_20.setFont(font1)
        self.theme_20.setToolTipDuration(-1)
        self.theme_20.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"border: 2px solid #df6277;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #2b2b3e;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #323248;\n"
"}")
        self.theme_21 = QPushButton(self.background)
        self.theme_21.setObjectName(u"theme_21")
        self.theme_21.setGeometry(QRect(0, 3020, 361, 121))
        self.theme_21.setFont(font1)
        self.theme_21.setToolTipDuration(-1)
        self.theme_21.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"border: 2px solid #df6277;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #2b2b3e;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #323248;\n"
"}")
        self.theme_22 = QPushButton(self.background)
        self.theme_22.setObjectName(u"theme_22")
        self.theme_22.setGeometry(QRect(0, 3160, 361, 131))
        self.theme_22.setFont(font1)
        self.theme_22.setToolTipDuration(-1)
        self.theme_22.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"border: 2px solid #df6277;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #2b2b3e;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #323248;\n"
"}")
        self.theme_23 = QPushButton(self.background)
        self.theme_23.setObjectName(u"theme_23")
        self.theme_23.setGeometry(QRect(0, 3310, 361, 131))
        self.theme_23.setFont(font1)
        self.theme_23.setToolTipDuration(-1)
        self.theme_23.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"border: 2px solid #df6277;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #2b2b3e;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #323248;\n"
"}")
        self.theme_24 = QPushButton(self.background)
        self.theme_24.setObjectName(u"theme_24")
        self.theme_24.setGeometry(QRect(0, 3460, 361, 71))
        self.theme_24.setFont(font1)
        self.theme_24.setToolTipDuration(-1)
        self.theme_24.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"border: 2px solid #df6277;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #2b2b3e;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #323248;\n"
"}")
        self.theme_25 = QPushButton(self.background)
        self.theme_25.setObjectName(u"theme_25")
        self.theme_25.setGeometry(QRect(0, 3550, 361, 71))
        self.theme_25.setFont(font1)
        self.theme_25.setToolTipDuration(-1)
        self.theme_25.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"border: 2px solid #df6277;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #2b2b3e;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #323248;\n"
"}")
        self.background_7 = QFrame(self.background)
        self.background_7.setObjectName(u"background_7")
        self.background_7.setGeometry(QRect(0, 3720, 361, 72))
        self.background_7.setStyleSheet(u"background-color: #df6277;")
        self.background_7.setFrameShape(QFrame.StyledPanel)
        self.background_7.setFrameShadow(QFrame.Raised)
        self.text_9 = QLabel(self.background_7)
        self.text_9.setObjectName(u"text_9")
        self.text_9.setGeometry(QRect(30, 0, 311, 67))
        self.text_9.setFont(font1)
        self.text_9.setStyleSheet(u"color: white;")
        self.text_9.setAlignment(Qt.AlignCenter)
        self.line_4 = QFrame(self.background)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(0, 3660, 361, 20))
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)
        self.theme_26 = QPushButton(self.background)
        self.theme_26.setObjectName(u"theme_26")
        self.theme_26.setGeometry(QRect(0, 3810, 361, 71))
        self.theme_26.setFont(font1)
        self.theme_26.setToolTipDuration(-1)
        self.theme_26.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"border: 2px solid #df6277;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #2b2b3e;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #323248;\n"
"}")
        self.theme_27 = QPushButton(self.background)
        self.theme_27.setObjectName(u"theme_27")
        self.theme_27.setGeometry(QRect(0, 3900, 361, 71))
        self.theme_27.setFont(font1)
        self.theme_27.setToolTipDuration(-1)
        self.theme_27.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"border: 2px solid #df6277;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #2b2b3e;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #323248;\n"
"}")
        self.theme_28 = QPushButton(self.background)
        self.theme_28.setObjectName(u"theme_28")
        self.theme_28.setGeometry(QRect(0, 3990, 361, 101))
        self.theme_28.setFont(font1)
        self.theme_28.setToolTipDuration(-1)
        self.theme_28.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"border: 2px solid #df6277;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #2b2b3e;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #323248;\n"
"}")
        self.theme_29 = QPushButton(self.background)
        self.theme_29.setObjectName(u"theme_29")
        self.theme_29.setGeometry(QRect(0, 4110, 361, 101))
        self.theme_29.setFont(font1)
        self.theme_29.setToolTipDuration(-1)
        self.theme_29.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"border: 2px solid #df6277;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #2b2b3e;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #323248;\n"
"}")
        self.theme_30 = QPushButton(self.background)
        self.theme_30.setObjectName(u"theme_30")
        self.theme_30.setGeometry(QRect(0, 4230, 361, 71))
        self.theme_30.setFont(font1)
        self.theme_30.setToolTipDuration(-1)
        self.theme_30.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"border: 2px solid #df6277;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #2b2b3e;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #323248;\n"
"}")
        self.theme_31 = QPushButton(self.background)
        self.theme_31.setObjectName(u"theme_31")
        self.theme_31.setGeometry(QRect(0, 4320, 361, 71))
        self.theme_31.setFont(font1)
        self.theme_31.setToolTipDuration(-1)
        self.theme_31.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"border: 2px solid #df6277;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #2b2b3e;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #323248;\n"
"}")
        self.back = QPushButton(self.background)
        self.back.setObjectName(u"back")
        self.back.setGeometry(QRect(240, 30, 121, 51))
        self.back.setFont(font1)
        self.back.setToolTipDuration(-1)
        self.back.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"border: 2px solid #df6277;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #2b2b3e;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #323248;\n"
"}")

        self.verticalLayout_2.addWidget(self.background)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.background_2)

        MainWindow_2.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow_2)

        QMetaObject.connectSlotsByName(MainWindow_2)
    # setupUi

    def retranslateUi(self, MainWindow_2):
        MainWindow_2.setWindowTitle(QCoreApplication.translate("MainWindow_2", u"MainWindow", None))
        self.help.setText(QCoreApplication.translate("MainWindow_2", u"\u041f\u043e\u043c\u043e\u0449\u044c", None))
        self.develop.setText(QCoreApplication.translate("MainWindow_2", u"\u0421\u0432\u044f\u0437\u044c \u0441 \u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u0447\u0438\u043a\u043e\u043c", None))
        self.close_window.setText("")
        self.minimize_window.setText("")
        self.icon.setText("")
        self.text_3.setText(QCoreApplication.translate("MainWindow_2", u"\u0412\u0406\u0414 \u041d\u0410\u0419\u0414\u0406\u0412\u041d\u0406\u0428\u0418\u0425 \u0427\u0410\u0421\u0406\u0412 \u0414\u041e\n"
"\u041f\u0415\u0420\u0428\u041e\u0407 \u041f\u041e\u041b\u041e\u0412\u0418\u041d\u0418 XVI \u0421\u0422.", None))
#if QT_CONFIG(tooltip)
        self.theme_1.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.theme_1.setText(QCoreApplication.translate("MainWindow_2", u"\u0421\u0422\u0410\u0420\u041e\u0414\u0410\u0412\u041d\u042f \u0406\u0421\u0422\u041e\u0420\u0406\u042f\n"
"\u0423\u041a\u0420\u0410\u0407\u041d\u0418", None))
#if QT_CONFIG(tooltip)
        self.theme_3.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.theme_3.setText(QCoreApplication.translate("MainWindow_2", u"\u041a\u041e\u0420\u041e\u041b\u0406\u0412\u0421\u0422\u0412\u041e \u0420\u0423\u0421\u042c\u041a\u0415.\n"
"\u041c\u041e\u041d\u0413\u041e\u041b\u042c\u0421\u042c\u041a\u0410 \u041d\u0410\u0412\u0410\u041b\u0410", None))
#if QT_CONFIG(tooltip)
        self.theme_4.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.theme_4.setText(QCoreApplication.translate("MainWindow_2", u"\u0420\u0423\u0421\u042c\u041a\u0406 \u041a\u041d\u042f\u0417\u0406\u0412\u0421\u0422\u0412\u0410 \u0414\u0420\u0423\u0413\u041e\u0407\n"
"\u041f\u041e\u041b\u041e\u0412\u0418\u041d\u0418 XIV \u2014 \u041f\u0415\u0420\u0428\u041e\u0407\n"
"\u041f\u041e\u041b\u041e\u0412\u0418\u041d\u0418 XVI \u0421\u0422.\n"
"\u041a\u0420\u0418\u041c\u0421\u042c\u041a\u0415 \u0425\u0410\u041d\u0421\u0422\u0412\u041e", None))
#if QT_CONFIG(tooltip)
        self.theme_2.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.theme_2.setText(QCoreApplication.translate("MainWindow_2", u"\u0420\u0423\u0421\u042c-\u0423\u041a\u0420\u0410\u0407\u041d\u0410:\n"
"\u041a\u0418\u0407\u0412\u0421\u042c\u041a\u0410 \u0414\u0415\u0420\u0416\u0410\u0412\u0410", None))
        self.text_4.setText(QCoreApplication.translate("MainWindow_2", u"\u0414\u0420\u0423\u0413\u0410 \u041f\u041e\u041b\u041e\u0412\u0418\u041d\u0410 XVI \u0421\u0422. \u2014 \n"
"\u041f\u0415\u0420\u0428\u0410 \u041f\u041e\u041b\u041e\u0412\u0418\u041d\u0410 XVIII \u0421\u0422.", None))
#if QT_CONFIG(tooltip)
        self.theme_5.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.theme_5.setText(QCoreApplication.translate("MainWindow_2", u"\u0423\u041a\u0420\u0410\u0407\u041d\u0421\u042c\u041a\u0406 \u0417\u0415\u041c\u041b\u0406 \u0423 \u0421\u041a\u041b\u0410\u0414\u0406\n"
"\u0420\u0415\u0427\u0406 \u041f\u041e\u0421\u041f\u041e\u041b\u0418\u0422\u041e\u0407 \u0412 \u0414\u0420\u0423\u0413\u0406\u0419\n"
"\u041f\u041e\u041b\u041e\u0412\u0418\u041d\u0406 XVI \u0421\u0422.", None))
#if QT_CONFIG(tooltip)
        self.theme_6.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.theme_6.setText(QCoreApplication.translate("MainWindow_2", u"\u0423\u041a\u0420\u0410\u0407\u041d\u0421\u042c\u041a\u0406 \u0417\u0415\u041c\u041b\u0406 \u0423 \u0421\u041a\u041b\u0410\u0414\u0406\n"
"\u0420\u0415\u0427\u0406 \u041f\u041e\u0421\u041f\u041e\u041b\u0418\u0422\u041e\u0407 \u0412 \u041f\u0415\u0420\u0428\u0406\u0419\n"
"\u041f\u041e\u041b\u041e\u0412\u0418\u041d\u0406 XVII \u0421\u0422.", None))
#if QT_CONFIG(tooltip)
        self.theme_7.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.theme_7.setText(QCoreApplication.translate("MainWindow_2", u"\u041d\u0410\u0426\u0406\u041e\u041d\u0410\u041b\u042c\u041d\u041e-\u0412\u0418\u0417\u0412\u041e\u041b\u042c\u041d\u0410\n"
"\u0412\u0406\u0419\u041d\u0410 \u0423\u041a\u0420\u0410\u0407\u041d\u0421\u042c\u041a\u041e\u0413\u041e\n"
"\u041d\u0410\u0420\u041e\u0414\u0423 \u0421\u0415\u0420\u0415\u0414\u0418\u041d\u0418 XVII \u0421\u0422.", None))
#if QT_CONFIG(tooltip)
        self.theme_8.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.theme_8.setText(QCoreApplication.translate("MainWindow_2", u"\u041a\u041e\u0417\u0410\u0426\u042c\u041a\u0410 \u0423\u041a\u0420\u0410\u0407\u041d\u0410\n"
"\u041d\u0410\u041f\u0420\u0418\u041a\u0406\u041d\u0426\u0406 50-80-\u0425 \u0420\u0420.\n"
"XVII \u0441\u0442.", None))
#if QT_CONFIG(tooltip)
        self.theme_9.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.theme_9.setText(QCoreApplication.translate("MainWindow_2", u"\u0423\u041a\u0420\u0410\u0407\u041d\u0421\u042c\u041a\u0406 \u0417\u0415\u041c\u041b\u0406\n"
"\u041d\u0410\u041f\u0420\u0418\u041a\u0406\u041d\u0426\u0406 XVII \u2014 \u0412 \u041f\u0415\u0420\u0428\u0406\u0419\n"
"\u041f\u041e\u041b\u041e\u0412\u0418\u041d\u0406 XVIII \u0421\u0422.", None))
#if QT_CONFIG(tooltip)
        self.theme_10.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.theme_10.setText(QCoreApplication.translate("MainWindow_2", u"\u0423\u041a\u0420\u0410\u0407\u041d\u0421\u042c\u041a\u0406 \u0417\u0415\u041c\u041b\u0406 \u0412 \u0414\u0420\u0423\u0413\u0406\u0419\n"
"\u041f\u041e\u041b\u041e\u0412\u0418\u041d\u0406 XVIII \u0421\u0422.", None))
        self.text_5.setText(QCoreApplication.translate("MainWindow_2", u"\u041a\u0406\u041d\u0415\u0426\u042c XVIII \u0421\u0422. \u2014 XIX \u0421\u0422.", None))
#if QT_CONFIG(tooltip)
        self.theme_11.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.theme_11.setText(QCoreApplication.translate("MainWindow_2", u"\u0423\u041a\u0420\u0410\u0407\u041d\u0421\u042c\u041a\u0406 \u0417\u0415\u041c\u041b\u0406 \u0423 \u0421\u041a\u041b\u0410\u0414\u0406\n"
"\u0420\u041e\u0421\u0406\u0419\u0421\u042c\u041a\u041e\u0407 \u0406\u041c\u041f\u0415\u0420\u0406\u0407\n"
"\u041d\u0410\u041f\u0420\u0418\u041a\u0406\u041d\u0426\u0406 XVIII \u2014 \u0423\n"
"\u041f\u0415\u0420\u0428\u0406\u0419 \u041f\u041e\u041b\u041e\u0412\u0418\u041d\u0406 XIX \u0421\u0422.", None))
#if QT_CONFIG(tooltip)
        self.theme_12.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.theme_12.setText(QCoreApplication.translate("MainWindow_2", u"\u0423\u041a\u0420\u0410\u0407\u041d\u0421\u042c\u041a\u0406 \u0417\u0415\u041c\u041b\u0406 \u0423 \u0421\u041a\u041b\u0410\u0414\u0406\n"
"\u0410\u0412\u0421\u0422\u0420\u0406\u0419\u0421\u042c\u041a\u041e\u0407 \u0406\u041c\u041f\u0415\u0420\u0406\u0407\n"
"\u041d\u0410\u041f\u0420\u0418\u041a\u0406\u041d\u0426\u0406 XVIII \u2014 \u0423\n"
"\u041f\u0415\u0420\u0428\u0406\u0419 \u041f\u041e\u041b\u041e\u0412\u0418\u041d\u0406 XIX \u0421\u0422.", None))
#if QT_CONFIG(tooltip)
        self.theme_13.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.theme_13.setText(QCoreApplication.translate("MainWindow_2", u"\u041a\u0423\u041b\u042c\u0422\u0423\u0420\u0410 \u0423\u041a\u0420\u0410\u0407\u041d\u0418 \u041a\u0406\u041d\u0426\u042f\n"
"XVIII \u2014 \u041f\u0415\u0420\u0428\u041e\u0407 \u041f\u041e\u041b\u041e\u0412\u0418\u041d\u0418\n"
"XIX \u0421\u0422.", None))
#if QT_CONFIG(tooltip)
        self.theme_14.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.theme_14.setText(QCoreApplication.translate("MainWindow_2", u"\u0423\u041a\u0420\u0410\u0407\u041d\u0421\u042c\u041a\u0406 \u0417\u0415\u041c\u041b\u0406 \u0423 \u0421\u041a\u041b\u0410\u0414\u0406\n"
"\u0420\u041e\u0421\u0406\u0419\u0421\u042c\u041a\u041e\u0407 \u0406\u041c\u041f\u0415\u0420\u0406\u0407 \u0412\n"
"\u0414\u0420\u0423\u0413\u0406\u0419 \u041f\u041e\u041b\u041e\u0412\u0418\u041d\u0406 XIX \u0421\u0422.", None))
#if QT_CONFIG(tooltip)
        self.theme_15.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.theme_15.setText(QCoreApplication.translate("MainWindow_2", u"\u0423\u041a\u0420\u0410\u0407\u041d\u0421\u042c\u041a\u0406 \u0417\u0415\u041c\u041b\u0406 \u0423 \u0421\u041a\u041b\u0410\u0414\u0406\n"
"\u0410\u0412\u0421\u0422\u0420\u041e-\u0423\u0413\u041e\u0420\u0429\u0418\u041d\u0418 \u0412\n"
"\u0414\u0420\u0423\u0413\u0406\u0419 \u041f\u041e\u041b\u041e\u0412\u0418\u041d\u0406 XIX \u0421\u0422.", None))
#if QT_CONFIG(tooltip)
        self.theme_16.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.theme_16.setText(QCoreApplication.translate("MainWindow_2", u"\u041a\u0423\u041b\u042c\u0422\u0423\u0420\u0410 \u0423\u041a\u0420\u0410\u0407\u041d\u0418 \u0412 \u0414\u0420\u0423\u0413\u0406\u0419\n"
"\u041f\u041e\u041b\u041e\u0412\u0418\u041d\u0406 XIX \u0421\u0422. \u2014 \u041d\u0410\n"
"\u041f\u041e\u0427\u0410\u0422\u041a\u0423 XX \u0421\u0422.", None))
#if QT_CONFIG(tooltip)
        self.theme_17.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.theme_17.setText(QCoreApplication.translate("MainWindow_2", u"\u0423\u041a\u0420\u0410\u0407\u041d\u0421\u042c\u041a\u0406 \u0417\u0415\u041c\u041b\u0406 \u0423 \u0421\u041a\u041b\u0410\u0414\u0406\n"
"\u0420\u041e\u0421\u0406\u0419\u0421\u042c\u041a\u0406\u0419 \u0406\u041c\u041f\u0415\u0420\u0406\u0407 \u0412\n"
"1900-1914 \u0420\u0420.", None))
#if QT_CONFIG(tooltip)
        self.theme_18.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.theme_18.setText(QCoreApplication.translate("MainWindow_2", u"\u0423\u041a\u0420\u0410\u0407\u041d\u0421\u042c\u041a\u0406 \u0417\u0415\u041c\u041b\u0406 \u0423 \u0421\u041a\u041b\u0410\u0414\u0406\n"
"\u0410\u0412\u0421\u0422\u0420\u041e-\u0423\u0413\u041e\u0420\u0429\u0418\u041d\u0418 \u0412\n"
"1900-1914 \u0420\u0420.", None))
        self.text_7.setText(QCoreApplication.translate("MainWindow_2", u"1914-1945 \u0420\u0420.", None))
#if QT_CONFIG(tooltip)
        self.theme_19.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.theme_19.setText(QCoreApplication.translate("MainWindow_2", u"\u0423\u041a\u0420\u0410\u0407\u041d\u0410 \u0412 \u0420\u041e\u041a\u0418 \u041f\u0415\u0420\u0428\u041e\u0407\n"
"\u0421\u0412\u0406\u0422\u041e\u0412\u041e\u0407 \u0412\u0406\u0419\u041d\u0418", None))
#if QT_CONFIG(tooltip)
        self.theme_20.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.theme_20.setText(QCoreApplication.translate("MainWindow_2", u"\u041f\u041e\u0427\u0410\u0422\u041e\u041a \u0423\u041a\u0420\u0410\u0407\u041d\u0421\u042c\u041a\u041e\u0407\n"
"\u0420\u0415\u0412\u041e\u041b\u042e\u0426\u0406\u0407", None))
#if QT_CONFIG(tooltip)
        self.theme_21.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.theme_21.setText(QCoreApplication.translate("MainWindow_2", u"\u0420\u041e\u0417\u0413\u041e\u0420\u0422\u0410\u041d\u041d\u042f \u0423\u041a\u0420\u0410\u0407\u041d\u0421\u042c\u041a\u041e\u0407\n"
"\u0420\u0415\u0412\u041e\u041b\u042e\u0426\u0406\u0407. \u0411\u041e\u0420\u041e\u0422\u042c\u0411\u0410\n"
"\u0417\u0410 \u0412\u0406\u0414\u041d\u041e\u0412\u041b\u0415\u041d\u041d\u042f\n"
"\u0414\u0415\u0420\u0416\u0410\u0412\u041d\u041e\u0421\u0422\u0406", None))
#if QT_CONFIG(tooltip)
        self.theme_22.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.theme_22.setText(QCoreApplication.translate("MainWindow_2", u"\u0412\u0421\u0422\u0410\u041d\u041e\u0412\u041b\u0415\u041d\u041d\u042f\n"
"\u041a\u041e\u041c\u0423\u041d\u0406\u0421\u0422\u0418\u0427\u041d\u041e\u0413\u041e\n"
"\u0422\u041e\u0422\u0410\u041b\u0406\u0422\u0410\u0420\u041d\u041e\u0413\u041e \u0420\u0415\u0416\u0418\u041c\u0423\n"
"\u0412 \u0423\u041a\u0420\u0410\u0407\u041d\u0406", None))
#if QT_CONFIG(tooltip)
        self.theme_23.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.theme_23.setText(QCoreApplication.translate("MainWindow_2", u"\u0423\u0422\u0412\u0415\u0420\u0414\u0416\u0415\u041d\u041d\u042f\n"
"\u0411\u0406\u041b\u042c\u0428\u041e\u0412\u0418\u0426\u042c\u041a\u041e\u0413\u041e\n"
"\u0422\u041e\u0422\u0410\u041b\u0406\u0422\u0410\u0420\u041d\u041e\u0413\u041e \u0420\u0415\u0416\u0418\u041c\u0423 \u0412\n"
"\u0423\u041a\u0420\u0410\u0407\u041d\u0406", None))
#if QT_CONFIG(tooltip)
        self.theme_24.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.theme_24.setText(QCoreApplication.translate("MainWindow_2", u"\u0417\u0410\u0425\u0406\u0414\u041d\u041e\u0423\u041a\u0420\u0410\u0407\u041d\u0421\u042c\u041a\u0406 \u0417\u0415\u041c\u041b\u0406 \u0412\n"
"\u041c\u0406\u0416\u0412\u041e\u0404\u041d\u041d\u0418\u0419 \u041f\u0415\u0420\u0406\u041e\u0414", None))
#if QT_CONFIG(tooltip)
        self.theme_25.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.theme_25.setText(QCoreApplication.translate("MainWindow_2", u"\u0423\u041a\u0420\u0410\u0407\u041d\u0410 \u0412 \u0420\u041e\u041a\u0418\n"
"\u0414\u0420\u0423\u0413\u041e\u0407 \u0421\u0412\u0406\u0422\u041e\u0412\u041e\u0407 \u0412\u0406\u0419\u041d\u0418", None))
        self.text_9.setText(QCoreApplication.translate("MainWindow_2", u"1945 \u0420. \u2014 \u041f\u041e\u0427\u0410\u0422\u041e\u041a XXI \u0421\u0422.", None))
#if QT_CONFIG(tooltip)
        self.theme_26.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.theme_26.setText(QCoreApplication.translate("MainWindow_2", u"\u0423\u041a\u0420\u0410\u0407\u041d\u0410 \u0412 \u041f\u0415\u0420\u0428\u0406\u0407\n"
"\u041f\u041e\u0412\u041e\u0404\u041d\u041d\u0406 \u0420\u041e\u041a\u0418", None))
#if QT_CONFIG(tooltip)
        self.theme_27.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.theme_27.setText(QCoreApplication.translate("MainWindow_2", u"\u0423\u041a\u0420\u0410\u0407\u041d\u0410 \u0412 \u0423\u041c\u041e\u0412\u0410\u0425\n"
"\u0414\u0415\u0421\u0422\u0410\u041b\u0406\u041d\u0406\u0417\u0410\u0426\u0406\u0407", None))
#if QT_CONFIG(tooltip)
        self.theme_28.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.theme_28.setText(QCoreApplication.translate("MainWindow_2", u"\u0423\u041a\u0420\u0410\u0407\u041d\u0410 \u0423 \u041f\u0415\u0420\u0406\u041e\u0414\n"
"\u0417\u0410\u0413\u041e\u0421\u0422\u0420\u0415\u041d\u041d\u042f \u041a\u0420\u0418\u0417\u0418\n"
"\u0420\u0410\u0414\u042f\u041d\u0421\u042c\u041a\u041e\u0407 \u0421\u0418\u0421\u0422\u0415\u041c\u0418", None))
#if QT_CONFIG(tooltip)
        self.theme_29.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.theme_29.setText(QCoreApplication.translate("MainWindow_2", u"\u0412\u0406\u0414\u041d\u041e\u0412\u041b\u0415\u041d\u041d\u042f\n"
"\u041d\u0415\u0417\u0410\u041b\u0415\u0416\u041d\u041e\u0421\u0422\u0406\n"
"\u0423\u041a\u0420\u0410\u0407\u041d\u0418", None))
#if QT_CONFIG(tooltip)
        self.theme_30.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.theme_30.setText(QCoreApplication.translate("MainWindow_2", u"\u0421\u0422\u0410\u041d\u041e\u0412\u041b\u0415\u041d\u041d\u042f \u0423\u041a\u0420\u0410\u0407\u041d\u0418\n"
"\u042f\u041a \u041d\u0415\u0417\u0410\u041b\u0415\u0416\u041d\u041e\u0407 \u0414\u0415\u0420\u0416\u0410\u0412\u0418", None))
#if QT_CONFIG(tooltip)
        self.theme_31.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.theme_31.setText(QCoreApplication.translate("MainWindow_2", u"\u0422\u0412\u041e\u0420\u0415\u041d\u041d\u042f \u041d\u041e\u0412\u041e\u0407\n"
"\u0423\u041a\u0420\u0410\u0407\u041d\u0418", None))
#if QT_CONFIG(tooltip)
        self.back.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.back.setText(QCoreApplication.translate("MainWindow_2", u"\u041d\u0410\u0417\u0410\u0414", None))
    # retranslateUi

