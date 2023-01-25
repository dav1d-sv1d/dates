# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings_question.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import photo_rc

class Ui_MainWindow_5(object):
    def setupUi(self, MainWindow_5):
        if not MainWindow_5.objectName():
            MainWindow_5.setObjectName(u"MainWindow_5")
        MainWindow_5.resize(299, 126)
        MainWindow_5.setMinimumSize(QSize(0, 0))
        MainWindow_5.setMaximumSize(QSize(352, 141))
        MainWindow_5.setStyleSheet(u"background-color: rgb(72, 77, 98);")
        self.centralwidget = QWidget(MainWindow_5)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(72, 77, 98")
        self.switch_2 = QPushButton(self.centralwidget)
        self.switch_2.setObjectName(u"switch_2")
        self.switch_2.setGeometry(QRect(160, 15, 51, 51))
        self.switch_2.setMinimumSize(QSize(30, 30))
        self.switch_2.setStyleSheet(u"border: none;\n"
"")
        icon = QIcon()
        icon.addFile(u":/images/switch_off.png", QSize(), QIcon.Normal, QIcon.Off)
        self.switch_2.setIcon(icon)
        self.switch_2.setIconSize(QSize(61, 51))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 18, 131, 41))
        font = QFont()
        font.setFamily(u"Tahoma")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: white;")
        self.info_about_switch = QPushButton(self.centralwidget)
        self.info_about_switch.setObjectName(u"info_about_switch")
        self.info_about_switch.setGeometry(QRect(210, 10, 13, 13))
        self.info_about_switch.setStyleSheet(u"border: none;")
        icon1 = QIcon()
        icon1.addFile(u":/images/settings_question.png", QSize(), QIcon.Normal, QIcon.Off)
        self.info_about_switch.setIcon(icon1)
        self.info_about_switch.setIconSize(QSize(13, 13))
        self.accept = QPushButton(self.centralwidget)
        self.accept.setObjectName(u"accept")
        self.accept.setGeometry(QRect(220, 70, 51, 41))
        self.accept.setFont(font)
        self.accept.setStyleSheet(u"QPushButton {\n"
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
        MainWindow_5.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow_5)

        QMetaObject.connectSlotsByName(MainWindow_5)
    # setupUi

    def retranslateUi(self, MainWindow_5):
        MainWindow_5.setWindowTitle(QCoreApplication.translate("MainWindow_5", u"MainWindow", None))
        self.switch_2.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow_5", u"\u041f\u0420\u0418\u0425\u041e\u0412\u0410\u0422\u0418\n"
"\u0412\u0406\u0414\u041f\u041e\u0412\u0406\u0414\u0406", None))
        self.info_about_switch.setText("")
        self.accept.setText(QCoreApplication.translate("MainWindow_5", u"\u041e\u041a", None))
    # retranslateUi

