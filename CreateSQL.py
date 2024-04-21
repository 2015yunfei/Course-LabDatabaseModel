import pymysql.cursors
import tkinter as tk
from tkinter import messagebox


def add_student(sno_entry, sname_entry, ssex_entry, sage_entry, sdept_entry, scholarship_entry, connect):
    # 获取输入框的内容
    Sno = sno_entry.get()
    Sname = sname_entry.get()
    Ssex = ssex_entry.get()
    Sage = sage_entry.get()
    Sdept = sdept_entry.get()
    Scholarship = scholarship_entry.get()

    # 检查主键是否为空
    if not Sno:
        messagebox.showerror("错误", "学号不能为空")
        return

    # 检查年龄是否为数字
    if Sage and not Sage.isdigit():
        messagebox.showerror("错误", "年龄必须是数字")
        return

    # 这里可以添加将数据插入到数据库的逻辑
    try:
        cursor = connect.cursor()
        cursor.execute(
            "INSERT INTO student (Sno, Sname, Ssex, Sage, Sdept, Scholarship) VALUES (%s, %s, %s, %s, %s, %s)",
            (Sno, Sname, Ssex if Ssex else None, Sage if Sage else None, Sdept if Sdept else None,
             Scholarship if Scholarship else None))
        connect.commit()
    except pymysql.cursors.connector.Error as e:
        messagebox.showerror("数据库错误", str(e))
        return

    # 清空输入框
    sno_entry.delete(0, tk.END)
    sname_entry.delete(0, tk.END)
    ssex_entry.delete(0, tk.END)
    sage_entry.delete(0, tk.END)
    sdept_entry.delete(0, tk.END)
    scholarship_entry.delete(0, tk.END)

    messagebox.showinfo("成功", "新生信息已添加")


def add_course(Cno_entry, Cname_entry, Cpno_entry, Ccredit_entry, connect):
    # 获取输入框的内容
    Cno = Cno_entry.get()
    Cname = Cname_entry.get()
    Cpno = Cpno_entry.get()
    Ccredit = Ccredit_entry.get()

    # 检查主键是否为空
    if not Cno:
        messagebox.showerror("错误", "课程编号不能为空")
        return

    # 检查学分是否为数字
    if Ccredit and not Ccredit.isdigit():
        messagebox.showerror("错误", "学分必须是数字")
        return

    # 将数据插入到数据库中
    try:
        cursor = connect.cursor()
        cursor.execute("INSERT INTO course (Cno, Cname, Cpno, Ccredit) VALUES (%s, %s, %s, %s)",
                       (Cno, Cname, Cpno if Cpno else None, Ccredit if Ccredit else None))
        connect.commit()
    except pymysql.err.IntegrityError as e:
        messagebox.showerror("数据库错误", str(e))
        return

    # 清空输入框
    Cno_entry.delete(0, tk.END)
    Cname_entry.delete(0, tk.END)
    Cpno_entry.delete(0, tk.END)
    Ccredit_entry.delete(0, tk.END)

    messagebox.showinfo("成功", "课程信息已添加")


def modify_course(Cno_entry, Cname_entry, Cpno_entry, Ccredit_entry, connect):
    # 获取输入框的内容
    Cno = Cno_entry.get()
    Cname = Cname_entry.get()
    Cpno = Cpno_entry.get()
    Ccredit = Ccredit_entry.get()

    # 检查主键是否为空
    if not Cno:
        messagebox.showerror("错误", "课程编号不能为空")
        return

    # 检查学分是否为数字
    if Ccredit and not Ccredit.isdigit():
        messagebox.showerror("错误", "学分必须是数字")
        return

    # 构造更新语句
    query = "SELECT EXISTS(SELECT 1 FROM course WHERE Cno = %s)"

    # 执行查询
    cursor = connect.cursor()
    cursor.execute(query, (Cno,))

    # 获取查询结果
    result = cursor.fetchone()

    # 检查记录是否存在
    key = 'EXISTS(SELECT 1 FROM course WHERE Cno = \'%s\')' % Cno
    if not result[key]:
        messagebox.showerror("错误", "课程编号不存在")
        return

    # 将数据插入到数据库中
    if Cname:
        try:
            cursor = connect.cursor()
            cursor.execute("UPDATE Course SET Cname = %s WHERE Cno = %s", (Cname, Cno))
            connect.commit()
        except pymysql.err.IntegrityError as e:
            # 捕获IntegrityError异常
            messagebox.showerror("数据库错误", f"更新课程信息时发生错误：{str(e)}")
        except pymysql.err.ProgrammingError as e:
            # 捕获ProgrammingError异常
            messagebox.showerror("数据库错误", f"更新课程信息时发生错误：{str(e)}")
        except pymysql.err.InternalError as e:
            # 捕获InternalError异常
            messagebox.showerror("数据库错误", f"更新课程信息时发生错误：{str(e)}")
        except pymysql.err.OperationalError as e:
            # 捕获OperationalError异常
            messagebox.showerror("数据库错误", f"更新课程信息时发生错误：{str(e)}")
        finally:
            messagebox.showinfo("成功", "课程信息已修改")

    if Cpno:
        try:
            cursor = connect.cursor()
            cursor.execute("UPDATE Course SET Cpno = %s WHERE Cno = %s", (Cpno, Cno))
            connect.commit()
        except pymysql.err.IntegrityError as e:
            # 捕获IntegrityError异常
            messagebox.showerror("数据库错误", f"更新课程信息时发生错误：{str(e)}")
        except pymysql.err.ProgrammingError as e:
            # 捕获ProgrammingError异常
            messagebox.showerror("数据库错误", f"更新课程信息时发生错误：{str(e)}")
        except pymysql.err.InternalError as e:
            # 捕获InternalError异常
            messagebox.showerror("数据库错误", f"更新课程信息时发生错误：{str(e)}")
        except pymysql.err.OperationalError as e:
            # 捕获OperationalError异常
            messagebox.showerror("数据库错误", f"更新课程信息时发生错误：{str(e)}")
        finally:
            messagebox.showinfo("成功", "课程信息已修改")

    if Ccredit:
        try:
            cursor = connect.cursor()
            cursor.execute("UPDATE Course SET Ccredit = %s WHERE Cno = %s", (Ccredit, Cno))
            connect.commit()
        except pymysql.err.IntegrityError as e:
            # 捕获IntegrityError异常
            messagebox.showerror("数据库错误", f"更新课程信息时发生错误：{str(e)}")
        except pymysql.err.ProgrammingError as e:
            # 捕获ProgrammingError异常
            messagebox.showerror("数据库错误", f"更新课程信息时发生错误：{str(e)}")
        except pymysql.err.InternalError as e:
            # 捕获InternalError异常
            messagebox.showerror("数据库错误", f"更新课程信息时发生错误：{str(e)}")
        except pymysql.err.OperationalError as e:
            # 捕获OperationalError异常
            messagebox.showerror("数据库错误", f"更新课程信息时发生错误：{str(e)}")
        finally:
            messagebox.showinfo("成功", "课程信息已修改")

    # 清空输入框
    Cno_entry.delete(0, tk.END)
    Cname_entry.delete(0, tk.END)
    Cpno_entry.delete(0, tk.END)
    Ccredit_entry.delete(0, tk.END)
