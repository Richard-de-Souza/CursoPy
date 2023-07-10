# QWidget e QLayout de PySide6.QtWidgets
# QWidget -> genérico
# QLayout -> Um widget de layout que recebe outros widgets
import sys

from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QApplication, QGridLayout,
                               QPushButton, QWidget, QMainWindow)

app = QApplication(sys.argv)


class MyWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.botao1 = self.button_maker('Fiz um botão')
        self.botao1.clicked.connect(self.segunda_acao_marcada)

        self.botao2 = self.button_maker('Fiz mais um botão')

        self.botao3 = self.button_maker('Fiz mais um 3° botão')

        self.central_widget = QWidget()

        self.setCentralWidget(self.central_widget)
        self.setWindowTitle('Um app massa')

        self.grid_layout = QGridLayout()
        self.central_widget.setLayout(self.grid_layout)

        self.grid_layout.addWidget(self.botao1, 1, 1, 1, 1)
        self.grid_layout.addWidget(self.botao2, 1, 2, 1, 1)
        self.grid_layout.addWidget(self.botao3, 3, 1, 1, 2)

        self.status_bar = self.statusBar()
        self.status_bar.showMessage('Olá mundo')

        self.menu = self.menuBar()
        self.primeiro_menu = self.menu.addMenu('TESTE')
        self.primeira_acao = self.primeiro_menu.addAction('Primeira ação')
        self.primeira_acao.triggered.connect(self.muda_mensagem)

        self.segunda_acao = self.primeiro_menu.addAction('Segunda ação')
        self.segunda_acao.setCheckable(True)
        self.segunda_acao.toggled.connect(self.segunda_acao_marcada)

    @Slot()
    def muda_mensagem(self):
        self.status_bar.showMessage('Mudei')

    @Slot()
    def segunda_acao_marcada(self, checked):
        print('Está marcado?', self.segunda_acao.isChecked())

    def button_maker(self, text):
        btn = QPushButton(text)
        btn.setStyleSheet('font-size: 80px;')
        return btn


window = MyWindow()
window.show()  # Central widget entre na hierarquia e mostre sua janela
app.exec()  # O loop da aplicação
