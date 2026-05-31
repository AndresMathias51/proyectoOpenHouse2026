from PySide6.QtWidgets import QFrame, QVBoxLayout, QLabel, QSizePolicy

def make_card(title: str, subtitle: str, max_width: int = 860):
    card = QFrame()
    card.setObjectName("Card")
    card.setMaximumWidth(max_width)
    card.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)

    lay = QVBoxLayout(card)
    lay.setContentsMargins(26, 22, 26, 22)
    lay.setSpacing(12)

    t = QLabel(title)
    t.setObjectName("CardTitle")

    s = QLabel(subtitle)
    s.setObjectName("CardSub")
    s.setWordWrap(True)

    lay.addWidget(t)
    lay.addWidget(s)
    return card, lay