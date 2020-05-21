# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_form.ui'
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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1213, 958)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QRect(10, 10, 1191, 911))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayoutWidget = QWidget(self.tab)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 1081, 809))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_12 = QGridLayout()
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.city8 = QLineEdit(self.gridLayoutWidget)
        self.city8.setObjectName(u"city8")

        self.gridLayout_12.addWidget(self.city8, 0, 0, 1, 1, Qt.AlignLeft)

        self.city9 = QLineEdit(self.gridLayoutWidget)
        self.city9.setObjectName(u"city9")

        self.gridLayout_12.addWidget(self.city9, 1, 0, 1, 1, Qt.AlignLeft)


        self.gridLayout.addLayout(self.gridLayout_12, 15, 2, 1, 1)

        self.fio5 = QLineEdit(self.gridLayoutWidget)
        self.fio5.setObjectName(u"fio5")
        self.fio5.setMinimumSize(QSize(300, 0))

        self.gridLayout.addWidget(self.fio5, 12, 1, 1, 1, Qt.AlignLeft)

        self.startTime = QLineEdit(self.gridLayoutWidget)
        self.startTime.setObjectName(u"startTime")
        self.startTime.setMinimumSize(QSize(300, 0))
        self.startTime.setMaximumSize(QSize(300, 16777215))

        self.gridLayout.addWidget(self.startTime, 27, 1, 1, 1)

        self.gates = QLineEdit(self.gridLayoutWidget)
        self.gates.setObjectName(u"gates")
        self.gates.setMinimumSize(QSize(300, 0))
        self.gates.setMaximumSize(QSize(300, 16777215))

        self.gridLayout.addWidget(self.gates, 25, 1, 1, 1)

        self.label_18 = QLabel(self.gridLayoutWidget)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout.addWidget(self.label_18, 4, 0, 1, 3)

        self.label_12 = QLabel(self.gridLayoutWidget)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 10, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, -1, -1, -1)
        self.label_39 = QLabel(self.gridLayoutWidget)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setMaximumSize(QSize(82, 16777215))

        self.horizontalLayout_5.addWidget(self.label_39)

        self.runsComboBox = QComboBox(self.gridLayoutWidget)
        self.runsComboBox.addItem("")
        self.runsComboBox.addItem("")
        self.runsComboBox.setObjectName(u"runsComboBox")
        self.runsComboBox.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_5.addWidget(self.runsComboBox)


        self.gridLayout.addLayout(self.horizontalLayout_5, 1, 2, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 15, 0, 1, 1)

        self.city6 = QLineEdit(self.gridLayoutWidget)
        self.city6.setObjectName(u"city6")

        self.gridLayout.addWidget(self.city6, 13, 2, 1, 1, Qt.AlignLeft)

        self.label_19 = QLabel(self.gridLayoutWidget)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout.addWidget(self.label_19, 7, 0, 1, 3)

        self.label_28 = QLabel(self.gridLayoutWidget)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout.addWidget(self.label_28, 27, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_40 = QLabel(self.gridLayoutWidget)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_4.addWidget(self.label_40)

        self.qualificationsComboBox = QComboBox(self.gridLayoutWidget)
        self.qualificationsComboBox.addItem("")
        self.qualificationsComboBox.addItem("")
        self.qualificationsComboBox.setObjectName(u"qualificationsComboBox")
        self.qualificationsComboBox.setMaximumSize(QSize(50, 16777215))
        self.qualificationsComboBox.setFrame(True)

        self.horizontalLayout_4.addWidget(self.qualificationsComboBox)


        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 2, 1, 1)

        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.fio8 = QLineEdit(self.gridLayoutWidget)
        self.fio8.setObjectName(u"fio8")
        self.fio8.setMinimumSize(QSize(300, 0))

        self.gridLayout_11.addWidget(self.fio8, 0, 0, 1, 1, Qt.AlignLeft)

        self.fio9 = QLineEdit(self.gridLayoutWidget)
        self.fio9.setObjectName(u"fio9")
        self.fio9.setMinimumSize(QSize(300, 0))

        self.gridLayout_11.addWidget(self.fio9, 1, 0, 1, 1, Qt.AlignLeft)


        self.gridLayout.addLayout(self.gridLayout_11, 15, 1, 1, 1)

        self.fio2 = QLineEdit(self.gridLayoutWidget)
        self.fio2.setObjectName(u"fio2")
        self.fio2.setMinimumSize(QSize(300, 0))

        self.gridLayout.addWidget(self.fio2, 9, 1, 1, 1, Qt.AlignLeft)

        self.label_26 = QLabel(self.gridLayoutWidget)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout.addWidget(self.label_26, 25, 0, 1, 1)

        self.label_29 = QLabel(self.gridLayoutWidget)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout.addWidget(self.label_29, 28, 0, 1, 1)

        self.label_21 = QLabel(self.gridLayoutWidget)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout.addWidget(self.label_21, 17, 0, 1, 1)

        self.label_22 = QLabel(self.gridLayoutWidget)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout.addWidget(self.label_22, 20, 0, 1, 1)

        self.city7 = QLineEdit(self.gridLayoutWidget)
        self.city7.setObjectName(u"city7")

        self.gridLayout.addWidget(self.city7, 14, 2, 1, 1, Qt.AlignLeft)

        self.fio7 = QLineEdit(self.gridLayoutWidget)
        self.fio7.setObjectName(u"fio7")
        self.fio7.setMinimumSize(QSize(300, 0))

        self.gridLayout.addWidget(self.fio7, 14, 1, 1, 1, Qt.AlignLeft)

        self.label_13 = QLabel(self.gridLayoutWidget)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout.addWidget(self.label_13, 11, 0, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)

        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)

        self.typelineEdit = QLineEdit(self.gridLayoutWidget)
        self.typelineEdit.setObjectName(u"typelineEdit")
        self.typelineEdit.setMinimumSize(QSize(300, 0))

        self.gridLayout.addWidget(self.typelineEdit, 2, 1, 1, 1, Qt.AlignLeft)

        self.titlelineEdit = QLineEdit(self.gridLayoutWidget)
        self.titlelineEdit.setObjectName(u"titlelineEdit")
        self.titlelineEdit.setMinimumSize(QSize(300, 0))

        self.gridLayout.addWidget(self.titlelineEdit, 0, 1, 1, 1, Qt.AlignLeft)

        self.finals = QLineEdit(self.gridLayoutWidget)
        self.finals.setObjectName(u"finals")
        self.finals.setMinimumSize(QSize(300, 0))
        self.finals.setMaximumSize(QSize(300, 16777215))

        self.gridLayout.addWidget(self.finals, 28, 1, 1, 1)

        self.label_11 = QLabel(self.gridLayoutWidget)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 9, 0, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 14, 0, 1, 1)

        self.label_16 = QLabel(self.gridLayoutWidget)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout.addWidget(self.label_16, 6, 1, 1, 1, Qt.AlignLeft)

        self.finishTemp = QLineEdit(self.gridLayoutWidget)
        self.finishTemp.setObjectName(u"finishTemp")
        self.finishTemp.setMinimumSize(QSize(300, 0))
        self.finishTemp.setMaximumSize(QSize(300, 16777215))

        self.gridLayout.addWidget(self.finishTemp, 32, 1, 1, 1)

        self.altitudeDiff = QLineEdit(self.gridLayoutWidget)
        self.altitudeDiff.setObjectName(u"altitudeDiff")
        self.altitudeDiff.setMinimumSize(QSize(300, 0))
        self.altitudeDiff.setMaximumSize(QSize(300, 16777215))

        self.gridLayout.addWidget(self.altitudeDiff, 23, 1, 1, 1)

        self.label_14 = QLabel(self.gridLayoutWidget)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout.addWidget(self.label_14, 12, 0, 1, 1)

        self.label_24 = QLabel(self.gridLayoutWidget)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout.addWidget(self.label_24, 22, 0, 1, 1)

        self.start = QLineEdit(self.gridLayoutWidget)
        self.start.setObjectName(u"start")
        self.start.setMinimumSize(QSize(300, 0))
        self.start.setMaximumSize(QSize(300, 16777215))

        self.gridLayout.addWidget(self.start, 21, 1, 1, 1)

        self.label_10 = QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(300, 16777215))

        self.gridLayout.addWidget(self.label_10, 8, 0, 1, 1)

        self.orglineEdit = QLineEdit(self.gridLayoutWidget)
        self.orglineEdit.setObjectName(u"orglineEdit")
        self.orglineEdit.setMinimumSize(QSize(300, 0))

        self.gridLayout.addWidget(self.orglineEdit, 3, 1, 1, 1, Qt.AlignLeft)

        self.fio1 = QLineEdit(self.gridLayoutWidget)
        self.fio1.setObjectName(u"fio1")
        self.fio1.setMinimumSize(QSize(300, 0))

        self.gridLayout.addWidget(self.fio1, 8, 1, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_37 = QLabel(self.gridLayoutWidget)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMaximumSize(QSize(78, 16777215))

        self.horizontalLayout_6.addWidget(self.label_37)

        self.roundsComboBox = QComboBox(self.gridLayoutWidget)
        self.roundsComboBox.addItem("")
        self.roundsComboBox.addItem("")
        self.roundsComboBox.addItem("")
        self.roundsComboBox.setObjectName(u"roundsComboBox")
        self.roundsComboBox.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_6.addWidget(self.roundsComboBox)


        self.gridLayout.addLayout(self.horizontalLayout_6, 2, 2, 1, 1)

        self.label_7 = QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)

        self.label_25 = QLabel(self.gridLayoutWidget)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout.addWidget(self.label_25, 24, 0, 1, 1)

        self.label_17 = QLabel(self.gridLayoutWidget)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout.addWidget(self.label_17, 6, 2, 1, 1, Qt.AlignLeft)

        self.label_34 = QLabel(self.gridLayoutWidget)
        self.label_34.setObjectName(u"label_34")

        self.gridLayout.addWidget(self.label_34, 33, 0, 1, 1)

        self.datelineEdit = QLineEdit(self.gridLayoutWidget)
        self.datelineEdit.setObjectName(u"datelineEdit")
        self.datelineEdit.setMinimumSize(QSize(300, 0))

        self.gridLayout.addWidget(self.datelineEdit, 1, 1, 1, 1, Qt.AlignLeft)

        self.homologation = QLineEdit(self.gridLayoutWidget)
        self.homologation.setObjectName(u"homologation")
        self.homologation.setMinimumSize(QSize(300, 0))
        self.homologation.setMaximumSize(QSize(300, 16777215))

        self.gridLayout.addWidget(self.homologation, 24, 1, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 18, 0, 1, 3, Qt.AlignHCenter)

        self.label_8 = QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 5, 0, 1, 3, Qt.AlignHCenter)

        self.city3 = QLineEdit(self.gridLayoutWidget)
        self.city3.setObjectName(u"city3")

        self.gridLayout.addWidget(self.city3, 10, 2, 1, 1, Qt.AlignLeft)

        self.label_32 = QLabel(self.gridLayoutWidget)
        self.label_32.setObjectName(u"label_32")

        self.gridLayout.addWidget(self.label_32, 31, 0, 1, 1)

        self.label_15 = QLabel(self.gridLayoutWidget)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout.addWidget(self.label_15, 13, 0, 1, 1)

        self.startTemp = QLineEdit(self.gridLayoutWidget)
        self.startTemp.setObjectName(u"startTemp")
        self.startTemp.setMinimumSize(QSize(300, 0))
        self.startTemp.setMaximumSize(QSize(300, 16777215))

        self.gridLayout.addWidget(self.startTemp, 31, 1, 1, 1)

        self.label_23 = QLabel(self.gridLayoutWidget)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout.addWidget(self.label_23, 21, 0, 1, 1)

        self.city5 = QLineEdit(self.gridLayoutWidget)
        self.city5.setObjectName(u"city5")

        self.gridLayout.addWidget(self.city5, 12, 2, 1, 1, Qt.AlignLeft)

        self.label_30 = QLabel(self.gridLayoutWidget)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout.addWidget(self.label_30, 30, 0, 1, 3, Qt.AlignHCenter)

        self.city4 = QLineEdit(self.gridLayoutWidget)
        self.city4.setObjectName(u"city4")

        self.gridLayout.addWidget(self.city4, 11, 2, 1, 1, Qt.AlignLeft)

        self.finish = QLineEdit(self.gridLayoutWidget)
        self.finish.setObjectName(u"finish")
        self.finish.setMinimumSize(QSize(300, 0))
        self.finish.setMaximumSize(QSize(300, 16777215))

        self.gridLayout.addWidget(self.finish, 22, 1, 1, 1)

        self.trackName = QLineEdit(self.gridLayoutWidget)
        self.trackName.setObjectName(u"trackName")
        self.trackName.setMinimumSize(QSize(300, 0))
        self.trackName.setMaximumSize(QSize(300, 16777215))

        self.gridLayout.addWidget(self.trackName, 20, 1, 1, 1)

        self.label_9 = QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 6, 0, 1, 1, Qt.AlignLeft)

        self.fio3 = QLineEdit(self.gridLayoutWidget)
        self.fio3.setObjectName(u"fio3")
        self.fio3.setMinimumSize(QSize(300, 0))

        self.gridLayout.addWidget(self.fio3, 10, 1, 1, 1, Qt.AlignLeft)

        self.fio4 = QLineEdit(self.gridLayoutWidget)
        self.fio4.setObjectName(u"fio4")
        self.fio4.setMinimumSize(QSize(300, 0))

        self.gridLayout.addWidget(self.fio4, 11, 1, 1, 1, Qt.AlignLeft)

        self.city2 = QLineEdit(self.gridLayoutWidget)
        self.city2.setObjectName(u"city2")

        self.gridLayout.addWidget(self.city2, 9, 2, 1, 1, Qt.AlignLeft)

        self.saveParams = QPushButton(self.gridLayoutWidget)
        self.saveParams.setObjectName(u"saveParams")
        self.saveParams.setMaximumSize(QSize(150, 45))

        self.gridLayout.addWidget(self.saveParams, 33, 2, 1, 1)

        self.label_20 = QLabel(self.gridLayoutWidget)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout.addWidget(self.label_20, 23, 0, 1, 1)

        self.label_31 = QLabel(self.gridLayoutWidget)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout.addWidget(self.label_31, 29, 0, 1, 3)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.fio6 = QLineEdit(self.gridLayoutWidget)
        self.fio6.setObjectName(u"fio6")
        self.fio6.setMinimumSize(QSize(300, 0))

        self.gridLayout.addWidget(self.fio6, 13, 1, 1, 1, Qt.AlignLeft)

        self.snow = QLineEdit(self.gridLayoutWidget)
        self.snow.setObjectName(u"snow")
        self.snow.setMinimumSize(QSize(300, 0))
        self.snow.setMaximumSize(QSize(300, 16777215))

        self.gridLayout.addWidget(self.snow, 33, 1, 1, 1)

        self.label_33 = QLabel(self.gridLayoutWidget)
        self.label_33.setObjectName(u"label_33")

        self.gridLayout.addWidget(self.label_33, 32, 0, 1, 1)

        self.city1 = QLineEdit(self.gridLayoutWidget)
        self.city1.setObjectName(u"city1")

        self.gridLayout.addWidget(self.city1, 8, 2, 1, 1, Qt.AlignLeft)

        self.length = QLineEdit(self.gridLayoutWidget)
        self.length.setObjectName(u"length")
        self.length.setMinimumSize(QSize(300, 0))
        self.length.setMaximumSize(QSize(300, 16777215))

        self.gridLayout.addWidget(self.length, 26, 1, 1, 1)

        self.label_27 = QLabel(self.gridLayoutWidget)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout.addWidget(self.label_27, 26, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.participantsTable = QTableWidget(self.tab_3)
        if (self.participantsTable.columnCount() < 6):
            self.participantsTable.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.participantsTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.participantsTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.participantsTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.participantsTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.participantsTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.participantsTable.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.participantsTable.setObjectName(u"participantsTable")
        self.participantsTable.setGeometry(QRect(0, 0, 751, 761))
        self.horizontalLayoutWidget = QWidget(self.tab_3)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(160, 770, 401, 51))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.editpushButton = QPushButton(self.horizontalLayoutWidget)
        self.editpushButton.setObjectName(u"editpushButton")

        self.horizontalLayout_3.addWidget(self.editpushButton)

        self.addpushButton = QPushButton(self.horizontalLayoutWidget)
        self.addpushButton.setObjectName(u"addpushButton")

        self.horizontalLayout_3.addWidget(self.addpushButton)

        self.pushButtonLoadList = QPushButton(self.tab_3)
        self.pushButtonLoadList.setObjectName(u"pushButtonLoadList")
        self.pushButtonLoadList.setGeometry(QRect(870, 20, 181, 61))
        self.horizontalLayoutWidget_2 = QWidget(self.tab_3)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(759, 100, 351, 51))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_38 = QLabel(self.horizontalLayoutWidget_2)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout.addWidget(self.label_38)

        self.fileNameLabel = QLabel(self.horizontalLayoutWidget_2)
        self.fileNameLabel.setObjectName(u"fileNameLabel")

        self.horizontalLayout.addWidget(self.fileNameLabel, 0, Qt.AlignLeft)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayoutWidget_2 = QWidget(self.tab_2)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(0, 50, 1181, 771))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_36 = QLabel(self.gridLayoutWidget_2)
        self.label_36.setObjectName(u"label_36")

        self.gridLayout_2.addWidget(self.label_36, 0, 1, 1, 1, Qt.AlignHCenter)

        self.redListQ1 = QTableWidget(self.gridLayoutWidget_2)
        if (self.redListQ1.columnCount() < 4):
            self.redListQ1.setColumnCount(4)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.redListQ1.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.redListQ1.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.redListQ1.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.redListQ1.setHorizontalHeaderItem(3, __qtablewidgetitem9)
        self.redListQ1.setObjectName(u"redListQ1")
        self.redListQ1.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_2.addWidget(self.redListQ1, 1, 0, 1, 1)

        self.label_35 = QLabel(self.gridLayoutWidget_2)
        self.label_35.setObjectName(u"label_35")

        self.gridLayout_2.addWidget(self.label_35, 0, 0, 1, 1, Qt.AlignHCenter)

        self.blueListQ1 = QTableWidget(self.gridLayoutWidget_2)
        if (self.blueListQ1.columnCount() < 4):
            self.blueListQ1.setColumnCount(4)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.blueListQ1.setHorizontalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.blueListQ1.setHorizontalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.blueListQ1.setHorizontalHeaderItem(2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.blueListQ1.setHorizontalHeaderItem(3, __qtablewidgetitem13)
        self.blueListQ1.setObjectName(u"blueListQ1")

        self.gridLayout_2.addWidget(self.blueListQ1, 1, 1, 1, 1)

        self.pushButtonAccept = QPushButton(self.tab_2)
        self.pushButtonAccept.setObjectName(u"pushButtonAccept")
        self.pushButtonAccept.setGeometry(QRect(800, 840, 331, 41))
        self.label_41 = QLabel(self.tab_2)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setGeometry(QRect(460, 20, 341, 16))
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayoutWidget_4 = QWidget(self.tab_4)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(0, 10, 1181, 771))
        self.gridLayout_6 = QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_109 = QLabel(self.gridLayoutWidget_4)
        self.label_109.setObjectName(u"label_109")

        self.gridLayout_6.addWidget(self.label_109, 0, 0, 1, 1, Qt.AlignHCenter)

        self.label_110 = QLabel(self.gridLayoutWidget_4)
        self.label_110.setObjectName(u"label_110")

        self.gridLayout_6.addWidget(self.label_110, 0, 1, 1, 1, Qt.AlignHCenter)

        self.ResSortListQ1 = QTableWidget(self.gridLayoutWidget_4)
        if (self.ResSortListQ1.columnCount() < 6):
            self.ResSortListQ1.setColumnCount(6)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.ResSortListQ1.setHorizontalHeaderItem(0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.ResSortListQ1.setHorizontalHeaderItem(1, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.ResSortListQ1.setHorizontalHeaderItem(2, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.ResSortListQ1.setHorizontalHeaderItem(3, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.ResSortListQ1.setHorizontalHeaderItem(4, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.ResSortListQ1.setHorizontalHeaderItem(5, __qtablewidgetitem19)
        self.ResSortListQ1.setObjectName(u"ResSortListQ1")

        self.gridLayout_6.addWidget(self.ResSortListQ1, 1, 1, 1, 1)

        self.ResUnsortListQ1 = QTableWidget(self.gridLayoutWidget_4)
        if (self.ResUnsortListQ1.columnCount() < 4):
            self.ResUnsortListQ1.setColumnCount(4)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.ResUnsortListQ1.setHorizontalHeaderItem(0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.ResUnsortListQ1.setHorizontalHeaderItem(1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.ResUnsortListQ1.setHorizontalHeaderItem(2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.ResUnsortListQ1.setHorizontalHeaderItem(3, __qtablewidgetitem23)
        self.ResUnsortListQ1.setObjectName(u"ResUnsortListQ1")
        self.ResUnsortListQ1.setMaximumSize(QSize(510, 16777215))

        self.gridLayout_6.addWidget(self.ResUnsortListQ1, 1, 0, 1, 1)

        self.label_42 = QLabel(self.tab_4)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(70, 820, 411, 20))
        self.tabWidget.addTab(self.tab_4, "")
        self.CC_Q_2_Tab = QWidget()
        self.CC_Q_2_Tab.setObjectName(u"CC_Q_2_Tab")
        self.label_45 = QLabel(self.CC_Q_2_Tab)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setGeometry(QRect(460, 10, 341, 16))
        self.gridLayoutWidget_3 = QWidget(self.CC_Q_2_Tab)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(0, 50, 1181, 771))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_43 = QLabel(self.gridLayoutWidget_3)
        self.label_43.setObjectName(u"label_43")

        self.gridLayout_3.addWidget(self.label_43, 0, 1, 1, 1, Qt.AlignHCenter)

        self.redListQ2 = QTableWidget(self.gridLayoutWidget_3)
        if (self.redListQ2.columnCount() < 3):
            self.redListQ2.setColumnCount(3)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.redListQ2.setHorizontalHeaderItem(0, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.redListQ2.setHorizontalHeaderItem(1, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.redListQ2.setHorizontalHeaderItem(2, __qtablewidgetitem26)
        self.redListQ2.setObjectName(u"redListQ2")
        self.redListQ2.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_3.addWidget(self.redListQ2, 1, 0, 1, 1)

        self.label_44 = QLabel(self.gridLayoutWidget_3)
        self.label_44.setObjectName(u"label_44")

        self.gridLayout_3.addWidget(self.label_44, 0, 0, 1, 1, Qt.AlignHCenter)

        self.blueListQ2 = QTableWidget(self.gridLayoutWidget_3)
        if (self.blueListQ2.columnCount() < 3):
            self.blueListQ2.setColumnCount(3)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.blueListQ2.setHorizontalHeaderItem(0, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.blueListQ2.setHorizontalHeaderItem(1, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.blueListQ2.setHorizontalHeaderItem(2, __qtablewidgetitem29)
        self.blueListQ2.setObjectName(u"blueListQ2")

        self.gridLayout_3.addWidget(self.blueListQ2, 1, 1, 1, 1)

        self.pushButtonAccept_2 = QPushButton(self.CC_Q_2_Tab)
        self.pushButtonAccept_2.setObjectName(u"pushButtonAccept_2")
        self.pushButtonAccept_2.setGeometry(QRect(800, 840, 331, 41))
        self.tabWidget.addTab(self.CC_Q_2_Tab, "")
        self.RES_Q_2_Tab = QWidget()
        self.RES_Q_2_Tab.setObjectName(u"RES_Q_2_Tab")
        self.gridLayoutWidget_5 = QWidget(self.RES_Q_2_Tab)
        self.gridLayoutWidget_5.setObjectName(u"gridLayoutWidget_5")
        self.gridLayoutWidget_5.setGeometry(QRect(0, 10, 1181, 771))
        self.gridLayout_7 = QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_111 = QLabel(self.gridLayoutWidget_5)
        self.label_111.setObjectName(u"label_111")

        self.gridLayout_7.addWidget(self.label_111, 0, 0, 1, 1, Qt.AlignHCenter)

        self.label_112 = QLabel(self.gridLayoutWidget_5)
        self.label_112.setObjectName(u"label_112")

        self.gridLayout_7.addWidget(self.label_112, 0, 1, 1, 1, Qt.AlignHCenter)

        self.ResSortListQ2 = QTableWidget(self.gridLayoutWidget_5)
        if (self.ResSortListQ2.columnCount() < 6):
            self.ResSortListQ2.setColumnCount(6)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.ResSortListQ2.setHorizontalHeaderItem(0, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.ResSortListQ2.setHorizontalHeaderItem(1, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.ResSortListQ2.setHorizontalHeaderItem(2, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.ResSortListQ2.setHorizontalHeaderItem(3, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.ResSortListQ2.setHorizontalHeaderItem(4, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.ResSortListQ2.setHorizontalHeaderItem(5, __qtablewidgetitem35)
        self.ResSortListQ2.setObjectName(u"ResSortListQ2")

        self.gridLayout_7.addWidget(self.ResSortListQ2, 1, 1, 1, 1)

        self.ResUnsortListQ2 = QTableWidget(self.gridLayoutWidget_5)
        if (self.ResUnsortListQ2.columnCount() < 5):
            self.ResUnsortListQ2.setColumnCount(5)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.ResUnsortListQ2.setHorizontalHeaderItem(0, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.ResUnsortListQ2.setHorizontalHeaderItem(1, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.ResUnsortListQ2.setHorizontalHeaderItem(2, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.ResUnsortListQ2.setHorizontalHeaderItem(3, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.ResUnsortListQ2.setHorizontalHeaderItem(4, __qtablewidgetitem40)
        self.ResUnsortListQ2.setObjectName(u"ResUnsortListQ2")
        self.ResUnsortListQ2.setMaximumSize(QSize(550, 16777215))

        self.gridLayout_7.addWidget(self.ResUnsortListQ2, 1, 0, 1, 1)

        self.tabWidget.addTab(self.RES_Q_2_Tab, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.gridLayoutWidget_7 = QWidget(self.tab_6)
        self.gridLayoutWidget_7.setObjectName(u"gridLayoutWidget_7")
        self.gridLayoutWidget_7.setGeometry(QRect(-1, -1, 1261, 771))
        self.gridLayout_9 = QGridLayout(self.gridLayoutWidget_7)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.gridLayoutWidget_8 = QWidget(self.tab_8)
        self.gridLayoutWidget_8.setObjectName(u"gridLayoutWidget_8")
        self.gridLayoutWidget_8.setGeometry(QRect(-1, -1, 1261, 771))
        self.gridLayout_10 = QGridLayout(self.gridLayoutWidget_8)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.tabWidget.addTab(self.tab_8, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1213, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.runsComboBox.setCurrentIndex(1)
        self.qualificationsComboBox.setCurrentIndex(1)
        self.roundsComboBox.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_18.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0444\u0435\u0440\u0438:", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b-\u0432\u043e \u0437\u0430\u0435\u0437\u0434\u043e\u0432", None))
        self.runsComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.runsComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))

        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0432\u0430\u044e\u0449\u0438\u0435:", None))
        self.label_19.setText("")
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0440\u0435\u043c\u044f \u043d\u0430\u0447\u0430\u043b\u0430", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u" \u041a\u0432\u0430\u043b\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u0438", None))
        self.qualificationsComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.qualificationsComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))

        self.qualificationsComboBox.setCurrentText(QCoreApplication.translate("MainWindow", u"2", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0432\u043e\u0440\u043e\u0442", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0438\u043d\u0430\u043b\u044b", None))
        self.label_21.setText("")
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0442\u0440\u0430\u0441\u0441\u044b", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043b\u0430\u0432\u043d\u044b\u0439 \u0441\u0435\u043a\u0440\u0435\u0442\u0430\u0440\u044c:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0441\u0442\u043e \u0438 \u0434\u0430\u0442\u0430 \u043f\u0440\u043e\u0432\u0435\u0434\u0435\u043d\u0438\u044f", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f \u0441\u043e\u0440\u0435\u0432\u043d\u043e\u0432\u0430\u043d\u0438\u0439", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0440\u0435\u043a\u0442\u043e\u0440 \u0441\u043e\u0440\u0435\u0432\u043d\u043e\u0432\u0430\u043d\u0438\u0439:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0442\u0430\u043d\u043e\u0432\u0449\u0438\u043a \u0442\u0440\u0430\u0441\u0441\u044b:", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0418\u041e", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u043b\u044c\u043d\u0438\u043a \u0442\u0440\u0430\u0441\u0441\u044b:", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0438\u043d\u0438\u0448", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u0445\u043d\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0434\u0435\u043b\u0435\u0433\u0430\u0442:", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0440\u0443\u0433\u0438", None))
        self.roundsComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"1/16", None))
        self.roundsComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"1/8", None))
        self.roundsComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"1/4", None))

        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0442\u043e\u0440\u044b", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"\u2116 \u0433\u043e\u043c\u043e\u043b\u043e\u0433\u0430\u0446\u0438\u0438", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0440\u043e\u0434", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043d\u0435\u0433", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0418\u041d\u0424\u041e\u0420\u041c\u0410\u0426\u0418\u042f \u041e \u0422\u0420\u0410\u0421\u0421\u0415", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0413\u041b\u0410\u0412\u041d\u0410\u042f \u0421\u0423\u0414\u0415\u0419\u0421\u041a\u0410\u042f \u041a\u041e\u041c\u0418\u0421\u0421\u0418\u042f", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043c\u043f\u0435\u0440\u0430\u0442\u0443\u0440\u0430 \u0441\u0442\u0430\u0440\u0442\u0430", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0444\u0435\u0440\u0438 \u043d\u0430 \u0441\u0442\u0430\u0440\u0442\u0435:", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0440\u0442", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"\u041f\u041e\u0413\u041e\u0414\u0410", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c", None))
        self.saveParams.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u043f\u0430\u0434 \u0432\u044b\u0441\u043e\u0442", None))
        self.label_31.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043c\u043f\u0435\u0440\u0430\u0442\u0443\u0440\u0430 \u0444\u0438\u043d\u0438\u0448\u0430", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043b\u0438\u043d\u043d\u0430 \u0442\u0440\u0430\u0441\u0441\u044b", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b", None))
        ___qtablewidgetitem = self.participantsTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"bib", None));
        ___qtablewidgetitem1 = self.participantsTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u0421.\u0424.", None));
        ___qtablewidgetitem2 = self.participantsTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0418\u041e", None));
        ___qtablewidgetitem3 = self.participantsTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0434 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f", None));
        ___qtablewidgetitem4 = self.participantsTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u0440\u044f\u0434", None));
        ___qtablewidgetitem5 = self.participantsTable.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u043a\u0438 \u041a\u0420", None));
        self.editpushButton.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.addpushButton.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0441\u043f\u043e\u0440\u0442\u0441\u043c\u0435\u043d\u0430", None))
        self.pushButtonLoadList.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0441\u043f\u0438\u0441\u043e\u043a \u0443\u0447\u0430\u0441\u0442\u043d\u0438\u043a\u043e\u0432", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b:", None))
        self.fileNameLabel.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u0421\u043f\u043e\u0440\u0442\u0441\u043c\u0435\u043d\u044b", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0418\u041d\u042f\u042f \u0422\u0420\u0410\u0421\u0421\u0410", None))
        ___qtablewidgetitem6 = self.redListQ1.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"bib", None));
        ___qtablewidgetitem7 = self.redListQ1.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u0421.\u0424.", None));
        ___qtablewidgetitem8 = self.redListQ1.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0418\u041e", None));
        ___qtablewidgetitem9 = self.redListQ1.horizontalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"\u0421.\u041a.", None));
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0420\u0410\u0421\u041d\u0410\u042f \u0422\u0420\u0410\u0421\u0421\u0410", None))
        ___qtablewidgetitem10 = self.blueListQ1.horizontalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"bib", None));
        ___qtablewidgetitem11 = self.blueListQ1.horizontalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"\u0421.\u0424.", None));
        ___qtablewidgetitem12 = self.blueListQ1.horizontalHeaderItem(2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0418\u041e", None));
        ___qtablewidgetitem13 = self.blueListQ1.horizontalHeaderItem(3)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"\u0421.\u041a.", None));
        self.pushButtonAccept.setText(QCoreApplication.translate("MainWindow", u"\u041f\u041e\u0414\u0422\u0412\u0415\u0420\u0414\u0418\u0422\u042c \u0421\u041f\u0418\u0421\u041e\u041a", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"\u041f\u041e\u0421\u0422\u0410\u041d\u041e\u0412\u041a\u0410 \u041d\u0410 \u0421\u0422\u0410\u0420\u0422 \u0420\u0423\u0427\u041a\u0410\u041c\u0418 \u041f\u041e \u0422\u042b\u041a\u0410\u041b\u041a\u0415??????", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"CC Q_1", None))
        self.label_109.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0415\u0421\u041e\u0420\u0422 \u0412\u0420\u0415\u041c\u042f \u0420\u0415\u0410\u041b\u0422\u0410\u0419\u041c", None))
        self.label_110.setText(QCoreApplication.translate("MainWindow", u"\u0421\u041e\u0420\u0422 \u0412\u0420\u0415\u041c\u042f \u0420\u0415\u0410\u041b\u0422\u0410\u0419\u041c + \u043c\u0435\u0441\u0442\u043e", None))
        ___qtablewidgetitem14 = self.ResSortListQ1.horizontalHeaderItem(0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0441\u0442\u043e", None));
        ___qtablewidgetitem15 = self.ResSortListQ1.horizontalHeaderItem(1)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"bib", None));
        ___qtablewidgetitem16 = self.ResSortListQ1.horizontalHeaderItem(2)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"\u0421.\u0424.", None));
        ___qtablewidgetitem17 = self.ResSortListQ1.horizontalHeaderItem(3)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0418\u041e", None));
        ___qtablewidgetitem18 = self.ResSortListQ1.horizontalHeaderItem(4)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0440\u0435\u043c\u044f", None));
        ___qtablewidgetitem19 = self.ResSortListQ1.horizontalHeaderItem(5)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0440\u0430\u0441\u0441\u0430", None));
        ___qtablewidgetitem20 = self.ResUnsortListQ1.horizontalHeaderItem(0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"bib", None));
        ___qtablewidgetitem21 = self.ResUnsortListQ1.horizontalHeaderItem(1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0418\u041e", None));
        ___qtablewidgetitem22 = self.ResUnsortListQ1.horizontalHeaderItem(2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0440\u0435\u043c\u044f", None));
        ___qtablewidgetitem23 = self.ResUnsortListQ1.horizontalHeaderItem(3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0440\u0430\u0441\u0441\u0430", None));
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0423\u0422 \u0412\u0421\u0415 \u0423\u0427\u0410\u0421\u0422\u041d\u0418\u041a\u0418. \u0412\u042b\u0414\u0415\u041b\u042f\u0422\u042c \u0426\u0412\u0415\u0422\u0410\u041c\u0418 \u0422\u0420\u0410\u0421\u0421\u0423 \u0418 \u0421\u0415\u0420\u042b\u041c \u041f\u0420\u041e\u0428\u0415\u0414\u0428\u0418\u0425", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Res Q_1", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"\u041f\u041e\u0421\u0422\u0410\u041d\u041e\u0412\u041a\u0410 \u041d\u0410 \u0421\u0422\u0410\u0420\u0422 \u0420\u0423\u0427\u041a\u0410\u041c\u0418 \u041f\u041e \u0422\u042b\u041a\u0410\u041b\u041a\u0415??????", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0418\u041d\u042f\u042f \u0422\u0420\u0410\u0421\u0421\u0410", None))
        ___qtablewidgetitem24 = self.redListQ2.horizontalHeaderItem(0)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"bib", None));
        ___qtablewidgetitem25 = self.redListQ2.horizontalHeaderItem(1)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0418\u041e", None));
        ___qtablewidgetitem26 = self.redListQ2.horizontalHeaderItem(2)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0440\u0435\u043c\u044f Q1", None));
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0420\u0410\u0421\u041d\u0410\u042f \u0422\u0420\u0410\u0421\u0421\u0410", None))
        ___qtablewidgetitem27 = self.blueListQ2.horizontalHeaderItem(0)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"bib", None));
        ___qtablewidgetitem28 = self.blueListQ2.horizontalHeaderItem(1)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0418\u041e", None));
        ___qtablewidgetitem29 = self.blueListQ2.horizontalHeaderItem(2)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0440\u0435\u043c\u044f Q1", None));
        self.pushButtonAccept_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u041e\u0414\u0422\u0412\u0415\u0420\u0414\u0418\u0422\u042c \u0421\u041f\u0418\u0421\u041e\u041a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.CC_Q_2_Tab), QCoreApplication.translate("MainWindow", u"CC Q_2", None))
        self.label_111.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0415\u0421\u041e\u0420\u0422 \u0412\u0420\u0415\u041c\u042f \u0420\u0415\u0410\u041b\u0422\u0410\u0419\u041c", None))
        self.label_112.setText(QCoreApplication.translate("MainWindow", u"\u0421\u041e\u0420\u0422 \u0412\u0420\u0415\u041c\u042f \u0420\u0415\u0410\u041b\u0422\u0410\u0419\u041c + \u043c\u0435\u0441\u0442\u043e", None))
        ___qtablewidgetitem30 = self.ResSortListQ2.horizontalHeaderItem(0)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0441\u0442\u043e", None));
        ___qtablewidgetitem31 = self.ResSortListQ2.horizontalHeaderItem(1)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"bib", None));
        ___qtablewidgetitem32 = self.ResSortListQ2.horizontalHeaderItem(2)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0418\u041e", None));
        ___qtablewidgetitem33 = self.ResSortListQ2.horizontalHeaderItem(3)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0440\u0435\u043c\u044fQ1", None));
        ___qtablewidgetitem34 = self.ResSortListQ2.horizontalHeaderItem(4)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0440\u0435\u043c\u044fQ2", None));
        ___qtablewidgetitem35 = self.ResSortListQ2.horizontalHeaderItem(5)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0440\u0430\u0441\u0441\u0430", None));
        ___qtablewidgetitem36 = self.ResUnsortListQ2.horizontalHeaderItem(0)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"bib", None));
        ___qtablewidgetitem37 = self.ResUnsortListQ2.horizontalHeaderItem(1)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0418\u041e", None));
        ___qtablewidgetitem38 = self.ResUnsortListQ2.horizontalHeaderItem(2)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0440\u0435\u043c\u044fQ1", None));
        ___qtablewidgetitem39 = self.ResUnsortListQ2.horizontalHeaderItem(3)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0440\u0435\u043c\u044fQ2", None));
        ___qtablewidgetitem40 = self.ResUnsortListQ2.horizontalHeaderItem(4)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0440\u0430\u0441\u0441\u0430", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.RES_Q_2_Tab), QCoreApplication.translate("MainWindow", u"Res Q_2", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"Finals", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), QCoreApplication.translate("MainWindow", u"\u0418\u0442\u043e\u0433", None))
    # retranslateUi

