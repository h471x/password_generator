import sys
from pypass.app.cli.pypass_cli import main as cli_main
from pypass.app.gui.desktop.pypass_gui import main as desktop_main
from pypass.app.gui.web.pypass_web import main as web_main

def main():
    if len(sys.argv) == 1:
        # No arguments
        # Default to CLI 
        cli_main()  
        return

    command = sys.argv[1].lower()

    if command == 'cli':
        cli_main()
    elif command == 'desktop':
        desktop_main()
    elif command == 'web':
        web_main()
    else:
        print(f"Unknown command: {command}")
        print("Commands: cli, desktop, web")

if __name__ == "__main__":
    main()