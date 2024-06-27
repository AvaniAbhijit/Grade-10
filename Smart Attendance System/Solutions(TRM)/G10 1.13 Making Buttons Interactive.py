import tkinter as tk
from tkcalendar import DateEntry

def update(): #creating a function to update the date label
  slabel.config(text="Text Updated") #changing the text of the label using config()

root = tk.Tk()
root.title("Training Program")
root.geometry("500x300")

root.configure(bg='skyblue')

label1 = tk.Label(root, text="Smart Attendance System", font=("Courier New", 24), bg="blue", fg="white")
label1.pack(padx=10,pady=10)

date_label = tk.Label(root, text="Select Date:",font=("Courier New", 10), bg="skyblue")
date_label.pack(pady=5)

date_var = tk.StringVar()

date_entry = DateEntry(root,relief="sunken",borderwidth=3,
justify="center",state="normal",selectbackground="blue",validate="focus",validatecommand=update)
date_entry.pack(pady=5)

button1 = tk.Button(root, text="Select Excel File",width=20,height=2,bg="#B4A3D8",
activebackground="grey",activeforeground="white")
button1.config(highlightbackground = "black",highlightthickness=3)
button1.pack(pady=10)

button2=tk.Button(root,text="Upload Photo",width=20,height=2,bg="#B4A3D8",
activebackground="grey",activeforeground="white")
button2.config(highlightbackground = "black",highlightthickness=3)
button2.pack(pady=10)

submit=tk.Button(root,text="Submit",width=20,height=2,bg="black",fg="white",
activebackground="blue",activeforeground="white",command=update)
#calling the function using command to update the label
submit.pack(pady=10)

#adding a label to display the updated text.
slabel=tk.Label(root)
slabel.pack()

root.mainloop()


















