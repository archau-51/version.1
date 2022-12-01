from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Button, Static
import glob
import subprocess
import time
import sys
folders = glob.glob("versions/*")
print(folders)
folders.remove('versions/versions.json')
folders = sorted(folders)
nopath = []
for folder in folders:
    nopath.append(folder[9:])
class Side(Static):
    """A widget to display."""
    def compose(self) -> ComposeResult:
        pass
class EVERversion(App):

    """Versioning at its finest"""

    CSS_PATH = "tui.css"
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]
    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        for x in nopath:
            yield Button(x, id="l_button", variant="success", name=x)
        yield Side("""                   (_)            
   __ 
  /_ |
   | |
   | |
  _| |
 (_)_|        """, id="current")
        yield Side("""
__   _____ _ __ ___ _  ___  _ __  
 \ \ / / _ \ '__/ __| |/ _ \| '_ \ 
  \ V /  __/ |  \__ \ | (_) | | | |
   \_/ \___|_|  |___/_|\___/|_| |_|            
                         """, id="selected")
        yield Footer()

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark
    def on_button_pressed(self, event: Button.Pressed):
        subprocess.run(["python3", "internal_tui.py", event.button.name])
        sys.exit()


if __name__ == "__main__":
    app = EVERversion()
    app.run()