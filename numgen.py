# Number Sequence Generator v0.0.1
# Date: 16-08-2023
# Developed by: Raymond C. TURNER

import tkinter as tk
from tkinter import scrolledtext, messagebox
import os
import random
from ttkthemes import ThemedStyle  # Import ThemedStyle from ttkthemes library


# Define log_text as a global variable
log_text = None

# Define log_window as a global variable
log_window = None


# Function to apply the selected theme
def apply_theme(theme):
    global log_text
    if theme == "light":
        root.config(bg="white")
        label.config(bg="white", fg="black")
        seed_entry.config(bg="white", fg="black")
        generate_button.config(bg="white", fg="black")
        open_log_button.config(bg="white", fg="black")
        close_log_button.config(bg="white", fg="black")
        clear_log_button.config(bg="white", fg="black")
        theme_button.config(bg="white", fg="black")
        close_button.config(bg="white", fg="black")
        if log_text:  # Check if log_text is defined
            log_text.config(bg="white", fg="black")
        result_label.config(bg="white", fg="black")
        root.tk_setPalette(background="white")
    elif theme == "dark":
        root.config(bg="black")
        label.config(bg="black", fg="white")
        seed_entry.config(bg="black", fg="white")
        generate_button.config(bg="black", fg="white")
        open_log_button.config(bg="black", fg="white")
        close_log_button.config(bg="black", fg="white")
        clear_log_button.config(bg="black", fg="white")
        theme_button.config(bg="black", fg="white")
        close_button.config(bg="black", fg="white")
        if log_text:  # Check if log_text is defined
            log_text.config(bg="black", fg="white")
        result_label.config(bg="black", fg="white")
        root.tk_setPalette(background="black")

    # Explicitly set the text color of the buttons for both light and dark themes
    generate_button.config(fg="black")
    open_log_button.config(fg="black")
    close_log_button.config(fg="black")
    clear_log_button.config(fg="black")
    theme_button.config(fg="black")
    close_button.config(fg="black")


# Toggle between light and dark themes
def toggle_theme():
    global current_theme
    current_theme = "light" if current_theme == "dark" else "dark"
    apply_theme(current_theme)


current_theme = "light"  # Default theme is light


def generate_numbers(seed):
    numbers = {seed}
    while len(numbers) < 7:  # Generate 6 unique numbers
        next_number = random.randint(0, 30)  # Generate a random number between 0 and 30
        numbers.add(next_number)
    return list(numbers)


def generate_sequence():
    try:
        seed = int(seed_entry.get())
        numbers = generate_numbers(seed)
        result_label.config(text="Generated sequence: " + " ".join(map(str, numbers)))

        # Append the generated sequence to a unique log file
        log_filename = f"log_{os.getpid()}.txt"
        log_directory = "logs"
        os.makedirs(log_directory, exist_ok=True)
        with open(os.path.join(log_directory, log_filename), "a") as log_file:
            log_file.write(
                "Seed: {}\nGenerated sequence: {}\n\n".format(
                    seed, " ".join(map(str, numbers))
                )
            )

    except ValueError:
        result_label.config(text="Please enter a valid number.")

        # Function to close the application


def close_application():
    if messagebox.askokcancel("Quit", "Do you really want to quit?"):
        root.destroy()


def open_log_file():
    global log_window

    if log_window:
        result_label.config(text="Log window already open.")
        messagebox.showerror("Error", "Log window is already open.")
        return

    log_directory = "logs"
    log_filename = f"log_{os.getpid()}.txt"
    log_filepath = os.path.join(log_directory, log_filename)

    log_window = tk.Toplevel(root)
    log_window.title("Log File")

    # Add a scrolled text widget with scroll bar
    global log_text
    log_text = scrolledtext.ScrolledText(log_window, wrap=tk.WORD)
    log_text.pack(fill=tk.BOTH, expand=True)

    def update_log_contents():
        try:
            with open(log_filepath, "r") as log_file:
                log_contents = log_file.read()
                log_text.delete("1.0", tk.END)
                log_text.insert(tk.END, log_contents)
        except FileNotFoundError:
            log_text.delete("1.0", tk.END)
            log_text.insert(tk.END, "Log file not found.")

        # Schedule the next update after a short delay (in milliseconds)
        log_window.after(1000, update_log_contents)

    # Bind the close event to the log window
    log_window.protocol("WM_DELETE_WINDOW", close_log_window)

    # Start the initial update and schedule subsequent updates
    update_log_contents()

# Function to close the log file window
def close_log_window():
    global log_window
    if log_window:
        log_window.destroy()
        log_window = None  # Reset log_window variable

def clear_log_file():
    try:
        log_directory = "logs"
        log_filename = f"log_{os.getpid()}.txt"
        log_filepath = os.path.join(log_directory, log_filename)

        if os.path.exists(log_filepath):
            os.remove(log_filepath)
            result_label.config(text="Log file cleared.")
        else:
            result_label.config(text="Log file not found.")

    except Exception as e:
        result_label.config(text="Error clearing log file.")

# Function to display the About window
def show_about_window():
    about_window = tk.Toplevel(root)
    about_window.title("About")
    about_text = "Number Sequence Generator\n\nVersion: 0.0.1-beta\n\nDate: 16-08-2023\n\nPython 3.10.8\n\nttkthemes 3.2.2\n\nTcl/TK version 8.6\n\nDeveloped By: codestak.io\n\nAuthor: Raymond C. TURNER\n\nDescription: This application generates unique number sequences based on a seed number."
    about_label = tk.Label(about_window, text=about_text, padx=20, pady=20)
    about_label.pack()
    
    
# Create the main application window
root = tk.Tk()

# Set a custom icon for the main window
# icon_path = (
#     "path_to_your_icon_file.ico"  # Replace with the actual path to your icon file
# )
# root.iconbitmap(icon_path)

# Create a themed style
style = ThemedStyle(root)
style.set_theme("default")  # Set the theme to "default"

# Enlarge the UI to three times the original size
root.geometry("900x700")

# Create a custom title with padding for the icon
custom_title = "Number Sequence Generator         "  # Adjust padding as needed
root.title(custom_title)

# Create and place widgets
label = tk.Label(root, text="Enter a seed number:")
label.pack(pady=30)

seed_entry = tk.Entry(root)
seed_entry.pack()

generate_button = tk.Button(
    root, text="Generate Unique Sequence", command=generate_sequence
)
generate_button.pack(pady=20)

# Create a "Open Log" button on UI
open_log_button = tk.Button(root, text="Open Log File", command=open_log_file)
open_log_button.pack(pady=10)

# Create a "Clear Log" button on UI
clear_log_button = tk.Button(root, text="Clear Log File", command=clear_log_file)
clear_log_button.pack(pady=10)

# Create a "Close Log File" button on the UI
close_log_button = tk.Button(root, text="Close Log File", command=close_log_window)
close_log_button.pack(pady=10)

# Create a "Toggle Theme" theme switcher button on the UI
theme_button = tk.Button(root, text="Toggle Theme", command=toggle_theme)
theme_button.pack(pady=10)

# Create a "Close Application" button on the UI
close_button = tk.Button(root, text="Close Application", command=close_application)
close_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack()

# Apply the initial theme
apply_theme(current_theme)

# Create a menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Create a File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open Log File", command=open_log_file)
file_menu.add_command(label="Clear Log File", command=clear_log_file)
file_menu.add_separator()
file_menu.add_command(
    label="Close Application", command=close_application
)  # Add Close Application option
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy)

# Create a Help menu
help_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=show_about_window)

# Start the GUI event loop
root.mainloop()
