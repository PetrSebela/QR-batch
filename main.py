import tkinter as tk
from tkinter import Button, ttk,filedialog
from tkinter.constants import END

import qrcode
import qr


class MainApplication():
    def __init__(self,master):
        self.master = master
        master.geometry('500x500')
        self.location = ''

        #export setting
        self.button = []
        names = ['from:','to:']
        self.f = ttk.Labelframe(master,text='generate qr code')

        for x in names:
            self.button.append([])
            self.button[len(self.button)-1].append(ttk.Label(self.f,text=x))
            self.button[len(self.button)-1].append(ttk.Entry(self.f))

        self.f.pack(pady=(10,0))
        for cnt,x in enumerate(self.button, start=1):
            x[0].grid(column=cnt,row=1)
            x[1].grid(column=cnt,row=2,pady=(0,10),padx=10)


        #export location
        def chooseFile():
            self.location = filedialog.askdirectory()
            self.folderWrite.delete(0,END)
            self.folderWrite.insert(0,self.location)
            print(self.location)

        self.location = ttk.LabelFrame(master,text='location')

        self.folderWrite = ttk.Entry(self.location,width=30)
        self.folderChoose = ttk.Button(self.location,text='choose file',command=chooseFile)

        self.folderWrite.grid(column=1,row=0,padx=10,pady=10)
        self.folderChoose.grid(column=2,row=0,padx=10,pady=10)

        self.location.pack(pady=10)

        #export button
        def export():
            print(self.location)
            if type(self.location) == str:
                print(self.location)
                qr.generate(int(self.button[0][1].get()),int(self.button[1][1].get()),self.location)

        self.generate = ttk.Button(text='generate batch',command=export)
        self.generate.pack()



if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root)
    root.mainloop()