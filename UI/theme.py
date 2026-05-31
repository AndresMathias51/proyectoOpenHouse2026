QSS = """
QMainWindow { background: #070b14; }
QWidget { color: #dbeafe; font-size: 13px; }

#Background {
  background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
    stop:0 #070b14, stop:1 #0b1630);
}

QFrame#TopBar {
  background: rgba(5, 8, 16, 0.75);
  border-bottom: 1px solid rgba(148, 163, 184, 0.14);
}

QLabel#Brand {
  font-size: 18px;
  font-weight: 900;
  color: #93c5fd;
}

/* botones de navegación */
QPushButton#NavBtn {
  background: transparent;
  border: 1px solid transparent;
  padding: 9px 14px;
  border-radius: 10px;
  color: rgba(226,232,240,0.9);
}
QPushButton#NavBtn:hover {
  background: rgba(59,130,246,0.18);
  border-color: rgba(59,130,246,0.35);
}
QPushButton#NavBtn:checked {
  background: rgba(59,130,246,0.85);
  border-color: rgba(96,165,250,0.9);
  color: #eff6ff;
  font-weight: 800;
}

/* card central */
QFrame#Card {
  background: rgba(17, 24, 39, 0.62);
  border: 1px solid rgba(148,163,184,0.16);
  border-radius: 18px;
}
QLabel#CardTitle { font-size: 22px; font-weight: 900; color: #e5e7eb; }
QLabel#CardSub { color: rgba(148,163,184,0.9); }

/* botones */
QPushButton#Blue {
  background: rgba(59,130,246,0.92);
  border: 1px solid rgba(37,99,235,0.95);
  color: #eff6ff;
  padding: 11px 14px;
  border-radius: 12px;
  font-weight: 800;
}
QPushButton#Blue:hover { background: rgba(96,165,250,0.95); }

QPushButton#Green {
  background: rgba(16,185,129,0.92);
  border: 1px solid rgba(5,150,105,0.95);
  color: #052e16;
  padding: 11px 14px;
  border-radius: 12px;
  font-weight: 900;
}
QPushButton#Green:hover { background: rgba(52,211,153,0.95); }

QPushButton:disabled {
  background: rgba(51,65,85,0.35);
  border-color: rgba(71,85,105,0.35);
  color: rgba(226,232,240,0.35);
}

/* consola */
QTextEdit#Console {
  background: #000;
  border: 1px solid rgba(148,163,184,0.18);
  border-radius: 14px;
  padding: 10px;
  font-family: Consolas, Menlo, monospace;
  font-size: 12px;
  color: #22c55e;
}
QLabel#Hint { color: rgba(148,163,184,0.9); font-style: italic; }

# UI/theme.py (agrega dentro del string QSS)
QLineEdit#PathInput {
  background: rgba(2, 6, 23, 0.65);
  border: 1px solid rgba(148,163,184,0.18);
  border-radius: 12px;
  padding: 10px 12px;
  color: #e2e8f0;
}
"""