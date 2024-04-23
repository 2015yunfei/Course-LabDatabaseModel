import tkinter as tk
import pymysql.cursors
import MainWindows as Win
import ConnectToMySql as Cno


# 连接到数据库
connection = Cno.connect()

# print(Che.check(connection, student=True, Sno=12))

# 创建界面实例
gui = Win.create_gui(connection)

# 在主界面运行后立即执行do_after_gui_runs函数
gui.after(0, Win.do_after_gui_runs(gui, connection))

# 启动界面
gui.mainloop()
