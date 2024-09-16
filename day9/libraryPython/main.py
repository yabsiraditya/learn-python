import datetime

dataWaktu = datetime.datetime.now()
print(f"Datetime Now : {dataWaktu}")
print(f"Tahun : {dataWaktu.year}")
print(f"Hari : {dataWaktu.strftime('%A')}")

from collections import Counter

data = ["a","b","c","d","e","a","c","d","a"]

# count = 0
# for i in data:
#     if i == "a":
#         count += 1

# print(count)

dataCount = Counter(data)

print(f"data count = {dataCount}")
print(f"data count a = {dataCount['a']}")
print(f"data count b = {dataCount['b']}")
print(f"data count c = {dataCount['c']}")
print(f"data count d = {dataCount['d']}")
print(f"data count e = {dataCount['e']}")

import io 

file = io.open("fileText.txt","r")
print(file.read())

# from tkinter import *
# from tkinter import ttk
# root = Tk()
# frm = ttk.Frame(root, padding=10)
# frm.grid()
# ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
# root.mainloop()