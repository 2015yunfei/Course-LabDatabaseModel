import pymysql.cursors
import tkinter as tk
from tkinter import messagebox
import func


# def get_student_info(Sno_entry, connect):
#     Sno = Sno_entry.get()
#     # 编写SQL查询语句
#     query = "SELECT Sname, Ssex, Sage, Sdept, Scholarship FROM Student WHERE Sno = %s"
#
#     # 执行查询
#     cursor = connect.cursor()
#     cursor.execute(query, (Sno,))
#
#     # 获取查询结果
#     result = cursor.fetchone()
#     print(result)
#     return result
