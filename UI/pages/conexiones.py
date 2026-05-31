from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QLineEdit, QFileDialog
)

from UI.widgets.card import make_card

class ConexionesPage(QWidget):
    def __init__(self, console, parent=None):
        super().__init__(parent)
        self.console = console
        self.csv_path: str | None = None

        lay = QVBoxLayout(self)
        lay.addStretch(1)

        card, cl = make_card(
            "Gestor de Topología Base",
            "Selecciona el archivo CSV que contiene las conexiones físicas de la red."
        )

        # fila: botón buscar + input ruta
        row = QHBoxLayout()
        self.btn_buscar = QPushButton("Buscar Archivo CSV")
        self.btn_buscar.setObjectName("Blue")

        self.input_path = QLineEdit()
        self.input_path.setObjectName("PathInput")
        self.input_path.setPlaceholderText("Selecciona conexiones.csv ...")
        self.input_path.setReadOnly(True)

        row.addWidget(self.btn_buscar)
        row.addWidget(self.input_path, 1)
        cl.addLayout(row)

        # botón iniciar
        self.btn_iniciar = QPushButton("Iniciar Análisis de Grafo")
        self.btn_iniciar.setObjectName("Green")
        self.btn_iniciar.setEnabled(False)  # se habilita cuando haya archivo
        cl.addWidget(self.btn_iniciar)

        self.lbl_estado = QLabel("Aún no se ha seleccionado un archivo.")
        self.lbl_estado.setObjectName("Hint")
        cl.addWidget(self.lbl_estado)

        lay.addWidget(card, alignment=Qt.AlignHCenter)
        lay.addStretch(1)

        # señales
        self.btn_buscar.clicked.connect(self._on_buscar_csv)
        self.btn_iniciar.clicked.connect(self._on_iniciar)

    def _on_buscar_csv(self):
        path, _ = QFileDialog.getOpenFileName(
            self,
            "Seleccionar conexiones.csv",
            "",
            "CSV (*.csv);;Todos los archivos (*.*)"
        )
        if not path:
            return

        self.csv_path = path
        self.input_path.setText(path)
        self.btn_iniciar.setEnabled(True)
        self.lbl_estado.setText("Archivo cargado. Listo para iniciar.")
        self.console.write(f"> CSV cargado: {path}")

    def _on_iniciar(self):
        # Por ahora solo demo (luego conectamos backend aquí)
        if not self.csv_path:
            return
        self.console.write("> Enviando ruta real de topología al núcleo de Python... (pendiente backend)")
        self.console.write("> Éxito: True (demo)")