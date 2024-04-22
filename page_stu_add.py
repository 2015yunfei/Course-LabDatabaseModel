import tkinter as tk
from tkinter import messagebox
import pymysql.cursors
import ConnectToMySql as Con
import SqlCreate as Cre
import SqlModify as Mod
import func
import page_sc_add
import page_course


def add_new_student(root, connect):
    # 创建主窗口
    window = tk.Toplevel(root)  # 这里使用root作为父窗口
    window.title("增加新生入学信息")
    window.geometry("360x360")  # 设置窗口大小
    window.grab_set()

    # 创建输入框
    sno_label = tk.Label(window, text="学号(Sno):")
    sno_label.pack()
    sno_entry = tk.Entry(window)
    sno_entry.pack()

    sname_label = tk.Label(window, text="姓名(Sname):")
    sname_label.pack()
    sname_entry = tk.Entry(window)
    sname_entry.pack()

    ssex_label = tk.Label(window, text="性别(Ssex):")
    ssex_label.pack()
    ssex_entry = tk.Entry(window)
    ssex_entry.pack()

    sage_label = tk.Label(window, text="年龄(Sage):")
    sage_label.pack()
    sage_entry = tk.Entry(window)
    sage_entry.pack()

    sdept_label = tk.Label(window, text="学院(Sdept):")
    sdept_label.pack()
    sdept_entry = tk.Entry(window)
    sdept_entry.pack()

    scholarship_label = tk.Label(window, text="奖学金(Scholarship):")
    scholarship_label.pack()
    scholarship_entry = tk.Entry(window)
    scholarship_entry.pack()

    # 创建按钮
    add_button = tk.Button(window, text="添加新生信息",
                           command=lambda: Cre.add_student(sno_entry, sname_entry, ssex_entry, sage_entry, sdept_entry,
                                                           scholarship_entry, connect), width="25", height="2")
    add_button.pack()

    # 启动Tkinter事件循环
    window.mainloop()
