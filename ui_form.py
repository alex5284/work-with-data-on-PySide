# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QPushButton, QSizePolicy,
    QTableView, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1005, 637)
        self.btn_file = QPushButton(Widget)
        self.btn_file.setObjectName(u"btn_file")
        self.btn_file.setGeometry(QRect(70, 40, 101, 31))
        self.tableView = QTableView(Widget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(20, 90, 331, 421))
        self.tableView_2 = QTableView(Widget)
        self.tableView_2.setObjectName(u"tableView_2")
        self.tableView_2.setGeometry(QRect(360, 90, 421, 281))
        self.btn_calc = QPushButton(Widget)
        self.btn_calc.setObjectName(u"btn_calc")
        self.btn_calc.setGeometry(QRect(190, 40, 101, 31))
        self.btn_bubble = QPushButton(Widget)
        self.btn_bubble.setObjectName(u"btn_bubble")
        self.btn_bubble.setGeometry(QRect(300, 40, 101, 31))
        self.btn_scatter_matrix = QPushButton(Widget)
        self.btn_scatter_matrix.setObjectName(u"btn_scatter_matrix")
        self.btn_scatter_matrix.setGeometry(QRect(410, 40, 111, 31))
        self.btn_par_coord = QPushButton(Widget)
        self.btn_par_coord.setObjectName(u"btn_par_coord")
        self.btn_par_coord.setGeometry(QRect(530, 40, 151, 31))

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.btn_file.setText(QCoreApplication.translate("Widget", u"File", None))
        self.btn_calc.setText(QCoreApplication.translate("Widget", u"Calc", None))
        self.btn_bubble.setText(QCoreApplication.translate("Widget", u"Bubble", None))
        self.btn_scatter_matrix.setText(QCoreApplication.translate("Widget", u"Scatter matrix", None))
        self.btn_par_coord.setText(QCoreApplication.translate("Widget", u"Parallel coordinates", None))
    # retranslateUi

