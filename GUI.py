import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

from symmetric_encryption import *


def browse_files() -> None:
    filename = filedialog.askopenfilename(initialdir = "/", title="Select a File",
                                          filetypes = (("Text files", "*.txt*"), ("all files", "*.*")))
    
    # Open file
    with open(filename+'.txt', 'r') as file:
        print(top_text_field.get('1.0', 'end-1c'))
        top_text_field.delete('1.0', 'end')
        top_text = file.read()
        top_text_field.insert('1.0', top_text)
        print(top_text_field.get('1.0', 'end-1c'))
    print(filename)


def save_file() -> None:
    filename = filedialog.asksaveasfilename(initialdir = "/", title="Select a File",
                                          filetypes = (("Text files", "*.txt*"), ("all files", "*.*")))
    
    # Open file
    with open(filename+'txt', 'w') as file:
        file.write(bottom_text_field.get('1.0', 'end-1c'))
    print(filename)



# def take_text():
#     print(top_text_field.get('1.0', 'end-1c'))
#     print(key.get())
#     print(radio_bool.get())
    
#     if radio_bool.get():
#         print('Encrypt Selected')
#         if key.get() == '':
#             key.set(generate_key())
#             print('Key Generated')
#         else:
#             print('Key Provided')
#         print(encrypt_message(top_text_field.get('1.0', 'end-1c'), key.get()))
        

def clear_key() -> None:
    print(key.get())
    # take_text()
    key.set('')

# app
app = tk.Tk()
app.title("Magpie")
# app.geometry("300x150") # for 730p 'ish screens
app.geometry('550x500')
app.minsize(width=450, height=500)



# VARIABLES
top_text = tk.StringVar()
bottom_text = tk.StringVar()
key = tk.StringVar()
radio_bool = tk.BooleanVar(value=True)

# label
greeting_label = ttk.Label(app, text="Welcome to")
greeting_label.pack()

# title
title_label = ttk.Label(app, text='TEXT Encrypter', font='calibre 24 bold')
title_label.pack(side='top')

input_lable = ttk.Label(app, text="Enter your text:")
input_lable.pack(side='top', fill='x', padx=(10, 0))

# top entry field
top_text_field = tk.Text(app, width=50, height=5, background='light blue')
top_text_field.pack(side='top', expand=True, fill='both', padx=10, pady=5)

# key Frame
key_frame = ttk.Frame(app)

key_lable = ttk.Label(key_frame, text="Enter your KEY:")
key_lable.pack(side='left', pady=0)

key_entry = ttk.Entry(key_frame, show=u"\u25CF", width=32, textvariable=key)
key_entry.pack(side='left', padx=10)

key_clear_button: object = ttk.Button(key_frame, text='Clear Key', command=clear_key)
key_clear_button.pack()

key_frame.pack(pady=10, side='top')

# Options Frame
options_frame = ttk.Frame(app, relief=tk.GROOVE, padding=(10, 5))

# Radio button field
radio_frame = ttk.Frame(options_frame, relief=tk.GROOVE, padding=10)

debug_mode = True


def radio_func():
    print(radio_bool.get())
    if debug_mode:
        if radio_bool.get():
            print('Encrypt Selected')
        else:
            print('Decrypt Selected')


# options
encrypt_radio = (ttk.Radiobutton(radio_frame,
                                 text='Encrypt',
                                 value=True,
                                 command=radio_func,
                                 variable=radio_bool)
                 .pack(side='left', fill='y', padx=20))

decrypt_radio = (ttk.Radiobutton(radio_frame,
                                 text='Decrypt',
                                 value=False,
                                 command=radio_func,
                                 variable=radio_bool)
                 .pack(side='left', fill='y', padx=20))

radio_frame.pack(side='left')

# convert button
convert_button = ttk.Button(options_frame, text='Convert')
convert_button.pack(side='left', padx=(10, 10))

options_frame.pack(side='top', pady=10)

file_frame = ttk.Frame(options_frame, relief=tk.GROOVE, padding=5)

open_file_button = (ttk.Button(file_frame, text='Open File', command=browse_files).
                    pack(side="top", pady=5))
save_file_button = (ttk.Button(file_frame, text='Save Text', command=save_file).
                    pack(side="top", pady=5))

file_frame.pack(expand=True, fill='x', pady=10, side='right')

output_lable = (ttk.Label(app, text="Your Output:").
                pack(side='top', fill='x', padx=(10, 0)))
# Output field

# bottom entry field
bottom_text_field = tk.Text(app, width=50, height=5, background='light yellow')
bottom_text_field.pack(side='top', expand=True, fill='both', padx=10, pady=5)

credits_label = (ttk.Label(app, text="Made by: Magpie", font='calibre 10 bold').
                 pack(side='bottom', pady=10))

# Start the main event loop
app.mainloop()
