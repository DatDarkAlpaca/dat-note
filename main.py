from PySide6.QtWidgets import QApplication
from src.dat_note_main import DatNote


def main():
    app = QApplication()

    window = DatNote()
    window.show()

    app.exec()


if __name__ == '__main__':
    main()
