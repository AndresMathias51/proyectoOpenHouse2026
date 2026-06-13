from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QFrame

from UI.widgets.card import make_card
from app import General_Core

class VerRedPage(QWidget):
    def __init__(self, console, calculadora, parent=None):
        super().__init__(parent)
        self.console = console
        self.calculadora: General_Core = calculadora

        lay = QVBoxLayout(self)
        lay.addStretch(1)

        card, cl = make_card(
            "Renderizado y Exportación",
            "Reservado para mostrar el grafo y generar el PKT final (después conectamos backend)."
        )

        canvas = QFrame()
        canvas.setMinimumHeight(220)
        canvas.setStyleSheet(
            "background:#000; border-radius:12px; border:1px solid rgba(148,163,184,0.18);"
        )
        c_l = QVBoxLayout(canvas)

        msg = QLabel("[Lienzo reservado para render de red]")
        msg.setAlignment(Qt.AlignCenter)
        msg.setStyleSheet("color:#64748b;")
        c_l.addWidget(msg)
        cl.addWidget(canvas)

        self.btn_build = QPushButton("CONSTRUIR ARCHIVO PKT FINAL")
        self.btn_build.setObjectName("Green")
        self.btn_build.clicked.connect(self.on_construir_pkt)
        cl.addWidget(self.btn_build)

        lay.addWidget(card, alignment=Qt.AlignHCenter)
        lay.addStretch(1)

    def on_construir_pkt(self):
        # Por ahora hace lo mismo que el lambda
        self.console.write("> Archivo pkt generado correctamente")
        self.calculadora.send_devices_attributes_xml()
        # Aquí después le agregas más pasos, por ejemplo:
        # - validar que ya cargaste conexiones/ips/posiciones
        # - aplicar protocolos
        # - llamar self.calculadora.send_devices_attributes_xml()
        # - actualizar UI/estado