import tkinter

mainWindow = tkinter.Tk()

label1 = tkinter.Label(mainWindow, text="Selamat Datang label1")
label2 = tkinter.Label(mainWindow, text="Selamat Datang label2")

tombol1 = tkinter.Button(mainWindow, text="Pencet1",background="red")
tombol2 = tkinter.Button(mainWindow, text="Pencet2",background="yellow")

# method positioning
label1.pack()
label2.pack()
tombol1.pack()
tombol2.pack()

# method menampilkan GUI
mainWindow.mainloop()