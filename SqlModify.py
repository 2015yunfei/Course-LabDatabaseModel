import pymysql.cursors
import tkinter as tk
from tkinter import messagebox
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
    if not func.check(connect, course=True, Cno=Cno):
        messagebox.showerror("错误", "课程号不存在")
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
            messagebox.showinfo("成功", "已修改课程号为：%s 的课程信息Cname" % Cno)

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
            messagebox.showinfo("成功", "已修改课程号为：%s 的课程信息Cpno" % Cno)

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
            messagebox.showinfo("成功", "已修改课程号为：%s 的课程信息Ccredit" % Cno)

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

    if not func.check(connect, student=True, Sno=Sno):
        messagebox.showerror("错误", "学号不存在")
    else:
        # 将数据更新到数据库中
        if Sname:
            try:
                cursor = connect.cursor()
                cursor.execute("UPDATE student SET Sname = %s WHERE Sno = %s", (Sname, Sno))
                connect.commit()
            except pymysql.err.IntegrityError as e:
                # 捕获IntegrityError异常
                messagebox.showerror("数据库错误", f"更新学生信息时发生错误：{str(e)}")
            except pymysql.err.ProgrammingError as e:
                # 捕获ProgrammingError异常
                messagebox.showerror("数据库错误", f"更新学生信息时发生错误：{str(e)}")
            except pymysql.err.InternalError as e:
                # 捕获InternalError异常
                messagebox.showerror("数据库错误", f"更新学生信息时发生错误：{str(e)}")
            except pymysql.err.OperationalError as e:
                # 捕获OperationalError异常
                messagebox.showerror("数据库错误", f"更新学生信息时发生错误：{str(e)}")
            finally:
                messagebox.showinfo("成功", "已修改学号为：%s 的学生信息Sname" % Sno)
        if Ssex:
            try:
                cursor = connect.cursor()
                cursor.execute("UPDATE student SET Ssex = %s WHERE Sno = %s", (Ssex, Sno))
                connect.commit()
            except pymysql.err.IntegrityError as e:
                # 捕获IntegrityError异常
                messagebox.showerror("数据库错误", f"更新学生信息时发生错误：{str(e)}")
            except pymysql.err.ProgrammingError as e:
                # 捕获ProgrammingError异常
                messagebox.showerror("数据库错误", f"更新学生信息时发生错误：{str(e)}")
            except pymysql.err.InternalError as e:
                # 捕获InternalError异常
                messagebox.showerror("数据库错误", f"更新学生信息时发生错误：{str(e)}")
            except pymysql.err.OperationalError as e:
                # 捕获OperationalError异常
                messagebox.showerror("数据库错误", f"更新学生信息时发生错误：{str(e)}")
            finally:
                messagebox.showinfo("成功", "已修改学号为：%s 的学生信息Ssex" % Sno)
        if Sage:
            try:
                cursor = connect.cursor()
                cursor.execute("UPDATE student SET Sage = %s WHERE Sno = %s", (Sage, Sno))
                connect.commit()
            except pymysql.err.IntegrityError as e:
                # 捕获IntegrityError异常
                messagebox.showerror("数据库错误", f"更新学生信息时发生错误：{str(e)}")
            except pymysql.err.ProgrammingError as e:
                # 捕获ProgrammingError异常
                messagebox.showerror("数据库错误", f"更新学生信息时发生错误：{str(e)}")
            except pymysql.err.InternalError as e:
                # 捕获InternalError异常
                messagebox.showerror("数据库错误", f"更新学生信息时发生错误：{str(e)}")
            except pymysql.err.OperationalError as e:
                # 捕获OperationalError异常
                messagebox.showerror("数据库错误", f"更新学生信息时发生错误：{str(e)}")
            finally:
                messagebox.showinfo("成功", "已修改学号为：%s 的学生信息Sage" % Sno)
        if Sdept:
            try:
                cursor = connect.cursor()
                cursor.execute("UPDATE student SET Sdept = %s WHERE Sno = %s", (Sdept, Sno))
                connect.commit()
            except pymysql.err.IntegrityError as e:
                # 捕获IntegrityError异常
                messagebox.showerror("数据库错误", f"更新学生信息时发生错误：{str(e)}")
            except pymysql.err.ProgrammingError as e:
                # 捕获ProgrammingError异常
                messagebox.showerror("数据库错误", f"更新学生信息时发生错误：{str(e)}")
            except pymysql.err.InternalError as e:
                # 捕获InternalError异常
                messagebox.showerror("数据库错误", f"更新学生信息时发生错误：{str(e)}")
            except pymysql.err.OperationalError as e:
                # 捕获OperationalError异常
                messagebox.showerror("数据库错误", f"更新学生信息时发生错误：{str(e)}")
            finally:
                messagebox.showinfo("成功", "已修改学号为：%s 的学生信息Sdept" % Sno)
        if Scholarship:
            try:
                cursor = connect.cursor()
                cursor.execute("UPDATE student SET Scholarship = %s WHERE Sno = %s", (Scholarship, Sno))
                connect.commit()
            except pymysql.err.IntegrityError as e:
                # 捕获IntegrityError异常
                messagebox.showerror("数据库错误", f"更新学生信息时发生错误：{str(e)}")
            except pymysql.err.ProgrammingError as e:
                # 捕获ProgrammingError异常
                messagebox.showerror("数据库错误", f"更新学生信息时发生错误：{str(e)}")
            except pymysql.err.InternalError as e:
                # 捕获InternalError异常
                messagebox.showerror("数据库错误", f"更新学生信息时发生错误：{str(e)}")
            except pymysql.err.OperationalError as e:
                # 捕获OperationalError异常
                messagebox.showerror("数据库错误", f"更新学生信息时发生错误：{str(e)}")
            finally:
                messagebox.showinfo("成功", "已修改学号为：%s 的学生信息Scholarship" % Sno)

        # 清空输入框
        sno_entry.delete(0, tk.END)
        sname_entry.delete(0, tk.END)
        ssex_entry.delete(0, tk.END)
        sage_entry.delete(0, tk.END)
        sdept_entry.delete(0, tk.END)
        scholarship_entry.delete(0, tk.END)


def modify_stu_grade_sno():
    pass
