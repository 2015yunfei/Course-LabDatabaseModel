import tkinter as tk
from tkinter import messagebox
import pymysql.cursors
import ConnectToMySql as Con
import SqlCreate as Cre
import SqlModify as Mod
import SqlSelect

def query_student_info(root, connect):
    # 创建主窗口
    window = tk.Toplevel(root)  # 这里使用root作为父窗口
    window.title("查询学生信息")
    window.geometry("360x360")  # 设置窗口大小
    window.grab_set()

    # 创建输入框
    Sno_label = tk.Label(window, text="要查询学生的学号(Sno):")
    Sno_label.pack()
    Sno_entry = tk.Entry(window)
    Sno_entry.pack()

    # 按照学号查询
    modify_sno = tk.Button(window, text="按照学号修改",
                           command=lambda: SqlSelect.get_student_info(Sno_entry, connect),
                           width="25", height="2")
    modify_sno.pack()

    # 启动Tkinter事件循环
    window.mainloop()
