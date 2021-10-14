import Tkinter as Tk

root = Tk.Tk()

def submit():

    print ("entered text were ") + entry.get()
entry = Tk.Entry(root)
entry.pack()
button = Tk.Button(root,text='Start Calculation:',command=submit)
button.pack()

root.mainloop()
