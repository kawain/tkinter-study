# Textウィジェットは、挿入 insert() 値の取得 get() 削除　delete()
import tkinter as tk
import tkinter.scrolledtext as st


def print_display():
    print("【タイトル】")
    print(buff1.get())
    buff1.set("")

    print("【内容】")
    print(st1.get("1.0", "end -1c"))
    st1.delete("1.0", "end")


root = tk.Tk()

root.option_add("*Font", "Consolas 12")
root.title("テスト")
root.geometry("400x300+500+200")

buff1 = tk.StringVar()
buff1.set("")

# ウィジェット
label1 = tk.Label(root, text="タイトル")
entry1 = tk.Entry(root, width=32, textvariable=buff1)

label2 = tk.Label(root, text="内容")
st1 = st.ScrolledText(root, width=30, height=5)

button1 = tk.Button(root, text="クリック", command=print_display)

# 配置
label1.grid(row=0, column=1, pady=10, sticky="")
entry1.grid(row=0, column=2)

label2.grid(row=1, column=1, pady=10, sticky="N")
st1.grid(row=1, column=2)

button1.grid(row=2, column=2, sticky="EW")


root.mainloop()
