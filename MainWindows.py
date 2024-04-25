import tkinter as tk
from tkinter import messagebox
import pymysql.cursors
import ConnectToMySql as Con
import Debug
import func
import page_sc_add
import page_course
import page_stu_modify
import page_stu_add
import page_select_grades
import page_select_order
import page_sc_modify
import page_select_stu
import ConnectToMySql


def on_closing(root, connection):
    try:
        connection.close()
    except pymysql.Error as e:
        messagebox.showerror("错误", f"关闭和远程数据库时发生数据库错误：{e}")
    root.destroy()


def all_button_main_window(root, index, connection):
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
        # ”关闭“按钮的作用
        try:
            connection.close()
        except pymysql.Error as e:
            messagebox.showerror("错误", f"关闭和远程数据库时发生数据库错误：{e}")
        root.destroy()


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
                           command=lambda index=i: all_button_main_window(root, index, connection))
        button.pack(anchor="center")

    return root


def check_window_no(root, connection):
    window = tk.Toplevel(root)  # 这里使用root作为父窗口
    window.title("不存在旧表")
    window.geometry("360x250")
    window.grab_set()

    # 创建一个帧来包含所有内容，以便更容易居中
    content_frame = tk.Frame(window)
    content_frame.pack(pady=20)  # 添加一些外部填充

    # 创建一个行帧来包含标签和按钮
    row_frame = tk.Frame(content_frame)
    row_frame.pack(fill="x", padx=5, pady=5)  # 使用填充使行之间有间隔

    label = tk.Label(row_frame, text="数据库中没有基本表：student、course、sc")
    label.pack()

    row_frame = tk.Frame(content_frame)
    row_frame.pack(fill="x", padx=5, pady=5)
    use_new_table = tk.Button(row_frame, text="新建空表", command=lambda: Con.create_3_table(connection),
                              width="30", height="2")
    use_new_table.pack()

    row_frame = tk.Frame(content_frame)
    row_frame.pack(fill="x", padx=5, pady=5)
    use_default_table = tk.Button(row_frame, text="使用默认数据",
                                  command=lambda: [Con.create_3_table(connection),
                                                   Con.insert_data(connection)],
                                  width="30", height="2")
    use_default_table.pack()

    # 启动事件循环，使窗口保持打开状态
    window.mainloop()


def check_window_yes(root, connection):
    # 创建一个新的窗口
    window = tk.Toplevel(root)
    window.title("表已经存在")
    window.geometry("360x250")
    window.grab_set()

    # 创建一个帧来包含所有内容，以便更容易居中
    content_frame = tk.Frame(window)
    content_frame.pack(pady=20)  # 添加一些外部填充

    # 创建一个行帧来包含标签和按钮
    row_frame = tk.Frame(content_frame)
    row_frame.pack(fill="x", padx=10, pady=10)  # 使用填充使行之间有间隔
    # 在窗口中添加一个标签，显示文本“三个基本表已经存在”
    label = tk.Label(row_frame, text="数据库中已经含有三个基本表：\nstudent\ncourse\nsc")
    label.pack()

    row_frame = tk.Frame(content_frame)
    row_frame.pack(fill="x", padx=5, pady=5)
    use_new_table = tk.Button(row_frame, text="新建空表",
                              command=lambda: [Con.cascade_delete_tables(connection),
                                               Con.create_3_table(connection),
                                               messagebox.showinfo("成功删除", "原有的基本表已经成功删除"),
                                               func.close_window(window)])
    use_new_table.pack(anchor="center")

    row_frame = tk.Frame(content_frame)
    row_frame.pack(fill="x", padx=5, pady=5)
    use_old_table = tk.Button(row_frame, text="使用原有数据",
                              command=lambda: [messagebox.showinfo("提示", "为您保留了数据库中的所有数据"),
                                               func.close_window(window)])
    use_old_table.pack(anchor="center")

    row_frame = tk.Frame(content_frame)
    row_frame.pack(fill="x", padx=5, pady=5)
    use_default_table = tk.Button(row_frame, text="使用默认数据",
                                  command=lambda: [Con.cascade_delete_tables(connection),
                                                   Con.create_3_table(connection),
                                                   Con.insert_data(connection),
                                                   messagebox.showinfo("提示", "已经插入实验指导书中给出的参考数据"),
                                                   func.close_window(window)])
    use_default_table.pack(anchor="center")

    # 启动事件循环，使窗口保持打开状态
    window.mainloop()


def do_after_gui_runs(root, connection):
    # 右上角×按钮关闭时，关闭和远程数据库的连接
    root.protocol("WM_DELETE_WINDOW", lambda: on_closing(root, connection))  # 设置关闭窗口时的协议

    # 检查表是否存在
    if (Con.check_table_exists(connection, "student") and Con.check_table_exists(connection, "sc")
            and Con.check_table_exists(connection, "course")):
        # 三个表都存在，意味着存在原本数据
        if Debug.debug_mod == 1:
            print("三个表存在")

        # 弹出窗口，1新建空表，2使用原有数据，3使用默认数据
        check_window_yes(root, connection)
    else:
        # 三个表存在一个或者两个的时候，将三个表全部删除
        ConnectToMySql.cascade_delete_tables(connection)

        if Debug.debug_mod == 1:
            print("不存在表")

        # 创建三个新表
        Con.create_3_table(connection)
        # 弹出窗口，1新建空表，2使用默认数据
        check_window_no(root, connection)
