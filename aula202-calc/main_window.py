from PySide6.QtWidgets import (
    QWidget, QMainWindow, QVBoxLayout, QMessageBox)


class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, *kwargs)

        # configurando o layout
        self.cw = QWidget()
        self.vLayout = QVBoxLayout()
        self.cw.setLayout(self.vLayout)
        self.setCentralWidget(self.cw)

        # titulo
        self.setWindowTitle('Calculadora')

    def adjustFixedSize(self):
        # ultima coisa a se fazer
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    def addWidgetToVLayout(self, widget: QWidget):
        self.vLayout.addWidget(widget)

    def makeMsgBox(self):
        return QMessageBox(self)
