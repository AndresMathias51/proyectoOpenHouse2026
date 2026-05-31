from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QFrame, QLabel

from UI.widgets.card import make_card

class InicioPage(QWidget):
    def __init__(self, console, parent=None):
        super().__init__(parent)
        self.console = console

        lay = QVBoxLayout(self)
        lay.addStretch(1)

        card, cl = make_card(
            "Bienvenido a AutoPKT",
            "Plataforma para automatización y modelado de topologías. Sigue el flujo en las pestañas superiores."
        )

        grid = QGridLayout()
        grid.setSpacing(12)
        grid.addWidget(self._mini("1. Ingresa Datos", "Carga CSV de conexiones e IPs."), 0, 0)
        grid.addWidget(self._mini("2. Lógica de Red", "Protocolos (OSPF, RIP, EIGRP)."), 0, 1)
        grid.addWidget(self._mini("3. Exportación", "Genera XML / PKT final."), 0, 2)
        cl.addLayout(grid)

        lay.addWidget(card, alignment=Qt.AlignHCenter)
        lay.addStretch(1)

    def _mini(self, title: str, body: str) -> QFrame:
        c, l = make_card(title, body, max_width=9999)
        l.setContentsMargins(16, 12, 16, 12)
        return c