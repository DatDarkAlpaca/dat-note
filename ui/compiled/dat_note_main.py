# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dat_note_main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLayout, QMainWindow,
    QMenu, QMenuBar, QSizePolicy, QStatusBar,
    QTextEdit, QWidget)

class Ui_DatNote(object):
    def setupUi(self, DatNote):
        if not DatNote.objectName():
            DatNote.setObjectName(u"DatNote")
        DatNote.resize(609, 409)
        DatNote.setStyleSheet(u"QMenuBar\n"
"{\n"
"	color: white;\n"
"	padding-left: 5px;\n"
"	background: transparent;\n"
"}\n"
"\n"
"QTextEdit\n"
"{\n"
"	color: white;\n"
"	background-color: rgb(39, 39, 39);\n"
"	border: 0;\n"
"}")
        self.action_new = QAction(DatNote)
        self.action_new.setObjectName(u"action_new")
        self.action_new_window = QAction(DatNote)
        self.action_new_window.setObjectName(u"action_new_window")
        self.action_open = QAction(DatNote)
        self.action_open.setObjectName(u"action_open")
        self.action_save = QAction(DatNote)
        self.action_save.setObjectName(u"action_save")
        self.action_save_as = QAction(DatNote)
        self.action_save_as.setObjectName(u"action_save_as")
        self.action_exit = QAction(DatNote)
        self.action_exit.setObjectName(u"action_exit")
        self.action_undo = QAction(DatNote)
        self.action_undo.setObjectName(u"action_undo")
        self.action_cut = QAction(DatNote)
        self.action_cut.setObjectName(u"action_cut")
        self.action_copy = QAction(DatNote)
        self.action_copy.setObjectName(u"action_copy")
        self.action_pasta = QAction(DatNote)
        self.action_pasta.setObjectName(u"action_pasta")
        self.action_delete = QAction(DatNote)
        self.action_delete.setObjectName(u"action_delete")
        self.action_find = QAction(DatNote)
        self.action_find.setObjectName(u"action_find")
        self.action_go_to = QAction(DatNote)
        self.action_go_to.setObjectName(u"action_go_to")
        self.action_select_all = QAction(DatNote)
        self.action_select_all.setObjectName(u"action_select_all")
        self.action_font = QAction(DatNote)
        self.action_font.setObjectName(u"action_font")
        self.action_status_bar = QAction(DatNote)
        self.action_status_bar.setObjectName(u"action_status_bar")
        self.action_status_bar.setCheckable(True)
        self.action_word_wrap = QAction(DatNote)
        self.action_word_wrap.setObjectName(u"action_word_wrap")
        self.action_word_wrap.setCheckable(True)
        self.action_zoom_in = QAction(DatNote)
        self.action_zoom_in.setObjectName(u"action_zoom_in")
        self.action_zoom_out = QAction(DatNote)
        self.action_zoom_out.setObjectName(u"action_zoom_out")
        self.action_zoom_restore = QAction(DatNote)
        self.action_zoom_restore.setObjectName(u"action_zoom_restore")
        self.central_widget = QWidget(DatNote)
        self.central_widget.setObjectName(u"central_widget")
        self.central_widget.setMinimumSize(QSize(240, 70))
        self.central_widget.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.central_widget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.text_edit = QTextEdit(self.central_widget)
        self.text_edit.setObjectName(u"text_edit")
        self.text_edit.setOverwriteMode(False)
        self.text_edit.setAcceptRichText(False)

        self.horizontalLayout.addWidget(self.text_edit)

        self.text_preview = QTextEdit(self.central_widget)
        self.text_preview.setObjectName(u"text_preview")
        self.text_preview.setStyleSheet(u"")
        self.text_preview.setReadOnly(True)

        self.horizontalLayout.addWidget(self.text_preview)

        DatNote.setCentralWidget(self.central_widget)
        self.menu_bar = QMenuBar(DatNote)
        self.menu_bar.setObjectName(u"menu_bar")
        self.menu_bar.setGeometry(QRect(0, 0, 609, 26))
        self.menu_bar.setStyleSheet(u"")
        self.menuFile = QMenu(self.menu_bar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menu_bar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuView = QMenu(self.menu_bar)
        self.menuView.setObjectName(u"menuView")
        self.menu_zoom = QMenu(self.menuView)
        self.menu_zoom.setObjectName(u"menu_zoom")
        DatNote.setMenuBar(self.menu_bar)
        self.status_bar = QStatusBar(DatNote)
        self.status_bar.setObjectName(u"status_bar")
        DatNote.setStatusBar(self.status_bar)

        self.menu_bar.addAction(self.menuFile.menuAction())
        self.menu_bar.addAction(self.menuEdit.menuAction())
        self.menu_bar.addAction(self.menuView.menuAction())
        self.menuFile.addAction(self.action_new)
        self.menuFile.addAction(self.action_open)
        self.menuFile.addAction(self.action_save)
        self.menuFile.addAction(self.action_save_as)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.action_exit)
        self.menuEdit.addAction(self.action_undo)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.action_cut)
        self.menuEdit.addAction(self.action_copy)
        self.menuEdit.addAction(self.action_pasta)
        self.menuEdit.addAction(self.action_delete)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.action_find)
        self.menuEdit.addAction(self.action_go_to)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.action_select_all)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.action_font)
        self.menuView.addAction(self.menu_zoom.menuAction())
        self.menu_zoom.addAction(self.action_zoom_in)
        self.menu_zoom.addAction(self.action_zoom_out)
        self.menu_zoom.addAction(self.action_zoom_restore)

        self.retranslateUi(DatNote)
        self.action_exit.triggered.connect(DatNote.close)

        QMetaObject.connectSlotsByName(DatNote)
    # setupUi

    def retranslateUi(self, DatNote):
        DatNote.setWindowTitle(QCoreApplication.translate("DatNote", u"Untitled - Dat Note", None))
        self.action_new.setText(QCoreApplication.translate("DatNote", u"New", None))
