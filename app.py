from PySide2 import QtWidgets
import files
import sys


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = files.History()
    window.show()
    sys.exit(app.exec_())
