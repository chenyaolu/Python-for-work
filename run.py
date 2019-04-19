from test import writetoxlsx, timenow, name
import tkinter.messagebox


if __name__ == "__main__":
     # start = time.perf_counter()
     writetoxlsx()
     tkinter.messagebox.showinfo('提示', '文件已写入！')
     # elapsed = (time.perf_counter() - start)
     # print("Time used:", elapsed)

