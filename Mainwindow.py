import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.uic import loadUi

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        loadUi("untitled.ui", self)  # 直接加载 .ui 文件
       
    def addControl(self,str_message):
        self.text_control.appendPlainText(str_message)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())