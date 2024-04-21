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


def Create_3_table(connection):
    # 创建表的SQL语句
    create_student_table = """
    CREATE TABLE IF NOT EXISTS student (
        id INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(50) NOT NULL,
        age INT,
        gender VARCHAR(10)
    );
    """

    create_sc_table = """
    CREATE TABLE IF NOT EXISTS sc (
        student_id INT,
        course_id INT,
        grade INT
    );
    """

    create_course_table = """
    CREATE TABLE IF NOT EXISTS course (
        id INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(50) NOT NULL,
        teacher VARCHAR(50)
    );
    """

    # 执行创建表的命令
    try:
        with connection.cursor() as cursor:
            cursor.execute(create_student_table)
            cursor.execute(create_sc_table)
            cursor.execute(create_course_table)
        # 提交更改
        connection.commit()
    except pymysql.Error as e:
        print(f"数据库错误：{e}")
    # finally:


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
