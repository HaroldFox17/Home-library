# Головна програма

from actions import *
from search import *
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):  # Розміщення об'єктів на головному вікні
        self.fcursor = -1  # Курсор визначає з чим користувач хоче працювати
        MainWindow.setObjectName("Main Page")
        MainWindow.resize(475, 796)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        MainWindow.setStyleSheet("background-color: #17b9eb; border-radius: 10px")
        self.btnVid = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnVid.sizePolicy().hasHeightForWidth())
        self.btnVid.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        stylesheet1 = '''QPushButton{background-color:#cde0f3; border-style:outset; border-radius:10px}
        QPushButton:hover{background-color:#9ec793;}'''
        self.btnVid.setFont(font)
        self.btnVid.setObjectName("btnVid")
        self.verticalLayout.addWidget(self.btnVid)
        self.btnVid.setStyleSheet(stylesheet1)
        self.btnVid.clicked.connect(self.click)
        self.btnAut = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy.setHeightForWidth(self.btnAut.sizePolicy().hasHeightForWidth())
        self.btnAut.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btnAut.setFont(font)
        self.btnAut.setObjectName("btnAut")
        self.verticalLayout.addWidget(self.btnAut)
        self.btnAut.setStyleSheet(stylesheet1)
        self.btnAut.clicked.connect(self.click1)
        self.btnJan = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy.setHeightForWidth(self.btnJan.sizePolicy().hasHeightForWidth())
        self.btnJan.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btnJan.setFont(font)
        self.btnJan.setObjectName("btnJan")
        self.verticalLayout.addWidget(self.btnJan)
        self.btnJan.setStyleSheet(stylesheet1)
        self.btnJan.clicked.connect(self.click2)
        self.btnPlace = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy.setHeightForWidth(self.btnPlace.sizePolicy().hasHeightForWidth())
        self.btnPlace.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btnPlace.setFont(font)
        self.btnPlace.setObjectName("btnPlace")
        self.verticalLayout.addWidget(self.btnPlace)
        self.btnPlace.setStyleSheet(stylesheet1)
        self.btnPlace.clicked.connect(self.click3)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.verticalLayout.addWidget(self.pushButton_6)
        self.pushButton_6.setFont(font)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setStyleSheet(stylesheet1)
        self.pushButton_6.clicked.connect(self.click4)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btnSearch = QtWidgets.QPushButton(self.centralwidget)
        self.verticalLayout.addWidget(self.btnSearch)
        sizePolicy.setHeightForWidth(self.btnSearch.sizePolicy().hasHeightForWidth())
        self.btnSearch.setSizePolicy(sizePolicy)
        self.btnSearch.setStyleSheet('''QPushButton{background-color:#659179; border-style:outset; border-radius:15px}
        QPushButton:hover{background-color:#a2ded7}''')
        self.btnSearch.clicked.connect(self.look)
        self.btnSearch.setFont(font)
        self.btnSearch.setObjectName("btnSearch")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def click(self):  # Перейти до дій з виданнями
        self.fcursor = 1
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ActionsWindow()
        self.ui.setup(self.window, self.fcursor)
        self.window.show()

    def click1(self):  # Перейти до дій з авторами
        self.fcursor = 2
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ActionsWindow()
        self.ui.setup(self.window, self.fcursor)
        self.window.show()

    def click2(self):  # Перейти до дій з місцями
        self.fcursor = 3
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ActionsWindow()
        self.ui.setup(self.window, self.fcursor)
        self.window.show()

    def click3(self):  # Перейти до дій з видами
        self.fcursor = 4
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ActionsWindow()
        self.ui.setup(self.window, self.fcursor)
        self.window.show()

    def click4(self):  # Перейти до дій з жанрами
        self.fcursor = 5
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ActionsWindow()
        self.ui.setup(self.window, self.fcursor)
        self.window.show()

    def look(self):  # Перейти до пошуку
        self.fcursor = 5
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SearchWindow()
        self.ui.setupS(self.window)
        self.window.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Main Page", "Main Page"))
        self.btnVid.setText(_translate("MainWindow", "Дії з виданнями"))
        self.btnAut.setText(_translate("MainWindow", "Дії з авторами"))
        self.btnJan.setText(_translate("MainWindow", "Дії з місцями"))
        self.btnPlace.setText(_translate("MainWindow", "Дії з видами"))
        self.btnSearch.setText(_translate("MainWindow", "Пошук"))
        self.pushButton_6.setText(_translate("MainWindow", "Дії з жанрами"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))


if __name__ == "__main__":  # Запуск головної програми
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
