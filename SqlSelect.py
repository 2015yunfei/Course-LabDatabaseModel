import pymysql.cursors
import tkinter as tk
from tkinter import messagebox
import func


def get_student_info(Sno_entry, connect):
    # 编写SQL查询语句
    sql = "SELECT Sname, Ssex, Sage, Sdept, Scholarship FROM Student WHERE Sno = %s"
