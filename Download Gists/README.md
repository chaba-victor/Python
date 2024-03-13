## Breakdown of the code:

1. `import requests`: Imports the `requests` module, which allows making HTTP requests in Python.
2. `import os`: Imports the `os` module, which provides a portable way of interacting with the operating system.
3. `def create_directory(dirname):`: Defines a function named `create_directory` that takes a directory name (`dirname`) as an argument.
    - `try` block: Attempts to check if the directory exists using `os.stat()`.
    - `except` block: If the directory doesn't exist, it creates it using `os.mkdir()`.
4. `def show(obj):`: Defines a function named `show` that takes an object (`obj`) as an argument.
    - Iterates through the elements of `obj` and prints each element with its index.
5. `def auth():`: Defines a function named `auth` that prompts the user for authentication details.
    - Asks the user if they want to download gists from their GitHub account.
    - Depending on the user's response, prompts for username and password (if yes) and constructs a request to GitHub's API to retrieve gists.
6. `def load(request):`: Defines a function named `load` that processes the response from the GitHub API request.
    - Splits the response text into individual items.
    - Extracts gist URLs and filenames from the response.
7. `def write_gist(filename, text):`: Defines a function named `write_gist` that writes text (gist content) to a file specified by `filename`.
8. `def download(permission, user, request, fileno):`: Defines a function named `download` that downloads gists based on user permissions and choices.
    - Processes the response from the GitHub API request using `load()`.
    - Creates a directory for storing downloaded gists.
    - Downloads gists based on user input (all gists or specific ones).
9. `def detailed(urls, pos):`: Defines a function named `detailed` that retrieves and prints the content of a specific gist.
10. `def main():`: Defines the main function of the program.
    - Authenticates the user and retrieves gists.
    - Enters a loop to process user commands:
        - `download`: Calls `download()` function to download gists.
        - `detailed`: Calls `detailed()` function to print detailed content of a gist.
        - `show`: Calls `show()` function to display available files.
        - `exit`: Exits the program.
11. `if(__name__ == '__main__'):`: Checks if the script is being run as the main program.
    - Calls the `main()` function if true.