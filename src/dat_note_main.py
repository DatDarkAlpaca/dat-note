from ui.compiled.dat_note_main import Ui_DatNote
from PySide6.QtWidgets import QMainWindow, QFileDialog
import os


class DatNote(QMainWindow, Ui_DatNote):
    def __init__(self, parent=None):
        super(DatNote, self).__init__(parent)
        self.setupUi(self)

        # Document:
        self.current_document_filepath = os.getcwd()

        # Connect Signals:
        self.text_edit.textChanged.connect(self.update_preview)

        self.action_new.triggered.connect(self.action_file_new)

        self.action_open.triggered.connect(self.action_file_open)

    # Text Preview:
    def update_preview(self):
        self.text_preview.setMarkdown(self.text_edit.toPlainText())

    # Actions:
    def action_file_new(self):
        self.text_edit.clear()

    def action_file_open(self):
        # 1. Get file
        results = QFileDialog.getOpenFileName(self, 'Open', self.current_document_filepath, 'Text documents (*.txt)')

        if results:
            # 2. Set current document filepath
            filepath, _ = results
            self.current_document_filepath = filepath

            # 3. Open file
            with open(filepath, mode='r') as file:
                content = file.read()

            # 4. Set file contents
            self.text_edit.setText(content)

