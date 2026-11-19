"""Завдання 4: два компоненти, два кастомні сигнали та blockSignals."""
import sys
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLineEdit, QSpinBox, QPushButton, QLabel, QGroupBox, QCheckBox)

class InputPanel(QWidget):
    text_sent = pyqtSignal(str)
    record_sent = pyqtSignal(int, str)

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        self.name = QLineEdit()
        self.name.setPlaceholderText('Назва запису')
        self.score = QSpinBox()
        self.score.setRange(0, 100)
        self.score.setValue(50)
        self.send_text = QPushButton('Надіслати назву')
        self.send_record = QPushButton('Надіслати запис')
        layout.addWidget(QLabel('Назва:'))
        layout.addWidget(self.name)
        layout.addWidget(QLabel('Оцінка:'))
        layout.addWidget(self.score)
        layout.addWidget(self.send_text)
        layout.addWidget(self.send_record)
        self.send_text.clicked.connect(lambda: self.text_sent.emit(self.name.text().strip()))
        self.send_record.clicked.connect(lambda: self.record_sent.emit(self.score.value(), self.name.text().strip()))

class OutputPanel(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        self.text = QLabel('Назва ще не надходила')
        self.record = QLabel('Запис ще не надходив')
        self.record.setWordWrap(True)
        layout.addWidget(self.text)
        layout.addWidget(self.record)

    def display_text(self, value):
        self.text.setText(f'Отримано текст: {value or "(порожньо)"}')

    def display_record(self, score, value):
        self.record.setText(f'Отримано запис: {value or "(без назви)"}; оцінка {score}')

class SignalsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('ЛБ №4 — Завдання 4: кастомні сигнали')
        self.setMinimumSize(650, 320)
        root = QVBoxLayout(self)
        panels = QHBoxLayout()
        self.source = InputPanel()
        self.target = OutputPanel()
        left = QGroupBox('Компонент введення')
        left_layout = QVBoxLayout(left)
        left_layout.addWidget(self.source)
        right = QGroupBox('Компонент відображення')
        right_layout = QVBoxLayout(right)
        right_layout.addWidget(self.target)
        panels.addWidget(left)
        panels.addWidget(right)
        root.addLayout(panels)
        self.pause = QCheckBox('Призупинити сигнали введення (blockSignals)')
        self.pause.toggled.connect(self.source.blockSignals)
        root.addWidget(self.pause)
        self.state = QLabel('Сигнали активні')
        root.addWidget(self.state)
        self.pause.toggled.connect(lambda blocked: self.state.setText('Сигнали заблоковано — значення не оновлюються' if blocked else 'Сигнали активні'))
        # Зв'язки між компонентами створюються ТІЛЬКИ в батьківському вікні.
        self.source.text_sent.connect(self.target.display_text)
        self.source.record_sent.connect(self.target.display_record)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SignalsWindow()
    window.show()
    sys.exit(app.exec())
