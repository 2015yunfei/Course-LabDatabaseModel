import pymysql.cursors
import Debug
from pymysql.err import Error
from tkinter import messagebox


def connect():
    """

    :return: 返回一个用于sql连接的字段
    """
    # 创建连接
    connection = pymysql.connect(
        host=Debug.host,
        port=Debug.port,
        user=Debug.user,
        password=Debug.password,
        db=Debug.db,
        charset=Debug.charset,
        cursorclass=pymysql.cursors.DictCursor)

    return connection


def check_table_exists(connection, table_name):
    """
    检查表是否存在。

    :param connection: pymysql.connect对象，已建立数据库连接。
    :param table_name: 要检查的表名。
    :return: 如果表存在，返回True；否则返回False。
    """
    try:
        with connection.cursor() as cursor:
            # 使用INFORMATION_SCHEMA.TABLES查询表是否存在
            cursor.execute("SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = %s", (table_name,))
            # 如果查询结果不为空，则表存在
            if cursor.fetchone():
                return True
            else:
                return False
    except Error as e:
        messagebox.showerror("数据库错误", f"检查是否存在旧表时发生错误：{str(e)}")


def create_3_table(connection):
    # 创建表的SQL语句
    create_student_table = """
    CREATE TABLE IF NOT EXISTS student (
        Sno CHAR(20) PRIMARY KEY,
        Sname CHAR(20) UNIQUE,
        Ssex CHAR(8),
        Sage SMALLINT,
        Sdept CHAR(20),
        Scholarship CHAR(20)
    );
    """

    create_course_table = """
    CREATE TABLE IF NOT EXISTS course (
        Cno CHAR(20) PRIMARY KEY,
        Cname CHAR(40),
        Cpno CHAR(20),
        Ccredit SMALLINT,
        FOREIGN KEY (Cpno) REFERENCES course(Cno)
    );
    """

    create_sc_table = """
    CREATE TABLE IF NOT EXISTS sc (
        Sno CHAR(20),
        Cno CHAR(20),
        Grade SMALLINT,
        PRIMARY KEY (Sno, Cno),
        FOREIGN KEY (Sno) REFERENCES student(Sno),
        FOREIGN KEY (Cno) REFERENCES course(Cno)
    );
    """
    try:
        with connection.cursor() as cursor:
            # 创建 student 表
            cursor.execute(create_student_table)
            if Debug.debug_mod == 1:
                print("student 表创建成功")

            # 创建 course 表
            cursor.execute(create_course_table)
            if Debug.debug_mod == 1:
                print("course 表创建成功")

            # 创建 sc 表
            cursor.execute(create_sc_table)
            if Debug.debug_mod == 1:
                print("sc 表创建成功")

            # 提交更改
            connection.commit()

    except Error as e:
        connection.rollback()
        messagebox.showerror("数据库错误", f"创建新表时发生错误：{str(e)}")


def cascade_delete_tables(connection):
    """
    级联删除三个表的函数
    :param connection:
    :return:
    """
    try:
        with connection.cursor() as cursor:
            # 首先删除sc表中的记录
            cursor.execute("DROP TABLE IF EXISTS sc")

            # 提交更改
            connection.commit()

            # 然后删除course表中的记录
            cursor.execute("DROP TABLE IF EXISTS course")

            # 提交更改
            connection.commit()

            # 最后删除student表中的记录
            cursor.execute("DROP TABLE IF EXISTS student")

            # 提交更改
            connection.commit()

        if Debug.debug_mod == 1:
            print("所有表的记录已经级联删除。")

    except Error as e:
        connection.rollback()
        messagebox.showerror("数据库错误", f"删除旧表时发生错误：{str(e)}")


def insert_data(connection):
    """
    插入实验指导书中给出的数据，使用该函数前，确保三个基本表的存在，同时三个基本表内容为空
    :param connection:
    :return:
    """

    sql1 = "insert into student values('200215121','李勇','男',20,'CS','否')"
    sql2 = "insert into student values('200215122','刘晨','女',19,'CS','否')"
    sql3 = "insert into student values('200215123','王敏','女',18,'MA','否')"
    sql4 = "insert into student values('200215125','张立','男',19,'IS','否')"
    sql5 = "INSERT INTO course VALUES ('1', '数据库', NULL, 4)"
    sql6 = "INSERT INTO course VALUES ('2', '数学', NULL, 2)"
    sql7 = "INSERT INTO course VALUES ('3', '信息系统', NULL, 4)"
    sql8 = "INSERT INTO course VALUES ('4', '操作系统', NULL, 3)"
    sql9 = "INSERT INTO course VALUES ('5', '数据结构', NULL, 4)"
    sql10 = "INSERT INTO course VALUES ('6', '数据处理', NULL, 2)"
    sql12 = "INSERT INTO course VALUES ('7', 'java', NULL, 4)"
    sql13 = "UPDATE course SET Cpno = '5' WHERE Cno = '1'"
    sql14 = "UPDATE course SET Cpno = '1' WHERE Cno = '3'"
    sql15 = "UPDATE course SET Cpno = '6' WHERE Cno = '4'"
    sql16 = "UPDATE course SET Cpno = '7' WHERE Cno = '5'"
    sql17 = "UPDATE course SET Cpno = '6' WHERE Cno = '7'"
    sql18 = "INSERT INTO sc VALUES ('200215121', '1', 92)"
    sql19 = "INSERT INTO sc VALUES ('200215121', '2', 85)"
    sql20 = "INSERT INTO sc VALUES ('200215121', '3', 88)"
    sql21 = "INSERT INTO sc VALUES ('200215122', '2', 90)"
    sql22 = "INSERT INTO sc VALUES ('200215122', '3', 80)"

    try:
        with connection.cursor() as cursor:
            cursor.execute(sql1)
            cursor.execute(sql2)
            cursor.execute(sql3)
            cursor.execute(sql4)
            cursor.execute(sql5)
            cursor.execute(sql6)
            cursor.execute(sql7)
            cursor.execute(sql8)
            cursor.execute(sql9)
            cursor.execute(sql10)
            cursor.execute(sql12)
            cursor.execute(sql13)
            cursor.execute(sql14)
            cursor.execute(sql15)
            cursor.execute(sql16)
            cursor.execute(sql17)
            cursor.execute(sql18)
            cursor.execute(sql19)
            cursor.execute(sql20)
            cursor.execute(sql21)
            cursor.execute(sql22)

            # 一次提交，确保原子性
            connection.commit()
    except Error as e:
        connection.rollback()
        messagebox.showerror("数据库错误", f"插入数据时发生错误：{str(e)}")
