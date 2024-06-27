import tkinter as tk

root = tk.Tk()
root.title("Training Program")
root.geometry("500x300")

root.configure(bg='skyblue')


label1 = tk.Label(root, text="Smart Attendance System", font=("Courier New", 24), bg="blue", fg="white")
label1.pack()

button1 = tk.Button(root, text="Select Excel File",width=20,height=2,bg="#B4A3D8") #defining the width and height of the button in terms of pixels
button1.config(highlightbackground = "black",highlightthickness=3)#adding border around the button and increasing it's thickness
button1.pack()

root.mainloop()
