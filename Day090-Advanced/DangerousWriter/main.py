import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit
from PyQt5.QtCore import QTimer

class DangerousWriter(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.text_edit = QTextEdit()
        self.start_button = QPushButton('Start Challenge')
        self.start_button.clicked.connect(self.start_challenge)

        vbox = QVBoxLayout()
        vbox.addWidget(self.text_edit)
        vbox.addWidget(self.start_button)

        self.setLayout(vbox)
        self.setWindowTitle('The Most Dangerous Writing App')

    def start_challenge(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.clear_text)
        self.timer.start(1000)  # Check every second

    def clear_text(self):
        if self.text_edit.toPlainText() == '':
            return
        self.text_edit.clear()
        self.timer.stop()

def main():
    app = QApplication(sys.argv)
    ex = DangerousWriter()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
