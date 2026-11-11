#step 1 loading the data set
import csv


def load_file():
    
    input_folder= "0_input"
    
    available_files = ["hardset.csv","easyset.csv"] #both data sets loaded into 0_input folder
    
    

    if not available_files:
        print(f"'{input_folder}' is empty please add your own files")
        return

    print("pick the file you want to work with")
    for i, file in enumerate(available_files, start=1):
        print(f"{i}.) {file}")


   
    while True:
        try:
            answer = int(input("Enter the number for the file: "))
            if 1 <= answer <= len(available_files):
                selected_file = available_files[answer - 1]
                break
            else:
                print(f"Enter a valid number between 1 and {len(available_files)}.")
        except ValueError:
            print("Enter a valid number.")

    file_path = input_folder + "/" + selected_file

    errors = []
    data = []

    try:
        with open(file_path, "r") as file:
            reader = csv.reader(file)
            rows = list(reader)

            # Check if the file is empty
            if not rows:
                print("The file is empty.")
                return None

        

            for line_num, row in enumerate(rows, start=1):
                if not any(row):  # Check for empty rows
                    errors.append((line_num, "Empty row"))  # Append to 'errors' list
                    continue
                data.append(row)

#make error cvs file
        if errors:
            log_file_path = "errors_on_input.csv"
            with open(log_file_path, mode="w", newline="") as log_file:
                writer = csv.writer(log_file)
                writer.writerow(["Row Number", "Error Description"])
                writer.writerows(errors)
            print(f"Errors have been logged to '{log_file_path}'.")
        else:
            print("No errors found in the dataset.")

        print(f"Loaded {len(data)} rows")
        return data

    except FileNotFoundError:
        print(f"Error: The file '{selected_file}' was not found in the '{input_folder}' folder.")
        return None  # Return None if the file is not found
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None  # Return None for any unexpected error           

       
          
               


#step 2 define headers

#video I used for creating the output table: https://www.youtube.com/watch?v=B9BRuhqEb2Q

def print_first_5(data):
    
    if not data or len(data) < 1:
        print("No data available to display.")
        return

    # Assuming the first row is the header
    headers = data[0]
    rows = data[1:6] # first 5, 6 if there is no header

    # Calculate column widths dynamically based on the longest value in each column
    column_widths = [max(len(str(value)) for value in column) for column in zip(*([headers]+rows))]

    column_widths = [width + 2 for width in column_widths]

    line_number_width = len(str(len(rows))) + 2

    # Print header
    print("-" * (line_number_width + sum(column_widths) + 3 * len(headers) + 1))
    print(f"{'Line':<{line_number_width}}" + " | " + " | ".join(f"{header:<{column_widths[i]}}" for i, header in enumerate(headers)))
    print("-" * (line_number_width + sum(column_widths) + 3 * len(headers) + 1))
    
    for i, row in enumerate(rows, start=1):
        print(f"{i:<{line_number_width}}" + " | " + " | ".join(f"{str(value):<{column_widths[i]}}" for i, value in enumerate(row)))


    # End of table
    print("-" * (line_number_width + sum(column_widths) + 3 * len(headers) + 1))


def set_header_row(data):
    print_first_5(data)
    
    print()
    print("does this data set have headers?")
    
    while True:
        try:
            user_answer = input("Enter yes or no: ").strip().lower()  # Get user input and normalize it (lowercase)
            
            if user_answer == "yes":
                print("You chose Yes.")
                headers = list(data[0])
                rows = data[1:51] 
                return headers, rows
                
                break  # Exit the loop if input is valid
            elif user_answer == "no":
                print("You chose No.")
                headers = None
                rows = data  # All rows, including the first, are data
                return headers, rows
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
        
        except ValueError:
            print("Invalid input. Please enter 'yes' or 'no'.")        
    

   
#step 3

#copied step 2 print and adjusted for rows or header            
def print_first_50(rows, headers=None):
    
    if not rows or len(rows) < 1:
        print("No data available to display.")
        return

    # Calculate column widths dynamically for rows (and header, if present)
    if headers:
        column_widths = [
            max(len(str(value)) for value in column)
            for column in zip(*([headers] + rows[:50]))
        ]
    else:
        column_widths = [
            max(len(str(value)) for value in column)
            for column in zip(*rows[:50])
        ]

    #adds extra space just incase data is long
    column_widths = [width + 2 for width in column_widths]

    line_number_width = len(str(min(len(rows), 50))) + 2

    # Print header if it exists
    if headers:
        print("-" * (line_number_width + sum(column_widths) + 3 * len(headers) + 1))
        print(f"{'Line':<{line_number_width}}" + " | " + " | ".join(f"{str(header_col):<{column_widths[i]}}" for i, header_col in enumerate(headers)))
        print("-" * (line_number_width + sum(column_widths) + 3 * len(headers) + 1))
    else:
        print("-" * (line_number_width + sum(column_widths) + 3 * len(rows[0]) + 1))

    # Print the first 50 rows
    for i, row in enumerate(rows[:50], start=1):
        print(f"{i:<{line_number_width}}" + " | " + " | ".join(f"{str(value):<{column_widths[i]}}" for i, value in enumerate(row)))


    # End of table
    print("-" * (sum(column_widths) + 3 * len(headers if headers else rows[0]) + 1))

