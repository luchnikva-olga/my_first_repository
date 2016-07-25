import tkinter

def print_hello (event):
    print ('Hello')
    print (event)

root=tkinter.Tk()
button=tkinter.Button(root, text="Button")
button.bind("<Button-1>",print_hello)
button.pack()
root.mainloop()

