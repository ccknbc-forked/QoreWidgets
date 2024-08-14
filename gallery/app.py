

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PySide6.QtGui import QIcon
# from qdarktheme import load_stylesheet

try:
    import QoreWidgets
except ImportError:
    import sys
    import os
    # switch to current path
    curdir=os.path.dirname(os.path.abspath(__file__))
    # get parent dir
    sys.path.append(
        os.path.join(os.path.dirname(curdir) , 'src')
    )
    import QoreWidgets

import rc_assets
from ui_main import Ui_MainWindow

class MainWindow(QoreWidgets.FramelessWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.sidebar_example()
        self.titlebar_example()

    def sidebar_example(self):
        def update_foldState(fold: bool):
            self.ui.label_foldState.setText(f"The Sidebar is {'folded >_<' if fold else 'unfolded OvO'}")

        self.ui.sidetab.foldStateChanged.connect(update_foldState)
        update_foldState(self.ui.sidetab.is_folded())

        self.ui.btn_expand.clicked.connect(lambda: self.ui.sidetab.set_foldState(False))
        self.ui.btn_fold.clicked.connect(lambda: self.ui.sidetab.set_foldState(True))

    def titlebar_example(self):
        self.ui.label_appIcon.setPixmap(QIcon(":/icons/account").pixmap(20))
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    # app.setStyleSheet(load_stylesheet())
    window = MainWindow()
    window.show()
    sys.exit(app.exec())