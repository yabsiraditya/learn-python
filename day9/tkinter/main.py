# GUI -> Graphical User Interface

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

window = tk.Tk()
window.configure(bg="white")
window.geometry("400x300")
window.resizable(False,False)
window.title("Sapa Dia")

namaBelakang = tk.StringVar()
namaDepan = tk.StringVar()

def btnClick():
    pesan = f"Hallo {namaDepan.get()} {namaBelakang.get()} Gantenggg!"
    showinfo(title="Sapa Dia!",message=pesan)


# Frame Iput
inputFrame = ttk.Frame(window)
# Penempatan Grid, Pack, Place
inputFrame.pack(padx=10,pady=10,fill="x",expand=True)

# Components
# 1. Label Nama Depan
namaLabelDepan = ttk.Label(inputFrame,text="Nama Depan")
namaLabelDepan.pack(padx=10,fill="x",expand=True)

# 2. Entry Nama Depan
namaDepanEntry = ttk.Entry(inputFrame,textvariable=namaDepan)
namaDepanEntry.pack(padx=10,fill="x",expand=True)

# 3. Label Nama Belakang
namaLabelBelakang = ttk.Label(inputFrame,text="Nama Belakang")
namaLabelBelakang.pack(padx=10,fill="x",expand=True)

# 4. Entry Nama Belakang
namaBelakangEntry = ttk.Entry(inputFrame,textvariable=namaBelakang)
namaBelakangEntry.pack(padx=10,fill="x",expand=True)

# 5. Button
sapaButton = ttk.Button(inputFrame,text="Sapa!",command=btnClick)
sapaButton.pack(fill="x",expand=True,padx=10,pady=10)

window.mainloop()