from pathlib import Path
from repos import projects

def read_csv_and_print_matching_columns(file_path, match_column, match_value, column1, column2):
    Path('io/original_orders_test').mkdir(parents=True, exist_ok=True)
    with open(file_path, 'r') as file:
        # Read the header line
        header = file.readline().strip().split(',')
        
        # Get the index of the columns we are interested in
        try:
            match_index = header.index(match_column)
            column1_index = header.index(column1)
            column2_index = header.index(column2)
        except ValueError as e:
            print(f"Error: {e}")
            return
        
        with open('io/original_orders_test/'+match_value,'w') as out:
        
            # Read each subsequent line in the file
            for line in file:
                # Split the line into values
                values = line.strip().split(',')
                
                # Check if the match value in the specified column matches
                if values[match_index] == match_value:
                    # Print the values of the specified columns
                    print(f"{header[column1_index]}: {values[column1_index]}, {header[column2_index]}: {values[column2_index]}")
                    out.write(f"{values[column1_index]}\n{values[column2_index]}\n")

# Example usage
file_path = 'data.csv'  # Replace with your CSV file path
match_column = 'Identifier'  # The column to match against
column1 = 'victim/brittle'  # The first column to print
column2 = 'polluter/state-setter'  # The second column to print

projects = projects

for project in projects:
    read_csv_and_print_matching_columns(file_path, match_column, project["identifier"], column1, column2)


