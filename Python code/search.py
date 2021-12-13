# Вікно пошуку


from PyQt5 import QtCore, QtGui, QtWidgets
from output import *  #
from models import DBHandler


class Ui_SearchWindow(object):  # Вікно пошуку
    def setupS(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(284, 217)
        stylesheet1 = '''QPushButton{background-color:#cde0f3; border-style:outset; border-radius:5px; height:23px;
                        width:80px}
                        QPushButton:hover{background-color:#9ec793;}'''
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_5)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.out)
        self.pushButton.setStyleSheet(stylesheet1)
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.pushButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 284, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def out(self):  # Перехід до вікна виведення інформації
        nameg = self.lineEdit.text()
        typg = self.lineEdit_2.text()
        authorg = self.lineEdit_3.text()
        genreg = self.lineEdit_5.text()
        db = DBHandler()  # Робота з БД
        x = db.search(name=nameg, genre=genreg, author=authorg, typ=typg)
        self.window = QtWidgets.QMainWindow()  # Робота з вікном виводу, див відповідний клас
        self.ui = Ui_OutputWindow()
        self.ui.setupO(self.window)
        self.ui.mod(x)
        self.window.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("SearchWindow", "Search Window"))
        self.label.setText(_translate("MainWindow", "Введіть назву"))
        self.label_2.setText(_translate("MainWindow", "Введіть вид"))
        self.label_3.setText(_translate("MainWindow", "Введіть автора"))
        self.label_4.setText(_translate("MainWindow", "Введіть жанр"))
        self.pushButton.setText(_translate("MainWindow", "Ok"))
