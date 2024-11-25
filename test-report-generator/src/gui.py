import tkinter as tk
from tkinter import filedialog, messagebox
import os

# Dummy function to simulate report generation
def generate_report():
    report_file = "generated_report.txt"
    with open(report_file, 'w') as file:
        file.write("Test Results Report\n")
        file.write(f"Test Type: {test_type.get()}\n")
        file.write("Summary:\n")
        file.write("All tests passed successfully.\n")
    messagebox.showinfo("Success", f"Report generated: {report_file}")

# Function to open file dialog and load a test result file
def upload_file():
    file_path = filedialog.askopenfilename(
        title="Select Test Results File",
        filetypes=(("Text files", "*.txt"), ("All files", "*.*"))
    )
    if file_path:
        file_label.config(text=f"File Selected: {os.path.basename(file_path)}")

# Function to update report type based on selection
def update_template(*args):
    template_info_label.config(text=f"Selected Template: {test_type.get()}")

# Create the main window
root = tk.Tk()
root.title("Test Report Generator")

# Create widgets for the GUI
title_label = tk.Label(root, text="Test Report Generator", font=("Helvetica", 16))
title_label.pack(pady=10)

# File upload section
upload_button = tk.Button(root, text="Upload Test Result File", command=upload_file)
upload_button.pack(pady=5)

file_label = tk.Label(root, text="No file selected", font=("Helvetica", 10))
file_label.pack(pady=5)

# Template selection
template_label = tk.Label(root, text="Select Test Type", font=("Helvetica", 12))
template_label.pack(pady=10)

test_type = tk.StringVar(value="Smoke Testing")  # Default selection
test_type.trace("w", update_template)

test_type_dropdown = tk.OptionMenu(root, test_type, "Smoke Testing", "Regression Testing", "API Testing", "Performance Testing", "Functional Testing")
test_type_dropdown.pack(pady=5)

template_info_label = tk.Label(root, text="Selected Template: Smoke Testing", font=("Helvetica", 10))
template_info_label.pack(pady=5)

# Generate report button
generate_button = tk.Button(root, text="Generate Report", command=generate_report)
generate_button.pack(pady=20)

# Output Section (status message)
output_label = tk.Label(root, text="Report will be displayed here.", font=("Helvetica", 10))
output_label.pack(pady=10)

# Run the GUI
root.mainloop()
