from PySide2 import QtWidgets, QtCore


def message_box(icon="", stylesheet="", text=""):
    msgs = {

        "Information": QtWidgets.QMessageBox.Icon.Information,
        "Question": QtWidgets.QMessageBox.Icon.Question,
        "Warning": QtWidgets.QMessageBox.Icon.Warning,
        "Critical": QtWidgets.QMessageBox.Icon.Critical

    }

    box = QtWidgets.QMessageBox()
    box.setStyleSheet(stylesheet)
    box.setIcon(msgs[icon])
    box.setText(text)
    box.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
    box.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
    box.exec_()
