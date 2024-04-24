import tkinter as tk
from tkinter import messagebox
from pymysql.err import Error
from tkinter import ttk
import pymysql.cursors
import Debug
import func


def view_grades(root, connect):
    # 创建主窗口
    window = tk.Toplevel(root)  # 这里使用root作为父窗口
    window.title("查询学生成绩")
    window.geometry("800x800")  # 设置窗口大小
    window.grab_set()

    result = {}

    def select_stu_by_dept():
        nonlocal result

        # 编写SQL查询语句
        query = "SELECT " \
                "   s.Sdept," \
                "   AVG(sc.Grade) AS average_grade," \
                "   MAX(sc.Grade) AS highest_grade," \
                "   MIN(sc.Grade) AS lowest_grade," \
                "   SUM(CASE WHEN sc.Grade >= 90 THEN 1 ELSE 0 END) * 100.0 / COUNT(*) AS excellence_rate," \
                "   SUM(CASE WHEN sc.Grade < 60 THEN 1 ELSE 0 END) AS failing_count " \
                "FROM" \
                "   student s " \
                "JOIN" \
                "   sc ON s.Sno = sc.Sno " \
                "GROUP BY" \
                "   s.Sdept;"

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

    select_stu_by_dept()

    # 创建一个Treeview控件
    tree = ttk.Treeview(window, columns=(
        "Sdept", "average_grade", "highest_grade", "lowest_grade", "excellence_rate", "failing_count"), show='headings')
    tree.pack(expand=True, fill='both')

    # 设置列标题
    tree.heading("Sdept", text="院系")
    tree.heading("average_grade", text="平均成绩")
    tree.heading("highest_grade", text="最高成绩")
    tree.heading("lowest_grade", text="最低成绩")
    tree.heading("excellence_rate", text="优秀率")
    tree.heading("failing_count", text="不及格人数")

    # 设置列宽
    tree.column("Sdept", width=100)
    tree.column("average_grade", width=100)
    tree.column("highest_grade", width=100)
    tree.column("lowest_grade", width=100)
    tree.column("excellence_rate", width=100)
    tree.column("failing_count", width=100)

    # 添加查询结果到Treeview控件
    for row in result:
        tree.insert('', 'end', values=(
            row['Sdept'], row['average_grade'], row['highest_grade'], row['lowest_grade'],
            "{:.2f}".format(row['excellence_rate']), row['failing_count']))

    # 启动Tkinter事件循环
    window.mainloop()
