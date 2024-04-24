import tkinter as tk
from tkinter import messagebox
from pymysql.err import Error
from tkinter import ttk
import pymysql.cursors
import Debug
import func


def view_ranking(root, connect):
    # 创建主窗口
    window = tk.Toplevel(root)  # 这里使用root作为父窗口
    window.title("查询学生成绩")
    window.geometry("800x800")  # 设置窗口大小
    window.grab_set()

    result = {}

    def select_stu_by_dept_order():
        nonlocal result

        # 编写SQL查询语句
        query = "SELECT s.Sno,s.Sname,s.Sdept,c.Cno,c.Cname,sc.Grade,c.Cname,c.Cpno,c.Ccredit FROM student s JOIN sc " \
                "ON s.Sno = sc.Sno JOIN course c ON sc.Cno = c.Cno ORDER BY s.Sdept,sc.Grade DESC;"

        if Debug.debug_mod == 1:
            print(query)

        try:
            # 执行查询
            cursor = connect.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
        except Error as e:
            messagebox.showerror("数据库错误", f"获得学生成绩时发生错误：{str(e)}")

        if Debug.debug_mod == 1:
            for row in result:
                print(row)

    select_stu_by_dept_order()

    # 创建一个Treeview控件
    tree = ttk.Treeview(window, columns=(
        "Sdept", "Sno", "Sname", "Cno", "Grade", "Cname", "Cpno", "Ccredit"), show='headings')
    tree.pack(expand=True, fill='both')

    # 设置列标题
    tree.heading("Sdept", text="院系")
    tree.heading("Sno", text="学号")
    tree.heading("Sname", text="学生姓名")
    tree.heading("Cno", text="课程号")
    tree.heading("Grade", text="成绩")
    tree.heading("Cname", text="课程名称")
    tree.heading("Cpno", text="该课程先修课的课程号")
    tree.heading("Ccredit", text="课程学分")

    # 设置列宽
    tree.column("Sdept", width=100)
    tree.column("Sno", width=100)
    tree.column("Sname", width=100)
    tree.column("Cno", width=100)
    tree.column("Grade", width=100)
    tree.column("Cname", width=100)
    tree.column("Cpno", width=130)
    tree.column("Ccredit", width=70)

    # 添加查询结果到Treeview控件
    for row in result:
        tree.insert('', 'end', values=(
            row['Sdept'], row['Sno'], row['Sname'], row['Cno'],
            row['Grade'], row['Cname'], row['Cpno'], row['Ccredit']))

    # 启动Tkinter事件循环
    window.mainloop()
