from ui.compiled.dat_note_main import Ui_DatNote
from PySide6.QtWidgets import QMainWindow


class DatNote(QMainWindow, Ui_DatNote):
    def __init__(self, parent=None):
        super(DatNote, self).__init__(parent)
        self.setupUi(self)

        self.text_edit.textChanged.connect(self.initialize_preview)

    def initialize_preview(self):
        self.text_preview.setMarkdown(self.text_edit.toPlainText())
