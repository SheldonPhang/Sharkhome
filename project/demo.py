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
    QProgressDialog,
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
    def open_readme(self):
        readme_path = os.path.join(os.getcwd(), "readme.txt")
        os.startfile(readme_path)
    def update_result_text(self, text):
        self.result_text.insertPlainText(text + '\n\n')
        self.result_text.moveCursor(self.result_text.textCursor().End)
    def init_ui(self):
        self.setWindowTitle("OA漏扫工具")  # 设置主窗口标题为“OA漏扫工具”
        self.setWindowIcon(QIcon('images/xg.ico'))  # 设置主窗口图标为“images/xg.ico”
        self.setGeometry(300, 300, 1000, 600)  # 设置主窗口位置和大小
        self.setFixedSize(1000, 600)  # 固定主窗口大小

        main_layout = QVBoxLayout()  # 创建一个垂直布局
        central_widget = QWidget(self)  # 创建一个QWidget对象，作为中央窗口部件
        central_widget.setLayout(main_layout)  # 设置中央窗口部件的布局为垂直布局
        self.setCentralWidget(central_widget)  # 将中央窗口部件设置为主窗口的中央窗口部件

        # 顶部布局
        top_layout = QGridLayout()
        main_layout.addLayout(top_layout)
        self.show_poc_button = QPushButton("查看当前库")  # 创建一个QPushButton对象，文本为“查看当前库”
        self.show_poc_button.clicked.connect(self.show_poc_list)  # 绑定按钮的clicked信号到self.show_poc_list槽函数上
        top_layout.addWidget(self.show_poc_button, 2, 1)  # 将按钮添加到top_layout中的第2行、第1列

        #添加按钮
        self.add_poc_button = QPushButton("添加新的漏洞")  # 创建一个QPushButton对象，文本为“添加新的漏洞”
        self.add_poc_button.clicked.connect(self.add_poc)  # 绑定按钮的clicked信号到self.add_poc槽函数上
        self.how_to_use_button = QPushButton("如何使用")  # 创建一个QPushButton对象，文本为“如何使用”
        self.how_to_use_button.clicked.connect(self.open_readme)  # 绑定按钮的clicked信号到self.open_readme槽函数上

        # Row 0
        self.url_label = QLabel("Target:")  # 创建一个QLabel对象，文本为“Target:”
        self.url_input = QLineEdit()  # 创建一个QLineEdit对象
        self.url_input.setPlaceholderText("请输入URL")  # 设置QLineEdit对象的提示文本为“请输入URL”
        self.url_input.returnPressed.connect(self.start_scan)  # 绑定QLineEdit对象的returnPressed信号到self.start_scan槽函数上

        self.file_button = QPushButton("批量输入")  # 创建一个QPushButton对象，文本为“批量输入”
        self.file_button.clicked.connect(self.select_file)  # 绑定QPushButton对象的clicked信号到self.select_file槽函数上
        self.file_path = ''  # 创建一个文件路径变量，初始值为空

        # Row 1
        self.oa_label = QLabel("OA类型:")  # 创建一个QLabel对象，文本为“OA类型:”
        self.oa_combobox = QComboBox()  # 创建一个QComboBox对象
        self.oa_combobox.addItems(["蓝凌OA", "万户OA","用友OA", "致远OA", "通达OA", "泛微OA","自定义" ])  # 在QComboBox对象中添加7
        self.oa_combobox.setCurrentIndex(0) #这一行代码将下拉菜单的默认选项设置为第一个选项（即“蓝凌OA”）。
        self.start_button = QPushButton("开始扫描")
        self.start_button.clicked.connect(self.start_scan)

        # Row 2
        result_layout = QVBoxLayout() #创建了一个垂直布局
        main_layout.addLayout(result_layout) #将上述垂直布局添加到主布局中。
        self.result_label = QLabel("扫描结果：")
        result_layout.addWidget(self.result_label) #将上述文本标签添加到垂直布局中。

        # 输出框
        self.result_text = QTextBrowser() #创建了一个文本浏览器。
        self.result_text.setFrameShape(QFrame.StyledPanel) #设置了文本浏览器的边框样式为QFrame.StyledPanel。
        self.result_text.setFrameShadow(QFrame.Sunken) #设置了文本浏览器的边框阴影为QFrame.Sunken。
        self.result_text.setLineWidth(1) #设置了文本浏览器的边框线宽度为1。
        result_layout.addWidget(self.result_text)

        # Row 3
        self.status_label = QLabel("状态：未扫描")
        self.scan_status_label = QLabel("扫描状态：未扫描")
        top_layout.addWidget(self.scan_status_label, 3, 0, 1, 3) #将上述文本标签添加到主布局中的第三行第一列，并占据1行3列的位置。
        self.progress_bar = QProgressBar() #创建了一个进度条
        self.progress_signal.connect(self.update_progress_bar)
        #将进度信号progress_signal连接到update_progress_bar槽函数上，当进度更新时，update_progress_bar函数会被执行。

        top_layout.addWidget(self.url_label, 0, 0)
        top_layout.addWidget(self.url_input, 0, 1)
        top_layout.addWidget(self.file_button, 0, 2)
        top_layout.addWidget(self.oa_label, 1, 0)
        top_layout.addWidget(self.oa_combobox, 1, 1)
        top_layout.addWidget(self.start_button, 1, 2)
        top_layout.addWidget(self.how_to_use_button, 3, 2)
        top_layout.addWidget(self.add_poc_button, 2, 2)  # 将按钮添加到top_layout中的第2行、第2列


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
        self.scan_status_label.setText("扫描状态：扫描中")
        self.update_result_text_signal.emit(f'开始扫描{self.oa_combobox.currentText()}...')
        self.progress_dialog = QProgressDialog("处理中，请稍候...", "取消", 0, 100, self)
        self.progress_dialog.setFixedSize(450, 100)  # 设置进度对话框的大小为 400x200
        self.progress_dialog.setWindowTitle("扫描中")
        self.progress_dialog.setWindowModality(Qt.WindowModal)
        self.progress_dialog.setAutoClose(True)
        self.progress_dialog.setAutoReset(True)
        self.progress_dialog.canceled.connect(self.progress_dialog.close)
        self.progress_signal.connect(self.progress_dialog.setValue)

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
            oa_types = ["通达OA", "泛微OA", "用友OA", "致远OA", "蓝凌OA", "万户OA", "自定义"]
            oa_type, ok_pressed = QInputDialog.getItem(self, "选择添加POC的OA 类型", "OA 类型:", oa_types, 0, False)
            
            if ok_pressed:
                # 将 POC 文件复制到相应的目录
                base_dir = "main"  # 这里可以根据实际情况修改
                type_dirs = {"通达OA": "Anywhere", "泛微OA": "weaver", "用友OA": "yongyou", "致远OA": "seeyou", "蓝凌OA": "Landray", "万户OA": "ezoffice", "自定义": "useradd"}
                target_dir = os.path.join(base_dir, type_dirs[oa_type])

                if not os.path.exists(target_dir):
                    os.makedirs(target_dir)

                dest_file = os.path.join(target_dir, os.path.basename(file_name))
                with open(file_name, "r", encoding="utf-8") as src_file, open(dest_file, "w", encoding="utf-8") as dst_file:
                    dst_file.write(src_file.read())

                self.result_text.append(f"已添加新的漏洞 POC 文件: {os.path.basename(file_name)} (OA 类型: {oa_type})")
                QMessageBox.information(self, "添加成功", f"已添加新的漏洞 POC 文件: {os.path.basename(file_name)} (OA 类型: {oa_type})")

    def show_poc_list(self):
        # 创建一个窗口
        self.poc_list_window = QMainWindow()
        self.poc_list_window.setWindowTitle("当前库")
        self.poc_list_window.setGeometry(300, 300, 400, 600)
        self.poc_list_window.setFixedSize(480, 600)

        # 创建一个垂直布局
        main_layout = QVBoxLayout()
        central_widget = QWidget(self.poc_list_window)
        central_widget.setLayout(main_layout)
        self.poc_list_window.setCentralWidget(central_widget)

        # 创建一个文本浏览器
        self.poc_list_text = QTextBrowser()
        main_layout.addWidget(self.poc_list_text)

        # 遍历文件夹
        base_dir = "main"
        type_dirs = {"通达OA": "Anywhere", "泛微OA": "weaver", "用友OA": "yonyou", "致远OA": "seeyou", "蓝凌OA": "Landray", "万户OA": "ezoffice", "自定义": "useradd"}
        for oa_type, dir_name in type_dirs.items():
            self.poc_list_text.append(f"{oa_type}:")
            target_dir = os.path.join(base_dir, dir_name)
            if os.path.exists(target_dir):
                for file_name in os.listdir(target_dir):
                    if file_name.endswith(".py"):
                        self.poc_list_text.append(f"  - {file_name}")
            self.poc_list_text.append("")

        # 显示窗口
        self.poc_list_window.show()



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
        elif oa_type == "自定义":
            res = main.mode.addpoc(user, url)
        else:
            res = ['wrong input']

        total_items = len(res)
        for index, item in enumerate(res):
            self.update_result_text_signal.emit(str(item))
            self.result_text.moveCursor(self.result_text.textCursor().End)
            time.sleep(1)
            self.progress_dialog.show()
            self.progress_signal.emit(int((index + 1) / total_items * 100))  # 发送信号更新进度条

        self.update_result_text_signal.emit(f'扫描结束{self.oa_combobox.currentText()}...')
        self.result_text.moveCursor(self.result_text.textCursor().End)
        self.scan_status_label.setText("扫描状态：扫描结束")
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
    app.setWindowIcon(QIcon('images/xg.ico'))  # 设置任务栏图标
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
