# Вікно з діями

from PyQt5 import QtCore, QtGui, QtWidgets
from inputs import *


class Ui_ActionsWindow(object):  # Вікно з можливими діями
    def setup(self, ActionsWindow, i):
        self.fcursor = i  # Перший курсор з минулого класу
        self.scursor = -1  # Другий курсор визначає тип дії
        self.a = ActionsWindow
        ActionsWindow.setObjectName("ActionsWindow")
        ActionsWindow.resize(483, 343)
        self.centralwidget = QtWidgets.QWidget(ActionsWindow)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        ActionsWindow.setStyleSheet("background-color: #facd7e; border-radius: 10px")
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setFamily("MS Shell Dlg 2")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton.setStyleSheet('background-color: #ccaf8c; border-style:outset; border-radius:10px')
        self.pushButton.clicked.connect(self.click1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_2.setStyleSheet('background-color: #ccaf8c; border-style:outset; border-radius:10px')
        self.pushButton_2.clicked.connect(self.delet)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_3.setStyleSheet('background-color: #ccaf8c; border-style:outset; border-radius:10px')
        self.pushButton_3.clicked.connect(self.click2)
        ActionsWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ActionsWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 483, 26))
        self.menubar.setObjectName("menubar")
        ActionsWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ActionsWindow)
        self.statusbar.setObjectName("statusbar")
        ActionsWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ActionsWindow)
        QtCore.QMetaObject.connectSlotsByName(ActionsWindow)

    def click1(self):  # Перейти до додання
        self.scursor = 1
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_InputWindow()
        self.ui.setupI(self.window, self.fcursor, self.scursor)
        self.ui.modify()
        self.window.show()
        self.a.hide()

    def click2(self):  # Перейти до редагування
        self.scursor = 3
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_InputWindow()
        self.ui.setupI(self.window, self.fcursor, self.scursor)
        self.ui.modify()
        self.window.show()
        self.a.hide()

    def delet(self):  # Перейти до видалення
        self.scursor = 2
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_InputWindow()
        self.ui.setupI(self.window, self.fcursor, self.scursor)
        self.ui.modify()
        self.window.show()
        self.a.hide()


    def retranslateUi(self, ActionsWindow):
        _translate = QtCore.QCoreApplication.translate
        ActionsWindow.setWindowTitle(_translate("ActionsWindow", "Actions Window"))
        self.pushButton.setText(_translate("ActionsWindow", "Додати"))
        self.pushButton_2.setText(_translate("ActionsWindow", "Видалити"))
        self.pushButton_3.setText(_translate("ActionsWindow", "Змінити"))
