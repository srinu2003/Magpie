import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
# import ttkbootstrap as ttk
from symmetric_encryption import *


def browse_files() -> None:
    filename = filedialog.askopenfilename(initialdir="/", title="Select a File",
                                          filetypes=(("Text files", "*.txt*"), ("all files", "*.*")))

    # Change label contents


def take_text():
    text = entry.get()
    greeting_label.config(text=f"Hello, {text}!")


# app
app = tk.Tk()
app.title("Magpie")
# app.geometry("300x150") # for 730p 'ish screens
app.geometry('400x600')
app.minsize(width=350, height=500)

# label
greeting_label = ttk.Label(app, text="Welcome to")
greeting_label.pack()

# title
title_label = ttk.Label(app, text='CHAT Encrypter', font='calibre 24 bold')
title_label.pack()

# top entry field
top_text_field = tk.Text(app, width=50, height=10, background='light blue')  # widget

top_text_field.pack(side='top', expand=True, fill='both', padx=10, pady=10)

# input Frame 
key_frame = ttk.Frame(app)
key_lable = ttk.Label(key_frame, text="Enter your KEY:")
key_lable.pack(side='left', pady=0)

entry = ttk.Entry(key_frame, show=u"\u25CF", width=32)  # ,textvariable='hellll')
entry.pack(side='left', padx=10)

key_frame.pack(pady=10, side='top',fill='x')

# Radio button field
radio_frame = ttk.Frame(app, relief = tk.GROOVE, padding = 10)
radio_bool = tk.BooleanVar(value=True)
file_frame = ttk.Frame(app, relief = tk.GROOVE, padding = 10)

debug_mode = True

def radio_func():
    print(radio_bool.get())
    if debug_mode:
        if radio_bool.get():
            print('Encrypt Selected')
        else:
            print('Decrypt Selected')

# widgets
encrypt_radio = ttk.Radiobutton( radio_frame, 
    text = 'Encrypt', 
    value = True, 
    command = radio_func, 
    variable = radio_bool).pack(side='left',fill='y', padx = 20)

decrypt_radio = ttk.Radiobutton( radio_frame, 
	text = 'Decrypt', 
	value = False, 
	command = radio_func, 
	variable = radio_bool).pack(side='left',fill='y', padx= 20)

# radio_frame.pack(fill='x', pady=10, side='top')
radio_frame.pack(side='left')

open_file_button = ttk.Button(file_frame, text='Open File', command=browse_files).pack(side="top", padx=10, pady = 10)
save_file_button = ttk.Button(file_frame, text='Save File', command=browse_files).pack(side="top", padx=10, pady = 10)
file_frame.pack(fill='x', pady=10, side='right')

# Output field
output_lable = ttk.Label(app, text='output', font='calibri 24', textvariable='str')

# bottom entry field
bottom_text_field = tk.Text(app, width=50, height=10, background='light yellow')  # widget
# bottom_text_field.pack(fill='x',padx=5,pady=2)
bottom_text_field.pack(side='top', expand=True, fill='both', padx=10, pady=10)

top = 5
bottom = 5
output_lable.pack(side='top', pady=[top, bottom])

# Start the main event loop
app.mainloop()
