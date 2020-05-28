from PySide2 import QtWidgets

import errordialog


class ErrorController(QtWidgets.QMainWindow, errordialog.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButtonOK.clicked.connect(self.close)

    def error_msg_fio(self, i):
        self.labelError.setText('Ошибка в строке {}: неверные ФИО!'.format(i))

    def error_msg_bib(self, i):
        self.labelError.setText('Ошибка в строке {}: неверный bib!'.format(i))

    def error_msg_double(self, i):
        self.labelError.setText('Ошибка в строке {}: неверные bib и ФИО!'.format(i))