#step 4

def define_ranges(rows,headers):

    if not rows:
        print("Data failed to load.")
        return
    
    if headers is None:
        # Create a dictionary using column indices as keys
        data_dict = {f"Column {i + 1}": [row[i] for row in rows] for i in range(len(rows[0]))}
    else:
        # Use the first row as headers for dictionary keys
        data_dict = {headers[i]: [row[i] for row in rows] for i in range(len(headers))}
    
    return data_dict

def sort_ranges(data_dict, ascending=True):

        
    
    for key in data_dict:
        try:
            # Attempt to convert all items to floats for numerical sorting
            numeric_values = [float(item) for item in data_dict[key]]
            numeric_values.sort(reverse=not ascending)  # Sort numerically
            data_dict[key] = numeric_values
        
        except ValueError:
            # If conversion fails, sort as strings alphabetically
            data_dict[key].sort(reverse=not ascending)



    
def count_unique_values(data_dict):
    
    counts_dict = {}
    print()
    print()
    print("--"*20)
    print("here are how many unique values each column has")
    for key in data_dict:
        unique_count = len(set(data_dict[key]))
        counts_dict[key] = unique_count
        print()
        print(f"Column '{key}' has {unique_count} unique value(s).")


    return counts_dict


def count_unique_occurances(data_dict,limit=50):
    counts_occurance = {}
    print("--"*20)
    print()
    print()
    print("here is how many times each value per column appears\n")
    
    for key, values in data_dict.items():
        counts = {}
        for value in values:
            counts[value] = counts.get(value, 0) + 1  # Increment count for each value
            
        counts_occurance[key] = counts

        total_unique = len(counts)
        display_counts = list(counts.items())[:limit]
        remaining = total_unique - limit

        display_str = {key: value for key, value in display_counts}
        print()
        print(f"{key}: {display_str }")

        print()
        if remaining > 0:
            print(f"here are the remainig {remaining} unique values  not being displayed")
    return counts_occurance
     
#step 5
def display_ranges(data_dict):
    

    print("--"*20)
    print("--"*20)
    print()
    print()
    print("here are the columns and sorted alphabetically or numerically depending on the data")
    for key, values in data_dict.items():
        print(f"{key}: {values}")
        print()
    

#step 6

import random

#get sample size 
def get_user_input():
  
    while True:
        try:
            num_records = int(input("Enter the number of synthetic records to generate: "))
            if num_records <= 0:
                print("Please enter a positive number.")
            else:
                return num_records
        except ValueError:
            print("Invalid input. Please enter a whole number.")

#prepare data statistices 
def prepare_sampling_options(data_dict, counts_occurance):
    
    sampling_options = {}
    for column, values in counts_occurance.items():
        unique_values = list(values.keys())
        counts = list(values.values())
        total = sum(counts)
        probabilities = [count / total for count in counts]
        
        sampling_options[column] = {'values': unique_values,'weights': probabilities}
        
    return sampling_options

#generate the data using randoms and stats
def generate_synthetic_data(data_dict, sampling_options, num_records):
    
    headers = list(data_dict.keys())
    synthetic_data = []

    for _ in range(num_records):
        record = {}
        for column in headers:
            if not data_dict[column]:  # If no data in the column
                record[column] = None
            else:
                record[column] = random.choices(sampling_options[column]['values'],
                    weights=sampling_options[column]['weights'],k=1)[0]
                
        synthetic_data.append(record)
    return synthetic_data

#print the first 50 rows of the data
def display_data(synthetic_data, headers, num_records):
    print("\nHere is the synthetic data:")
    display_count = min(50, num_records)  # Display up to 50 records

    # Print the headers
    print(" | ".join(headers))
    print("-" * (len(headers) * 15))  # Separator line

    # Print each record
    for i in range(display_count):
        record = synthetic_data[i]
        record_values = [str(record[column]) for column in headers]
        print(" | ".join(record_values))


