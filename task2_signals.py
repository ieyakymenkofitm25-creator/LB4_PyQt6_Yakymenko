"""Завдання 2: інтерактивна форма, сигнали, слоти та валідація."""
import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QSpinBox,
    QComboBox, QCheckBox, QPushButton, QVBoxLayout, QFormLayout, QHBoxLayout)

def validate_form(name, age, role, confirmed):
    if len(name.strip()) < 2:
        return False, 'Ім’я має містити щонайменше 2 символи.'
    if not 16 <= age <= 80:
        return False, 'Вік повинен бути від 16 до 80 років.'
    if role == 'Оберіть роль':
        return False, 'Оберіть роль.'
    if not confirmed:
        return False, 'Потрібно підтвердити дані.'
    return True, f'Дані прийнято: {name.strip()}, {age} років, роль: {role}.'

class FormWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('ЛБ №4 — Завдання 2: сигнали та слоти')
        self.setMinimumSize(480, 300)
        root = QVBoxLayout(self)
        form = QFormLayout()
        self.name = QLineEdit()
        self.name.setPlaceholderText('Мінімум два символи')
        self.age = QSpinBox()
        self.age.setRange(0, 120)
        self.age.setValue(18)
        self.role = QComboBox()
        self.role.addItems(['Оберіть роль', 'Студент', 'Викладач'])
        self.confirm = QCheckBox('Підтверджую правильність даних')
        form.addRow('Ім’я:', self.name)
        form.addRow('Вік:', self.age)
        form.addRow('Роль:', self.role)
        root.addLayout(form)
        root.addWidget(self.confirm)
        self.preview = QLabel('Ім’я: — | Вік: 18 | Роль: —')
        self.preview.setWordWrap(True)
        self.result = QLabel('Очікування введення')
        self.result.setWordWrap(True)
        root.addWidget(self.preview)
        root.addWidget(self.result)
        buttons = QHBoxLayout()
        self.submit = QPushButton('Підтвердити')
        self.reset = QPushButton('Скинути')
        buttons.addWidget(self.submit)
        buttons.addWidget(self.reset)
        root.addLayout(buttons)
        # 1: textChanged -> метод; 2: valueChanged -> метод;
        # 3: currentTextChanged -> lambda; 4: toggled -> setEnabled;
        # 5: clicked -> метод; 6: clicked -> метод.
        self.name.textChanged.connect(self.update_preview)
        self.age.valueChanged.connect(self.update_preview)
        self.role.currentTextChanged.connect(lambda _value: self.update_preview())
        self.confirm.toggled.connect(self.submit.setEnabled)
        self.submit.clicked.connect(self.submit_form)
        self.reset.clicked.connect(self.reset_form)
        self.submit.setEnabled(False)

    def update_preview(self, *_args):
        self.preview.setText(f'Ім’я: {self.name.text() or "—"} | Вік: {self.age.value()} | Роль: {self.role.currentText()}')

    def submit_form(self):
        valid, message = validate_form(self.name.text(), self.age.value(),
                                       self.role.currentText(), self.confirm.isChecked())
        self.result.setText(('✓ ' if valid else '⚠ ') + message)

    def reset_form(self):
        self.name.clear()
        self.age.setValue(18)
        self.role.setCurrentIndex(0)
        self.confirm.setChecked(False)
        self.result.setText('Очікування введення')
        self.update_preview()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FormWindow()
    window.show()
    sys.exit(app.exec())
