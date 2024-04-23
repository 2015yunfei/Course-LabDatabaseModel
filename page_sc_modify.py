import tkinter as tk
from tkinter import messagebox
import pymysql.cursors
import ConnectToMySql as Con
import SqlModify


def modify_student_grades(root, connect):
    # 创建主窗口
    window = tk.Toplevel(root)  # 这里使用root作为父窗口
    window.title("修改学生成绩")
    window.geometry("360x360")  # 设置窗口大小
    window.grab_set()

    # 创建输入框
    Sno_label = tk.Label(window, text="学号(Sno):")
    Sno_label.pack()
    Sno_entry = tk.Entry(window)
    Sno_entry.pack()

    Cno_label = tk.Label(window, text="课程号(Cno):")
    Cno_label.pack()
    Cno_entry = tk.Entry(window)
    Cno_entry.pack()

    Grade_label = tk.Label(window, text="成绩(Grade):")
    Grade_label.pack()
    Grade_entry = tk.Entry(window)
    Grade_entry.pack()

    # 创建按钮
    add_button = tk.Button(window, text="修改学生成绩",
                           command=lambda: SqlModify.modify_stu_grade(Sno_entry, Cno_entry, Grade_entry, connect))
    add_button.pack()

    # 启动Tkinter事件循环
    window.mainloop()