#if QT_CONFIG(shortcut)
        self.action_new.setShortcut(QCoreApplication.translate("DatNote", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.action_new_window.setText(QCoreApplication.translate("DatNote", u"New window", None))
#if QT_CONFIG(shortcut)
        self.action_new_window.setShortcut(QCoreApplication.translate("DatNote", u"Ctrl+Shift+N", None))
#endif // QT_CONFIG(shortcut)
        self.action_open.setText(QCoreApplication.translate("DatNote", u"Open", None))
#if QT_CONFIG(shortcut)
        self.action_open.setShortcut(QCoreApplication.translate("DatNote", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.action_save.setText(QCoreApplication.translate("DatNote", u"Save", None))
#if QT_CONFIG(shortcut)
        self.action_save.setShortcut(QCoreApplication.translate("DatNote", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.action_save_as.setText(QCoreApplication.translate("DatNote", u"Save as", None))
#if QT_CONFIG(shortcut)
        self.action_save_as.setShortcut(QCoreApplication.translate("DatNote", u"Ctrl+Shift+S", None))
#endif // QT_CONFIG(shortcut)
        self.action_exit.setText(QCoreApplication.translate("DatNote", u"Exit", None))
#if QT_CONFIG(shortcut)
        self.action_exit.setShortcut(QCoreApplication.translate("DatNote", u"Ctrl+E", None))
#endif // QT_CONFIG(shortcut)
        self.action_undo.setText(QCoreApplication.translate("DatNote", u"Undo", None))
#if QT_CONFIG(shortcut)
        self.action_undo.setShortcut(QCoreApplication.translate("DatNote", u"Ctrl+Z", None))
#endif // QT_CONFIG(shortcut)
        self.action_cut.setText(QCoreApplication.translate("DatNote", u"Cut", None))
#if QT_CONFIG(shortcut)
        self.action_cut.setShortcut(QCoreApplication.translate("DatNote", u"Ctrl+X", None))
#endif // QT_CONFIG(shortcut)
        self.action_copy.setText(QCoreApplication.translate("DatNote", u"Copy", None))
#if QT_CONFIG(shortcut)
        self.action_copy.setShortcut(QCoreApplication.translate("DatNote", u"Ctrl+C", None))
#endif // QT_CONFIG(shortcut)
        self.action_pasta.setText(QCoreApplication.translate("DatNote", u"Paste", None))
#if QT_CONFIG(shortcut)
        self.action_pasta.setShortcut(QCoreApplication.translate("DatNote", u"Ctrl+V", None))
#endif // QT_CONFIG(shortcut)
        self.action_delete.setText(QCoreApplication.translate("DatNote", u"Delete", None))
#if QT_CONFIG(shortcut)
        self.action_delete.setShortcut(QCoreApplication.translate("DatNote", u"Del", None))
#endif // QT_CONFIG(shortcut)
        self.action_find.setText(QCoreApplication.translate("DatNote", u"Find", None))
#if QT_CONFIG(shortcut)
        self.action_find.setShortcut(QCoreApplication.translate("DatNote", u"Ctrl+F", None))
#endif // QT_CONFIG(shortcut)
        self.action_go_to.setText(QCoreApplication.translate("DatNote", u"Go to", None))
        self.action_select_all.setText(QCoreApplication.translate("DatNote", u"Select all", None))
#if QT_CONFIG(shortcut)
        self.action_select_all.setShortcut(QCoreApplication.translate("DatNote", u"Ctrl+A", None))
#endif // QT_CONFIG(shortcut)
        self.action_font.setText(QCoreApplication.translate("DatNote", u"Font", None))
        self.action_status_bar.setText(QCoreApplication.translate("DatNote", u"Status bar", None))
        self.action_word_wrap.setText(QCoreApplication.translate("DatNote", u"Word wrap", None))
        self.action_zoom_in.setText(QCoreApplication.translate("DatNote", u"Zoom In", None))
#if QT_CONFIG(shortcut)
        self.action_zoom_in.setShortcut(QCoreApplication.translate("DatNote", u"Ctrl++", None))
#endif // QT_CONFIG(shortcut)
        self.action_zoom_out.setText(QCoreApplication.translate("DatNote", u"Zoom Out", None))
#if QT_CONFIG(shortcut)
        self.action_zoom_out.setShortcut(QCoreApplication.translate("DatNote", u"Ctrl+-", None))
#endif // QT_CONFIG(shortcut)
        self.action_zoom_restore.setText(QCoreApplication.translate("DatNote", u"Restore default zoom", None))
#if QT_CONFIG(shortcut)
        self.action_zoom_restore.setShortcut(QCoreApplication.translate("DatNote", u"Ctrl+0", None))
#endif // QT_CONFIG(shortcut)
        self.text_edit.setHtml(QCoreApplication.translate("DatNote", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.menuFile.setTitle(QCoreApplication.translate("DatNote", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("DatNote", u"Edit", None))
        self.menuView.setTitle(QCoreApplication.translate("DatNote", u"View", None))
        self.menu_zoom.setTitle(QCoreApplication.translate("DatNote", u"Zoom", None))
    # retranslateUi

