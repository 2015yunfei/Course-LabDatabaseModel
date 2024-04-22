import pymysql.cursors
import tkinter as tk
from tkinter import messagebox


def check(connect, sc=False, student=False, course=False, Sno=None, Cno=None):
    # 检查查询个数
    if int(sc) + int(student) + int(course) != 1:
        messagebox.showerror("一次只能查询一个基本表")
        return False

    cursor = connect.cursor()
    query = ""
    if course:
        # 构造更新语句
        query = "SELECT EXISTS(SELECT 1 FROM course WHERE Cno = %s)" % Cno
        # 执行查询
        cursor.execute(query)
    if sc:
        # 构造更新语句
        query = "SELECT EXISTS(SELECT 1 FROM sc WHERE Cno = %s AND Sno = %s)" % (Cno, Sno)
        # 执行查询
        cursor.execute(query)
    if student:
        # 构造更新语句
        query = "SELECT EXISTS(SELECT 1 FROM student WHERE Sno = %s)" % Sno
        # 执行查询
        cursor.execute(query)

    # 获取查询结果
    result = cursor.fetchone()
    # print(result)

    # 获取键的值，如果键不存在，则返回一个默认值
    key = query[7:]
    value = result.get(key, None)
    if value is None:
        return False

    # 如果键存在则查询值
    if result[key]:
        return True
    else:
        return False


def close_window(root):
    # 销毁当前窗口
    root.destroy()
