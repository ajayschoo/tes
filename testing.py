import tkinter as tk
from PIL import ImageTk

window = tk.Tk()
window.title('testing img')
imagse = ImageTk.PhotoImage(file= "images/lol.jpg")
x = tk.Label(window, image= imagse)
x.pack()
window.mainloop()