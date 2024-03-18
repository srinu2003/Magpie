import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from symmetric_encryption import generate_key, load_key, encrypt_message, decrypt_message, InvalidToken, BinasciiError



def browse_files() -> None:
    try:
        filename = filedialog.askopenfilename(initialdir = "/", title="Select a File",
                                          filetypes = (("Text files", "*.txt*"), ("all files", "*.*")))

        # Open and read file
        with open(filename, 'r') as file:
            print(top_text_field.get('1.0', 'end-1c'))
            top_text_field.delete('1.0', 'end')
            top_text = file.read()
            top_text_field.insert('1.0', top_text)
            print(top_text_field.get('1.0', 'end-1c'))
        print(filename)
    except FileNotFoundError:
        print('No file selected')
        return None


def save_file() -> None:
    filename = filedialog.asksaveasfilename(initialdir="/", title="Save File",
                                            filetypes=(("Text files", "*.txt*"), ("all files", "*.*")))
    
    if filename.partition('.')[2] != 'txt':
        # C:\\users\tsrin\downloaded_files\test.txt.csv
        if filename.partition('.')[2] == '':
            filename += '.txt'
        else:
            filename = filename.partition('.')[0] + '.txt'

    # Open and write file
    with open(filename, 'w') as file:
        file.write(bottom_text_field.get('1.0', 'end-1c'))
    
    print(filename)



def convert_text() -> None:
    top_text = top_text_field.get('1.0', 'end-1c')
    print(top_text)
    bottom_text = bottom_text_field.get('1.0', 'end-1c')
    print(bottom_text)
    print(key.get())
    print(radio_bool.get())
    
    if radio_bool.get():
        # TO DO: Complete the encrypt function and also the decrypt function
        if top_text_field.get('1.0', 'end-1c') == '':
            return None
        if key.get() == '':
            key.set(generate_key().decode())
            print('Key Generated')

        _key = key.get()
        plain_text = top_text_field.get('1.0', 'end-1c')
        cipher_text = encrypt_message(plain_text, _key.encode())

        bottom_text_field.delete('1.0', 'end')
        bottom_text_field.insert('1.0', cipher_text)
        
        print(cipher_text)
    else:
        print('Decrypt Selected')
        if key.get() == '':
            key.set(load_key().decode())
            print('Key Loaded')

        _key = key.get()
        cipher_text = top_text_field.get('1.0', 'end-1c')

        # Extract the decrypted message from the result based on its type
        plain_text = decrypt_message(cipher_text, _key.encode())
        
        # Check the type of the decrypted message
        if isinstance(plain_text, str):
            # Insert the decrypted message as a string
            bottom_text_field.delete('1.0', 'end')
            bottom_text_field.insert('1.0', plain_text)
        elif isinstance(plain_text, InvalidToken):
            print('Invalid Token error occurred')
            # Handle InvalidToken error
        elif isinstance(plain_text, Exception):
            print('Exception occurred during decryption')
            # Handle other exceptions
        elif isinstance(plain_text, BinasciiError):
            print('Binascii Error occurred')
            # Handle BinasciiError
        else:
            print('Unknown error occurred')
            # Handle other unknown errors
        print(plain_text)
        

def clear_key() -> None:
    print(key.get())
    key.set('')
    # convert_text()

def get_key() -> None:
    key.set(load_key().decode())


# app
app = tk.Tk()
app.title("Magpie")
# app.geometry("300x150") # for 730p 'ish screens
app.geometry('550x500')
app.minsize(width=500, height=500)



# VARIABLES
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
top_text_field = tk.Text(app, width=50, height=5, background='light blue', wrap='word')
top_text_field.pack(side='top', expand=True, fill='both', padx=10, pady=5)
top_text_field.focus()

# key Frame
key_frame = ttk.Frame(app)

key_lable = ttk.Label(key_frame, text="Enter your KEY:")
key_lable.pack(side='left', padx=(10,0), pady=0)

key_entry = ttk.Entry(key_frame, show=u"\u25CF", width=30, textvariable=key)
key_entry.pack(side='left', padx=10)
key_entry.pack_forget()
key_entry.pack(side='left', fill="x",expand = True, padx=10)


key_load_button: object = ttk.Button(key_frame, text='Load Key', command=get_key)
key_load_button.pack(side='right', padx=10)
key_clear_button: object = ttk.Button(key_frame, text='Clear Key', command=clear_key)
key_clear_button.pack(side='right', padx=10)

key_frame.pack(pady=10, side='top', fill='x', anchor='center')

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
convert_button = ttk.Button(options_frame, text='Convert', command = convert_text)
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
bottom_text_field = tk.Text(app, width=50, height=5, background='light yellow', wrap='word')
bottom_text_field.pack(side='top', expand=True, fill='both', padx=10, pady=5)

credits_label = (ttk.Label(app, text="Made by: Magpie", font='calibre 10 bold').
                 pack(side='bottom', pady=10))

# Start the main event loop
app.mainloop()
