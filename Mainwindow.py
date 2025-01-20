import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QFileDialog
from PyQt6.uic import loadUi
from Package import streaming_asr_demo
from Package import http_method as htp
class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        loadUi("untitled.ui", self)  # 直接加载 .ui 文件
       
    def addControl(self,str_message):
        self.text_control.appendPlainText(str_message)

    def on_btn_start_clicked(self):
         # 弹出文件选择对话框
        file_path, _ = QFileDialog.getOpenFileName(
            self,  # 父窗口
            "选择音频文件",  # 对话框标题
            "",  # 初始目录（空字符串表示当前目录）
            "音频文件 (*.wav)"  # 文件过滤器
        )
        
        if(file_path == "") :
            self.addControl("没有正确找到文件路径")
            return
        
        ret = streaming_asr_demo.test_one(file_path)
        print(ret)
        text = ret['result']['payload_msg']['result'][0]['text']
        self.text_raw_texture.appendPlainText(text)

        api_key = "24d25586-dd58-46ff-adfa-1a3867f599ba"  # 替换为你的API密钥
        model = "ep-20250120114002-t7pgg"  # 替换为你的模型名称
        


        str_simplify = "请你使用MarkDown形式，将我接下来说的话简单摘要一下 ：" + text

        messages = [
        {"role": "system", "content": str_simplify},
        ]
        
        ret_simplify = htp.send_chat_request(api_key,model,messages)
        self.text_simplify_texture.appendPlainText(ret_simplify)

        str_mindmap = "请你使用MarkDown的形式，将我接下来的话使用MarkMap的格式转换成一个思维导图，并且发还给我：" + text
        messages = [
        {"role": "system", "content": str_mindmap},
        ]
        ret_mindmap = htp.send_chat_request(api_key,model,str_mindmap)

        self.text_mindmap.appendPlainText(ret_mindmap)

        self.addControl("分析完毕！")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())