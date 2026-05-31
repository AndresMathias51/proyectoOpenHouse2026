from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QFrame

from UI.widgets.card import make_card

class IpsPage(QWidget):
    def __init__(self, console, parent=None):
        super().__init__(parent)
        self.console = console

        lay = QVBoxLayout(self)
        lay.addStretch(1)

        card, cl = make_card(
            "Configuración de Direccionamiento IP",
            "Aquí pondremos selección de ips.csv y validación (después conectamos backend)."
        )
        card.setMaximumWidth(1000)   # prueba 950, 1050, etc.
        card.setMinimumHeight(360)   # prueba 340, 420, etc.

        btn = QPushButton("Seleccionar archivo ips.csv (demo)")
        btn.setObjectName("Blue")
        btn.clicked.connect(lambda: self.console.write("> (demo) seleccionar ips.csv"))
        cl.addWidget(btn)

        btn2 = QPushButton("Cargar y Validar IPs (demo)")
        btn2.setObjectName("Green")
        btn2.clicked.connect(lambda: self.console.write("> (demo) cargar y validar IPs"))
        cl.addWidget(btn2)

        hint = QLabel("Aún no conectado al backend.")
        hint.setObjectName("Hint")
        cl.addWidget(hint)

        lay.addWidget(card, alignment=Qt.AlignHCenter)
        lay.addStretch(1)