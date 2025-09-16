from tkinter import *

def open_page(root):
    order_window = Toplevel(root)
    order_window.title("Menu")
    order_window.geometry("400x650")
    Label(order_window, text="Enter Your Order", font=("calibri", 30, "bold"), bg="lightgray").pack(fill="x")

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
    prices = [2, 3, 2, 4, 3, 5, 1, 4, 6, 4]

    # Frame to contain the list with a grid layout
    list_frame = Frame(order_window)
    list_frame.pack(padx=10, pady=8, fill="both", expand=True)

    # Header row
    Label(list_frame, text="Item", font=("calibri", 12, "bold")).grid(row=0, column=0, sticky="w", padx=4)
    Label(list_frame, text="Price", font=("calibri", 12, "bold")).grid(row=0, column=1, padx=4)
    Label(list_frame, text="Qty", font=("calibri", 12, "bold")).grid(row=0, column=2, padx=4)
    Label(list_frame, text="Cost", font=("calibri", 12, "bold")).grid(row=0, column=3, padx=4)

    qty_vars = []
    cost_labels = []
    item_costs = [0] * len(drinks)

    def update_cost(index):
        s = qty_vars[index].get().strip()
        try:
            qty = int(s) if s != "" else 0
            if qty < 0:
                qty = 0
        except ValueError:
            qty = 0
        cost = prices[index] * qty
        item_costs[index] = cost
        cost_labels[index].config(text=f"${cost:.2f}")
        total_var.set(f"Total: ${sum(item_costs):.2f}")

    # create each row with labels, entry and cost
    # Start enumerating at 1 so row 1 is the first item (row 0 is header)
    for row_index, item_text in enumerate(drinks, start=1):
        Label(list_frame, text=item_text, font=("calibri", 11)).grid(row=row_index, column=0, sticky="w", pady=6)
        Label(list_frame, text=f"${prices[row_index-1]}", font=("calibri", 11)).grid(row=row_index, column=1, padx=6)

        v = StringVar(value="0")
        qty_vars.append(v)
        ent = Entry(list_frame, textvariable=v, width=4, font=("calibri", 11))
        ent.grid(row=row_index, column=2, padx=6)

        cost_lbl = Label(list_frame, text="$0.00", font=("calibri", 11))
        cost_lbl.grid(row=row_index, column=3, padx=6)
        cost_labels.append(cost_lbl)

        # capture the correct index using the row_index-1 value at definition time
        idx = row_index - 1
        v.trace_add("write", lambda *a, idx=idx: update_cost(idx))
        ent.bind("<FocusOut>", lambda ev, idx=idx: update_cost(idx))

    # Total and buttons
    total_var = StringVar(value="Total: $0.00")
    total_label = Label(order_window, textvariable=total_var, font=("calibri", 16, "bold"))
    total_label.pack(pady=8)

    def confirm_order():
        order = []
        for idx in range(len(drinks)):
            try:
                qty = int(qty_vars[idx].get().strip() or 0)
            except ValueError:
                qty = 0
            if qty > 0:
                order.append((drinks[idx], prices[idx], qty, item_costs[idx]))
        summary = Toplevel(order_window)
        summary.title("Order Summary")
        summary.geometry("350x300")
        Label(summary, text="Order Summary", font=("calibri", 18, "bold")).pack(fill="x")
        if not order:
            Label(summary, text="No items selected.", font=("calibri", 12)).pack(pady=10)
        else:
            for it, pr, q, c in order:
                Label(summary, text=f"{q} x {it.split('. ',1)[1]} = ${c:.2f}", font=("calibri", 12)).pack(anchor="w", padx=10)
            Label(summary, text=total_var.get(), font=("calibri", 14, "bold")).pack(pady=10)
        Button(summary, text="Close", command=summary.destroy).pack(pady=10)

    btn_frame = Frame(order_window)
    btn_frame.pack(pady=6)
    Button(btn_frame, text="Confirm Order", font=("calibri", 12), bg="#4CAF50", fg="white", command=confirm_order).grid(row=0, column=0, padx=8)
    Button(btn_frame, text="Close", font=("calibri", 12), bg="red", fg="white", command=order_window.destroy).grid(row=0, column=1, padx=8)

    # initial compute (in case defaults changed)
    for i in range(len(drinks)):
        update_cost(i)
