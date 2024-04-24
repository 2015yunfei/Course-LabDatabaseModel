import tkinter as tk
from tkinter import messagebox
from pymysql.err import Error
import pymysql.cursors
import ConnectToMySql as Con
import Debug
import SqlCreate as Cre
import SqlModify as Mod
import SqlSelect
import func


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

    result = {}
    flag = False

    def get_student_info():
        # 获取查询结果
        nonlocal result  # 声明result为非局部变量
        nonlocal flag

        Sno = Sno_entry.get()

        if flag:
            for var in labels.values():
                var.set("")
            flag = False

        if not (func.check_single(connect, student=True, Sno=Sno)):
            messagebox.showerror("错误", "学生表中不存在学号为：%s的学生" % Sno)
            return

        # 编写SQL查询语句
        query = "SELECT Sname, Ssex, Sage, Sdept, Scholarship FROM Student WHERE Sno = %s"

        try:
            # 执行查询
            cursor = connect.cursor()
            cursor.execute(query, (Sno,))
            result = cursor.fetchone()
        except Error as e:
            messagebox.showerror("数据库错误", f"获得学生信息时发生错误：{str(e)}")

        flag = True

        if Debug.debug_mod == 1:
            print(result)

    def update_label():
        nonlocal result  # 声明result为非局部变量
        nonlocal flag

        if not flag:
            return
        else:
            # 如果bool变量为True，则更新显示组件中的内容
            if flag:
                for key, value in result.items():
                    if key in labels:
                        labels[key].set(value)

    # 按照学号查询
    modify_sno = tk.Button(window, text="按照学号查询", command=lambda: [get_student_info(), update_label()],
                           width="25", height="2")
    modify_sno.pack()

    print("no1")

    # 创建字典存储标签和对应的字符串变量
    labels = {
        'Sname': tk.StringVar(),
        'Ssex': tk.StringVar(),
        'Sage': tk.StringVar(),
        'Sdept': tk.StringVar(),
        'Scholarship': tk.StringVar()
    }

    # 创建标签和对应的显示组件
    for i, (key, var) in enumerate(labels.items()):
        # 创建标签
        label = tk.Label(window, text=key + ":")
        label.pack()

        # 创建显示组件
        entry = tk.Entry(window, textvariable=var, state='readonly')
        entry.pack()

    # 启动Tkinter事件循环
    window.mainloop()
