from PyQt5 import QtCore, QtGui, QtWidgets
import requests
import ctypes


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(204, 115)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.username = QtWidgets.QLineEdit(self.centralwidget)
        self.username.setGeometry(QtCore.QRect(80, 10, 113, 20))
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(80, 40, 113, 20))
        self.password.setObjectName("password")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 61, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 71, 16))
        self.label_2.setObjectName("label_2")
        self.register_2 = QtWidgets.QPushButton(self.centralwidget)
        self.register_2.setGeometry(QtCore.QRect(10, 70, 81, 23))
        self.register_2.setObjectName("register_2")
        self.login = QtWidgets.QPushButton(self.centralwidget)
        self.login.setGeometry(QtCore.QRect(110, 70, 81, 23))
        self.login.setObjectName("login")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.register_2.clicked.connect(self.Register)
        self.login.clicked.connect(self.Login)

        try:
            r = requests.get('https://Server-1.jjtv.repl.co')
            if 'Im online!' in r.text:
                pass
            else:
                ctypes.windll.user32.MessageBoxW(0, f"Server is offline! Try again later!", "Server is offline!", 0)
                raise Exception
        except:
            ctypes.windll.user32.MessageBoxW(0, f"Couldn't connect to server!", "You are offline!", 0)
            exit()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Username:"))
        self.label_2.setText(_translate("MainWindow", "Password:"))
        self.register_2.setText(_translate("MainWindow", "Register"))
        self.login.setText(_translate("MainWindow", "Login"))

    def Register(self):
        username = self.username.text()
        password = self.password.text()
        r = requests.get(f'https://Server-1.jjtv.repl.co/reg/{username}/{password}')
        if 'Ok' in r.text:
            ctypes.windll.user32.MessageBoxW(0, f"Successfully Registered with name {username}!", "Success!", 0)
        elif 'already' in r.text:
            ctypes.windll.user32.MessageBoxW(0, f"Account with username {username} already exists!!", "Fail!!", 5)

    def Login(self):
        username = self.username.text()
        password = self.password.text()
        r = requests.get(f'https://Server-1.jjtv.repl.co/login/{username}/{password}/')
        if 'Success' in r.text:
            ctypes.windll.user32.MessageBoxW(0, f"Successfully logged in with name {username}!", "Success!", 0)
        elif 'Wrong' in r.text:
            ctypes.windll.user32.MessageBoxW(0, f"Wrong Password for username {username}!", "Fail!", 5)
        elif 'existing' in r.text:
            ctypes.windll.user32.MessageBoxW(0, f"This account is not existing! Please register!!", "Not existing!", 5)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
