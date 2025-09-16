from tkinter import *
from menu import *
from New_order import *
root = Tk()
root.geometry("1000x500")
root.title("Bill Mangement")
Label(text="Bill Mangement" , bg = "gray" , fg = "black" , font = ("calibri" , 35) , width='220' , height= "2").pack()
ButtonFrame = Frame(root)
ButtonFrame.pack(pady=50)

#menu 
menu_button = Button(ButtonFrame, text="Menu", font=("calibri", 24 , "bold" ), width=16, height=1,
    bg="#4CAF50", fg="white", activebackground="#45a049", activeforeground="white",  command=lambda: open_page(root))
menu_button.grid(row=0, column=0, padx=30, pady=10)

#new order
new_button = Button(ButtonFrame, text="New Order", font=("calibri", 24 , "bold" ), width=16, height=1,
    bg="#FF9800", fg="white", activebackground="#F57C00", activeforeground="white" , command=lambda: open_page(root))
new_button.grid(row=1, column=0, padx=20, pady=10)

#exit 
ex_button = Button(ButtonFrame, text="Exist", font=("calibri", 24 , "bold" ), width=16, height=1,
    bg="#F44336", fg="white", activebackground="#D32F2F", activeforeground="white",command=root.destroy)
ex_button.grid(row=2, column = 0, padx=20, pady=10)

root.mainloop()
