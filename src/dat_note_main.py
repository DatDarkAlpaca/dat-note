from ui.compiled.dat_note_main import Ui_DatNote
from PySide6.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from PySide6.QtCore import QFileInfo


class DatNote(QMainWindow, Ui_DatNote):
    def __init__(self, parent=None):
        super(DatNote, self).__init__(parent)
        self.setupUi(self)

        # Document:
        self.current_document_filepath = None
        self.document_name = 'Untitled'

        # Connect Signals:
        self.text_edit.textChanged.connect(self.update_preview)

        self.text_edit.document().modificationChanged.connect(self.update_title)

        # Action Signals:
        self.action_new.triggered.connect(self.action_file_new)

        self.action_open.triggered.connect(self.action_file_open)

        self.action_save.triggered.connect(self.action_file_save)

        self.action_save_as.triggered.connect(self.action_file_save_as)

    def closeEvent(self, event) -> None:
        if not self.text_edit.document().isModified():
            return

        answer = QMessageBox.question(self, None, "You have unsaved changes. Save before closing?",
                                      QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)

        if answer & QMessageBox.Save:
            self.action_file_save()
            if self.text_edit.document().isModified():
                event.ignore()

        elif answer & QMessageBox.Cancel:
            event.ignore()

    # Text Preview:
    def update_preview(self):
        self.text_preview.setMarkdown(self.text_edit.toPlainText())

    def update_title(self):
        modified = '*' if self.text_edit.document().isModified() else ''
        self.setWindowTitle(f"{self.document_name}{modified} - Dat Note")

    # Actions:
    def action_file_new(self):
        self.text_edit.clear()

    def action_file_open(self):
        path = QFileDialog.getOpenFileName(self, 'Open', self.current_document_filepath, 'Text documents (*.txt)')[0]

        if path:
            self.text_edit.setText(open(path).read())
            self.current_document_filepath = path

            info = QFileInfo(path)
            self.document_name = info.fileName()
            self.update_title()

    def action_file_save(self):
        if not self.current_document_filepath:
            self.action_file_save_as()
            return

        with open(self.current_document_filepath, "w") as file:
            file.write(self.text_edit.toPlainText())

        self.text_edit.document().setModified(False)

    def action_file_save_as(self):
        path = QFileDialog.getSaveFileName(self, 'Save As', self.current_document_filepath, 'Text documents (*.txt)')[0]
        if path:
            self.current_document_filepath = path
            self.action_file_save()

            info = QFileInfo(path)
            self.document_name = info.fileName()
            self.update_title()
