import tkinter as tk

def encrypt():
    message = message_text.get("1.0", "end-1c") # Get the message from the text widget
    shift = int(shift_entry.get()) # Get the shift value from the entry widget

    encrypted_message = ""
    for char in message:
        if char.isalpha(): # Encrypt only alphabetical characters
            shifted_char = chr((ord(char.upper()) - ord('A') + shift) % 26 + ord('A'))
            if char.islower(): # Preserve the original case of the character
                encrypted_message += shifted_char.lower()
            else:
                encrypted_message += shifted_char
        else:
            encrypted_message += char

    result_text.delete("1.0", "end") # Clear the result text widget
    result_text.insert("end", encrypted_message) # Update the result text widget

root = tk.Tk()
root.title("Message Encryptor")

# Create a text widget for inputting the message
message_label = tk.Label(root, text="Enter the message:")
message_label.pack()
message_text = tk.Text(root, height=5, width=30)
message_text.pack()

# Create an entry widget for inputting the shift value
shift_label = tk.Label(root, text="Enter the shift value:")
shift_label.pack()
shift_entry = tk.Entry(root)
shift_entry.pack()

# Create a button to trigger the encryption
encrypt_button = tk.Button(root, text="Encrypt", command=encrypt)
encrypt_button.pack()

# Create a text widget to display the encrypted result
result_label = tk.Label(root, text="Encrypted message:")
result_label.pack()
result_text = tk.Text(root, height=5, width=30)
result_text.pack()

# Start the main
root.mainloop()