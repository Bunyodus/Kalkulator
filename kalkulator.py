from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QVBoxLayout, QGridLayout
from PyQt5.QtGui import QPalette, QBrush, QPixmap
from PyQt5.QtCore import Qt

class MyWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_background("1.png")
        self.setFixedSize(620, 480)
        self.layout = QVBoxLayout(self)

        self.display = QLineEdit(self)
        self.display.setFixedHeight(50)
        self.display.setFixedWidth(480)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        self.display.move(70, 25)
        self.display.setStyleSheet("background:lightblue")

        self.grid_layout = QGridLayout()
        self.layout.addLayout(self.grid_layout)

        self.grid_layout.setContentsMargins(0, 0, 0, 0)
        self.grid_layout.setSpacing(0)

        self.buttons = {
            '1': (0, 0), '2': (0, 1), '3': (0, 2),
            '4': (1, 0), '5': (1, 1), '6': (1, 2),
            '7': (2, 0), '8': (2, 1), '9': (2, 2),
            '0': (3, 1), '+': (0, 3), '-': (1, 3),
            '*': (2, 3), '/': (3, 3), '=': (3, 2),
            'C': (3, 0)
        }

        for btn_text, pos in self.buttons.items():
            button = QPushButton(btn_text, self)
            button.setFixedSize(70, 70)
            button.setStyleSheet("background:lightblue")
            self.grid_layout.addWidget(button, pos[0], pos[1])
            self.grid_layout.setVerticalSpacing(10)
            button.clicked.connect(self.on_button_clicked)

    def on_button_clicked(self):
        sender = self.sender()
        text = sender.text()

        if text == 'C':
            self.display.clear()
        elif text == '=':
            
            result = eval(self.display.text())
            self.display.setText(str(result))
            
        else:
            self.display.setText(self.display.text() + text)

    def set_background(self, image_path):
        o_image = QPixmap(image_path)
        s_image = o_image.scaled(self.size())
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(s_image))
        self.setPalette(palette)

    def keyPressEvent(self, event):
        key = event.key()
        if key in (Qt.Key_0, Qt.Key_1, Qt.Key_2, Qt.Key_3, Qt.Key_4, Qt.Key_5, Qt.Key_6, Qt.Key_7, Qt.Key_8, Qt.Key_9):
            self.display.setText(self.display.text() + chr(key))
        elif key == Qt.Key_Plus:
            self.display.setText(self.display.text() + '+')
        elif key == Qt.Key_Minus:
            self.display.setText(self.display.text() + '-')
        elif key == Qt.Key_Asterisk:
            self.display.setText(self.display.text() + '*')
        elif key == Qt.Key_Slash:
            self.display.setText(self.display.text() + '/')
        elif key == Qt.Key_Return or key == Qt.Key_Enter:  
            result = eval(self.display.text())
            self.display.setText(str(result))
        elif key == Qt.Key_Escape:
            self.display.clear()

app = QApplication([])
win = MyWin()
win.show()
app.exec_()
