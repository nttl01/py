import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QApplication

class MyWin(QMainWindow):

    def __init__(self):
        super().__init__()

    def makeUI(self):
        self.setGeometry(100,200,300,400)
        self.setWindowTitle("my win")
        self.show()

app = QApplication(sys.argv)
myWin = MyWin()
myWin.makeUI()
sys.exit(app.exec())
