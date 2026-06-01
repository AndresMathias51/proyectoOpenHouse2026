from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout,
    QFrame, QMessageBox
)

from UI.widgets.card import make_card
from app import General_Core


class ProtocolosPage(QWidget):
    """
    - Carga routers desde calculadora.lista_routers
    - Permite seleccionar routers (chips) y aplicar OSPF/RIP/EIGRP
    - Máximo 2 protocolos distintos en total.
    - Al aplicar, los routers seleccionados desaparecen del panel.
    - Guarda en self.protocolos con el formato:
        {"OSPF": ["R1","R2"], "RIP": ["R3"]}
    """
    def __init__(self, console, calculadora: General_Core, parent=None):
        super().__init__(parent)
        self.console = console
        self.calculadora: General_Core = calculadora

        # Diccionario acumulado (máximo 2 protocolos distintos)
        self.protocolos: dict[str, list[str]] = self.calculadora.dic_protocolo_aux

        # Routers disponibles (no asignados todavía)
        self._routers_disponibles: list[str] = []

        # Selección actual (routers marcados)
        self._seleccion: set[str] = set()

        lay = QVBoxLayout(self)
        lay.addStretch(1)

        card, cl = make_card(
            "Enrutamiento Dinámico por Zonas",
            "Selecciona routers, luego aplica OSPF/RIP/EIGRP. Máximo 2 protocolos distintos por topología."
        )
        card.setMaximumWidth(900)
        card.setMinimumHeight(380)

        # Botón para cargar routers desde Python
        self.btn_cargar = QPushButton("Obtener lista de routers de Python")
        self.btn_cargar.setObjectName("Blue")
        self.btn_cargar.clicked.connect(self._cargar_routers)
        cl.addWidget(self.btn_cargar)

        cl.addWidget(QLabel("1. Selecciona routers para la zona:"))

        # Panel negro contenedor de chips
        self.panel_routers = QFrame()
        self.panel_routers.setStyleSheet(
            "background:#000; border-radius:12px; border:1px solid rgba(148,163,184,0.18);"
        )
        self.panel_routers.setMinimumHeight(80)
        self.panel_routers_layout = QHBoxLayout(self.panel_routers)
        self.panel_routers_layout.setContentsMargins(12, 12, 12, 12)
        self.panel_routers_layout.setSpacing(10)

        self.lbl_hint = QLabel("Presiona el botón superior para cargar los routers.")
        self.lbl_hint.setObjectName("Hint")
        self.panel_routers_layout.addWidget(self.lbl_hint)

        cl.addWidget(self.panel_routers)

        # Botones aplicar
        cl.addWidget(QLabel("2. Aplicar protocolo a selección:"))

        row = QHBoxLayout()
        self.btn_ospf = QPushButton("Aplicar OSPF")
        self.btn_ospf.setObjectName("Green")
        self.btn_rip = QPushButton("Aplicar RIP")
        self.btn_rip.setObjectName("Green")
        self.btn_eigrp = QPushButton("Aplicar EIGRP")
        self.btn_eigrp.setObjectName("Green")

        for b in (self.btn_ospf, self.btn_rip, self.btn_eigrp):
            b.setEnabled(False)
            b.setMinimumHeight(44)

        self.btn_ospf.clicked.connect(lambda: self._aplicar("OSPF"))
        self.btn_rip.clicked.connect(lambda: self._aplicar("RIP"))
        self.btn_eigrp.clicked.connect(lambda: self._aplicar("EIGRP"))

        row.addWidget(self.btn_ospf)
        row.addWidget(self.btn_rip)
        row.addWidget(self.btn_eigrp)
        cl.addLayout(row)

        # Estado
        self.lbl_estado = QLabel("Zonas configuradas en memoria: (vacío)")
        self.lbl_estado.setObjectName("Hint")
        cl.addWidget(self.lbl_estado)

        lay.addWidget(card, alignment=Qt.AlignHCenter)
        lay.addStretch(1)

    # ---------------------------
    # Cargar routers desde backend
    # ---------------------------
    def _cargar_routers(self):
        routers = list(getattr(self.calculadora, "lista_routers", []) or [])
        routers = [str(r) for r in routers]  # asegurar texto "R1", "R2", ...

        if not routers:
            QMessageBox.information(
                self,
                "Sin routers",
                "No hay routers en lista_routers.\nPrimero carga la topología (Conexiones) para llenar esa lista."
            )
            return

        # Si ya había asignaciones, solo mostramos los routers aún no asignados
        asignados = {r for lst in self.protocolos.values() for r in lst}
        self._routers_disponibles = [r for r in routers if r not in asignados]

        self._seleccion.clear()
        self._render_routers()
        self._actualizar_estado_botones()

        self.console.write(f"> Lista sincronizada: {len(routers)} routers totales.")
        self.console.write(f"> Routers disponibles para asignar: {len(self._routers_disponibles)}")

    # ---------------------------
    # Render de chips con QPushButton checkable (R1, R2, ...)
    # ---------------------------
    def _render_routers(self):
        # limpiar panel
        while self.panel_routers_layout.count():
            item = self.panel_routers_layout.takeAt(0)
            w = item.widget()
            if w:
                w.deleteLater()

        if not self._routers_disponibles:
            lbl = QLabel("No hay routers disponibles (ya todos fueron asignados).")
            lbl.setObjectName("Hint")
            self.panel_routers_layout.addWidget(lbl)
            return

        for r in self._routers_disponibles:
            chip = QPushButton(r)
            chip.setCheckable(True)
            chip.setMinimumWidth(56)
            chip.setMinimumHeight(34)

            chip.setStyleSheet("""
                QPushButton {
                    color: #e2e8f0;
                    font-weight: 900;
                    padding: 6px 12px;
                    background: rgba(59,130,246,0.18);
                    border: 1px solid rgba(59,130,246,0.28);
                    border-radius: 12px;
                    text-align: center;
                }
                QPushButton:hover {
                    background: rgba(59,130,246,0.28);
                    border-color: rgba(96,165,250,0.55);
                }
                QPushButton:checked {
                    background: rgba(16,185,129,0.25);
                    border: 1px solid rgba(16,185,129,0.60);
                }
            """)

            chip.toggled.connect(lambda checked, name=r: self._toggle_chip(name, checked))
            self.panel_routers_layout.addWidget(chip)

        self.panel_routers_layout.addStretch(1)

    def _toggle_chip(self, router: str, checked: bool):
        if checked:
            self._seleccion.add(router)
        else:
            self._seleccion.discard(router)

        self._actualizar_estado_botones()

    # ---------------------------
    # Reglas de habilitación
    # ---------------------------
    def _actualizar_estado_botones(self):
        hay_disponibles = bool(self._routers_disponibles)
        hay_seleccion = bool(self._seleccion)

        if not hay_disponibles:
            for b in (self.btn_ospf, self.btn_rip, self.btn_eigrp):
                b.setEnabled(False)
            return

        protocolos_existentes = set(self.protocolos.keys())

        # Máximo 2 protocolos distintos
        if len(protocolos_existentes) >= 2:
            self.btn_ospf.setEnabled(hay_seleccion and ("OSPF" in protocolos_existentes))
            self.btn_rip.setEnabled(hay_seleccion and ("RIP" in protocolos_existentes))
            self.btn_eigrp.setEnabled(hay_seleccion and ("EIGRP" in protocolos_existentes))
        else:
            # todavía se puede elegir cualquiera (si hay selección)
            self.btn_ospf.setEnabled(hay_seleccion)
            self.btn_rip.setEnabled(hay_seleccion)
            self.btn_eigrp.setEnabled(hay_seleccion)

    # ---------------------------
    # Aplicar protocolo y consumir routers
    # ---------------------------
    def _aplicar(self, protocolo: str):
        if not self._seleccion:
            QMessageBox.information(self, "Sin selección", "Selecciona al menos un router.")
            return

        protocolos_existentes = set(self.protocolos.keys())
        if len(protocolos_existentes) >= 2 and protocolo not in protocolos_existentes:
            QMessageBox.warning(
                self,
                "Límite de protocolos",
                f"Ya configuraste 2 protocolos ({', '.join(sorted(protocolos_existentes))}).\n"
                "Solo puedes asignar routers restantes a esos protocolos."
            )
            return

        seleccion_ordenada = sorted(self._seleccion)

        # Guardar acumulado (sin duplicados)
        self.protocolos.setdefault(protocolo, [])
        ya = set(self.protocolos[protocolo])
        nuevos = [r for r in seleccion_ordenada if r not in ya]
        self.protocolos[protocolo].extend(nuevos)

        # Consumir routers (quitarlos del panel)
        asignados_ahora = set(seleccion_ordenada)
        self._routers_disponibles = [r for r in self._routers_disponibles if r not in asignados_ahora]
        self._seleccion.clear()

        self._render_routers()
        self._actualizar_estado_botones()
        self._render_estado()

        self.console.write(f"> Zona {protocolo} configurada: {', '.join(seleccion_ordenada)}")
        self.console.write(f"> protocolos = {self.protocolos}")

    def _render_estado(self):
        if not self.protocolos:
            self.lbl_estado.setText("Zonas configuradas en memoria: (vacío)")
            return

        partes = []
        for proto, routers in self.protocolos.items():
            partes.append(f"{proto}: {', '.join(routers)}")
        self.lbl_estado.setText("Zonas configuradas en memoria: " + " | ".join(partes))