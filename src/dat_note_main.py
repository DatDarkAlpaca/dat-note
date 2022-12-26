from ui.compiled.dat_note_main import Ui_DatNote
from PySide6.QtWidgets import QFileDialog, QMessageBox
from PySide6.QtCore import QFileInfo
from win32mica import ApplyMica, MICAMODE
from src.mica_window import MicaWindow


class DatNote(MicaWindow, Ui_DatNote):
    def __init__(self):
        super(DatNote, self).__init__()
        self.setupUi(self)

        ApplyMica(self.menu_bar.winId().__int__(), MICAMODE.DARK)

        # Document:
        self.current_document_filepath = None
        self.document_name = 'Untitled'

        # Zoom:
        self.current_zoom = 0

        # Connect Signals:
        self.text_edit.textChanged.connect(self.update_preview)

        self.text_edit.document().modificationChanged.connect(self.update_title)

        # Action Signals:
        self.action_new.triggered.connect(self.action_file_new)

        self.action_open.triggered.connect(self.action_file_open)

        self.action_save.triggered.connect(self.action_file_save)

        self.action_save_as.triggered.connect(self.action_file_save_as)

        # Zoom Signals:
        self.action_zoom_in.triggered.connect(self.action_view_zoom_in)

        self.action_zoom_out.triggered.connect(self.action_view_zoom_out)

        self.action_zoom_restore.triggered.connect(self.action_view_zoom_restore)

    def closeEvent(self, event) -> None:
        if not self.text_edit.document().isModified():
            return

        answer = QMessageBox(self)
        answer.setText("You have unsaved changes. Save before closing?")
        answer.setWindowTitle('Dat Note')
        answer.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
        answer.exec()

        if answer.result() & QMessageBox.Save:
            self.action_file_save()
            if self.text_edit.document().isModified():
                event.ignore()

        elif answer.result() & QMessageBox.Cancel:
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

    # Zooming:
    def action_view_zoom_in(self):
        self.text_edit.zoomIn(2)
        self.current_zoom += 1

    def action_view_zoom_out(self):
        self.text_edit.zoomOut(2)
        self.current_zoom -= 1

    def action_view_zoom_restore(self):
        if self.current_zoom == 0:
            return

        if self.current_zoom > 0:
            for _ in range(self.current_zoom):
                self.text_edit.zoomOut(2)
        else:
            for _ in range(abs(self.current_zoom)):
                self.text_edit.zoomIn(2)

        self.current_zoom = 0
