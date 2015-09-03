__author__ = 'CPK'
import os,sys
from PyQt4 import QtGui
from PyQt4 import QtCore

class Login(QtGui.QMainWindow):

    def __init__(self):
        super(Login, self).__init__()
        self.setWindowTitle('Login')
        self.setWindowIcon(QtGui.QIcon('resource/images/login.png'))
        self.setFixedSize(400, 150)
        self.center()
        #create username icon
        self.username_icon = QtGui.QLabel(self)
        pixmap = QtGui.QPixmap(os.getcwd() + '/resource/images/user.png')
        pixmap = pixmap.scaled(20, 20, QtCore.Qt.KeepAspectRatio)
        self.username_icon.setPixmap(pixmap)
        self.username_icon.move(50,20)
        #create username textbox
        self.username = QtGui.QLineEdit(self)
        self.username.setPlaceholderText("Username...")
        self.username.move(70, 20)
        self.username.resize(280,20)
        #create password icon
        self.password_icon = QtGui.QLabel(self)
        pixmap = QtGui.QPixmap(os.getcwd() + '/resource/images/password.png')
        pixmap = pixmap.scaled(20, 20, QtCore.Qt.KeepAspectRatio)
        self.password_icon.setPixmap(pixmap)
        self.password_icon.move(50,50)
        #create password textbox
        self.password = QtGui.QLineEdit(self)
        self.password.setEchoMode(QtGui.QLineEdit.Password)
        self.password.setPlaceholderText("Password...")
        self.password.move(70, 50)
        self.password.resize(280,20)
        #create login button
        self.btn_login = QtGui.QPushButton('Login', self)
        #self.btn.setToolTip('This is a <b>QPushButton</b> widget')
        pixmap = QtGui.QPixmap(os.getcwd() + '/resource/images/login.png')
        pixmap = pixmap.scaled(20, 20, QtCore.Qt.KeepAspectRatio)
        self.btn_login.setIcon(QtGui.QIcon(pixmap))
        self.btn_login.resize(self.btn_login.sizeHint())
        self.btn_login.move(110, 80)
        self.btn_login.clicked.connect(self.loginClicked)
        #create cancel button cancel
        self.btn_cancel = QtGui.QPushButton('Cancel', self)
        #self.btn.setToolTip('This is a <b>QPushButton</b> widget')
        pixmap = QtGui.QPixmap(os.getcwd() + '/resource/images/cancel.png')
        pixmap = pixmap.scaled(20, 20, QtCore.Qt.KeepAspectRatio)
        self.btn_cancel.setIcon(QtGui.QIcon(pixmap))
        self.btn_cancel.resize(self.btn_cancel.sizeHint())
        self.btn_cancel.move(200, 80)
        self.btn_cancel.clicked.connect(self.cancelClicked)



    #hide
    def hide(self):
        #show form
        self.hide()

    #login method
    def loginClicked(self):
        self.statusBar().showMessage('Please wait to Login...')

    #cancel method
    def cancelClicked(self):
        self.statusBar().showMessage('Please wait to Cancel...')

    #move form to center of monitor
    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
