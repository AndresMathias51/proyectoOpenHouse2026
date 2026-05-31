from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton

from UI.widgets.card import make_card

class ConexionesPage(QWidget):
    def __init__(self, console, parent=None):
        super().__init__(parent)
        self.console = console

        lay = QVBoxLayout(self)
        lay.addStretch(1)

        card, cl = make_card(
            "Gestor de Topología Base",
            "Aquí irán los botones para cargar conexiones.csv y construir el grafo (después conectamos backend)."
        )
        card.setMaximumWidth(1000)   # prueba 950, 1050, etc.
        card.setMinimumHeight(320)   # prueba 340, 420, etc.

        btn = QPushButton("Buscar Archivo CSV (demo)")
        btn.setObjectName("Blue")
        btn.clicked.connect(lambda: self.console.write("> (demo) seleccionar conexiones.csv"))
        cl.addWidget(btn)

        btn2 = QPushButton("Iniciar Análisis de Grafo (demo)")
        btn2.setObjectName("Green")
        btn2.clicked.connect(lambda: self.console.write("> (demo) iniciar análisis de grafo"))
        cl.addWidget(btn2)

        hint = QLabel("Aún no conectado al backend.")
        hint.setObjectName("Hint")
        cl.addWidget(hint)

        lay.addWidget(card, alignment=Qt.AlignHCenter)
        lay.addStretch(1)