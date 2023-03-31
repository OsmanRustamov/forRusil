from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton
from PyQt5.QtCore import Qt


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Калькулятор')
        self.setGeometry(300, 300, 300, 300)

        # Создание виджета для отображения введенных символов
        self.display = QLineEdit()
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        self.display.setMaxLength(15)

        # Создание кнопок
        self.buttons = {}
        buttons_layout = QVBoxLayout()
        rows = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+']
        ]
        for row in rows:
            hbox = QHBoxLayout()
            for label in row:
                button = QPushButton(label)
                button.setMinimumSize(40, 40)
                self.buttons[label] = button
                hbox.addWidget(button)
            buttons_layout.addLayout(hbox)

        # Создание главного макета
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.display)
        main_layout.addLayout(buttons_layout)

        # Привязка кнопок к обработчику событий
        for label, button in self.buttons.items():
            button.clicked.connect(lambda checked, label=label: self.on_button_clicked(label))

        self.setLayout(main_layout)

    def on_button_clicked(self, label):
        if label == 'C':
            self.display.clear()
        elif label == '=':
            try:
                result = eval(self.display.text())
                self.display.setText(str(result))
            except Exception as e:
                self.display.setText('Error')
        else:
            self.display.setText(self.display.text() + label)


if __name__ == '__main__':
    app = QApplication([])
    calculator = Calculator()
    calculator.show()
    app.exec_()
