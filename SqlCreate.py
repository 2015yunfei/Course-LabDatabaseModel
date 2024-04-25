import tkinter as tk
from tkinter import messagebox
import func
from pymysql.err import Error


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

    # 检查记录是否存在
    if func.check_single(connect, student=True, Sno=Sno):
        messagebox.showerror("错误", "学号已经存在，插入失败！")
    else:
        # 这里可以添加将数据插入到数据库的逻辑
        try:
            cursor = connect.cursor()
            cursor.execute(
                "INSERT INTO student (Sno, Sname, Ssex, Sage, Sdept, Scholarship) VALUES (%s, %s, %s, %s, %s, %s)",
                (Sno, Sname, Ssex if Ssex else None, Sage if Sage else None, Sdept if Sdept else None,
                 Scholarship if Scholarship else None))
            connect.commit()
        except Error as e:
            connect.rollback()
            messagebox.showerror("数据库错误", f"插入数据时发生错误：{str(e)}")
        finally:
            messagebox.showinfo("成功", "已经插入学号为：%s 的学生信息" % Sno)

            # 清空输入框
            sno_entry.delete(0, tk.END)
            sname_entry.delete(0, tk.END)
            ssex_entry.delete(0, tk.END)
            sage_entry.delete(0, tk.END)
            sdept_entry.delete(0, tk.END)
            scholarship_entry.delete(0, tk.END)


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

    # 检查记录是否存在
    if func.check_single(connect, course=True, Cno=Cno):
        messagebox.showerror("错误", "课程号已经存在，插入失败！")
    else:
        # 将数据插入到数据库中
        try:
            cursor = connect.cursor()
            cursor.execute("INSERT INTO course (Cno, Cname, Cpno, Ccredit) VALUES (%s, %s, %s, %s)",
                           (Cno, Cname, Cpno if Cpno else None, Ccredit if Ccredit else None))
            connect.commit()
        except Error as e:
            connect.rollback()
            messagebox.showerror("数据库错误", f"插入数据时发生错误：{str(e)}")
        finally:
            messagebox.showinfo("成功", "已经添加课程号为：%s 的课程信息" % Cno)

            # 清空输入框
            Cno_entry.delete(0, tk.END)
            Cname_entry.delete(0, tk.END)
            Cpno_entry.delete(0, tk.END)
            Ccredit_entry.delete(0, tk.END)


def add_grades(Sno_entry, Cno_entry, Grade_entry, connect):
    Sno = Sno_entry.get()
    Cno = Cno_entry.get()
    Grade = Grade_entry.get()

    # 检查主键是否为空
    if not Sno:
        messagebox.showerror("错误", "学号不能为空")
        return

    # 检查主键是否为空
    if not Cno:
        messagebox.showerror("错误", "课程号不能为空")
        return

    # 检查记录是否存在
    if func.check_single(connect, sc=True, Sno=Sno, Cno=Cno):
        messagebox.showerror("错误", "学号为%s的学生成绩已经存在已经存在，插入失败！" % Sno)
    else:
        # 将数据插入到数据库中
        try:
            cursor = connect.cursor()
            cursor.execute("INSERT INTO sc (Sno, Cno, Grade) VALUES (%s, %s, %s)",
                           (Sno, Cno, Grade if Grade else None))
            connect.commit()
        except Error as e:
            connect.rollback()
            messagebox.showerror("数据库错误", f"插入数据时发生错误：{str(e)}")
        finally:
            messagebox.showinfo("成功", "已经添加学号为：%s 的学生成绩\n课程号：%s\n成绩：%s" % (Sno, Cno, Grade))

            # 清空输入框
            Sno_entry.delete(0, tk.END)
            Cno_entry.delete(0, tk.END)
            Grade_entry.delete(0, tk.END)
