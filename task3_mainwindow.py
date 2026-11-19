"""Завдання 3: QMainWindow, QAction, QToolBar, statusBar, діалоги."""
import sys
from pathlib import Path
from PyQt6.QtGui import QAction, QKeySequence
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QFileDialog, QMessageBox, QToolBar

class EditorWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('ЛБ №4 — Завдання 3: текстовий редактор')
        self.resize(720, 480)
        self.editor = QTextEdit()
        self.editor.setPlaceholderText('Введіть текст або відкрийте файл...')
        self.setCentralWidget(self.editor)
        self.editor.textChanged.connect(self.update_status)
        self.statusBar().showMessage('Готово. Символів: 0')
        file_menu = self.menuBar().addMenu('Файл')
        help_menu = self.menuBar().addMenu('Довідка')
        toolbar = QToolBar('Основні дії', self)
        toolbar.setMovable(False)
        self.addToolBar(toolbar)
        actions = [
            ('Новий', 'Ctrl+N', self.new_file),
            ('Відкрити', 'Ctrl+O', self.open_file),
            ('Зберегти як', 'Ctrl+Shift+S', self.save_file),
            ('Вихід', 'Ctrl+Q', self.close),
        ]
        for label, shortcut, handler in actions:
            action = QAction(label, self)
            action.setShortcut(QKeySequence(shortcut))
            action.triggered.connect(handler)
            file_menu.addAction(action)
            if label in ('Новий', 'Відкрити', 'Зберегти як'):
                toolbar.addAction(action)
        about = QAction('Про програму', self)
        about.triggered.connect(self.show_about)
        help_menu.addAction(about)
        instructions = QAction('Підказка', self)
        instructions.triggered.connect(lambda: QMessageBox.information(self, 'Підказка', 'Скорочення: Ctrl+N, Ctrl+O, Ctrl+Shift+S.'))
        help_menu.addAction(instructions)

    def update_status(self):
        self.statusBar().showMessage(f'Символів: {len(self.editor.toPlainText())}')

    def new_file(self):
        self.editor.clear()
        self.statusBar().showMessage('Створено новий документ')

    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, 'Відкрити текст', '', 'Текстові файли (*.txt);;Усі файли (*)')
        if filename:
            try:
                self.editor.setPlainText(Path(filename).read_text(encoding='utf-8'))
                self.statusBar().showMessage(f'Відкрито: {filename}')
            except (OSError, UnicodeError) as exc:
                QMessageBox.warning(self, 'Помилка відкриття', str(exc))

    def save_file(self):
        filename, _ = QFileDialog.getSaveFileName(self, 'Зберегти текст', 'notes.txt', 'Текстові файли (*.txt);;Усі файли (*)')
        if filename:
            try:
                Path(filename).write_text(self.editor.toPlainText(), encoding='utf-8')
                self.statusBar().showMessage(f'Збережено: {filename}')
            except OSError as exc:
                QMessageBox.warning(self, 'Помилка збереження', str(exc))

    def show_about(self):
        QMessageBox.about(self, 'Про програму', 'Демонстрація QMainWindow, меню, панелі інструментів та рядка стану. ЛБ №4.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = EditorWindow()
    window.show()
    sys.exit(app.exec())
