from pymysql.err import Error
from tkinter import messagebox
import tkinter as tk
import func


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

    # 检查记录是否存在
    if not func.check_single(connect, course=True, Cno=Cno):
        messagebox.showerror("错误", "课程号不存在")
        return

    # 将数据插入到数据库中
    try:
        cursor = connect.cursor()
        if Cname:
            cursor.execute("UPDATE Course SET Cname = %s WHERE Cno = %s", (Cname, Cno))
        if Cpno:
            cursor.execute("UPDATE Course SET Cpno = %s WHERE Cno = %s", (Cpno, Cno))
        if Ccredit:
            cursor.execute("UPDATE Course SET Ccredit = %s WHERE Cno = %s", (Ccredit, Cno))
        connect.commit()
    except Error as e:
        connect.rollback()
        messagebox.showerror("数据库错误", f"更新课程信息时发生错误：{str(e)}")
    finally:
        messagebox.showinfo("成功", "课程信息已经更新")

        # 清空输入框
        Cno_entry.delete(0, tk.END)
        Cname_entry.delete(0, tk.END)
        Cpno_entry.delete(0, tk.END)
        Ccredit_entry.delete(0, tk.END)


def modify_stu_info_sno(sno_entry, sname_entry, ssex_entry, sage_entry, sdept_entry, scholarship_entry, connect):
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

    if not func.check_single(connect, student=True, Sno=Sno):
        messagebox.showerror("错误", "学号不存在")
    else:
        # 将存在更新的部分数据更新到数据库中
        try:
            cursor = connect.cursor()
            if Sname:
                cursor.execute("UPDATE student SET Sname = %s WHERE Sno = %s", (Sname, Sno))
            if Ssex:
                cursor.execute("UPDATE student SET Ssex = %s WHERE Sno = %s", (Ssex, Sno))
            if Sage:
                cursor.execute("UPDATE student SET Sage = %s WHERE Sno = %s", (Sage, Sno))
            if Sdept:
                cursor.execute("UPDATE student SET Sdept = %s WHERE Sno = %s", (Sdept, Sno))
            if Scholarship:
                cursor.execute("UPDATE student SET Scholarship = %s WHERE Sno = %s", (Scholarship, Sno))
            connect.commit()
        except Error as e:
            messagebox.showerror("数据库错误", f"更新学生奖学金信息时发生错误：{str(e)}")
        finally:
            messagebox.showinfo("成功", "学生信息已经更新")

            # 清空输入框
            sno_entry.delete(0, tk.END)
            sname_entry.delete(0, tk.END)
            ssex_entry.delete(0, tk.END)
            sage_entry.delete(0, tk.END)
            sdept_entry.delete(0, tk.END)
            scholarship_entry.delete(0, tk.END)


def modify_stu_grade(sno_entry, cno_entry, grade_entry, connect):
    # 获取输入框的内容
    Sno = sno_entry.get()
    Cno = cno_entry.get()
    Grade = grade_entry.get()

    # 检查主键是否为空
    if not Sno:
        messagebox.showerror("错误", "学号不能为空")
        return
    if not Cno:
        messagebox.showerror("错误", "课程编号不能为空")
        return
    if not Grade:
        messagebox.showerror("错误", "成绩不能为空")
        return

    # 检查记录是否存在
    if not func.check_sc(connect, Sno, Cno):
        messagebox.showerror("错误", "学号为：%s 学生没有课程号为：%s 课程的成绩" % (Sno, Cno))
        return

    try:
        cursor = connect.cursor()
        update_sql = "UPDATE sc SET Grade = %s WHERE Sno = %s AND Cno = %s"
        cursor.execute(update_sql, (Grade, Sno, Cno))
        connect.commit()
    except Error as err:
        connect.rollback()
        messagebox.showinfo("提示", "Something went wrong: {}".format(err))
    finally:
        messagebox.showinfo("成功", "已经将学号为：%s 的学生课程号为：%s 的成绩修改为：%s" % (Sno, Cno, Grade))

        # 清空输入
        sno_entry.delete(0, tk.END)
        cno_entry.delete(0, tk.END)
        grade_entry.delete(0, tk.END)
