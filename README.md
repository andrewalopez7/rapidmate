# RapidMate

RapidMate streamlines the launching of applications on Windows with optimized shortcut management and startup configurations. 

## Features

- Add, remove, and manage application shortcuts.
- Launch applications using their configured shortcuts.
- List all configured applications in an easy-to-read format.

## Requirements

- Windows OS
- Python 3.x

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/rapidmate.git
   ```

2. Navigate to the directory:

   ```bash
   cd rapidmate
   ```

## Usage

The `rapidmate.py` script can be used to manage and launch your application shortcuts.

### Commands

- **List Applications**

  List all configured applications:

  ```bash
  python rapidmate.py list
  ```

- **Add Application**

  Add a new application shortcut:

  ```bash
  python rapidmate.py add <application_name> <application_path>
  ```

  Example:

  ```bash
  python rapidmate.py add Notepad "C:\Windows\System32\notepad.exe"
  ```

- **Remove Application**

  Remove an existing application shortcut:

  ```bash
  python rapidmate.py remove <application_name>
  ```

  Example:

  ```bash
  python rapidmate.py remove Notepad
  ```

- **Launch Application**

  Launch an application using its shortcut:

  ```bash
  python rapidmate.py launch <application_name>
  ```

  Example:

  ```bash
  python rapidmate.py launch Notepad
  ```

## Configuration

RapidMate uses a configuration file named `rapidmate_config.json` to store application shortcuts. This file is automatically created and updated when you add or remove applications.

## Contribution

Feel free to fork the repository and submit pull requests. Any contributions are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.