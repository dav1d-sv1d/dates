# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'history.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import photo_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(370, 196)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setMaximumSize(QSize(370, 226))
        self.help = QAction(MainWindow)
        self.help.setObjectName(u"help")
        icon1 = QIcon()
        icon1.addFile(u":/images/help.png", QSize(), QIcon.Normal, QIcon.Off)
        self.help.setIcon(icon1)
        font = QFont()
        font.setFamily(u"Montserrat Medium")
        self.help.setFont(font)
        self.develop = QAction(MainWindow)
        self.develop.setObjectName(u"develop")
        icon2 = QIcon()
        icon2.addFile(u":/images/developer.png", QSize(), QIcon.Normal, QIcon.Off)
        self.develop.setIcon(icon2)
        self.develop.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(49, 52, 67)")
        self.background_1 = QFrame(self.centralwidget)
        self.background_1.setObjectName(u"background_1")
        self.background_1.setGeometry(QRect(50, 30, 321, 71))
        self.background_1.setStyleSheet(u"background-color: #df6277;")
        self.background_1.setFrameShape(QFrame.StyledPanel)
        self.background_1.setFrameShadow(QFrame.Raised)
        self.title = QLabel(self.background_1)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(30, 10, 271, 51))
        font1 = QFont()
        font1.setFamily(u"Tahoma")
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setWeight(75)
        font1.setStrikeOut(False)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.title.setFont(font1)
        self.title.setStyleSheet(u"color: white;")
        self.title.setTextFormat(Qt.AutoText)
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setWordWrap(True)
        self.select_theme = QPushButton(self.centralwidget)
        self.select_theme.setObjectName(u"select_theme")
        self.select_theme.setGeometry(QRect(80, 120, 261, 51))
        font2 = QFont()
        font2.setFamily(u"Tahoma")
        font2.setPointSize(22)
        font2.setBold(True)
        font2.setWeight(75)
        self.select_theme.setFont(font2)
        self.select_theme.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"border: 2px solid #df6277;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #2b2b3e;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #323248;\n"
"}")
        self.settings_grame = QFrame(self.centralwidget)
        self.settings_grame.setObjectName(u"settings_grame")
        self.settings_grame.setGeometry(QRect(0, 30, 51, 161))
        self.settings_grame.setStyleSheet(u"background-color: rgb(49, 52, 67)")
        self.settings_grame.setFrameShape(QFrame.StyledPanel)
        self.settings_grame.setFrameShadow(QFrame.Raised)
        self.info_about_program = QPushButton(self.settings_grame)
        self.info_about_program.setObjectName(u"info_about_program")
        self.info_about_program.setGeometry(QRect(6, 6, 41, 41))
        self.info_about_program.setMinimumSize(QSize(30, 30))
        self.info_about_program.setStyleSheet(u"QPushButton {\n"
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
        self.info_about_program.setIcon(icon1)
        self.info_about_program.setIconSize(QSize(30, 30))
        self.comunication_with_developer = QPushButton(self.settings_grame)
        self.comunication_with_developer.setObjectName(u"comunication_with_developer")
        self.comunication_with_developer.setGeometry(QRect(7, 53, 40, 40))
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.comunication_with_developer.sizePolicy().hasHeightForWidth())
        self.comunication_with_developer.setSizePolicy(sizePolicy1)
        self.comunication_with_developer.setMinimumSize(QSize(30, 30))
        self.comunication_with_developer.setMaximumSize(QSize(40, 16777215))
        font3 = QFont()
        font3.setFamily(u"Tahoma")
        font3.setPointSize(16)
        font3.setBold(True)
        font3.setWeight(75)
        self.comunication_with_developer.setFont(font3)
        self.comunication_with_developer.setStyleSheet(u"QPushButton {\n"
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
        self.comunication_with_developer.setIcon(icon2)
        self.comunication_with_developer.setIconSize(QSize(30, 30))
        self.header_frame = QFrame(self.centralwidget)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setGeometry(QRect(0, 0, 371, 30))
        self.header_frame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.header_frame.setFrameShape(QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.close_window = QPushButton(self.header_frame)
        self.close_window.setObjectName(u"close_window")
        self.close_window.setGeometry(QRect(340, 0, 30, 30))
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
        self.minimize_window.setGeometry(QRect(310, 0, 30, 30))
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
        self.icon.setStyleSheet(u"border: none;")
        icon5 = QIcon()
        icon5.addFile(u":/hs.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.icon.setIcon(icon5)
        self.icon.setIconSize(QSize(20, 20))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.help.setText("")
        self.develop.setText("")
        self.title.setText(QCoreApplication.translate("MainWindow", u"\u041f\u041e\u041c\u0406\u0427\u041d\u0418\u041a \u0417 \u0406\u0421\u0422\u041e\u0420\u0406\u0407 \u0423\u041a\u0420\u0410\u0407\u041d\u0418 (\u0414\u0410\u0422\u0418)", None))
        self.select_theme.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0411\u0420\u0410\u0422\u0418 \u0422\u0415\u041c\u0423", None))
        self.info_about_program.setText("")
#if QT_CONFIG(tooltip)
        self.comunication_with_developer.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.comunication_with_developer.setText("")
        self.close_window.setText("")
        self.minimize_window.setText("")
        self.icon.setText("")
    # retranslateUi

