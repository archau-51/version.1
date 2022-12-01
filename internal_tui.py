from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Button, Static
from textual.reactive import reactive
import glob
import subprocess
import sys
from difflib import Differ
files = glob.glob("versions/{}/*".format(sys.argv[1]))
print(files)
files = sorted(files)
nopath = []
for folder in files:
    nopath.append(folder.split("/")[-1])
class Side(Static):
    """A widget to display."""
    
    text = reactive("""    __ 
  /_ |
   | |
   | |
  _| |
 (_)_| 
   
   
   
   Selected file""")

    def render(self) -> str:
        return self.text
class Sidell(Static):
    """A widget to display."""
    
    textor = reactive("""   __   _____ _ __ ___ _  ___  _ __  
 \ \ / / _ \ '__/ __| |/ _ \| '_ \ 
  \ V /  __/ |  \__ \ | (_) | | | |
   \_/ \___|_|  |___/_|\___/|_| |_|      
  
  
  
  Current file""")

    def render(self) -> str:
        return self.textor


class EVERversion(App):

    """Versioning at its finest"""

    CSS_PATH = "tui.css"
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode"), ("m", "diff", "show diffs")]
    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Button("Back", id="r_button", variant="error")
        for x in nopath:
            yield Button(x, id="l_button", variant="success", name=x)
        yield Button("Restore file", id="restore", variant="warning")
        yield Side("""                   (_)            
   __ 
  /_ |
   | |
   | |
  _| |
 (_)_| 
                                  
                    """, id="current")
        yield Sidell("""
__   _____ _ __ ___ _  ___  _ __  
 \ \ / / _ \ '__/ __| |/ _ \| '_ \ 
  \ V /  __/ |  \__ \ | (_) | | | |
   \_/ \___|_|  |___/_|\___/|_| |_|             
                         """, id="selected")
        yield Footer()

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark
    def action_diff(self) -> None:
        """An action to diff."""
        difference = subprocess.run(['python3', 'diff.py', origi, sys.argv[1]],stdout=subprocess.PIPE).stdout.decode('utf-8')
        self.query_one(Side).text = difference
        self.query_one(Sidell).textor = "Running diff algorithm:\n\nUse diff.py to see full difference"
    def on_button_pressed(self, event: Button.Pressed):
        if event.button.id == "r_button":
            subprocess.run(["python3", "tui.py"])
            sys.exit()
        elif event.button.id == "l_button":
            global origi
            origi = event.button.name
            global versioned
            with open("./{}".format(files[nopath.index(event.button.name)])) as f:
                versioned = f.read()
                versioned2 = f.readlines()
            self.query_one(Side).text = versioned
            global curren
            try:
                with open("../{}".format(event.button.name)) as f:
                    curren = f.read()
                    curren2 = f.readlines()
            except:
                curren = "This file has been deleted"
            self.query_one(Sidell).textor = curren
        elif event.button.id == 'restore':
                subprocess.run(["python3", "restore.py", origi, sys.argv[1]])



if __name__ == "__main__":
    app = EVERversion()
    app.run()