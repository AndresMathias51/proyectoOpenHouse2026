from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QFrame

from UI.widgets.card import make_card

class VerRedPage(QWidget):
    def __init__(self, console, parent=None):
        super().__init__(parent)
        self.console = console

        lay = QVBoxLayout(self)
        lay.addStretch(1)

        card, cl = make_card(
            "Renderizado y Exportación",
            "Reservado para mostrar el grafo y generar el PKT final (después conectamos backend)."
        )

        canvas = QFrame()
        canvas.setMinimumHeight(220)
        canvas.setStyleSheet("background:#000; border-radius:12px; border:1px solid rgba(148,163,184,0.18);")
        c_l = QVBoxLayout(canvas)
        msg = QLabel("[Lienzo reservado para render de red]")
        msg.setAlignment(Qt.AlignCenter)
        msg.setStyleSheet("color:#64748b;")
        c_l.addWidget(msg)
        cl.addWidget(canvas)

        btn = QPushButton("CONSTRUIR ARCHIVO PKT FINAL (demo)")
        btn.setObjectName("Green")
        btn.clicked.connect(lambda: self.console.write("> (demo) construir PKT final"))
        cl.addWidget(btn)

        lay.addWidget(card, alignment=Qt.AlignHCenter)
        lay.addStretch(1)