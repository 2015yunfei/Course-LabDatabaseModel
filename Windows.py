import tkinter as tk
from tkinter import messagebox
import pymysql.cursors
import ConnectToMySql as Con
import CreateSQL as Cre


# 创建一个函数，用于处理按钮点击事件
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
                           command=lambda: Cre.modify_course(Cno_entry, Cname_entry, Cpno_entry, Ccredit_entry,
                                                             connect))
    add_button.pack()

    # 启动Tkinter事件循环
    window.mainloop()


def on_delete_course():
    print("删除没有选课的课程信息")


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
                                                           scholarship_entry, connect))
    add_button.pack()

    # 启动Tkinter事件循环
    window.mainloop()


def update_student_info(root, connect):
    # 创建主窗口

    # 按照姓名修改

    # 按照学号修改

    pass


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

    add_button = tk.Button(row_frame, text="增加课程", command=lambda: on_add_course(root, connect), width="30",
                           height="2")
    add_button.pack()

    row_frame = tk.Frame(content_frame)
    row_frame.pack(fill="x", padx=10, pady=10)  # 使用填充使行之间有间隔

    modify_button = tk.Button(row_frame, text="修改课程信息", command=lambda: on_modify_course(root, connect),
                              width="30", height="2")
    modify_button.pack()

    row_frame = tk.Frame(content_frame)
    row_frame.pack(fill="x", padx=10, pady=10)  # 使用填充使行之间有间隔

    delete_button = tk.Button(row_frame, text="删除没有选课的课程信息", command=on_delete_course, width="30",
                              height="2")
    delete_button.pack()

    # 启动Tkinter事件循环
    window.mainloop()


def record_student_grades(root, connect):
    pass


def modify_student_grades(root, connect):
    pass


def view_grades(root, connect):
    pass


def view_ranking(root, connect):
    pass


def query_student_info(root, connect):
    pass


def close_window(root):
    # 销毁当前窗口
    root.destroy()


def on_button_click(root, index, connection):
    functions = [add_new_student,
                 update_student_info,
                 course_information_maintenance,
                 record_student_grades,
                 modify_student_grades,
                 view_grades,
                 view_ranking,
                 query_student_info]

    if 0 <= index < 8:
        functions[index](root, connection)
    else:
        try:
            connection.close()
        except pymysql.Error as e:
            messagebox.showerror(f"数据库错误：{e}")
        root.destroy()
        return


def delete_exist_tables_win(root):
    # 创建一个新的窗口
    window = tk.Toplevel(root)  # 这里使用root作为父窗口
    window.title("成功删除")
    window.geometry("300x70")  # 设置窗口大小
    window.grab_set()

    # 在窗口中添加一个标签，显示文本“三个基本表已经存在”
    label = tk.Label(window, text="原有的基本表已经成功删除")
    label.pack()

    button = tk.Button(window, text="确定", command=lambda: [close_window(window), close_window(root)])
    button.pack(anchor="center")
    print(123)


def create_gui(connection):
    # 创建包含八个字符串的数组
    options = [
        "新生入学信息增加",
        "学生信息修改",
        "课程信息维护",
        "录入学生成绩",
        "修改学生成绩",
        "查看成绩",
        "查看排名",
        "查询学生信息",
        "关闭"
    ]

    # 创建主窗口
    root = tk.Tk()
    root.title("学生管理系统")
    root.geometry("300x700")  # 设置窗口大小

    # 创建一个帧来包含所有内容，以便更容易居中
    content_frame = tk.Frame(root)
    content_frame.pack(pady=20)  # 添加一些外部填充

    # 创建内容
    for i in range(9):
        # 创建一个行帧来包含标签和按钮
        row_frame = tk.Frame(content_frame)
        row_frame.pack(fill="x", padx=10, pady=10)  # 使用填充使行之间有间隔

        # 创建占满行宽度的按钮
        button = tk.Button(row_frame, text=options[i], width="30", height="2",
                           command=lambda i=i: on_button_click(root, i, connection))
        button.pack(anchor="center")

    return root


def check_window_no(root, connection):
    # 创建一个新的窗口
    window = tk.Toplevel(root)  # 这里使用root作为父窗口
    window.title("未创建表")
    window.geometry("300x70")  # 设置窗口大小
    window.grab_set()

    # 在窗口中添加一个标签，显示文本
    label = tk.Label(window, text="三个基础表未创建，已经新的空表！")
    label.pack()

    Con.Create_3_table(connection)

    # 启动事件循环，使窗口保持打开状态
    window.mainloop()


def check_window_yes(root, connection):
    # 创建一个新的窗口
    window = tk.Toplevel(root)  # 这里使用root作为父窗口
    window.title("表已经存在")
    window.geometry("300x70")  # 设置窗口大小
    window.grab_set()

    # 在窗口中添加一个标签，显示文本“三个基本表已经存在”
    label = tk.Label(window, text="三个基本表已经存在")
    label.pack()

    # 创建两个按钮，并设置它们的文本
    button1 = tk.Button(window,
                        text="删除旧表",
                        command=lambda: [Con.cascade_delete_tables(connection), Con.Create_3_table(connection),
                                         delete_exist_tables_win(window)])
    button2 = tk.Button(window, text="使用原有数据", command=lambda: close_window(window))

    # 布局按钮
    button1.pack(side="left", anchor="center")
    button2.pack(side="right", anchor="center")

    # 启动事件循环，使窗口保持打开状态
    window.mainloop()


def do_after_gui_runs(root, connection):
    # 检查表是否存在
    if (Con.check_table_exists(connection, "student") and Con.check_table_exists(connection, "sc")
            and Con.check_table_exists(connection, "course")):

        print("表存在")

        # 调用函数以弹出窗口
        check_window_yes(root, connection)
    else:

        print("不存在表")

        Con.Create_3_table(connection)
        # 调用函数以弹出窗口
        check_window_no(root, connection)
