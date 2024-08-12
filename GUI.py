import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from symmetric_encryption import generate_key, load_key, encrypt_message, decrypt_message, InvalidToken, BinasciiError

ICON_DATA = b''


def browse_files() -> None:
    """Browse for a file and load its content into the top field."""
    key_lable.setvar(key.get())
    try:
        filename = filedialog.askopenfilename(initialdir="/", title="Select a File",
                                              filetypes=(("Text files", "*.txt*"), ("all files", "*.*")))

        # Open and read file
        with open(filename, 'r') as file:
            top_text_field.delete('1.0', 'end')
            top_text = file.read()
            top_text_field.insert('1.0', top_text)
    except FileNotFoundError:
        return None


def save_file() -> None:
    """Save the text in the bottom field to a file."""
    filename = filedialog.asksaveasfilename(initialdir="/", title="Save File",
                                            filetypes=(("Text files", "*.txt*"), ("all files", "*.*")))
    if filename.partition('.')[0] == '':
        # TODO: Handle empty filename
        return None
    if filename.partition('.')[2] != 'txt':
        # C:\\users\%USERNAME%\downloaded_files\test.txt.csv
        if filename.partition('.')[2] == '':
            filename += '.txt'
        else:
            filename = filename.partition('.')[0] + '.txt'

    # Open and write file
    with open(filename, 'w') as file:
        file.write(bottom_text_field.get('1.0', 'end-1c'))


def convert_text() -> None:
    """Convert the text in the top field to the desired format and display it in the bottom field.
    The text is converted based on the radio button selected.
    If the radio button is selected to encrypt, the text is encrypted and displayed in the bottom field."""

    if radio_bool.get():
        # TODO: Complete the encrypt function and also the decrypt function
        if top_text_field.get('1.0', 'end-1c') == '':
            credits_label.config(text='Magpie: No text to encrypt', foreground='red')
            return None

        if key.get() == '':
            get_key()

        _key = key.get()
        plain_text = top_text_field.get('1.0', 'end-1c')
        cipher_text = encrypt_message(plain_text, _key.encode())
        credits_label.config(text='Magpie: Encryption successful', foreground='green')

        bottom_text_field.config(state='normal')  # Enable editing
        bottom_text_field.delete('1.0', 'end')
        bottom_text_field.insert('1.0', cipher_text)
        bottom_text_field.config(state='disabled')  # Disable editing

    else:
        _key = key.get()
        cipher_text = top_text_field.get('1.0', 'end-1c')

        # Extract the decrypted message from the result based on its type
        plain_text = decrypt_message(cipher_text, _key.encode())

        # TODO: Handle the decrypted message based on its type
        # Check the type of the decrypted message
        bottom_text_field.config(state='normal')  # Enable editing
        bottom_text_field.delete('1.0', 'end')
        if isinstance(plain_text, str):
            # Insert the decrypted message as a string

            bottom_text_field.insert('1.0', plain_text)
            bottom_text_field.config(state='disabled')  # Disable editing
            credits_label.config(text='Magpie: Decryption successful', foreground='green')
        elif isinstance(plain_text, InvalidToken):
            credits_label.config(text='Magpie: Invalid Token error occurred', foreground='red')
        elif isinstance(plain_text, Exception):
            credits_label.config(text='Magpie: Exception occurred during decryption', foreground='red')
        elif isinstance(plain_text, BinasciiError):
            credits_label.config(text='Magpie: Binascii Error occurred', foreground='red')
        elif isinstance(plain_text, ValueError):
            credits_label.config(text='Magpie: Value Error occurred, key must be 32 url-safe base64-encoded bytes', foreground='red')
        else:
            credits_label.config(text='Magpie: Unknown error occurred. Please enter correct Cipher text.',
                                 foreground='red')


def new_key() -> None:
    key.set(generate_key().decode())
    key_lable_text.set('Using KEY:  ' + key.get() + " (Generated)")
    return None


def clear_key() -> None:
    key.set('')
    # convert_text()


def get_key() -> None:
    key.set(load_key().decode())
    if radio_bool.get():
        key_lable_text.set('Using KEY:  ' + key.get() + " (Loaded)")
    return None


# app
app = tk.Tk()
app.title("Magpie")
app.iconbitmap(r'./magpie.ico')
# app.geometry("300x150") # for 730p 'ish screens
app.geometry('685x500')
app.minsize(width=685, height=500)

# VARIABLES
key = tk.StringVar()
radio_bool = tk.BooleanVar(value=True)
key_lable_text: tk.StringVar = tk.StringVar(
    value='Using KEY: ' + key.get() + " (Not yet loaded. Will be loaded on conversion.)")

# label
greeting_label = ttk.Label(app, text="Welcome to")
greeting_label.pack()

# title
title_label = ttk.Label(app, text='TEXT Encrypter', font='calibre 24 bold')
title_label.pack(side='top')

input_lable = ttk.Label(app, text="Enter your text:")
input_lable.pack(side='top', fill='x', padx=(10, 0))

# top entry field
top_text_field = tk.Text(app, width=50, height=5, background='light blue', wrap='word', maxundo=15, undo=True, )
top_text_field.pack(side='top', expand=True, fill='both', padx=10, pady=5)
top_text_field.focus()

# key Frame
key_frame = ttk.Frame(app)

key_lable = ttk.Label(key_frame, textvariable=key_lable_text, font='courier 8 bold')
key_lable.pack(side='left', padx=(10, 0), pady=0)

key_entry = ttk.Entry(key_frame, show=u"\u25CF", width=30, textvariable=key, foreground='black')
# key_entry = ttk.Entry(key_frame, width=30, textvariable=key,foreground='green')
# TODO: Validate the key length and display a warning if the key length is less than 44
key_entry.configure(validate='key', validatecommand=(key_entry.register(lambda text: len(text) <= 44), "%P"))

# def validate_key_length(text):
#     if len(text) < 44:
#         key_entry.configure(foreground='red')
#     else:
#         key_entry.configure(background='black')
#     return len(text) <= 44

# key_entry.configure(validatecommand=(key_entry.register(validate_key_length), "%P"))


key_load_button: object = ttk.Button(key_frame, text='Load Key', command=get_key, state='normal')
key_load_button.pack(side='right', padx=10)

key_clear_button: object = ttk.Button(key_frame, text='Generate Key', command=new_key, state='normal')
key_clear_button.pack(side='right', padx=10)

key_frame.pack(pady=10, side='top', fill='x', anchor='center')

# Options Frame
options_frame = ttk.Frame(app, relief=tk.GROOVE, padding=(10, 5))

# Radio button field
radio_frame = ttk.Frame(options_frame, relief=tk.GROOVE, padding=10)


def radio_func():
    if radio_bool.get():
        get_key()
        key_entry.pack_forget()
        key_clear_button.configure(state='normal', text='Generate Key', command=new_key)

    else:
        key_lable_text.set('Enter your KEY:')
        key_entry.pack(side='left', fill="x", expand=True, padx=10)
        key.set('')
        key_clear_button.configure(text='Clear Key', command=clear_key)


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
# radio_func()

# convert button
convert_button = ttk.Button(options_frame, text='Convert', command=convert_text)
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

credits_label = ttk.Label(app, text="Made by: Magpie", font='calibre 10 bold')
credits_label.pack(side='bottom', pady=10)

# Start the main event loop
app.mainloop()
