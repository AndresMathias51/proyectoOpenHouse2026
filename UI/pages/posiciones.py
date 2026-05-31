from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QLineEdit, QFileDialog
)
from app import General_Core

from UI.widgets.card import make_card

class PosicionesPage(QWidget):
    def __init__(self, console, parent=None):
        super().__init__(parent)
        self.console = console
        self.pos_path: str | None = None
        self.general_core = General_Core()

        lay = QVBoxLayout(self)
        lay.addStretch(1)

        card, cl = make_card(
            "Configuración de Posiciones",
            "Selecciona el archivo CSV con coordenadas (x, y) para posicionar los dispositivos."
        )

        row = QHBoxLayout()
        self.btn_buscar = QPushButton("Seleccionar pos.csv")
        self.btn_buscar.setObjectName("Blue")

        self.input_path = QLineEdit()
        self.input_path.setObjectName("PathInput")
        self.input_path.setPlaceholderText("Selecciona pos.csv ...")
        self.input_path.setReadOnly(True)

        row.addWidget(self.btn_buscar)
        row.addWidget(self.input_path, 1)
        cl.addLayout(row)

        self.btn_aplicar = QPushButton("Aplicar Posiciones")
        self.btn_aplicar.setObjectName("Green")
        self.btn_aplicar.setEnabled(False)
        cl.addWidget(self.btn_aplicar)

        self.lbl_estado = QLabel("Aún no se ha seleccionado un archivo.")
        self.lbl_estado.setObjectName("Hint")
        cl.addWidget(self.lbl_estado)

        lay.addWidget(card, alignment=Qt.AlignHCenter)
        lay.addStretch(1)

        self.btn_buscar.clicked.connect(self._on_buscar_pos)
        self.btn_aplicar.clicked.connect(self._on_aplicar)

    def _on_buscar_pos(self):
        path, _ = QFileDialog.getOpenFileName(
            self,
            "Seleccionar pos.csv",
            "",
            "CSV (*.csv);;Todos los archivos (*.*)"
        )
        if not path:
            return

        self.general_core.asignar_posiciones(path, bandera=True)
        self.pos_path = path
        ##
        self.input_path.setText(path)
        self.btn_aplicar.setEnabled(True)
        self.lbl_estado.setText("Archivo seleccionado. Listo para aplicar.")
        self.console.write(f"> Archivo de posiciones seleccionado: {path}")

    def _on_aplicar(self):
        if not self.pos_path:
            return
        # demo por ahora
        self.console.write("> Aplicando posiciones... (pendiente backend)")
        self.console.write("> Respuesta: ok (demo)")