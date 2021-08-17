from tkinter import *
from PIL import Image, ImageTk
from resizeCanvas import ResizingCanvas
from playsound import playsound
root = Tk()
root.resizable(False,False)
root.title('Duck')
playsound('joke.mp3', block=False)

canvas = ResizingCanvas(root, width = 500, height = 500)
canvas.pack()
def handle_configure(event):
	global img, imag  
	w, h = root.winfo_height(), root.winfo_width()
	img = Image.open("vit.jpg")
	img = img.resize((w,h), Image.ANTIALIAS)
	imag = ImageTk.PhotoImage(img)
	canvas.create_image(w/2,h/2, image=imag)
root.bind("<Configure>", handle_configure)
mainloop()