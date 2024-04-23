import Debug
import tkinter as tk
from tkinter import messagebox
import pymysql.cursors
import pymysql
from pymysql.err import Error
import ConnectToMySql as Con
import SqlCreate as Cre
import SqlModify as Mod
import SqlDelete as Del
import func
import page_sc_add


def on_add_course(root, connect):
    print("增加课程")
    # 创建主窗口
    window = tk.Toplevel(root)  # 这里使用root作为父窗口
    window.title("增加课程信息")
    window.geometry("360x360")  # 设置窗口大小
    window.grab_set()

    # 创建输入框
    Cno_label = tk.Label(window, text="课程编号(Cno):")
    Cno_label.pack()
    Cno_entry = tk.Entry(window)
    Cno_entry.pack()

    Cname_label = tk.Label(window, text="课程名称(Cname):")
    Cname_label.pack()
    Cname_entry = tk.Entry(window)
    Cname_entry.pack()

    Cpno_label = tk.Label(window, text="父课程编号(Cpno):")
    Cpno_label.pack()
    Cpno_entry = tk.Entry(window)
    Cpno_entry.pack()

    Ccredit_label = tk.Label(window, text="学分(Ccredit):")
    Ccredit_label.pack()
    Ccredit_entry = tk.Entry(window)
    Ccredit_entry.pack()

    # 创建按钮
    add_button = tk.Button(window, text="增加课程信息",
                           command=lambda: Cre.add_course(Cno_entry, Cname_entry, Cpno_entry, Ccredit_entry, connect))
    add_button.pack()

    # 启动Tkinter事件循环
    window.mainloop()


def on_modify_course(root, connect):
    print("修改课程信息")
    # 创建主窗口
    window = tk.Toplevel(root)  # 这里使用root作为父窗口
    window.title("修改课程信息")
    window.geometry("360x360")  # 设置窗口大小
    window.grab_set()

    # 创建输入框
    Cno_label = tk.Label(window, text="根据课程编号修改信息，请输入课程编号(Cno):")
    Cno_label.pack()
    Cno_entry = tk.Entry(window)
    Cno_entry.pack()

    Cname_label = tk.Label(window, text="更新后的课程名称(Cname):")
    Cname_label.pack()
    Cname_entry = tk.Entry(window)
    Cname_entry.pack()

    Cpno_label = tk.Label(window, text="更新后的父课程编号(Cpno):")
    Cpno_label.pack()
    Cpno_entry = tk.Entry(window)
    Cpno_entry.pack()

    Ccredit_label = tk.Label(window, text="更新后的学分(Ccredit):")
    Ccredit_label.pack()
    Ccredit_entry = tk.Entry(window)
    Ccredit_entry.pack()

    # 创建按钮
    add_button = tk.Button(window, text="修改课程信息",
                           command=lambda: Mod.modify_course(Cno_entry, Cname_entry, Cpno_entry, Ccredit_entry,
                                                             connect))
    add_button.pack()

    # 启动Tkinter事件循环
    window.mainloop()


def course_information_maintenance(root, connect):
    # 创建主窗口
    window = tk.Toplevel(root)  # 这里使用root作为父窗口
    window.title("课程信息维护")
    window.geometry("360x250")  # 设置窗口大小
    window.grab_set()

    # 创建一个帧来包含所有内容，以便更容易居中
    content_frame = tk.Frame(window)
    content_frame.pack(pady=20)  # 添加一些外部填充

    # 创建一个行帧来包含标签和按钮
    row_frame = tk.Frame(content_frame)
    row_frame.pack(fill="x", padx=10, pady=10)  # 使用填充使行之间有间隔
    add_button = tk.Button(row_frame, text="增加课程", command=lambda: on_add_course(window, connect), width="30",
                           height="2")
    add_button.pack()

    # 创建一个行帧来包含标签和按钮
    row_frame = tk.Frame(content_frame)
    row_frame.pack(fill="x", padx=10, pady=10)  # 使用填充使行之间有间隔
    modify_button = tk.Button(row_frame, text="修改课程信息", command=lambda: on_modify_course(window, connect),
                              width="30", height="2")
    modify_button.pack()

    # 创建一个行帧来包含标签和按钮
    row_frame = tk.Frame(content_frame)
    row_frame.pack(fill="x", padx=10, pady=10)  # 使用填充使行之间有间隔
    delete_button = tk.Button(row_frame, text="删除没有选课信息的课程",
                              command=lambda: Del.delete_course_not_in_sc(connect), width="30",
                              height="2")
    delete_button.pack()

    # 启动Tkinter事件循环
    window.mainloop()
