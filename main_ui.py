import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar  # 日期選擇器，這個要另外安裝套件
import time  # 產生今天日期用的
from c_chat import c_chat_z as c_chat_z

def today_yyyymmdd():  # 日期參數後面可能會常常用到，先做成函式。
    year = time.localtime().tm_year
    month = time.localtime().tm_mon
    day = time.localtime().tm_mday
    return year, month, day

def day_choose(event):  # 如果要做成按鈕，記得把event刪掉
    global date_inp
    def insert_day():
        date_inp.delete(0, 'end')  # 插入日期資料前，先刪掉本來的資料
        selected_date = cal.selection_get()
        formatted_date = selected_date.strftime('%Y-%m-%d')
        date_inp.insert(0, formatted_date)  # 插入日期選擇器資料
        top.destroy()  # 最後把彈出式視窗關掉
    top = tk.Toplevel(window)  # 彈出式視窗
    # 日期選擇器，日期帶入預設今天日期
    cal = Calendar(top, font="10", selectmode='day',
                   cursor="hand1", year=today_yyyymmdd()[0], month=today_yyyymmdd()[1], day=today_yyyymmdd()[2])
    cal.pack(fill="both", expand=True)
    ttk.Button(top, text="ok", command=insert_day).pack()

# -*- Window -*-
window = tk.Tk()
window.title('ptt analysis')  # Title
window.geometry('300x160')  # Window size

# Create the first entry widget for input
label1 = tk.Label(window, text="關鍵字")
label1.grid(row=0, column=0)  # Position label in row 0, column 0
entry1 = tk.Entry(window)
entry1.grid(row=0, column=1)  # Position entry next to the label

# Label and Entry for Date Selection
label2 = tk.Label(window, text="截止日")
label2.grid(row=1, column=0)  # Position label in row 1, column 0

date_inp = tk.Entry(window)
date_inp.grid(row=1, column=1)  # Position entry next to the label
date_inp.insert(0, f"{today_yyyymmdd()[0]}-{today_yyyymmdd()[1]:02d}-{today_yyyymmdd()[2]:02d}")  # 預設今天日期
date_inp.bind('<1>', day_choose)  # 點選文字欄彈出日期選擇器

# Checkbox for Value 3
check_var = tk.IntVar()  # Variable to store the state of the checkbox
checkbox = tk.Checkbutton(window, text="只要出現關鍵字就搜尋", variable=check_var)
checkbox.grid(row=2, column=0, columnspan=2)  # Position the checkbox

# Function to handle button click
def handle_button_click():
    print()
    # Get the values from the entry widgets
    value1 = entry1.get().lower()
    value2 = date_inp.get().lower()
    # Determine the value of value3 based on the checkbox
    if check_var.get() == 1:
        value3 = "include all" 
    else:
        value3 = "title only"
    
    c_chat_z(value1, value2, value3)

# Button to trigger the action
bt1 = tk.Button(window, text='Analyze', command=handle_button_click)
bt1.grid(row=3, column=0, columnspan=2)

window.mainloop()
