from LoginForm import Login

__author__ = 'CPK'
import sys
from PyQt4 import QtGui

class SystemTrayIcon(QtGui.QSystemTrayIcon):

    def __init__(self, icon, parent=None):
        QtGui.QSystemTrayIcon.__init__(self, icon, parent)
        menu = QtGui.QMenu(parent)
        exitAction = menu.addAction("Exit")
        exitAction.triggered.connect(self.showLogin)
        loginAction = menu.addAction("Login")
        loginAction.triggered.connect(self.showLogin)
        self.setContextMenu(menu)

    def showLogin(self):
        self.loginForm = Login()
        self.loginForm.show()

def main():
    app = QtGui.QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)

    w = QtGui.QWidget()
    trayIcon = SystemTrayIcon(QtGui.QIcon("resource/images/app.png"), w)

    trayIcon.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()