import tkinter as tk
from tkinter import Button, ttk,filedialog
from tkinter.constants import END

import qrcode
import qr
#commit test

class MainApplication():
    def __init__(self,master):
        self.master = master
        master.geometry('')
        master.resizable(False,False)
        self.location = ''

        #row setting
        self.button = []
        names = ['from:','to:']
        self.f = ttk.Labelframe(text='generate qr code')

        for x in names:
            self.button.append([])
            self.button[len(self.button)-1].append(ttk.Label(self.f,text=x))
            self.button[len(self.button)-1].append(ttk.Entry(self.f))

        self.f.pack(pady=(10,0))
        for cnt,x in enumerate(self.button, start=1):
            x[0].grid(column=cnt,row=1)
            x[1].grid(column=cnt,row=2,pady=(0,10),padx=10)

        #picture size

        self.size = ttk.LabelFrame(master,text='size')
        self.sizeInput = ttk.Entry(self.size)
        self.sizeLabel = ttk.Label(self.size,text='qr code size:')
        self.size.pack()
        self.sizeLabel.grid(column=0,row=0,padx=10,pady=5)
        self.sizeInput.grid(column=1,row=0,padx=10,pady=10)

        #export location
        def chooseFile():
            self.location = filedialog.askdirectory()
            self.folderWrite.delete(0,END)
            self.folderWrite.insert(0,self.location)
            print(self.location)

        self.location = ttk.LabelFrame(text='location')

        self.folderWrite = ttk.Entry(self.location,width=30)
        self.folderChoose = ttk.Button(self.location,text='choose file',command=chooseFile)

        self.folderWrite.grid(column=1,row=0,padx=10,pady=10)
        self.folderChoose.grid(column=2,row=0,padx=10,pady=10)

        self.location.pack(pady=10,padx=10)

        #export button
        def export():
            print(self.location)
            if type(self.location) == str:
                exportList = qr.generate(int(self.button[0][1].get()),int(self.button[1][1].get()))
                for each in exportList:
                    qr.createQR(each,self.folderWrite.get(),int(self.sizeInput.get()))

        self.generate = ttk.Button(text='generate batch',command=export)
        self.generate.pack(pady=10)



if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root)
    root.mainloop()