def finalize_synthetic_data(synthetic_data, headers):
    
    while True:
        confirmation = input("\nDo you want to finalize the synthetic data generation? (yes/no): ").strip().lower()
        if confirmation == "yes":
            print(f"\nSynthetic data generation finalized with {len(synthetic_data)} records.")
            save_data(synthetic_data, headers)
            return synthetic_data
        elif confirmation == "no":
            print("\nSynthetic data generation canceled.")
            return []
        else:
            print("Please enter 'yes' or 'no'.")        

def roll_data(data_dict,counts_occurance):

    num_records = get_user_input()
    sampling_options = prepare_sampling_options(data_dict, counts_occurance)
    synthetic_data = generate_synthetic_data(data_dict, sampling_options, num_records)
    
    headers = list(data_dict.keys())
    display_data(synthetic_data, headers, num_records)
    
    return finalize_synthetic_data(synthetic_data, headers)


#step 7 save csv
def save_data(synthetic_data, headers):

    filename = input("Enter a filename for the synthetic data (without extension): ").strip()

    #check last 4 strings
    #add if not there
    if filename[-4:].lower() != ".csv":  
        filename += ".csv"
    
    with open(filename, "w") as file:
            file.write(",".join(headers) + "\n")
            for record in synthetic_data:
                row = [str(record.get(column, "")) for column in headers]
                file.write(",".join(row) + "\n")
                
    print(f" data saved to {filename}")

    

#step 8
def check_values(data, synthetic_data):
    """Compare the statistical distributions of source and synthetic data and provide total and column-wise scores."""
    if data is None or len(data) == 0:
        print("No source data loaded. Please load a file first.")
        return
    if synthetic_data is None or len(synthetic_data) == 0:
        print("No synthetic data available. Please generate data first using option 6.")
        return

    try:
        # Ask the user for a margin of error
        margin_of_error = float(input("Enter the margin of error percentage (e.g., 5 for 5%): ").strip())
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    # Remove header row if set
    source_data_values = data[1:] if isinstance(data[0], list) and data[0] == data[0] else data
    synthetic_data_values = synthetic_data

    # Determine the maximum column count
    max_columns = max(len(row) for row in source_data_values)

    # Prepare for comparison
    overall_total_divergence = 0
    overall_total_values = 0
    column_scores = []

    print("\nChecking statistical divergence between source and synthetic data...\n")

    for col_index in range(max_columns):
        # Safely collect column data
        source_column = [row[col_index] for row in source_data_values if col_index < len(row)]
        synthetic_column = [row[col_index] for row in synthetic_data_values if col_index < len(row)]

        if not source_column or not synthetic_column:
            # Skip empty or mismatched columns
            print(f"Skipping column {col_index + 1} due to missing data in source or synthetic data.")
            continue

        # Get counts for each value in the column
        source_counts = get_column_counts(source_column)
        synthetic_counts = get_column_counts(synthetic_column)

        # Normalize counts to percentages
        source_total = sum(source_counts.values())
        synthetic_total = sum(synthetic_counts.values())

        total_divergence = 0
        total_values = 0

        for value in set(source_counts.keys()).union(synthetic_counts.keys()):
            source_percentage = (source_counts.get(value, 0) / source_total) * 100
            synthetic_percentage = (synthetic_counts.get(value, 0) / synthetic_total) * 100
            divergence = abs(source_percentage - synthetic_percentage)

            # Track total divergence for scoring
            total_divergence += divergence
            total_values += 1

        # Calculate average divergence for the column
        average_divergence = total_divergence / total_values if total_values > 0 else 0
        column_scores.append((col_index + 1, average_divergence))

        # Update overall scores
        overall_total_divergence += total_divergence
        overall_total_values += total_values

    # Calculate overall score for the dataset
    overall_score = overall_total_divergence / overall_total_values if overall_total_values > 0 else 0

    # Display results
    print(f"Total Dataset Score: Average Divergence = {overall_score:.2f}%")
    print("\nColumn-Wise Score Breakdown:")
    for col_index, avg_divergence in column_scores:
        status = "<good>" if avg_divergence <= margin_of_error else "<bad>"
        print(f"Column {col_index}: Average Divergence = {avg_divergence:.2f}% {status}")

    input("\nPress the space bar to return to the menu...")


def main_menu():
    #step 1
    data=load_file()

    #step 2 
    headers, rows=set_header_row(data)

    #step 3 
    print_first_50(rows, headers)

    #step 4
    data_dict=define_ranges(rows,headers)
    sort_ranges(data_dict,ascending=True)
    
    
    #step 5
    counts_dict=count_unique_values(data_dict)
    counts_occurance=count_unique_occurances(data_dict)
    display_ranges(data_dict)

    #step 6
    synthetic_data =roll_data(data_dict,counts_occurance)

    #step 8
    check_values(data, synthetic_data)
    
    

main_menu()

















