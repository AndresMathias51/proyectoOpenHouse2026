from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout
from UI.widgets.card import make_card
from app import General_Core

class ProtocolosPage(QWidget):
    def __init__(self, console, calculadora, parent=None):
        super().__init__(parent)
        self.console = console
        self.calculadora: General_Core = calculadora
        lay = QVBoxLayout(self)
        lay.addStretch(1)

        card, cl = make_card(
            "Enrutamiento Dinámico por Zonas",
            "Aquí haremos la lista de routers y botones Aplicar OSPF/RIP/EIGRP (después conectamos backend)."
        )
        card.setMaximumWidth(700)   # ancho
        card.setMinimumHeight(300)   # alto

        btn = QPushButton("Obtener lista de routers de Python (demo)")
        btn.setObjectName("Blue")
        btn.clicked.connect(lambda: self.console.write("> (demo) obtener routers"))
        cl.addWidget(btn)

        cl.addWidget(QLabel("Aplicar protocolo (demo):"))

        row = QHBoxLayout()
        for name in ["Aplicar OSPF", "Aplicar RIP", "Aplicar EIGRP"]:
            b = QPushButton(name)
            b.setObjectName("Green")
            b.clicked.connect(lambda checked=False, n=name: self.console.write(f"> (demo) {n}"))
            row.addWidget(b)
        cl.addLayout(row)

        hint = QLabel("Aún no conectado al backend.")
        hint.setObjectName("Hint")
        cl.addWidget(hint)

        lay.addWidget(card)
        lay.addStretch(1)