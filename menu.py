from tkinter import *
def open_page(root):
    menu_window = Toplevel(root)
    menu_window.title("Menu")
    menu_window.geometry("400x650")
    Label(menu_window , text= "Our Menu" , font = ("calibri", 30, "bold") ,  bg="lightgray").pack(fill = "x")
    drinks = [
        "1. Cola - $2",
        "2. Orange Juice - $3",
        "3. Lemonade - $2",
        "4. Coffee - $4",
        "5. Tea - $3",
        "6. Milkshake - $5",
        "7. Water - $1",
        "8. Energy Drink - $4",
        "9. Smoothie - $6",
        "10. Hot Chocolate - $4"
    ]
    for item in drinks:
        Label(menu_window, text=item, font=("calibri", 20)).pack(pady=5)

    Button(menu_window, text="Close", font=("calibri", 18),bg = "red", command=menu_window.destroy).pack(pady=20)



