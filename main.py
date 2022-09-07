from tkinter import *
tk = Tk()
def lunch():
    import os
    os.system('python3 serveur.py')
def take():
    global a
    a = entry.get()
    print(a)
entry = Entry(tk)
button = Button(tk,command=take,text='ok')
b = Button(tk,text='test',command=lunch)
b.pack()
entry.pack()
button.pack()
tk.mainloop()
print('cc')