import tkinter as tk
from tkinter import messagebox
import pymysql.cursors
import ConnectToMySql as Con
import SqlCreate as Cre
import SqlModify as Mod
import func
import page_sc_add
import page_course
import page_stu_modify
import page_stu_add
import page_select_grades
import page_select_order
import page_sc_modify
import page_select_stu


def on_button_click(root, index, connection):
    functions = [page_stu_add.add_new_student,
                 page_stu_modify.modify_stu_info,
                 page_course.course_information_maintenance,
                 page_sc_add.record_student_grades,
                 page_sc_modify.modify_student_grades,
                 page_select_grades.view_grades,
                 page_select_order.view_ranking,
                 page_select_stu.query_student_info]

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

    button = tk.Button(window, text="确定", command=lambda: [func.close_window(window), func.close_window(root)])
    button.pack(anchor="center")
    print(123)

    # 启动Tkinter事件循环
    window.mainloop()


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

    Con.create_3_table(connection)

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
                        command=lambda: [Con.cascade_delete_tables(connection), Con.create_3_table(connection),
                                         delete_exist_tables_win(window)])
    button2 = tk.Button(window, text="使用原有数据", command=lambda: func.close_window(window))

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

        Con.create_3_table(connection)
        # 调用函数以弹出窗口
        check_window_no(root, connection)
