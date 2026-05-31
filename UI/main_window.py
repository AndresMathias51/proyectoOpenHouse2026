from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QStackedWidget

from UI.theme import QSS
from UI.widgets.topbar import TopBar
from UI.widgets.console import Console

from UI.pages.inicio import InicioPage
from UI.pages.conexiones import ConexionesPage
from UI.pages.ips import IpsPage
from UI.pages.protocolos import ProtocolosPage
from UI.pages.ver_red import VerRedPage
from UI.pages.posiciones import PosicionesPage


from app import General_Core

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("AutoPKT")
        self.setStyleSheet(QSS)

        bg = QWidget()
        bg.setObjectName("Background")
        self.setCentralWidget(bg)
        self.calculadora = General_Core()
        root = QVBoxLayout(bg)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(0)

        self.topbar = TopBar()
        root.addWidget(self.topbar)

        self.console = Console()
        self.stack = QStackedWidget()

        # Pages reciben la consola para escribir logs (por ahora solo demo)
        self.stack.addWidget(InicioPage(self.console))
        self.stack.addWidget(ConexionesPage(self.console, self.calculadora))
        self.stack.addWidget(IpsPage(self.console, self.calculadora))
        self.stack.addWidget(PosicionesPage(self.console, self.calculadora))
        self.stack.addWidget(ProtocolosPage(self.console, self.calculadora))
        self.stack.addWidget(VerRedPage(self.console, self.calculadora))

        root.addWidget(self.stack, 1)
        root.addWidget(self.console)

        self.topbar.navigate.connect(self.stack.setCurrentIndex)

        self.console.write("> Interfaz cargada (solo UI). Backend pendiente.")