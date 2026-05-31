from PySide6.QtWidgets import QTextEdit

class Console(QTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("Console")
        self.setReadOnly(True)
        self.setFixedHeight(190)

    def write(self, msg: str):
        self.append(msg)