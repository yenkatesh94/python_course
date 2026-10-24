"""A virtual environment isolates a project's Python interpreter and installed packages.
This example displays interpreter paths and lists commands to create and activate an environment.
"""

# Topic 31: Virtual environments

import sys


def main():
    print("Python executable:", sys.executable)
    print("Environment prefix:", sys.prefix)
    print("Base Python prefix:", sys.base_prefix)
    print("A virtual environment is active:", sys.prefix != sys.base_prefix)

    # In the project folder, create and activate an environment in PowerShell:
    #   python -m venv .venv
    #   .\.venv\Scripts\Activate.ps1
    # Install packages in that environment with:
    #   python -m pip install package_name
    # Leave the environment with:
    #   deactivate


if __name__ == "__main__":
    main()
