import sys

from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QMainWindow,QApplication
from  Ui_GiftWindow import Ui_MainWindow

class GifWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        self.num = 2
        super(GifWindow,self).__init__()
        self.setupUi(self)
        self.btnStart.clicked.connect(self.btnStart_Cilck)
        self.btnPaused.clicked.connect(self.btnPaused_Click)
        self.btnStop.clicked.connect(self.btnStop_Click)
        self.gifMovie =QMovie('image/run.gif')
        self.gifMovie.setScaledSize(self.label.size())
        self.label.setMovie(self.gifMovie)
        self.gifMovie.start()
        self.gifMovie.stop()
    def btnStart_Cilck(self):
        self.gifMovie.start()

    def btnPaused_Click(self):
        self.gifMovie.setPaused(self.num%2 == 1)
        print(145)
    def btnStop_Click(self):
        self.gifMovie.stop()

if __name__ == '__main__':
    app=QApplication(sys.argv)
    window = GifWindow()
    window.show()
    sys.exit(app.exec_())