import sys

from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
)

def main():
    app = QApplication(sys.argv)
    wiget = QWidget()

    text_labetl = QLabel(wiget)
    text_labetl.setText("Hello World!")
    text_labetl.move(115, 90)

    wiget.setWindowTitle("PyQt6 Hello World Example")
    wiget.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()