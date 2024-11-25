import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox
import os

# Dummy function to simulate report generation
def generate_report():
    # Load the CSV file
    file_path = filedialog.askopenfilename(
        title="Select JMeter CSV Test Results",
        filetypes=(("CSV files", "*.csv"), ("All files", "*.*"))
    )
    
    if file_path:
        # Read CSV into pandas DataFrame
        df = pd.read_csv(file_path)

        # Analyzing the data
        success_count = df['success'].sum()  # True is 1, False is 0
        total_requests = len(df)
        success_rate = (success_count / total_requests) * 100
        avg_response_time = df['elapsed'].mean()

        # Create a report file
        report_file = "jmeter_test_report.txt"
        with open(report_file, 'w') as file:
            file.write("JMeter Test Results Report\n")
            file.write(f"Total Requests: {total_requests}\n")
            file.write(f"Successful Requests: {success_count}\n")
            file.write(f"Success Rate: {success_rate:.2f}%\n")
            file.write(f"Average Response Time: {avg_response_time:.2f} ms\n")

            # Optional: write failure details
            failed_requests = df[df['success'] == False]
            if not failed_requests.empty:
                file.write("\nFailed Requests:\n")
                for index, row in failed_requests.iterrows():
                    file.write(f"URL: {row['URL']} - Response Code: {row['responseCode']} - Message: {row['responseMessage']}\n")

        messagebox.showinfo("Success", f"Report generated: {report_file}")

# Function to open file dialog and load a test result file
def upload_file():
    file_path = filedialog.askopenfilename(
        title="Select Test Results File",
        filetypes=(("CSV files", "*.csv"), ("All files", "*.*"))
    )
    if file_path:
        file_label.config(text=f"File Selected: {os.path.basename(file_path)}")

# Create the main window
root = tk.Tk()
root.title("Test Report Generator")

# Create widgets for the GUI
title_label = tk.Label(root, text="Test Report Generator", font=("Helvetica", 16))
title_label.pack(pady=10)

# File upload section
upload_button = tk.Button(root, text="Upload JMeter Test Result File", command=upload_file)
upload_button.pack(pady=5)

file_label = tk.Label(root, text="No file selected", font=("Helvetica", 10))
file_label.pack(pady=5)

# Generate report button
generate_button = tk.Button(root, text="Generate Report", command=generate_report)
generate_button.pack(pady=20)

# Output Section (status message)
output_label = tk.Label(root, text="Report will be displayed here.", font=("Helvetica", 10))
output_label.pack(pady=10)

# Run the GUI
root.mainloop()
