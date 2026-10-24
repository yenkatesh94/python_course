"""A package groups related Python modules, and pip installs third-party packages.
This example imports a local package and shows common pip commands to run in a terminal.
"""

# Topic 17: Packages and pip
# A package is a directory containing related Python modules.
# school_tools is a small package next to this lesson file.
from school_tools import make_greeting


if __name__ == "__main__":
    print(make_greeting("Maya"))

    # pip installs packages from package indexes such as PyPI.
    # Run these commands in a terminal, not inside the Python interpreter:
    #   python -m pip --version
    #   python -m pip install package_name
    #   python -m pip show package_name
    #   python -m pip uninstall package_name
    #
    # For example, install and inspect the third-party colorama package:
    #   python -m pip install colorama
    #   python -m pip show colorama
