import pandas as pd
import os

def convert_to_csv(input_path, target_sheet):
    parent_folder = os.path.dirname(input_path)
    output_folder = os.path.join(parent_folder, 'csv_data')
    os.makedirs(output_folder, exist_ok=True)

    # Read only the specific sheet provided in the argument
    # Skip the first row and column (empty)
    df = pd.read_excel(input_path, sheet_name = target_sheet, skiprows=1)
    df = df.iloc[:, 1:]

    filename = os.path.basename(input_path)
    base_name, _ = os.path.splitext(filename)
    
    # Create a dynamic filename using the specified sheet name/index
    csv_filename = f"{base_name}_{target_sheet}.csv"
    new_path = os.path.join(output_folder, csv_filename)
    
    df.to_csv(new_path, index=False)

    return df