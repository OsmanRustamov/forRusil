from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QRadioButton, QComboBox, QCheckBox, QVBoxLayout, QMessageBox, QPushButton, QHBoxLayout
from PyQt5.QtCore import QSize, QCoreApplication, QSettings
import sys

class Form(QWidget):

    def __init__(self):
        super().__init__()

        # Создаем поля ввода
        self.name = QLineEdit()
        self.group = QLineEdit()

        # Создаем радиокнопки для выбора пола
        self.male_radio = QRadioButton("Мужской")
        self.female_radio = QRadioButton("Женский")
        self.gender_layout = QVBoxLayout()
        self.gender_layout.addWidget(self.male_radio)
        self.gender_layout.addWidget(self.female_radio)

        # Создаем выпадающие списки для выбора дня, месяца и года рождения
        self.day_combo = QComboBox()
        self.day_combo.addItems([str(day) for day in range(1, 32)])
        self.month_combo = QComboBox()
        self.month_combo.addItems(["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"])
        self.year_combo = QComboBox()
        self.year_combo.addItems([str(year) for year in range(2023, 1899, -1)])

        # Создаем чекбокс для выбора наличия водительского удостоверения
        self.driving_license_checkbox = QCheckBox("Водительское удостоверение")

        # Создаем метки для полей ввода и устанавливаем их расположение в форме
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Имя"))
        layout.addWidget(self.name)
        layout.addWidget(QLabel("Группа"))
        layout.addWidget(self.group)
        layout.addWidget(QLabel("Пол"))
        layout.addLayout(self.gender_layout)
        layout.addWidget(QLabel("День рождения"))
        layout.addWidget(self.day_combo)
        layout.addWidget(QLabel("Месяц"))
        layout.addWidget(self.month_combo)
        layout.addWidget(QLabel("Год"))
        layout.addWidget(self.year_combo)
        layout.addWidget(self.driving_license_checkbox)

        # Создаем кнопку для отправки данных
        submit_button = QPushButton("Отправить")
        submit_button.clicked.connect(self.show_data)
        button_layout = QHBoxLayout()
        button_layout.addStretch(1)
        button_layout.addWidget(submit_button)

        # Устанавливаем созданное расположение в форме
        layout.addLayout(button_layout)
        self.setLayout(layout)

        # Загружаем сохраненные данные при открытии окна
        self.load_data()

    def load_data(self):
        # Создаем объект QSettings для чтения сохраненных данных
        settings = QSettings('MyCompany', 'MyApp')
        # Загружаем сохраненные значения для полей
        self.name.setText(settings.value('name', ''))
        self.group.setText(settings.value('group', ''))

    def save_data(self):
        # Создаем объект QSettings для записи данных
        settings = QSettings('MyCompany', 'MyApp')
        # Сохраняем значения полей
        settings.setValue('name', self.name.text())
        settings.setValue('group', self.group.text())

    def show_data(self):
        # Собираем данные из полей ввода
        name = self.name.text()
        group = self.group.text()
        if self.male_radio.isChecked():
            gender = "Мужской"
        elif self.female_radio.isChecked():
            gender = "Женский"
        else:
            gender = 0
        day = self.day_combo.currentText()
        month = self.month_combo.currentText()
        year = self.year_combo.currentText()
        driving_license = "да" if self.driving_license_checkbox.isChecked() else "нет"
        # Отображаем данные в новом окне
        if name == '':
            QMessageBox.information(self, "Введенные данные", f'Поле имя не заполнено')
        elif group == '':
            QMessageBox.information(self, "Введенные данные", f'Поле группа не заполнено')
        elif gender == 0:
            QMessageBox.information(self, "Введенные данные", f'Поле пол не заполнено')
        else:
            if gender == "Мужской":
                if 65 - (2023 - int(year)) > 0:
                    QMessageBox.information(self, "Введенные данные",f"Возраст: {2023 - int(year)}\n Лет до пенсии: {65 - (2023 - int(year))}")
                else:
                    QMessageBox.information(self, "Введенные данные", f"Возраст: {2023 - int(year)}\n Уже пенсионер")
            else:
                if 63 - (2023 - int(year)) > 0:
                    QMessageBox.information(self, "Введенные данные", f"Возраст: {2023 - int(year)}\n Лет до пенсии: {63 - (2023 - int(year))}")
                else:
                    QMessageBox.information(self, "Введенные данные", f"Возраст: {2023 - int(year)}\n Уже пенсионер")
if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    sys.exit(app.exec_())
