# Вікно введення інформації

from PyQt5 import QtCore, QtGui, QtWidgets
from output import *
from models import DBHandler


class Ui_InputWindow(object):  # Вікно введення інфорації
    def setupI(self, InputWindow, i, j):
        self.fcursor = i
        self.scursor = j
        self.i = InputWindow
        InputWindow.setObjectName("InputWindow")
        InputWindow.resize(514, 311)
        stylesheet1 = '''QPushButton{background-color:#cde0f3; border-style:outset; border-radius:5px; height:23px;
                width:80px}
                QPushButton:hover{background-color:#9ec793;}'''
        self.centralwidget = QtWidgets.QWidget(InputWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_6)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lineEdit_5)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet(stylesheet1)
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.pushButton)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_7)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_7)
        InputWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(InputWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 514, 26))
        self.menubar.setObjectName("menubar")
        InputWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(InputWindow)
        self.statusbar.setObjectName("statusbar")
        self.pushButton.clicked.connect(self.out)
        InputWindow.setStatusBar(self.statusbar)

        self.retranslateUi(InputWindow)
        QtCore.QMetaObject.connectSlotsByName(InputWindow)

    def modify(self):  # Модифікуємо вікно відповідно до значень курсор
        if self.scursor == 1:
            self.label.setParent(None)
            self.lineEdit.setParent(None)
            if self.fcursor == 1:
                self.i.resize(408, 269)
            else:
                self.label_3.setParent(None)
                self.lineEdit_3.setParent(None)
                self.label_4.setParent(None)
                self.lineEdit_4.setParent(None)
                self.label_5.setParent(None)
                self.lineEdit_5.setParent(None)
                self.label_6.setParent(None)
                self.lineEdit_6.setParent(None)
                self.label_7.setParent(None)
                self.lineEdit_7.setParent(None)
                self.i.resize(408, 105)
        elif self.scursor == 2:
            self.label_2.setParent(None)
            self.lineEdit_2.setParent(None)
            self.label_3.setParent(None)
            self.lineEdit_3.setParent(None)
            self.label_4.setParent(None)
            self.lineEdit_4.setParent(None)
            self.label_5.setParent(None)
            self.lineEdit_5.setParent(None)
            self.label_6.setParent(None)
            self.lineEdit_6.setParent(None)
            self.label_7.setParent(None)
            self.lineEdit_7.setParent(None)
            self.i.resize(408, 100)
        elif self.scursor == 3:
            if self.fcursor != 1:
                self.label_3.setParent(None)
                self.lineEdit_3.setParent(None)
                self.label_4.setParent(None)
                self.lineEdit_4.setParent(None)
                self.label_5.setParent(None)
                self.lineEdit_5.setParent(None)
                self.label_6.setParent(None)
                self.lineEdit_6.setParent(None)
                self.label_7.setParent(None)
                self.lineEdit_7.setParent(None)
                self.i.resize(408, 135)

    def out(self):  # Робота з БД відповідно до курсорів
        db = DBHandler()
        x = "Щось пішло не так"
        if self.scursor == 1:
            if self.fcursor == 1:
                name = self.lineEdit_2.text()
                author = self.lineEdit_3.text()
                typ = self.lineEdit_4.text()
                place = self.lineEdit_6.text()
                year = int(self.lineEdit_5.text())
                genre = self.lineEdit_7.text()
                db.add_edition(name, author, typ, genre, place, year)
                x = "Видання додано"
            elif self.fcursor == 2:
                name = self.lineEdit_2.text()
                print(name)
                db.add_author(name)
                x = "Автора додано"
            elif self.fcursor == 3:
                name = self.lineEdit_2.text()
                db.add_place(name)
                x = "Місце додано"
            elif self.fcursor == 4:
                name = self.lineEdit_2.text()
                db.add_type(name)
                x = "Вид додано"
            elif self.fcursor == 5:
                name = self.lineEdit_2.text()
                db.add_genre(name)
                x = "Жанр додано"
        elif self.scursor == 2:
            idg = int(self.lineEdit.text())
            if self.fcursor == 1:
                x = "Видання видалено"
                db.delete_edition(idg)
            elif self.fcursor == 2:
                x = "Автора видалено"
                db.delete_author(idg)
            elif self.fcursor == 3:
                x = "Місце видалено"
                db.delete_place(idg)
            elif self.fcursor == 4:
                x = "Вид видалено"
                db.delete_type(idg)
            elif self.fcursor == 1:
                x = "Жанр видалено"
                db.delete_genre(idg)
        elif self.scursor == 3:
            idg = int(self.lineEdit.text())
            nameg = self.lineEdit_2.text()
            if self.fcursor == 1:
                authorg = self.lineEdit_3.text()
                typg = self.lineEdit_4.text()
                placeg = self.lineEdit_6.text()
                yearg = int(self.lineEdit_5.text())
                genreg = self.lineEdit_7.text()
                db.redact_edition(idg, nameg, authorg, typg, genreg, placeg, yearg)
                x = "Видання відредаговано"
            elif self.fcursor == 2:
                x = "Автора відредаговано"
                db.redact_author(idg, nameg)
            elif self.fcursor == 3:
                x = "Місце відредаговано"
                db.redact_place(idg, nameg)
            elif self.fcursor == 4:
                x = "Вид відредаговано"
                db.redact_type(idg, nameg)
            elif self.fcursor == 5:
                x = "Жанр відредаговано"
                db.redact_genre(idg, nameg)

        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_OutputWindow()
        self.ui.setupO(self.window)
        self.ui.mod(x)
        self.window.show()

    def retranslateUi(self, InputWindow):
        _translate = QtCore.QCoreApplication.translate
        InputWindow.setWindowTitle(_translate("InputWindow", "Input Window"))
        self.label.setText(_translate("InputWindow", "Введіть id"))
        self.label_2.setText(_translate("InputWindow", "Введіть назву"))
        self.label_3.setText(_translate("InputWindow", "Введіть автора"))
        self.label_4.setText(_translate("InputWindow", "Введіть вид"))
        self.pushButton.setText(_translate("InputWindow", "Ok"))
        self.label_5.setText(_translate("InputWindow", "Введіть місце"))
        self.label_6.setText(_translate("InputWindow", "Введіть жанр"))
        self.label_7.setText(_translate("InputWindow", "Введіть рік"))

