import sys
from rich import print

print("[bold magenta]My Python environment works![/bold magenta]")
print(f"Interpreter: {sys.executable}")
print(f"Version: {sys.version.split()[0]}")


