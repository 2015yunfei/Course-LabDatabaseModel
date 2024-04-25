from pymysql.err import Error
from tkinter import messagebox


def check_single(connect, sc=False, student=False, course=False, Sno=None, Cno=None):
    # 检查查询个数
    if int(sc) + int(student) + int(course) != 1:
        messagebox.showerror("一次只能查询一个基本表")
        return False

    cursor = connect.cursor()
    query = ""

    if course:
        # 查询course中是否存在指定的Cno
        query = "SELECT EXISTS(SELECT 1 FROM course WHERE Cno = %s)" % Cno
        try:
            cursor.execute(query)
        except Error as e:
            connect.rollback()
            messagebox.showerror("数据库错误", f"查询时发生错误：{str(e)}")
    elif sc:
        # 查询sc中是否存在指定的Sno和Cno
        query = "SELECT EXISTS(SELECT 1 FROM sc WHERE Cno = %s AND Sno = %s)" % (Cno, Sno)
        try:
            cursor.execute(query)
        except Error as e:
            connect.rollback()
            messagebox.showerror("数据库错误", f"查询时发生错误：{str(e)}")
    elif student:
        # 查询student中是否存在指定的Sno
        query = "SELECT EXISTS(SELECT 1 FROM student WHERE Sno = %s)" % Sno
        try:
            cursor.execute(query)
        except Error as e:
            connect.rollback()
            messagebox.showerror("数据库错误", f"查询时发生错误：{str(e)}")
    # 获取查询结果
    result = cursor.fetchone()

    # 获取键的值，如果键不存在，则返回一个False
    key = query[7:]
    value = result.get(key, None)
    if value is None:
        return False

    # 如果键存在则返回True
    if result[key]:
        return True
    else:
        return False


def check_sc(connect, Sno, Cno):
    if not check_single(connect, student=True, Sno=Sno):
        messagebox.showerror("错误", "学号为：%s 的学生不存在" % Sno)
        return False
    if not check_single(connect, course=True, Cno=Cno):
        messagebox.showerror("错误", "课程号为：%s 的课程不存在" % Cno)
        return False

    query = "SELECT EXISTS(SELECT 1 FROM sc WHERE Sno = %s AND Cno = %s)" % (Sno, Cno)
    cursor = connect.cursor()
    try:
        cursor.execute(query)
    except Error as e:
        connect.rollback()
        messagebox.showerror("数据库错误", f"查询时发生错误：{str(e)}")

    # 获取查询结果
    result = cursor.fetchone()

    # 获取键的值，如果键不存在，则返回一个False
    key = query[7:]
    value = result.get(key, None)
    if value is None:
        return False

    # 如果键存在则返回True
    if result[key]:
        return True
    else:
        return False


def close_window(root):
    # 销毁当前窗口
    root.destroy()
