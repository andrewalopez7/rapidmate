import os
import subprocess
import json
import sys
from pathlib import Path

class RapidMate:
    def __init__(self, config_file='rapidmate_config.json'):
        self.config_file = config_file
        self.shortcuts = self.load_config()

    def load_config(self):
        """Load the configuration file with application paths and startup settings."""
        if not os.path.exists(self.config_file):
            return {}
        with open(self.config_file, 'r') as file:
            return json.load(file)

    def save_config(self):
        """Save the current configuration to the config file."""
        with open(self.config_file, 'w') as file:
            json.dump(self.shortcuts, file, indent=4)

    def add_application(self, name, path):
        """Add a new application shortcut."""
        if not os.path.exists(path):
            print(f"Error: The path {path} does not exist.")
            return
        self.shortcuts[name] = path
        self.save_config()

    def remove_application(self, name):
        """Remove an application shortcut."""
        if name in self.shortcuts:
            del self.shortcuts[name]
            self.save_config()
        else:
            print(f"Error: No shortcut found with the name {name}.")

    def launch_application(self, name):
        """Launch an application by its shortcut name."""
        if name in self.shortcuts:
            subprocess.Popen(self.shortcuts[name])
        else:
            print(f"Error: No shortcut found with the name {name}.")

    def list_applications(self):
        """List all configured application shortcuts."""
        if self.shortcuts:
            print("Configured Applications:")
            for name, path in self.shortcuts.items():
                print(f"- {name}: {path}")
        else:
            print("No applications configured.")

def main():
    rapidmate = RapidMate()

    if len(sys.argv) < 2:
        print("Usage: python rapidmate.py [list|add|remove|launch] <application_name> <application_path>")
        return

    command = sys.argv[1].lower()

    if command == 'list':
        rapidmate.list_applications()
    elif command == 'add' and len(sys.argv) == 4:
        name, path = sys.argv[2], sys.argv[3]
        rapidmate.add_application(name, path)
    elif command == 'remove' and len(sys.argv) == 3:
        name = sys.argv[2]
        rapidmate.remove_application(name)
    elif command == 'launch' and len(sys.argv) == 3:
        name = sys.argv[2]
        rapidmate.launch_application(name)
    else:
        print("Invalid command or arguments. Please use list, add, remove, or launch.")

if __name__ == "__main__":
    main()