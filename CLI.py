from symmetric_encryption import (
    generate_key,
    load_key,
    encrypt_message,
    decrypt_message,
    InvalidToken,
    BinasciiError
)

from rich import print as rprint
from rich.panel import Panel
from rich.console import Console


def cli_chat() -> None:
    console = Console()

    welcome_msg = Panel.fit("[bold yellow]Welcome to the Text encryption and decryption tool.", border_style="green")
    rprint(welcome_msg)
    rprint("""Here are the options:
           
        [green]1[/green] Encrypt : [green](e/E)[/green]
        [blue]2[/blue] Decrypt : [blue](d/D)[/blue]
        [red]3[/red] Exit    : [red](b/B)[/red]
          """)

    while True:
        option = console.input('[i bold]Enter option[/i bold]: ')
        match option[0] if option else '':
            case '1' | 'e' | 'E':
                # Text Encrypt
                message = console.input('Enter your [bold green]message[/bold green]: ')
                op = console.input("[#D0B344]Want to generate a new key?[/#D0B344] (y/n): ")
                if op == 'y':
                    key = generate_key()
                    rprint('Ciphered Text:\n[bold green]' + encrypt_message(message, key) + '[/bold green]')
                else:
                    key = load_key()
                    rprint('Ciphered Text:\n[bold green]' + encrypt_message(message, key) + '[/bold green]')

            case '2' | 'd' | 'D':
                # Text Decrypt
                message = console.input('Enter [bold blue]Ciphered Text[/bold blue]: ')
                op = console.input("[#D0B344]Want to enter key?[/#D0B344] (y/n): ")
                if op == 'y':
                    input_key = console.input('Enter your [bold #D0B344]key:[/bold #D0B344] ')
                    if len(input_key) != 44:  # 32 url-safe base64 to check key length
                        rprint("[red]Check the key and encrypted message. Key must be 32 url-safe base64.[/red]")
                        continue

                    msg = decrypt_message(message, input_key.encode())

                    if msg == InvalidToken:
                        rprint("[red]Invalid Key[/red]")
                    elif msg == BinasciiError:
                        rprint("[red]Invalid Ciphered Text[/red]")
                    else:
                        rprint('Message is:\n[blue]' + str(msg) + '[/blue]')
                else:
                    msg = decrypt_message(message, load_key())

                    if msg == InvalidToken:
                        rprint("[red]Ciphered Text did not match[/red]")
                    elif msg == BinasciiError:
                        rprint("[red]Invalid Bin Text[/red]")
                    else:
                        rprint('Message is:\n[blue]' + str(msg) + '[/blue]')

            case '3' | 'break' | 'b' | 'B' | 'exit' | 'Exit':
                rprint("Thank you :heart:  for using Magpie. Exiting.. :wave:")
                break
            case _:
                rprint("[red]Something's wrong with your input! Please try again.[/red]")
