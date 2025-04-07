# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'demo.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btnSay = QPushButton(self.centralwidget)
        self.btnSay.setObjectName(u"btnSay")
        self.btnSay.setGeometry(QRect(30, 80, 140, 50))
        self.edSay = QLineEdit(self.centralwidget)
        self.edSay.setObjectName(u"edSay")
        self.edSay.setGeometry(QRect(30, 30, 600, 25))
        self.btnListen = QPushButton(self.centralwidget)
        self.btnListen.setObjectName(u"btnListen")
        self.btnListen.setGeometry(QRect(30, 150, 140, 50))
        self.edListen = QLineEdit(self.centralwidget)
        self.edListen.setObjectName(u"edListen")
        self.edListen.setGeometry(QRect(30, 230, 600, 25))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 27))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btnSay.setText(QCoreApplication.translate("MainWindow", u"\ub9d0\ud558\uae30", None))
        self.btnListen.setText(QCoreApplication.translate("MainWindow", u"\ub4e3\uae30", None))
    # retranslateUi

