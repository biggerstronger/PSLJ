# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'errordialog.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(408, 174)
        self.labelError = QLabel(Dialog)
        self.labelError.setObjectName(u"labelError")
        self.labelError.setGeometry(QRect(26, 42, 361, 51))
        self.pushButtonOK = QPushButton(Dialog)
        self.pushButtonOK.setObjectName(u"pushButtonOK")
        self.pushButtonOK.setGeometry(QRect(270, 130, 121, 31))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.labelError.setText("")
        self.pushButtonOK.setText(QCoreApplication.translate("Dialog", u"OK", None))
    # retranslateUi

