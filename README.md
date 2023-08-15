
# Number Sequence Generator

This program utilizes the tkinter library in Python to create a Graphical User Interface (GUI) application that generates a sequence of numbers based on a seed provided by the user. The generated sequence follows a specific algorithm and is displayed within the application window.

## Program Overview

The program consists of several components:

1. **Importing the Required Module:**
    The program begins by importing the `tkinter` library, which provides functions and classes for creating a graphical user interface.

```python
import tkinter as tk
```

2. **Generating the Number Sequence:**
    The `generate_numbers` function takes a seed as input and generates a sequence of numbers based on a simple algorithm. It uses the seed to initialize the sequence and then generates additional numbers iteratively. Each number is generated using the formula `(previous_number * 2 + 1) % 100`.

```python
def generate_numbers(seed):
    numbers = [seed]
    for _ in range(10):  # Generate 10 more numbers
        next_number = (numbers[-1] * 2 + 1) % 100
        numbers.append(next_number)
    return numbers
```

3. **Generating the Sequence and Displaying it:**
    The `generate_sequence` function is responsible for fetching the seed entered by the user, generating the sequence using the `generate_numbers` function, and displaying the result in the GUI.

```python
def generate_sequence():
    try:
        seed = int(seed_entry.get())
        numbers = generate_numbers(seed)
        result_label.config(text="Generated sequence: " + " ".join(map(str, numbers)))
    except ValueError:
        result_label.config(text="Please enter a valid number.")
```

4. **Creating the GUI Application:**
    The `tk.Tk()` function is used to create the main application window. The title of the window is set to "Number Sequence Generator".

```python
root = tk.Tk()
root.title("Number Sequence Generator")
```

5. **Creating and Placing Widgets:**
    Various GUI elements, or widgets, are created using `tk.Label`, `tk.Entry`, and `tk.Button`. These widgets are placed in the application window using the `pack` method.

```python
label = tk.Label(root, text="Enter a seed number:")
label.pack(pady=10)

seed_entry = tk.Entry(root)
seed_entry.pack()

generate_button = tk.Button(root, text="Generate Sequence", command=generate_sequence)
generate_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack()
```

6. **Starting the GUI Event Loop:**
    The `root.mainloop()` call initiates the GUI event loop, allowing the user to interact with the application. This loop continues running until the user closes the application window.

```python
root.mainloop()
```

## Usage Instructions

1. Run the program using a Python interpreter.
2. A GUI window titled "Number Sequence Generator" will appear.
3. Enter an integer seed value in the provided text entry field.
4. Click the "Generate Sequence" button.
5. The generated number sequence will be displayed in the application window.
6. If an invalid input (non-integer) is provided as the seed, an error message will be displayed.

This program provides a simple example of using the `tkinter` library to create a basic GUI application for generating number sequences based on user input.

---

Please note that this Markdown document is a textual representation of the provided Python program's structure and functionality. You can use this document to provide an explanation or documentation for your program.




























Documentation by: **Raymond C. TURNER**# numgen
# Number-Sequence-Generator
# Number-Sequence-Generator
# Number-Sequence-Generator
