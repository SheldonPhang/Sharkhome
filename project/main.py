import threading
import main.mode
import time
import sys
import os
from PyQt5.QtWidgets import QFileDialog

from PyQt5.QtGui import QTextCursor
from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QLineEdit,
    QComboBox,
    QPushButton,
    QTextEdit,
    QMainWindow,
    QFrame,
    QGridLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("OA漏扫工具")
        self.setGeometry(300, 300, 800, 500)
        self.setFixedSize(800, 500)

        self.file_button = QPushButton("选择文件", self)
        self.file_button.setGeometry(650, 10, 80, 32)
        self.file_button.setStyleSheet("background-color: #333; color: #fff;")
        self.file_button.clicked.connect(self.select_file)

        self.url_label = QLabel("Url:", self)
        self.url_label.setGeometry(0, 5, 50, 32)

        self.url_input = QLineEdit(self)
        self.url_input.setGeometry(45, 10, 200, 32)
        self.url_input.setStyleSheet("background-color: #fff;")
        self.url_input.setPlaceholderText("请输入URL")
        self.url_input.returnPressed.connect(self.start_scan)

        self.oa_label = QLabel("OA类型:", self)
        self.oa_label.setGeometry(260, 5, 60, 32)

        self.oa_combobox = QComboBox(self)
        self.oa_combobox.setGeometry(320, 10, 200, 32)
        self.oa_combobox.addItems(["通达OA", "泛微OA", "用友OA", "致远OA", "蓝凌OA", "万户OA"])
        self.oa_combobox.setCurrentIndex(1)

        self.start_button = QPushButton("开始扫描", self)
        self.start_button.setGeometry(550, 10, 80, 32)
        self.start_button.setStyleSheet("background-color: #333; color: #fff;")
        self.start_button.clicked.connect(self.start_scan)

        self.result_text = QTextEdit(self)
        self.result_text.setGeometry(18, 80, 763, 390)
        self.result_text.setStyleSheet("background-color: #000; color: #fff; font-family: 'Courier New', Courier, monospace; border: 1px solid #ccc;")
        self.result_text.setReadOnly(True)

        self.status_label = QLabel("状态：未扫描", self)
        self.status_label.setGeometry(20, 470, 200, 20)

        self.result_label = QLabel("扫描结果：", self)
        self.result_label.setGeometry(20, 60, 80, 20)

        self.scan_progress = QFrame(self)
        self.scan_progress.setGeometry(20, 460, 760, 5)
        self.scan_progress.setStyleSheet("background-color: #ccc;")

        self.file_path = ''


    def select_file(self):
        # 显示文件选择对话框
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(
            self, "选择文件", "", "Text Files (*.txt);;All Files (*)", options=options
        )

        # 更新文本框内容
        if file_path:
            self.file_path = file_path
            self.url_input.setText(file_path)

    def start_scan(self):
        # 获取输入参数
        url = self.url_input.text().strip()
        if not url:
            return

        user = "url"
        if self.file_path and os.path.isfile(self.file_path):
            user = "urls"
            file_path = self.file_path
            url = file_path

        # 在子线程中执行扫描操作
        t = threading.Thread(target=self.scan, args=(url, self.oa_combobox.currentText(), user))
        t.start()



    def get_file_path(self):
        file_path, _ = QFileDialog.getOpenFileName(self, '选择文件', os.getcwd(), 'Text files(*.txt)')
        return file_path

    def scan(self, url, oa_type, user):

        if oa_type == "通达OA":
            res = main.mode.tdpoc(user, url)
        elif oa_type == "泛微OA":
            res = main.mode.fwpoc(user, url)
        elif oa_type == "用友OA":
            res = main.mode.yypoc(user, url)
        elif oa_type == "致远OA":
            res = main.mode.zypoc(user, url)
        elif oa_type == "蓝凌OA":
            res = main.mode.llpoc(user, url)
        elif oa_type == "万户OA":
            res = main.mode.whpoc(user, url)
        else:
            res = ['wrong input']

        
        for item in res:
            self.result_text.insertPlainText(str(item) + '\n\n')
            self.result_text.moveCursor(self.result_text.textCursor().End)
            time.sleep(1)
        self.result_text.insertPlainText(f'扫描结束{self.oa_combobox.currentText()}...\n\n')
        self.result_text.moveCursor(self.result_text.textCursor().End)

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
