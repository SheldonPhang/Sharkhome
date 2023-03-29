import threading
import main.mode
import time
import sys
import os
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QIcon
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
    QFileDialog,
    QMessageBox,
    QProgressBar,
    QVBoxLayout,
    QInputDialog,
    QTextBrowser,
)
from report_generator import generate_report  # 导入报告生成函数

class MainWindow(QMainWindow):
    progress_signal = pyqtSignal(int)  # 创建信号，用于更新进度条
    update_result_text_signal = pyqtSignal(str)
    scan_finished_signal = pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.update_result_text_signal.connect(self.update_result_text)
        self.scan_finished_signal.connect(self.show_scan_finished_message)
    def update_result_text(self, text):
        self.result_text.insertPlainText(text + '\n\n')
        self.result_text.moveCursor(self.result_text.textCursor().End)
    def init_ui(self):
        self.setWindowTitle("OA漏扫工具")
        self.setWindowIcon(QIcon('\\images\\1.ico'))

        self.setGeometry(300, 300, 1000, 600)
        self.setFixedSize(1000, 600)

        main_layout = QVBoxLayout()
        central_widget = QWidget(self)
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        # 顶部布局
        top_layout = QGridLayout()
        main_layout.addLayout(top_layout)

        #添加按钮
        self.add_poc_button = QPushButton("添加新的漏洞")
        self.add_poc_button.clicked.connect(self.add_poc)
        top_layout.addWidget(self.add_poc_button, 2, 2)
        # Row 0
        self.url_label = QLabel("Url:")
        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("请输入URL")
        self.url_input.returnPressed.connect(self.start_scan)

        self.file_button = QPushButton("选择文件")
        self.file_button.clicked.connect(self.select_file)
        self.file_path = ''
        # Row 1
        self.oa_label = QLabel("OA类型:")
        self.oa_combobox = QComboBox()
        self.oa_combobox.addItems(["通达OA", "泛微OA", "用友OA", "致远OA", "蓝凌OA", "万户OA"])
        self.oa_combobox.setCurrentIndex(1)

        self.start_button = QPushButton("开始扫描")
        self.start_button.clicked.connect(self.start_scan)

        # Row 2
        result_layout = QVBoxLayout()
        main_layout.addLayout(result_layout)
        self.result_label = QLabel("扫描结果：")
        result_layout.addWidget(self.result_label)

        # 输出框
        self.result_text = QTextBrowser()
        self.result_text.setFrameShape(QFrame.StyledPanel)
        self.result_text.setFrameShadow(QFrame.Sunken)
        self.result_text.setLineWidth(1)
        result_layout.addWidget(self.result_text)

        # Row 3
        self.status_label = QLabel("状态：未扫描")

        self.progress_bar = QProgressBar()
        self.progress_signal.connect(self.update_progress_bar)

        top_layout.addWidget(self.url_label, 0, 0)
        top_layout.addWidget(self.url_input, 0, 1)
        top_layout.addWidget(self.file_button, 0, 2)
        top_layout.addWidget(self.oa_label, 1, 0)
        top_layout.addWidget(self.oa_combobox, 1, 1)
        top_layout.addWidget(self.start_button, 1, 2)

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
        self.result_text.clear()  # 清空扫描结果
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

    # 添加槽函数
    def add_poc(self):
        # 弹出对话框选择 POC 文件
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(self, "选择 POC 文件", "", "Python Files (*.py)", options=options)
        
        if file_name:
            # 弹出对话框选择 OA 类型
            oa_types = ["通达OA", "泛微OA", "用友OA", "致远OA", "蓝凌OA", "万户OA"]
            oa_type, ok_pressed = QInputDialog.getItem(self, "选择添加POC的OA 类型", "OA 类型:", oa_types, 0, False)
            
            if ok_pressed:
                # 将 POC 文件复制到相应的目录
                base_dir = "main"  # 这里可以根据实际情况修改
                type_dirs = {"通达OA": "Anywhere", "泛微OA": "weaver", "用友OA": "yongyou", "致远OA": "seeyou", "蓝凌OA": "Landray", "万户OA": "ezoffice"}
                target_dir = os.path.join(base_dir, type_dirs[oa_type])

                if not os.path.exists(target_dir):
                    os.makedirs(target_dir)

                dest_file = os.path.join(target_dir, os.path.basename(file_name))
                with open(file_name, "r", encoding="utf-8") as src_file, open(dest_file, "w", encoding="utf-8") as dst_file:
                    dst_file.write(src_file.read())

                self.result_text.append(f"已添加新的漏洞 POC 文件: {os.path.basename(file_name)} (OA 类型: {oa_type})")
                QMessageBox.information(self, "添加成功", f"已添加新的漏洞 POC 文件: {os.path.basename(file_name)} (OA 类型: {oa_type})")

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

        total_items = len(res)
        for index, item in enumerate(res):
            self.update_result_text_signal.emit(str(item))
            self.result_text.moveCursor(self.result_text.textCursor().End)
            time.sleep(1)
            self.progress_signal.emit(int((index + 1) / total_items * 100))  # 发送信号更新进度条

        self.update_result_text_signal.emit(f'扫描结束{self.oa_combobox.currentText()}...')
        self.result_text.moveCursor(self.result_text.textCursor().End)

        # 生成报告
        report_path = generate_report(res, oa_type)  # 调用报告生成函数
        self.scan_finished_signal.emit(report_path)
    def show_scan_finished_message(self, report_path):
        QMessageBox.information(self, "扫描完成", f"扫描完成。报告已保存至 {report_path}")

    def update_progress_bar(self, value):
        self.progress_bar.setValue(value)




if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
