Let's break down the code line by line:

```python
import json
import os
import sys
import yaml
```
- These lines import the necessary modules: `json` for working with JSON data, `os` for interacting with the operating system, `sys` for system-specific parameters and functions, and `yaml` for working with YAML data.

```python
if len(sys.argv) > 1:
```
- This line checks if command-line arguments are provided (excluding the script name).

```python
    if os.path.exists(sys.argv[1]):
```
- This line checks if the first command-line argument (if provided) corresponds to an existing file path using `os.path.exists()`.

```python
        sourcefile = open(sys.argv[1], "r")
        contentsource = json.load(sourcefile)
        sourcefile.close()
```
- If the file exists, it opens the file specified by the first command-line argument in read mode (`"r"`), loads its contents using `json.load()`, and stores the JSON data in the variable `contentsource`. Then, it closes the file.

```python
    else:
        print("ERROR: " + sys.argv[1] + " not found")
        exit(1)
```
- If the file specified in the first command-line argument does not exist, it prints an error message indicating the file name and exits the script with status code 1.

```python
else:
    print("Usage: json2yaml.py <sourcefile.json> [target_file.yaml]")
```
- If no command-line arguments are provided (excluding the script name), it prints usage instructions indicating how to use the script.

```python
outs = yaml.dump(contentsource)
```
- This line converts the JSON data (`contentsource`) into YAML format using `yaml.dump()` and stores the resulting YAML string in the variable `outs`.

```python
if len(sys.argv) < 3:
```
- This line checks if fewer than three command-line arguments are provided (excluding the script name).

```python
    print(outs)
```
- If only one command-line argument is provided (source file), it prints the YAML output (`outs`) to the console.

```python
elif os.path.exists(sys.argv[2]):
```
- If two command-line arguments are provided (source file and target file), this line checks if the target file already exists using `os.path.exists()`.

```python
    print("ERROR: " + sys.argv[2] + " already exists")
    exit(1)
```
- If the target file exists, it prints an error message indicating the file name and exits the script with status code 1.

```python
else:
    target_file = open(sys.argv[2], "w")
    target_file.write(outs)
    target_file.close()
```
- If the target file does not exist, it opens the file specified by the second command-line argument in write mode (`"w"`), writes the YAML output (`outs`) to the file, and then closes the file.

This script converts JSON data from a source file to YAML format and either prints the YAML output to the console or writes it to a target file, depending on the command-line arguments provided.
