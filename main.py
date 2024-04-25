import MainWindows as Win
import ConnectToMySql as Cno

# 连接到数据库
connection = Cno.connect()

# 创建界面实例
gui = Win.create_gui(connection)

# 在主界面运行后立即执行do_after_gui_runs函数
gui.after(0, Win.do_after_gui_runs(gui, connection))

# 启动界面
gui.mainloop()
