
from tkinter import filedialog #importing module which helps us to open files
import tkinter as tk
from tkcalendar import DateEntry

def update(*args):
    date_label.config(text="Selected date is "+date_var.get())

def select_file(): #creating function to open file
    selected_file = filedialog.askopenfilename() #using function to allow users to select file and store it in variable
    print("Selected file:", selected_file)#printing the selected file for confirmation

root = tk.Tk()
root.title("Training Program")
root.geometry("500x500")

root.configure(bg='skyblue')

label1 = tk.Label(root, text="Smart Attendance System", font=("Courier New", 24), bg="blue", fg="white")
label1.pack(padx=10,pady=10)

date_label = tk.Label(root, text="Select Date:",font=("Courier New", 10), bg="skyblue")
date_label.pack(pady=5)

date_var = tk.StringVar()

date_entry = DateEntry(root,relief="sunken",borderwidth=3,justify="center",state="normal",selectbackground="blue",textvariable=date_var)
date_entry.pack(pady=5)

date_var.trace('w', update)

#call the function using command
button1 = tk.Button(root, text="Select Excel File",width=20,height=2,bg="#B4A3D8",activebackground="grey",activeforeground="white",command=select_file)
button1.config(highlightbackground = "black",highlightthickness=3)
button1.pack(pady=10)

button2=tk.Button(root,text="Upload Photo",width=20,height=2,bg="#B4A3D8",activebackground="grey",activeforeground="white")
button2.config(highlightbackground = "black",highlightthickness=3)
button2.pack(pady=10)

text_widget = tk.Text(root,width=50,height=5,spacing1=5,spacing2=5,spacing3=5,state="disabled")

text_widget.pack(pady=10)

submit=tk.Button(root,text="Submit",width=20,height=2,bg="black",fg="white",activebackground="blue",activeforeground="white")
submit.pack(pady=10)

root.mainloop()


1.1.py
Displaying 1.1.py.# Write your code here :-)
