from pathlib import Path
from set1 import set1

def read_csv_and_print_matching_columns(file_path, match_column, match_value, column1, column2):
    Path('io/expected_tests').mkdir(parents=True, exist_ok=True)
    
    unique_entries = set()  # To store unique (column1, column2) pairs
    
    with open(file_path, 'r') as file:
        # Read the header line
        header = file.readline().strip().split(',')
        
        # Get the index of the columns we are interested in
        try:
            match_index = header.index(match_column)
            column1_index = header.index(column1)
            # column2_index = header.index(column2)
        except ValueError as e:
            print(f"Error: {e}")
            return
        
        output_path = f'io/expected_tests/{match_value}'
        
        with open(output_path, 'w') as out:
            with open('od.csv', 'a+') as od:
                # Read each subsequent line in the file
                for line in file:
                    # Split the line into values
                    values = line.strip().split(',')
                    
                    # Check if the match value in the specified column matches
                    if values[match_index] == match_value:
                        
                        # Add to the set if it's unique
                        if values[column1_index] not in unique_entries:
                            unique_entries.add(values[column1_index])
                            od.write(f"{values[header.index("github_slug")]},{values[header.index("sha")]},{values[header.index("module")]},{values[column1_index]}\n")
                            out.write(f"{values[column1_index]}\n")
                        
                        # if values[column2_index] not in unique_entries:
                        #     unique_entries.add(values[column2_index])
                        #     out.write(f"{values[column2_index]}\n")

# Example usage
file_path = 'data/set1/data.csv'  # Replace with your CSV file path
match_column = 'Identifier'  # The column to match against
column1 = 'victim/brittle'  # The first column to print
column2 = 'polluter/state-setter'

projects = set1

for project in projects:
    read_csv_and_print_matching_columns(file_path, match_column, project["identifier"], column1, column2)
