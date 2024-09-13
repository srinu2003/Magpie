# Text Encryption and Decryption Tool

## Setup
```
pip install -r requirements.txt
```
# CLI Tool

This is a Python project that provides a text encryption and decryption tool using symmetric encryption.

## Usage

1. Run the script `symmetric_encryption.py` to import the necessary functions.
2. Execute the main script `text_encryption.py` to start the tool.
3. Choose one of the following options:
    - Encrypt a message: Enter `1`, `e`, or `E`.
    - Decrypt a message: Enter `2`, `d`, or `D`.
    - Exit the tool: Enter `3`, `break`, `b`, `B`, `exit`, or `Exit`.
4. Follow the prompts to enter the necessary information for encryption or decryption.
5. The tool will display the encrypted or decrypted message based on the chosen option.

## Dependencies

- Python 3.x
- The `symmetric_encryption` module
- The `rich` module


# GUI Tool

![alt text](<Project_overview.png>)

This is a Python project that provides a text encryption and decryption tool using symmetric encryption with a graphical user interface (GUI).

## Usage

1. Run the Magpie installer to install the necessary dependencies.
2. Enter the input text and key in the corresponding fields.
3. Choose one of the following options:
    - Encrypt a message: Select the `Encrypt` button.
    - Decrypt a message: Select the `Decrypt` button.
    - Exit the tool: Click the `X` button.
4. Follow the prompts to enter the necessary information for encryption or decryption.

### To encrypt-decrypt text files using the GUI tool:

1. Run the Magpie installer to install the necessary dependencies.
2. Click the `Open File` button to choose a text file.
3. Enter the key in the corresponding field.
4. Choose one of the following options:
    - Encrypt a message: Select the `Encrypt` button.
    - Decrypt a message: Select the `Decrypt` button.
    - Exit the tool: Click the `X` button.
5. Click on the `Convert` button to start the encryption or decryption process.
6. Save the encrypted or decrypted text file to the desired location.
7. Follow the prompts to enter the necessary information for encryption or decryption.

### Project Structure:
```
CLI.py
GUI.py
LICENSE
main.py
other/
    message_security.py
    verify_hash.py
plaintext.txt
README.md
requirements.txt
symmetric_encryption.py
```
```mermaid
graph LR;
    B[other/]
    B1[message_security.py]
    B2[verify_hash.py]

    F[symmetric_encryption.py]
    G[CLI.py]
    H[GUI.py]
    I[key.key]

    B --> B1
    B --> B2

    I --> F
    F --> G
    F --> H
```
### System Architecture:
```mermaid
graph TD;
    A[User] -->|Interacts with| B[CLI Interface];
    A -->|Interacts with| C[GUI Interface];
    
    B -->|Calls functions from| D[Symmetric Encryption Module];
    C -->|Calls functions from| D[Symmetric Encryption Module];
    
    D --> E[Generate Key];
    D --> F[Load Key];
    D --> G[Encrypt Message];
    D --> H[Decrypt Message];
    
    B -.->|Displays Output| I[(Terminal)];
    C -.->|Displays Output| J[(GUI Window)];
    
    E -->|Stores Key in| K[Key Storage];
    F -->|Retrieves Key from| K[Key Storage];
    
    subgraph Key Management
        K
    end
    
    subgraph Encryption/Decryption
        G
        H
    end
    
    style A fill:#f9f,stroke:#333,stroke-width:2px;
    style B fill:#bbf,stroke:#333,stroke-width:2px;
    style C fill:#bbf,stroke:#333,stroke-width:2px;
    style D fill:#afa,stroke:#333,stroke-width:2px;
    style I fill:#fbb,stroke:#333,stroke-width:2px;
    style J fill:#fbb,stroke:#333,stroke-width:2px;
    style K fill:#fff,stroke:#333,stroke-width:2px;
```
## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
