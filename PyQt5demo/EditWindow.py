import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from Ui_EditWindow import Ui_EditWindow

class Mainwindow(QMainWindow,Ui_EditWindow):
    def __init__(self):
        super(Mainwindow,self).__init__()
        self.setupUi(self)

    def btnQuery_Click(self):
        self.textinput.setText('1233')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window =Mainwindow()
    window.show()
    sys.exit(app.exec_())
