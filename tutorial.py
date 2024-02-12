import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
# import ttkbootstrap as ttk

def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("Text files","*.txt*"),("all files","*.*")))
      
    # Change label contents

def take_text():
    text = entry.get()
    greeting_label.config(text=f"Hello, {text}!")


# app
app = tk.Tk()
app.title("APP NAME")
# app.geometry("300x150") # for 730p 'ish screens
app.geometry('400x600')
app.minsize(width= 350,height= 500)

#lable
greeting_label = ttk.Label(app, text="Welcome to")
greeting_label.pack()

#title
title_lable = ttk.Label(app,text='CHAT DECRYPTION', font='calibri 24 bold')
title_lable.pack()

# top enetry field
top_text_field = tk.Text(app,width=50,height=10, background='light blue') #widget
# top_text_field.pack(fill='x',padx=5,pady=2)
top_text_field.pack(side = 'top', expand = True, fill = 'both', padx = 10, pady = 10)

# key Frame 
key_frame = ttk.Frame(app)

key_lable = ttk.Label(key_frame, text="Enter your KEY:")
key_lable.pack(side='left',pady=0)

entry = ttk.Entry(key_frame,show=u"\u25CF",width=32)#,textvariable='hellll')
entry.pack(side='left',padx=10)

key_frame.pack(pady=10,side='top')

# Button field
button_frame = ttk.Frame(app, borderwidth= 100,border= 10,relief= tk.RIDGE)

encrypt_button = ttk.Button(button_frame, text= 'Encrypt',command = lambda : print('Encrypt Presed')).pack(side='left',padx=10)
decrypt_button = ttk.Button(button_frame, text= 'Decrypt',command = browseFiles).pack(side='left',padx=10)

button_frame.pack()
# Output field
output_lable = ttk.Label(app,text='output', font='calibri 24',textvariable='sinu')

# bottom enetry field
botttom_text_field = tk.Text(app,width=50,height=10, background = 'light yellow') #widget
# botttom_text_field.pack(fill='x',padx=5,pady=2)
botttom_text_field.pack(side = 'top', expand = True, fill = 'both', padx = 10, pady = 10)

top = 5
botttom = 5
output_lable.pack(side = 'top',pady=[top,botttom])

# Start the main event loop
app.mainloop()
