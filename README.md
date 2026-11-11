
# Synthetic Data Generator | Python Final Project

## Project Overview

This project was developed as my final assignment for my introductory Python programming course. The goal was to take everything we had learned throughout the semester and apply it to one complete program.

For this project, I created a Python-based synthetic data generator that reads information from CSV files, analyzes the data, and generates new records based on the original dataset.

The project gave me the opportunity to demonstrate my understanding of Python fundamentals while learning how to organize a larger program with multiple functions working together.

## Project Features

The program was designed to complete several tasks:

1. **Load CSV Files**
   - Allows the user to select between two provided datasets.
   - Reads CSV files using Python's built-in CSV library.
   - Identifies empty rows and logs them into an error file.

2. **Identify and Display Data**
   - Displays a preview of the dataset.
   - Allows the user to identify whether the dataset contains headers.
   - Formats and displays up to 50 rows in the terminal.

3. **Organize and Analyze Data**
   - Organizes dataset columns using Python dictionaries.
   - Sorts values alphabetically or numerically.
   - Counts unique values within each column.
   - Calculates how frequently each value appears.

4. **Generate Synthetic Data**
   - Allows the user to choose how many new records to generate.
   - Calculates probabilities based on the frequency of existing values.
   - Uses Python's random library to generate new records.
   - Displays a preview of the generated dataset.

5. **Export Results**
   - Allows the user to name the output file.
   - Saves generated records into a new CSV file.

6. **Compare Datasets**
   - Includes a function intended to compare the original and generated datasets.
   - Calculates differences in value distributions.
   - Uses a user-defined margin of error to evaluate the results.

## Python Skills Demonstrated

This project brought together several programming concepts covered throughout the semester.

- **Functions:** Breaking the program into smaller, reusable sections.
- **Loops:** Processing datasets and repeating tasks.
- **Conditional Statements:** Controlling the program based on user input.
- **Lists and Dictionaries:** Storing, organizing, and accessing data.
- **File Handling:** Reading and writing CSV files.
- **Exception Handling:** Handling invalid inputs and file errors.
- **User Input:** Allowing users to interact with the program.
- **Randomization:** Generating new data using weighted random selection.
- **Basic Data Analysis:** Counting values and calculating probabilities.

## Technologies Used

- Python
- CSV Library
- Random Library
- CSV File Format

The program uses Python's standard library and does not require additional third-party packages.

## How to Run the Project

1. Download or clone this repository.
2. Make sure Python 3 is installed.
3. Keep the `0_input` folder and its CSV files in the project directory.
4. Open a terminal in the project directory.
5. Run the following command:

```bash
python "Final Draftt.py"
```

6. Follow the prompts to select a dataset, review the data, and generate synthetic records.

## What I Learned

Before this project, most of my programming experience came from smaller assignments focused on individual Python concepts.

This final required me to combine those concepts into one larger program. One of the biggest challenges was making sure information could be passed between functions correctly and that each part of the program worked with the others.

I also gained more experience troubleshooting errors, working with CSV files, and using dictionaries and lists to organize information.

Overall, this project helped me become more comfortable writing Python programs from start to finish and gave me a better understanding of how the fundamentals we learned in class can be applied to a practical project.

## Project Limitations

This was an introductory programming project, so the synthetic data generator has some limitations.

The program generates values independently for each column based on their frequency in the original dataset. This means it does not necessarily preserve relationships between different columns.

The dataset comparison functionality was also part of the learning process and may require additional debugging or improvements.

## Project Background

This project was completed as the final assignment for my Coding 1 course. Its purpose was to demonstrate the Python programming concepts and problem-solving skills I developed throughout the semester.
