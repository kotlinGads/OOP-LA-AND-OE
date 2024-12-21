import tkinter as tk


root = tk.Tk()
root.title("OOP OE #8")
root.geometry("800x600")
root.configure(bg="white")

pangalan = tk.Entry(root)
pangalan.grid(row=0, column=0, padx=20)

counter = 1 
def iprint_moto():
    global counter
    print(f"{counter}. {pangalan.get()}")
    counter +=1

button_print = tk.Button(root, text="Print", command=iprint_moto)
button_print.grid(row=0, column=1, padx=20, pady=20)
    
root.mainloop()