import Debug
from pymysql.err import Error
from tkinter import messagebox


def delete_course_not_in_sc(connect):
    cursor = connect.cursor()
    find_sql = "SELECT course.Cno FROM course WHERE NOT EXISTS (SELECT 1 FROM sc WHERE sc.Cno = course.Cno)"
    try:
        cursor.execute(find_sql)
    except Error as e:
        messagebox.showerror("数据库错误", f"寻找不在sc表中的课程时发生错误：{str(e)}")
        return

    result = cursor.fetchall()
    if result is None:
        messagebox.showinfo("提示", "所有没有选课信息的课程信息已经被删除")
        return

    delete_sql = "DELETE FROM course WHERE NOT EXISTS (SELECT 1 FROM sc WHERE sc.Cno = course.Cno);"
    try:
        cursor.execute(delete_sql)
        connect.commit()
    except Error as e:
        connect.rollback()
        messagebox.showerror("数据库错误", f"删除没有选课信息的课程时发生错误：{str(e)}")
        return

    if Debug.debug_mod == 1:
        for row in result:
            print(row['Cno'])

    if result:
        # 将多个记录转换为字符串
        records_str = ""
        records_str = records_str.join(str("\t" + row['Cno'] + "\n") for row in result)
        records_str = "以下课程已经删除(Cno)：\n" + records_str

        messagebox.showinfo("提示", records_str)
    else:
        messagebox.showinfo("提示", "没有任何课程被删除")
