import pymysql.cursors


def connect():
    # 数据库连接参数
    host = '47.94.173.36'
    port = 3306
    user = '2015yunfei'
    password = 'u202112032'
    db = 'cse_qyf'
    charset = 'utf8mb4'

    # 创建连接
    connection = pymysql.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        db=db,
        charset=charset,
        cursorclass=pymysql.cursors.DictCursor)

    return connection


def check_table_exists(connection, table_name):
    """
    检查表是否存在。

    :param connection: pymysql.connect对象，已建立数据库连接。
    :param table_name: 要检查的表名。
    :return: 如果表存在，返回True；否则返回False。
    """
    with connection.cursor() as cursor:
        # 使用INFORMATION_SCHEMA.TABLES查询表是否存在
        cursor.execute("SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = %s", (table_name,))
        # 如果查询结果不为空，则表存在
        if cursor.fetchone():
            return True
        else:
            return False


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
            print("student 表创建成功")

            # 创建 course 表
            cursor.execute(create_course_table)
            print("course 表创建成功")

            # 创建 sc 表
            cursor.execute(create_sc_table)
            print("sc 表创建成功")

        # 提交更改
        connection.commit()

    except pymysql.err.IntegrityError as e:
        print("数据库错误：", e)

    except pymysql.err.OperationalError as e:
        print("数据库错误：", e)


# 级联删除三个表的函数
def cascade_delete_tables(connection):
    try:
        # 首先删除sc表中的记录
        with connection.cursor() as cursor:
            cursor.execute("DROP TABLE IF EXISTS sc")

        # 提交更改
        connection.commit()

        # 然后删除course表中的记录
        with connection.cursor() as cursor:
            cursor.execute("DROP TABLE IF EXISTS course")

        # 提交更改
        connection.commit()

        # 最后删除student表中的记录
        with connection.cursor() as cursor:
            cursor.execute("DROP TABLE IF EXISTS student")

        # 提交更改
        connection.commit()

        print("所有表的记录已级联删除。")

    except pymysql.Error as e:
        print(f"数据库错误：{e}")
    # finally:
    # 关闭连接
    # connection.close()
