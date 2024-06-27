 import tkinter as tk
from tkcalendar import DateEntry

root = tk.Tk()
root.title("Training Program")
root.geometry("500x300")

root.configure(bg='skyblue')

label1 = tk.Label(root, text="Smart Attendance System", font=("Courier New", 24),
bg="blue", fg="white")
label1.pack(padx=10,pady=10)

date_label = tk.Label(root, text="Select Date:",font=("Courier New", 10),
bg="skyblue")
date_label.pack(pady=5)

# Define a StringVar to hold the selected date
date_var = tk.StringVar()

date_entry = DateEntry(root,relief="sunken",borderwidth=3,justify="center",
state="normal",selectbackground="blue",textvariable=date_var)
#bidirectional data binding: changes in the widget are reflected in
#variable and vice versa. This is used to store the date selected by the user
date_entry.pack(pady=5)

button1 = tk.Button(root, text="Select Excel File",width=20,height=2,
bg="#B4A3D8",activebackground="grey",activeforeground="white")
button1.config(highlightbackground = "black",highlightthickness=3)
button1.pack(pady=10)

button2=tk.Button(root,text="Upload Photo",width=20,height=2,bg="#B4A3D8",
activebackground="grey",activeforeground="white")
button2.config(highlightbackground = "black",highlightthickness=3)
button2.pack(pady=10)

submit=tk.Button(root,text="Submit",width=20,height=2,bg="black",
fg="white",activebackground="blue",activeforeground="white")
submit.pack(pady=10)

root.mainloop()
