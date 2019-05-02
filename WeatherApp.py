import tkinter as tk

root = tk.Tk()
root.resizable(False, False)

def test(entry):
    print(entry)

canvas = tk.Canvas(root,height = 700, width = 800)
canvas.pack()

background_image = tk.PhotoImage(file="background.png")
background_label = tk.Label(root, image = background_image)
background_label.place(relwidth=1,relheight=1)

frame = tk.Frame(root, bg = "#80c1ff", bd = 5)
frame.place(relx=0.5,rely=0.1,relwidth = 0.75, relheight = 0.1, anchor="n")

entry = tk.Entry(frame, bg = "white")
entry.place(relwidth = 0.65,relheight=1)

button =  tk.Button(frame, text = "Button", bg = "purple", fg = "white" , command = lambda: test(entry.get()))
button.place(relx=0.7,relheight=1,relwidth = 0.3)

lower_frame = tk.Frame(root, bg = "#80c1ff", bd = 10)
lower_frame.place(relx = 0.5, rely=0.25, relwidth = 0.75, relheight = 0.6, anchor = "n")

label = tk.Label(lower_frame, text="", bg="white")
label.place(relwidth=1,relheight=1)

root.mainloop()