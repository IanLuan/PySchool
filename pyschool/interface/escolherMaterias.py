import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.listCheckBox = ["Checkbox_1", "Checkbox_2", "Checkbox_3", "Checkbox_4", "Checkbox_5",
                             "Checkbox_6", "Checkbox_7", "Checkbox_8", "Checkbox_9", "Checkbox_10" ]
        grid = QGridLayout()

        for i, v in enumerate(self.listCheckBox):
            self.listCheckBox[i] = QCheckBox(v)
            grid.addWidget(self.listCheckBox[i], i, 0)

        self.button = QPushButton("Confirmar")
        self.button.clicked.connect(self.confirmarMaterias)

        grid.addWidget(self.button, 10, 0, 1,2)
        self.setLayout(grid)

    def confirmarMaterias(self):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = Window()
    clock.show()
    sys.exit(app.exec_())