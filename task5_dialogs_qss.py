"""Завдання 5: QMessageBox, QInputDialog, власний QDialog і QSS."""
import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QDialog, QLabel, QLineEdit,
    QSpinBox, QPushButton, QVBoxLayout, QHBoxLayout, QFormLayout,
    QDialogButtonBox, QMessageBox, QInputDialog)

STYLE = """
QWidget { background: #f4f7fb; color: #1c2940; font-size: 13px; }
QLabel { font-weight: 500; }
QPushButton { background: #2458ad; color: white; border: 0; border-radius: 6px; padding: 9px; }
QPushButton:hover { background: #3979df; }
QPushButton:pressed { background: #163e82; }
QLineEdit, QSpinBox { background: white; border: 1px solid #b4c2d7; border-radius: 5px; padding: 6px; }
QLineEdit:focus, QSpinBox:focus { border: 2px solid #3979df; }
QLabel#resultLabel { background: #e3edff; border: 1px solid #9bb9ed; padding: 12px; border-radius: 6px; }
"""

class StudentDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Новий студент')
        form = QFormLayout(self)
        self.name = QLineEdit()
        self.name.setPlaceholderText('Ім’я студента')
        self.age = QSpinBox()
        self.age.setRange(16, 80)
        self.age.setValue(18)
        form.addRow('Ім’я:', self.name)
        form.addRow('Вік:', self.age)
        buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        buttons.accepted.connect(self.validate_and_accept)
        buttons.rejected.connect(self.reject)
        form.addRow(buttons)

    def validate_and_accept(self):
        if not self.name.text().strip():
            QMessageBox.warning(self, 'Помилка', 'Введіть ім’я студента.')
            return
        self.accept()

    def get_data(self):
        return self.name.text().strip(), self.age.value()

class DialogsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('ЛБ №4 — Завдання 5: діалоги та QSS')
        self.setMinimumSize(480, 290)
        root = QVBoxLayout(self)
        root.addWidget(QLabel('Керування студентськими даними'))
        self.result = QLabel('Немає введених даних')
        self.result.setObjectName('resultLabel')
        self.result.setWordWrap(True)
        root.addWidget(self.result)
        buttons = QHBoxLayout()
        self.standard = QPushButton('Підтвердження')
        self.input = QPushButton('Ввести групу')
        self.custom = QPushButton('Новий студент')
        buttons.addWidget(self.standard)
        buttons.addWidget(self.input)
        buttons.addWidget(self.custom)
        root.addLayout(buttons)
        self.standard.clicked.connect(self.ask_confirmation)
        self.input.clicked.connect(self.ask_group)
        self.custom.clicked.connect(self.ask_student)
        self.group = 'Не вказана'
        self.student = 'Не вказаний'
        self.refresh()

    def refresh(self):
        self.result.setText(f'Група: {self.group}\nСтудент: {self.student}')

    def ask_confirmation(self):
        answer = QMessageBox.question(self, 'Підтвердження', 'Очистити введені дані?',
                                      QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if answer == QMessageBox.StandardButton.Yes:
            self.group, self.student = 'Не вказана', 'Не вказаний'
            self.refresh()

    def ask_group(self):
        value, ok = QInputDialog.getText(self, 'Введення групи', 'Назва групи:', text='' if self.group == 'Не вказана' else self.group)
        if ok and value.strip():
            self.group = value.strip()
            self.refresh()

    def ask_student(self):
        dialog = StudentDialog(self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            name, age = dialog.get_data()
            self.student = f'{name}, {age} років'
            self.refresh()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(STYLE)
    window = DialogsWindow()
    window.show()
    sys.exit(app.exec())
