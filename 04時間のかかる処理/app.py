import tkinter as tk
import time
import threading


def heavy1():
    print("重い処理開始")
    time.sleep(5)
    print("重く処理終了")


def heavy2():
    thread1 = threading.Thread(target=heavy1)
    thread1.start()


root = tk.Tk()

root.title("テスト")
root.geometry("300x150+500+200")

# ウィジェット
button1 = tk.Button(root, text="重い処理で固まる", command=heavy1)
button2 = tk.Button(root, text="重い処理でも固まらない", command=heavy2)

# 配置
button1.grid(row=0, column=0, padx=5, pady=5)
button2.grid(row=0, column=1, padx=5, pady=5)


root.mainloop()
