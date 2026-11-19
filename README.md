# Лабораторна робота №4 — PyQt6

**Тема:** Створення графічного користувацького інтерфейсу з використанням PyQt в Python  
**Виконав:** Якименко Іван Едуардович  
**Група:** БІКСб-2-25-4.0д

## Вимоги
Python 3.10+ та PyQt6. Програми працюють як окремі desktop-додатки.

## Встановлення та запуск

```bash
python -m venv .venv
# Windows PowerShell:
.venv\Scripts\Activate.ps1
# Windows cmd:
# .venv\Scripts\activate.bat
python -m pip install -r requirements.txt
python task1_widgets.py
```

Для наступних завдань замініть ім'я файлу на `task2_signals.py`, `task3_mainwindow.py`, `task4_custom_signals.py`, `task5_dialogs_qss.py`.

## Вміст
- `task1_widgets.py` — 9 типів віджетів; QVBoxLayout, QHBoxLayout, QFormLayout; адаптивне вікно.
- `task2_signals.py` — 6 з'єднань сигнал–слот; валідація та скидання.
- `task3_mainwindow.py` — меню, toolbar, statusBar, shortcuts, QFileDialog та QMessageBox.
- `task4_custom_signals.py` — 2 власні компоненти; `pyqtSignal(str)` і `pyqtSignal(int, str)`; `blockSignals`.
- `task5_dialogs_qss.py` — QMessageBox, QInputDialog, власний QDialog, глобальний QSS та псевдостани.

## Перевірка
Запустіть кожний файл і перевірте елементи керування. Для завдання 4 увімкніть прапорець блокування сигналів, змініть дані та переконайтеся, що правий компонент не оновлюється. Для завдання 5 відкрийте всі три діалоги.

## Звіт
PDF-звіт надається викладачеві окремо. Скріншоти інтерфейсу слід зробити під час запуску на комп'ютері з PyQt6.
