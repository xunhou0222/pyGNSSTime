import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from util import myCentralWiget


if __name__ == '__main__':
    app = QApplication([])
    win = QMainWindow()

    win.setGeometry(300, 300, 800, 600)
    win.setWindowTitle("GNSS时间转换程序 -- by jtw")
    qr = win.frameGeometry()
    cp = win.screen().availableGeometry().center()
    qr.moveCenter(cp)
    win.move( qr.topLeft() )

    cwig = myCentralWiget(win)
    win.setCentralWidget(cwig)

    win.show()
    sys.exit( app.exec() )