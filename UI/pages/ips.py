from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QLineEdit, QFileDialog
)
from app import General_Core

from UI.widgets.card import make_card

class IpsPage(QWidget):
    def __init__(self, console, calculadora, parent=None):
        super().__init__(parent)
        self.console = console
        self.calculadora: General_Core = calculadora

        self.ips_path: str | None = None
        lay = QVBoxLayout(self)
        lay.addStretch(1)

        card, cl = make_card(
            "Configuración de Direccionamiento IP",
            "Selecciona el archivo CSV de IPs y luego cárgalo/valídalo."
        )

        # fila: botón buscar + input ruta
        row = QHBoxLayout()
        self.btn_buscar = QPushButton("Seleccionar ips.csv")
        self.btn_buscar.setObjectName("Blue")

        self.input_path = QLineEdit()
        self.input_path.setObjectName("PathInput")
        self.input_path.setPlaceholderText("Selecciona ips.csv ...")
        self.input_path.setReadOnly(True)

        row.addWidget(self.btn_buscar)
        row.addWidget(self.input_path, 1)
        cl.addLayout(row)

        # botón cargar/validar
        self.btn_cargar = QPushButton("Cargar y Validar IPs")
        self.btn_cargar.setObjectName("Green")
        self.btn_cargar.setEnabled(False)
        cl.addWidget(self.btn_cargar)

        self.lbl_estado = QLabel("Aún no se ha seleccionado un archivo.")
        self.lbl_estado.setObjectName("Hint")
        cl.addWidget(self.lbl_estado)

        lay.addWidget(card, alignment=Qt.AlignHCenter)
        lay.addStretch(1)

        # señales
        self.btn_buscar.clicked.connect(self._on_buscar_ips)
        self.btn_cargar.clicked.connect(self._on_cargar)

    def _on_buscar_ips(self):
        path, _ = QFileDialog.getOpenFileName(
            self,
            "Seleccionar ips.csv",
            "",
            "CSV (*.csv);;Todos los archivos (*.*)"
        )
        if not path:
            return

        self.ips_path = path
        ##
        self.calculadora.put_ips_devices(path)
        ##
        self.input_path.setText(path)
        self.btn_cargar.setEnabled(True)
        self.lbl_estado.setText("Archivo seleccionado. Listo para cargar.")
        self.console.write(f"> Archivo de IPs seleccionado: {path}")

    def _on_cargar(self):
        # Por ahora solo demo (luego conectamos backend aquí)
        if not self.ips_path:
            return
        self.console.write("> Cargando y validando IPs... (pendiente backend)")
        self.console.write("> Respuesta: ok (demo)")