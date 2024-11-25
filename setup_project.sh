#!/bin/bash

# Create main project folder
mkdir -p test-report-generator/src/templates
mkdir -p test-report-generator/docs
mkdir -p test-report-generator/tests/mock_data

# Create initial files
touch test-report-generator/src/main.py
touch test-report-generator/src/gui.py
touch test-report-generator/src/report_generator.py
touch test-report-generator/src/utils.py
touch test-report-generator/src/data_processing.py
touch test-report-generator/docs/README.md
touch test-report-generator/docs/user_guide.md
touch test-report-generator/tests/test_report_generator.py
touch test-report-generator/tests/test_gui.py
touch test-report-generator/requirements.txt
touch test-report-generator/README.md
touch test-report-generator/.gitignore

# Populate .gitignore with common Python ignores
echo -e "__pycache__/\n*.pyc\n.vscode/\n*.log" > test-report-generator/.gitignore

# Print completion message
echo "Project structure created successfully!"

# Run the Script:

# Open a terminal, navigate to the directory where setup_project.sh is saved, and make it executable:
# chmod +x setup_project.sh


# Then, run the script:
# ./setup_project.sh


# This script will create all necessary folders and empty files as specified in the project structure.

