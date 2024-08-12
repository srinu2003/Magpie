### References

### `symmetric_encryption.py`

1. **Cryptography Library:**
   - *Cryptography*: A package designed to expose cryptographic recipes and primitives to Python developers. It includes both high-level recipes and low-level interfaces to common cryptographic algorithms such as symmetric ciphers, message digests, and key derivation functions.
     - Cryptography. (n.d.). Retrieved from https://cryptography.io/

2. **Python Standard Library:**
   - *os Module*: This module provides a way of using operating system-dependent functionality like reading or writing to the file system.
     - Python Software Foundation. (n.d.). os — Miscellaneous operating system interfaces. In *Python 3 Documentation*. Retrieved from https://docs.python.org/3/library/os.html
     
   - *os.path Module*: This module implements some useful functions on pathnames.
     - Python Software Foundation. (n.d.). os.path — Common pathname manipulations. In *Python 3 Documentation*. Retrieved from https://docs.python.org/3/library/os.path.html
   
   - *binascii Module*: This module contains a number of methods to convert between binary and various ASCII-encoded binary representations.
     - Python Software Foundation. (n.d.). binascii — Convert between binary and ASCII. In *Python 3 Documentation*. Retrieved from https://docs.python.org/3/library/binascii.html

3. **PEP 484 – Type Hints:**
   - *Type Annotations*: Python's type annotations enable optional type checking via static type checkers, which can find type errors before the code runs.
     - van Rossum, G., & Lehtosalo, J. (2014). PEP 484 – Type Hints. Python Enhancement Proposals. Retrieved from https://peps.python.org/pep-0484/

Here are the references for the two Python scripts:

### `CLI.py`

1. **Rich Library Documentation**: The Rich library is used for creating attractive command-line interfaces. The `print` function from `rich` and the `Panel`, `Console` classes are utilized for displaying text in various styles. You can refer to the official documentation for more details:
   - [Rich Documentation](https://rich.readthedocs.io/en/stable/)

2. **Python Match Statement**: The `match` statement in Python, introduced in version 3.10, is used for pattern matching. It helps in selecting code blocks to execute based on the structure of the input. Official documentation is available at:
   - [Python Pattern Matching](https://docs.python.org/3/whatsnew/3.10.html#pattern-matching)

3. **Python File I/O**: The script utilizes basic Python file I/O operations to load and save keys and messages. This includes opening, reading, and writing files. Documentation can be found here:
   - [Python File I/O](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)

### `GUI.py`

1. **Tkinter Library Documentation**: Tkinter is the standard Python interface to the Tk GUI toolkit. It is used extensively in this script for creating the GUI elements like buttons, labels, text fields, etc. The documentation provides a comprehensive guide to the various components:
   - [Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)

2. **Tkinter filedialog Module**: The `filedialog` module is part of Tkinter and is used to open and save files through a file dialog box in the GUI. The official reference is available at:
   - [Tkinter filedialog](https://docs.python.org/3/library/tkinter.filedialog.html)

3. **Python StringVar and BooleanVar**: The script uses `StringVar` and `BooleanVar` from Tkinter to manage the state of variables that are tied to widgets in the GUI. These are commonly used for managing user input and control states. Documentation is here:
   - [StringVar and BooleanVar](https://effbot.org/tkinterbook/variable.htm)

4. **Base64 Encoding**: The script checks the length of keys and utilizes Base64 encoding for secure message encryption. Python's `base64` module handles this encoding:
   - [Base64 Encoding in Python](https://docs.python.org/3/library/base64.html)

These references should help you understand the underlying components and libraries used in your Python scripts.