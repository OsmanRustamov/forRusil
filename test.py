from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt, QSettings
import sys


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Создаем виджеты для ввода имени и группы
        self.name_label = QLabel('Имя:')
        self.name_input = QLineEdit()
        self.group_label = QLabel('Группа:')
        self.group_input = QLineEdit()

        # Создаем вертикальный контейнер и добавляем виджеты
        layout = QVBoxLayout()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)
        layout.addWidget(self.group_label)
        layout.addWidget(self.group_input)

        # Устанавливаем вертикальный контейнер как основной макет окна
        self.setLayout(layout)

        # Загружаем сохраненные данные при открытии окна
        self.load_data()

    def load_data(self):
        # Создаем объект QSettings для чтения сохраненных данных
        settings = QSettings('MyCompany', 'MyApp')
        # Загружаем сохраненные значения для полей
        self.name_input.setText(settings.value('name', ''))
        self.group_input.setText(settings.value('group', ''))

    def save_data(self):
        # Создаем объект QSettings для записи данных
        settings = QSettings('MyCompany', 'MyApp')
        # Сохраняем значения полей
        settings.setValue('name', self.name_input.text())
        settings.setValue('group', self.group_input.text())

    def validate_inputs(self):
        # Создаем объект палитры для изменения цвета фона
        palette = QPalette()

        # Проверяем, что поля не пустые
        if not self.name_input.text():
            # Меняем цвет фона на красный
            palette.setColor(QPalette.Base, Qt.red)
            # Устанавливаем новую палитру для поля ввода
            self.name_input.setPalette(palette)

        if not self.group_input.text():
            palette.setColor(QPalette.Base, Qt.red)
            self.group_input.setPalette(palette)

    def reset_palette(self):
        # Создаем объект палитры для изменения цвета фона
        palette = QPalette()
        # Устанавливаем стандартный цвет фона
        palette.setColor(QPalette.Base, Qt.white)
        # Устанавливаем стандартную палитру для полей ввода
        self.name_input.setPalette(palette)
        self.group_input.setPalette(palette)

    def closeEvent(self, event):
        # Проверяем, что поля не пустые
        self.validate_inputs()

        # Если есть пустые поля, отменяем закрытие окна
        if self.name_input.palette().color(QPalette.Base) == Qt.red or \
           self.group_input.palette().color(QPalette.Base) == Qt.red:
            event.ignore()
            return

        # Если поля заполнены, сохраняем данные и закрываем окно
        self.save_data()
        event.accept()

    def focusInEvent(self, event):
        # При получении фокус
        # сбрасываем цвет фона полей
        self.reset_palette()

    def focusOutEvent(self, event):
        # При потере фокуса проверяем, что поля не пустые
        self.validate_inputs()

    def keyPressEvent(self, event):
        # Если пользователь нажимает Enter, сохраняем данные
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            self.validate_inputs()
            if self.name_input.palette().color(QPalette.Base) != Qt.red and \
                    self.group_input.palette().color(QPalette.Base) != Qt.red:
                self.save_data()

                # Закрываем окно
                self.close()
        else:
            # Если пользователь нажимает другую клавишу, обрабатываем событие стандартным образом
            super().keyPressEvent(event)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())