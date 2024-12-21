import tkinter as tk

anime_title = "One Piece"

root = tk.Tk()
root.title("OOP")
root.geometry("800x600")

frame = tk.Frame(root)
frame.grid(pady = 20)    

counter = 0
def iprint_moto():
    global counter
    print(f"My Favorite anime {anime_title}")
    counter +=1
    
button = tk.Button(root, text="Print", command=iprint_moto)
button.grid(row=0, column=0, padx=20, pady=20)

               
root.mainloop()