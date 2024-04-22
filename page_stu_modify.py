import tkinter as tk
from tkinter import messagebox
import pymysql.cursors
import ConnectToMySql as Con
import SqlCreate as Cre
import SqlModify as Mod
import func


def modify_stu_info(root, connect):
    # 创建主窗口
    window = tk.Toplevel(root)  # 这里使用root作为父窗口
    window.title("修改学生信息")
    window.geometry("360x360")  # 设置窗口大小
    window.grab_set()

    # 创建输入框
    Sno_label = tk.Label(window, text="学号(Sno):")
    Sno_label.pack()
    Sno_entry = tk.Entry(window)
    Sno_entry.pack()

    Sname_label = tk.Label(window, text="姓名(Sname):")
    Sname_label.pack()
    Sname_entry = tk.Entry(window)
    Sname_entry.pack()

    Ssex_label = tk.Label(window, text="性别(Ssex):")
    Ssex_label.pack()
    Ssex_entry = tk.Entry(window)
    Ssex_entry.pack()

    Sage_label = tk.Label(window, text="年龄(Sage):")
    Sage_label.pack()
    Sage_entry = tk.Entry(window)
    Sage_entry.pack()

    Sdept_label = tk.Label(window, text="学院(Sdept):")
    Sdept_label.pack()
    Sdept_entry = tk.Entry(window)
    Sdept_entry.pack()

    Scholarship_label = tk.Label(window, text="奖学金(Scholarship):")
    Scholarship_label.pack()
    Scholarship_entry = tk.Entry(window)
    Scholarship_entry.pack()

    # 按照学号修改
    modify_sno = tk.Button(window, text="按照学号修改",
                           command=lambda: Mod.modify_stu_info_sno(Sno_entry, Sname_entry, Ssex_entry, Sage_entry,
                                                                   Sdept_entry, Scholarship_entry, connect),
                           width="25", height="2")
    modify_sno.pack()

    # 启动Tkinter事件循环
    window.mainloop()
