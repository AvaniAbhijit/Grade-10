import tkinter as tk

root = tk.Tk()
root.title("Training Program")
root.geometry("500x300")

# Set the background color to blue
root.configure(bg='skyblue')


label1 = tk.Label(root, text="Smart Attendance System", font=("Courier New", 24), bg="blue", fg="white") #changing the font style and adding foreground color(fg) and background color(bg)
"""List of font-style available
1. Arial
2. Times New Roman
3. Comic Sans MS
4. Courier New
5. Impact
6. Georgia
7. Lexend (
8. Comfortaa"""
label1.pack()

button1 = tk.Button(root, text="Select Excel File")
button1.pack()

root.mainloop()
