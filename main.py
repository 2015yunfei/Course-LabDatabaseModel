import tkinter as tk
import pymysql.cursors
import Windows as win
import ConnectToMySql as con

# 连接到数据库
connection = con.connect()

# 创建界面实例
gui = win.create_gui(connection)

# 在主界面运行后立即执行do_after_gui_runs函数
gui.after(0, win.do_after_gui_runs(gui, connection))

# 启动界面
gui.mainloop()

# import tkinter as tk
#
# # 定义一个全局变量来引用Tkinter的root窗口
# root = None
#
# def create_window():
#     # 创建主窗口
#     global root
#     root = tk.Tk()
#     root.title("三个基本表已存在")
#
#     # 在窗口中添加一个标签，显示文本“三个基本表已经存在”
#     label = tk.Label(root, text="三个基本表已经存在")
#     label.pack()
#
#     # 创建一个关闭按钮，点击时调用close_window函数
#     close_button = tk.Button(root, text="关闭", command=close_window)
#     close_button.pack(side="bottom", anchor="s")  # 按钮放置在窗口底部
#
#     # 启动事件循环，使窗口保持打开状态
#     root.mainloop()
#
# def close_window():
#     # 销毁当前窗口
#     root.destroy()
#
# # 调用函数以创建窗口
# create_window()
