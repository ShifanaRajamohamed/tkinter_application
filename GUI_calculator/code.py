import tkinter as tk
def on_click(number):
    entry.insert(tk.END,number)

def clear():
    entry.delete(0,tk.END)
def calculate():
    result=eval(entry.get())
    entry.delete(0,tk,END)
    entry.insert(tk.END,result)
root=tk.Tk()
root.title("Calculator")
entry=tk.Entry(root,width=20,font=("Arial",18))
entry.grid(row=0,column=0,columnspan=4)
btn=[('7',1,0),('8',1,1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
]
for text,row,col in btn:
    if text == "=":
        btn=tk.Button(root,text=text,font=("Arial",14),width=5,height=2,command=calculate)
    elif text=="C":
        btn = tk.Button(root, text=text, font=("Arial", 14), width=5, height=2, command=clear)
    else:
        btn = tk.Button(root, text=text, font=("Arial", 14), width=5, height=2, command=lambda t=text: on_click(t))
    btn.grid(row=row, column=col, padx=5, pady=5)

root.mainloop()
