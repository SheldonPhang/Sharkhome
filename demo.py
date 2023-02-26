import tkinter
from tkinter import ttk
import threading
import main.mode
import time

windows = tkinter.Tk()
windows.title("OA漏扫工具")
windows.geometry('800x500')
windows.resizable(0,0)
images =tkinter.PhotoImage(file='.\\images\\1.jpg')
windows.iconphoto(False,images)

l = tkinter.Label(windows, text="Url:", width=5, height=2, justify='left')
l.place(x=0, y=5)

cv = tkinter.StringVar()
e = tkinter.Entry(windows, show=None, justify='left', bd=2, textvariable=cv)
e.place(x=45, y=10, width=200, height=32)

cho = ttk.Combobox(windows, values=['通达OA', '泛微OA', '用友OA', '致远OA', '蓝凌OA', '万户OA'], state='readonly')
cho.place(x=260, y=10, width=200, height=32)
cho.current(0) #设置默认为第一个泛微OA

t = tkinter.Text(windows)
t.place(x=18, y=100, width=763, height=350)

def scan():
    url = e.get().strip()
    if url == '':
        return
    t.delete('1.0', 'end')
    t.insert('insert', f"开始检测{cho.get()}...\n\n")
    t.see('end')
    user = 'url'
    if cho.get() == "通达OA":
        res = main.mode.tdpoc(user, url)
    elif cho.get() == "泛微OA":
        res = main.mode.fwpoc(user, url)
    elif cho.get() == "用友OA":
        res = main.mode.yypoc(user, url)
    elif cho.get() == "致远OA":
        res = main.mode.zypoc(user, url)
    elif cho.get() == "蓝凌OA":
        res = main.mode.llpoc(user, url)
    elif cho.get() == "万户OA":
        res = main.mode.whpoc(user, url)
    else:
        res = []
    for item in res:
        t.insert('insert', str(item) + "\n\n")
        t.see('end')
        time.sleep(1)
    t.insert('insert', f"扫描结束{cho.get()}...\n\n")
def start_scan(event):
    threading.Thread(target=scan).start()

b1 = tkinter.Button(windows,text='Start',width=4,height=0)
b1.place(x=500,y=10)
b1.bind("<Button-1>", start_scan)

windows.mainloop()
