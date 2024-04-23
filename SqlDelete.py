import Debug
from pymysql.err import Error
import pymysql.cursors
import tkinter as tk
from tkinter import messagebox
import func


def delete_course_not_in_sc(connect):
    cursor = connect.cursor()
    find_sql = "SELECT course.Cno FROM course WHERE NOT EXISTS (SELECT 1 FROM sc WHERE sc.Cno = course.Cno)"
    try:
        cursor.execute(find_sql)
    except Error as err:
        print("Something went wrong: {}".format(err))
        return

    result = cursor.fetchall()

    delete_sql = "DELETE FROM course WHERE NOT EXISTS (SELECT 1 FROM sc WHERE sc.Cno = course.Cno);"
    try:
        cursor.execute(delete_sql)
        connect.commit()
    except Error as err:
        print("Something went wrong: {}".format(err))
        return

    if Debug.Debug == 1:
        for row in result:
            print(row['Cno'])

    if result:
        # 将多个记录转换为字符串
        records_str = ""
        records_str = records_str.join(str("\t" + row['Cno'] + "\n") for row in result)
        records_str = "以下课程已经删除(Cno)：\n" + records_str

        messagebox.showinfo("Records", records_str)
    else:
        messagebox.showinfo("Records", "没有任何课程被删除")
