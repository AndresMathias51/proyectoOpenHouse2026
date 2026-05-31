from PySide6.QtCore import Signal
from PySide6.QtWidgets import QFrame, QHBoxLayout, QLabel, QPushButton

class TopBar(QFrame):
    navigate = Signal(int)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("TopBar")

        lay = QHBoxLayout(self)
        lay.setContentsMargins(18, 12, 18, 12)
        lay.setSpacing(25)

        brand = QLabel("AutoPKT")
        brand.setObjectName("Brand")
        lay.addWidget(brand)
        lay.addSpacing(16)

        self.buttons: list[QPushButton] = []
        names = ["Inicio", "Conexiones", "Asignar IPs", "Protocolos", "Ver Red"]

        for i, name in enumerate(names):
            b = QPushButton(name)
            b.setObjectName("NavBtn")
            b.setCheckable(True)
            b.clicked.connect(lambda checked=False, idx=i: self._go(idx))
            lay.addWidget(b)
            self.buttons.append(b)

        lay.addStretch(1)
        self.set_active(0)

    def _go(self, idx: int):
        self.set_active(idx)
        self.navigate.emit(idx)

    def set_active(self, idx: int):
        for i, b in enumerate(self.buttons):
            b.setChecked(i == idx)