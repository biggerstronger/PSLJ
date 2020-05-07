# -*- coding: utf-8 -*-

from PySide2 import QtWidgets
import sys

from ui_controller import Controller


def run_ui():
    app = QtWidgets.QApplication(sys.argv)
    window = Controller()
    window.show()
    sys.exit(app.exec_())


def main():
    run_ui()


if __name__ == "__main__":
    main()
