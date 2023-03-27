from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QRadioButton,
    QComboBox,
    QCheckBox,
    QGridLayout,
)
from PyQt5.QtCore import Qt, QSettings, QDate


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Инициализируем окно
        self.setWindowTitle('Моя программа')

        # Создаем элементы управления
        self.name_label = QLabel('Имя:')
        self.name_input = QLineEdit()
        self.group_label = QLabel('Группа:')
        self.group_input = QLineEdit()
        self.gender_label = QLabel('Пол:')
        self.male_radio = QRadioButton('Мужской')
        self.female_radio = QRadioButton('Женский')
        self.birthday_label = QLabel('Дата рождения:')
        self.day_combo = QComboBox()
        self.day_combo.addItems([str(day) for day in range(1, 32)])
        self.month_combo = QComboBox()
        self.month_combo.addItems([
            'Январь', 'Февраль', 'Март',
            'Апрель', 'Май', 'Июнь',
            'Июль', 'Август', 'Сентябрь',
            'Октябрь', 'Ноябрь', 'Декабрь',
        ])
        self.year_combo = QComboBox()
        self.year_combo.addItems([str(year) for year in range(2021, 1899, -1)])
        self.driver_license_checkbox = QCheckBox('Водительское удостоверение')

        # Создаем кнопку для сохранения данных
        self.save_button = QPushButton('Сохранить')
        self.save_button.clicked.connect(self.validate_inputs)

        # Создаем элементы для размещения на форме
        form_layout = QGridLayout()
        form_layout.addWidget(self.name_label, 0, 0)
        form_layout.addWidget(self.name_input, 0, 1)
        form_layout.addWidget(self.group_label, 1, 0)
        form_layout.addWidget(self.group_input, 1, 1)
        form_layout.addWidget(self.gender_label, 2, 0)
        gender_layout = QHBoxLayout()
        gender_layout.addWidget(self.male_radio)
        gender_layout.addWidget(self.female_radio)
        form_layout.addLayout(gender_layout, 2, 1)
        form_layout.addWidget(self.birthday_label, 3, 0)
        birthday_layout = QHBoxLayout()
        birthday_layout.addWidget(self.day_combo)
        birthday_layout.addWidget(self.month_combo)
        birthday_layout.addWidget(self.year_combo)
        form_layout.addLayout(birthday_layout, 3, 1)
        form_layout.addWidget(self.driver_license_checkbox, 4, 0, 1, 2)
        form_layout.addWidget(self.save_button, 5, 0, 1, 2)

        # Устанавливаем layout формы
        self.setLayout(form_layout)

        # Загружаем сохраненные данные
        self.load_data()

    def load_data(self):
        # Создаем объект QSettings для загрузки данных
        settings = QSettings('MyCompany', 'MyApp')

        # Загружаем данные из настроек
        name = settings.value('name', '')
        group = settings
        gender = settings.value('gender', '')
        birthday = settings.value('birthday', QDate(2000, 1, 1))
        has_driver_license = settings.value('has_driver_license', False)

        # Устанавливаем загруженные значения в соответствующие элементы управления
        self.name_input.setText(name)
        self.group_input.setText(group)
        if gender == 'male':
            self.male_radio.setChecked(True)
        elif gender == 'female':
            self.female_radio.setChecked(True)
        self.day_combo.setCurrentText(str(birthday.day()))
        self.month_combo.setCurrentText(birthday.toString('MMMM'))
        self.year_combo.setCurrentText(str(birthday.year()))
        self.driver_license_checkbox.setChecked(has_driver_license)

    def save_data(self):
        # Создаем объект QSettings для сохранения данных
        settings = QSettings('MyCompany', 'MyApp')

        # Сохраняем данные в настройки
        settings.setValue('name', self.name_input.text())
        settings.setValue('group', self.group_input.text())
        if self.male_radio.isChecked():
            settings.setValue('gender', 'male')
        elif self.female_radio.isChecked():
            settings.setValue('gender', 'female')
        birthday = QDate(int(self.year_combo.currentText()), self.month_combo.currentIndex() + 1,
                         int(self.day_combo.currentText()))
        settings.setValue('birthday', birthday)
        settings.setValue('has_driver_license', self.driver_license_checkbox.isChecked())

    def validate_inputs(self):
        # Проверяем заполнение обязательных полей
        if not self.name_input.text():
            self.name_input.setStyleSheet('border: 1px solid red;')
            return
        else:
            self.name_input.setStyleSheet('')
        if not self.group_input.text():
            self.group_input.setStyleSheet('border: 1px solid red;')
            return
        else:
            self.group_input.setStyleSheet('')

        # Сохраняем данные
        self.save_data()

        # Закрываем окно
        self.close()

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())