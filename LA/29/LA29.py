import tkinter as tk

your_name = "DAVID PAUL"
your_section = "BSIT -2A"

root = tk.Tk()
root.title("OOP")
root.geometry("800x600")

frame = tk.Frame(root)
frame.pack(pady = 20)

label = tk.Label(frame, text= f"OOP LA#29 {your_name} {your_section}")
label.grid(row=0, column=0, padx=10, pady=10)
               
root.mainloop()