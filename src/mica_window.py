from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Qt
from win32mica import ApplyMica
import darkdetect


class MicaWindow(QMainWindow):
    def __init__(self):
        super(MicaWindow, self).__init__()

        mode = darkdetect.isDark()
        self.setAttribute(Qt.WA_TranslucentBackground)
        ApplyMica(self.winId().__int__(), mode)
